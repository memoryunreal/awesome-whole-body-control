"""Read-only discovery from Scholar mail and primary bibliographic services.

Scholar mail is a discovery hint, not proof that one paper cites another. Only
the Semantic Scholar citations endpoint creates ``relation='cites'`` evidence.
No service is contacted merely by importing this module.
"""

from __future__ import annotations

import email.policy
import imaplib
import ipaddress
import json
import os
import re
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.parser import BytesParser
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable


MAX_MAIL_BYTES = 10 * 1024 * 1024
MAX_RESPONSE_BYTES = 4 * 1024 * 1024
S2_BASE = "https://api.semanticscholar.org/graph/v1"
ARXIV_API = "https://export.arxiv.org/api/query"
_ARXIV_LOCK = threading.Lock()
_ARXIV_LAST_REQUEST = 0.0
_ARXIV_ID = re.compile(r"^(?:\d{4}\.\d{4,5}|[a-z][a-z.\-]*/\d{7})(?:v\d+)?$", re.I)
_URL = re.compile(r"https?://[^\s<>\"\u201c\u201d]+", re.I)
_CONTROLS = re.compile(
    r"^(?:\[?(?:pdf|html|book|citation)\]?|save|cite|cited by(?: \d+)?|"
    r"related articles|all \d+ versions|view (?:all|article|pdf|profile)|"
    r"my (?:profile|library)|google scholar|unsubscribe|cancel alert|"
    r"manage (?:alerts|subscriptions)|privacy(?: policy)?|terms(?: of service)?|"
    r"help|settings|sign in|login|learn more|退订|取消订阅|管理提醒|引用|保存)$", re.I,
)


class SourceError(RuntimeError):
    """A retriable discovery failure, including any successfully read papers.

    Callers should ingest ``candidates`` and display/store ``errors``. Retrying
    is safe: mail is never marked read, moved, deleted, or checkpointed here.
    """

    def __init__(self, errors: list[dict], candidates: list[dict] | None = None):
        self.errors = errors
        self.candidates = candidates or []
        super().__init__("; ".join(f"{item['source']}: {item['message']}" for item in errors))


def _compact(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def _env_int(name: str, default: int, minimum: int, maximum: int) -> int:
    raw = os.environ.get(name, str(default))
    try:
        result = int(raw)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be an integer") from exc
    if not minimum <= result <= maximum:
        raise ValueError(f"{name} must be between {minimum} and {maximum}")
    return result


def normalize_paper_url(raw: str) -> str:
    """Unwrap known Google redirect URLs without making any network request."""
    value = unescape(str(raw or "")).strip().strip("<>")
    if value.startswith("//"):
        value = "https:" + value
    for _ in range(5):
        try:
            parsed = urllib.parse.urlsplit(value)
            host = (parsed.hostname or "").lower()
            if parsed.scheme not in {"http", "https"} or not host or parsed.username or parsed.password:
                return ""
            if host == "google.com" or host.endswith(".google.com") or host.startswith("scholar.google."):
                if parsed.path in {"/url", "/scholar_url"}:
                    query = urllib.parse.parse_qs(parsed.query)
                    target = next((query[key][0] for key in ("url", "q") if query.get(key)), "")
                    if target and target != value:
                        value = target
                        continue
            return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, parsed.query, ""))
        except ValueError:
            return ""
    return ""


def arxiv_id_from_url(value: str) -> str:
    """Return an unversioned arXiv identifier, or an empty string."""
    value = str(value or "").strip()
    value = re.sub(r"^arxiv:", "", value, flags=re.I)
    if _ARXIV_ID.fullmatch(value):
        return re.sub(r"v\d+$", "", value, flags=re.I)
    normalized = normalize_paper_url(value)
    if not normalized:
        return ""
    parsed = urllib.parse.urlsplit(normalized)
    if parsed.hostname in {"arxiv.org", "www.arxiv.org", "export.arxiv.org"}:
        match = re.match(r"^/(?:abs|pdf|html)/(.+?)(?:\.pdf)?/?$", parsed.path)
        if match and _ARXIV_ID.fullmatch(match.group(1)):
            return re.sub(r"v\d+$", "", match.group(1), flags=re.I)
    if parsed.hostname in {"doi.org", "dx.doi.org"}:
        match = re.match(r"^/10\.48550/arxiv\.(.+)$", parsed.path, flags=re.I)
        if match and _ARXIV_ID.fullmatch(match.group(1)):
            return re.sub(r"v\d+$", "", match.group(1), flags=re.I)
    return ""


def _doi_from_url(value: str) -> str:
    parsed = urllib.parse.urlsplit(value)
    if parsed.hostname in {"doi.org", "dx.doi.org"} and parsed.path.startswith("/10."):
        return urllib.parse.unquote(parsed.path[1:])
    return ""


def _key(paper: dict) -> str:
    return (
        "arxiv:" + paper["arxiv_id"] if paper.get("arxiv_id") else
        "doi:" + paper["doi"].lower() if paper.get("doi") else
        "title:" + re.sub(r"[^\w]", "", paper["title"].casefold())
    )


def _merge_candidates(papers: Iterable[dict]) -> list[dict]:
    results: dict[str, dict] = {}
    for paper in papers:
        if not paper.get("title"):
            continue
        key = _key(paper)
        if key not in results:
            results[key] = dict(paper)
            results[key]["seed_ids"] = list(paper.get("seed_ids", []))
            results[key]["sources"] = list(paper.get("sources", []))
            continue
        current = results[key]
        for field, value in paper.items():
            if field not in {"seed_ids", "sources"} and value and not current.get(field):
                current[field] = value
        for field in ("seed_ids", "sources"):
            for value in paper.get(field, []):
                if value not in current[field]:
                    current[field].append(value)
    return list(results.values())


def _seed_matches(text: str, seeds: Iterable[dict]) -> list[str]:
    found = []
    for seed in seeds:
        names = [seed.get("title", ""), seed.get("arxiv_id", ""), *seed.get("aliases", [])]
        if any(name and re.search(r"(?<!\w)" + re.escape(name) + r"(?!\w)", text, re.I) for name in names):
            found.append(str(seed["id"]))
    return found


class _MailHTML(HTMLParser):
    """Extract anchor text and structural title hints, preserving text order."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.anchors: list[dict] = []
        self.parts: list[str] = []
        self.stack: list[tuple[str, bool]] = []
        self.active: dict | None = None
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag in {"script", "style"}:
            self.hidden += 1
        title_hint = tag in {"h1", "h2", "h3", "h4"} or "gs_rt" in attributes.get("class", "").split()
        if tag not in {"br", "hr", "img", "input", "meta", "link"}:
            self.stack.append((tag, title_hint))
        if tag in {"br", "p", "div", "h1", "h2", "h3", "h4", "li"}:
            self.parts.append("\n")
        if tag == "a" and attributes.get("href") and not self.hidden:
            self.active = {
                "url": attributes["href"], "parts": [],
                "heading": any(hint for _, hint in self.stack), "position": len(self.parts),
            }

    def handle_endtag(self, tag):
        if tag == "a" and self.active is not None:
            self.active["text"] = _compact("".join(self.active.pop("parts")))
            self.active["end"] = len(self.parts)
            self.anchors.append(self.active)
            self.active = None
        if tag in {"script", "style"} and self.hidden:
            self.hidden -= 1
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                break
        if tag in {"p", "div", "h1", "h2", "h3", "h4", "li"}:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)
            if self.active is not None:
                self.active["parts"].append(data)


def _clean_title(text: str) -> str:
    return _compact(re.sub(r"^\s*\[(?:PDF|HTML|BOOK|CITATION)\]\s*", "", text, flags=re.I))


def _paper_anchor(url: str, title: str, heading: bool = False) -> bool:
    if not url or len(title) < 5 or _CONTROLS.fullmatch(title):
        return False
    if title.lower().startswith(("unsubscribe", "manage your", "cancel this alert", "create alert")):
        return False
    parsed = urllib.parse.urlsplit(url)
    host = (parsed.hostname or "").lower()
    if host == "google.com" or host.endswith(".google.com") or host.startswith("scholar.google."):
        # Scholar profile, settings, subscriptions, search and citation controls
        # are not article URLs. Real Scholar article redirects were unwrapped.
        return False
    if any(word in parsed.path.lower() for word in ("unsubscribe", "/preferences", "/settings", "/login", "/profile", "/author/", "/people/")):
        return False
    scholarly = (
        bool(arxiv_id_from_url(url)) or bool(_doi_from_url(url)) or
        host in {"openreview.net", "www.semanticscholar.org", "proceedings.mlr.press", "aclanthology.org"} or
        host.endswith((".ieee.org", ".springer.com", ".sciencedirect.com", ".acm.org"))
    )
    paper_path = re.search(r"/(?:papers?|articles?|abs|pdf|doi|publications?|proceedings|document|abstract|fulltext|forum|manuscripts?)(?:[/._-]|$)", parsed.path, re.I)
    return heading or scholarly or bool(paper_path and len(title.split()) >= 3) or (parsed.path.lower().endswith(".pdf") and len(title.split()) >= 3)


def _mail_candidate(title: str, url: str, seeds: list[str], source_url: str, snippet: str = "") -> dict:
    arxiv_id = arxiv_id_from_url(url)
    source = {"kind": "google_scholar_email", "url": source_url, "relation": "mentions", "evidence_url": source_url}
    # These are associations with an alert, never graph edges.
    sources = [{**source, "seed_id": seed_id} for seed_id in seeds] or [source]
    return {
        "title": title, "paper_url": f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else url,
        "arxiv_id": arxiv_id, "doi": _doi_from_url(url), "abstract": "", "authors": "", "year": "",
        "alert_snippet": _compact(snippet)[:2000], "seed_ids": seeds, "sources": sources,
    }


def _parse_html(body: str, seeds: list[str], source_url: str) -> list[dict]:
    parser = _MailHTML()
    parser.feed(body)
    selected = []
    for anchor in parser.anchors:
        url = normalize_paper_url(anchor["url"])
        title = _clean_title(anchor["text"])
        if _paper_anchor(url, title, anchor["heading"]):
            selected.append((anchor, title, url))
    papers = []
    for index, (anchor, title, url) in enumerate(selected):
        end = selected[index + 1][0]["position"] if index + 1 < len(selected) else len(parser.parts)
        snippet = "".join(parser.parts[anchor["end"]:end])
        # Footer/control text is not an abstract; retain it only as a bounded,
        # explicitly named alert snippet. arXiv supplies the actual abstract.
        papers.append(_mail_candidate(title, url, seeds, source_url, snippet))
    return papers


def _parse_plain(body: str, seeds: list[str], source_url: str) -> list[dict]:
    lines = body.splitlines()
    papers = []
    for index, line in enumerate(lines):
        for match in _URL.finditer(line):
            raw_url = match.group(0).rstrip(").,;]")
            url = normalize_paper_url(raw_url)
            title = _clean_title(line[:match.start()].strip(" <>-\t"))
            if not title:
                # Plain Scholar mail normally puts the title directly before
                # its URL. Do not guess using the email subject or URL slug.
                for prior in range(index - 1, max(-1, index - 3), -1):
                    previous = _compact(lines[prior])
                    if previous:
                        title = _clean_title(previous)
                        break
            if _paper_anchor(url, title):
                snippet = " ".join(lines[index + 1:index + 4])
                papers.append(_mail_candidate(title, url, seeds, source_url, snippet))
    return papers


def _parse_message(raw: bytes, seeds: list[dict], source_url: str) -> list[dict]:
    if len(raw) > MAX_MAIL_BYTES:
        raise ValueError(f"email exceeds {MAX_MAIL_BYTES // 1024 // 1024} MiB limit")
    message = BytesParser(policy=email.policy.default).parsebytes(raw)
    html_parts, plain_parts = [], []
    for part in message.walk():
        if part.is_multipart() or part.get_content_disposition() == "attachment":
            continue
        content_type = part.get_content_type()
        if content_type not in {"text/html", "text/plain"}:
            continue
        payload = part.get_payload(decode=True) or b""
        charset = part.get_content_charset() or "utf-8"
        try:
            text = payload.decode(charset, errors="replace")
        except LookupError:
            text = payload.decode("utf-8", errors="replace")
        (html_parts if content_type == "text/html" else plain_parts).append(text)
    context = "\n".join([str(message.get("subject", "")), *plain_parts, *html_parts])
    seed_ids = _seed_matches(context, seeds)
    result = [paper for body in html_parts for paper in _parse_html(body, seed_ids, source_url)]
    if not result:
        result = [paper for body in plain_parts for paper in _parse_plain(body, seed_ids, source_url)]
    return _merge_candidates(result)


def discover_eml(paths: Iterable[str | Path] | str | Path, seeds: list[dict]) -> list[dict]:
    """Import local .eml files or directories without changing their contents."""
    if isinstance(paths, (str, Path)):
        paths = [paths]
    candidates, errors, seen = [], [], set()
    for item in paths:
        path = Path(item).expanduser()
        files = sorted(path.rglob("*.eml")) if path.is_dir() else [path]
        for file in files:
            if file.resolve() in seen:
                continue
            seen.add(file.resolve())
            try:
                if file.stat().st_size > MAX_MAIL_BYTES:
                    raise ValueError("email exceeds 10 MiB limit")
                candidates.extend(_parse_message(file.read_bytes(), seeds, file.resolve().as_uri()))
            except (OSError, ValueError) as exc:
                errors.append({"source": "eml", "message": f"{file.name}: {exc}"})
    result = _merge_candidates(candidates)
    if errors:
        raise SourceError(errors, result)
    return result


def discover_imap(seeds: list[dict]) -> list[dict]:
    """Read recent Scholar mail using IMAP EXAMINE and BODY.PEEK, never STORE.

    Gmail is the default host. Required: IMAP_USER, IMAP_PASSWORD (for Gmail,
    an app password). Optional: IMAP_HOST, IMAP_PORT, IMAP_MAILBOX,
    IMAP_SENDER, IMAP_LOOKBACK_DAYS, IMAP_SINCE (YYYY-MM-DD),
    IMAP_MAX_MESSAGES and PAPER_WATCH_HTTP_TIMEOUT.
    """
    user, password = os.environ.get("IMAP_USER"), os.environ.get("IMAP_PASSWORD")
    if not user or not password:
        raise SourceError([{"source": "imap", "message": "Set IMAP_USER and IMAP_PASSWORD to read Scholar alerts."}])
    try:
        host = os.environ.get("IMAP_HOST", "imap.gmail.com")
        port = _env_int("IMAP_PORT", 993, 1, 65535)
        timeout = _env_int("PAPER_WATCH_HTTP_TIMEOUT", 20, 1, 60)
        max_messages = _env_int("IMAP_MAX_MESSAGES", 50, 1, 500)
        days = _env_int("IMAP_LOOKBACK_DAYS", 14, 1, 3650)
        since = datetime.now(timezone.utc) - timedelta(days=days)
        if os.environ.get("IMAP_SINCE"):
            since = datetime.strptime(os.environ["IMAP_SINCE"], "%Y-%m-%d")
        # IMAP dates use English months regardless of the machine locale.
        month = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")[since.month - 1]
        since_text = f"{since.day:02d}-{month}-{since.year}"
    except ValueError as exc:
        raise SourceError([{"source": "imap", "message": str(exc)}]) from exc
    candidates, errors = [], []
    client = None
    try:
        client = imaplib.IMAP4_SSL(host, port, timeout=timeout)
        client.login(user, password)
        status, _ = client.select(os.environ.get("IMAP_MAILBOX", "INBOX"), readonly=True)
        if status != "OK":
            raise ValueError("Could not open the configured IMAP mailbox read-only")
        sender = os.environ.get("IMAP_SENDER", "scholaralerts-noreply@google.com")
        if any(character in sender for character in '\r\n"'):
            raise ValueError("IMAP_SENDER contains unsupported characters")
        status, data = client.uid("search", None, "SINCE", since_text, "FROM", f'"{sender}"')
        if status != "OK":
            raise ValueError("IMAP search failed")
        identifiers = b" ".join(item for item in (data or []) if isinstance(item, bytes)).split()
        for uid in identifiers[-max_messages:]:
            uid_text = uid.decode("ascii", errors="replace")
            if not uid_text.isdigit():
                errors.append({"source": "imap", "message": "IMAP returned an invalid message UID"})
                continue
            try:
                status, message_data = client.uid("fetch", uid, f"(RFC822.SIZE BODY.PEEK[]<0.{MAX_MAIL_BYTES + 1}>)")
                if status != "OK":
                    raise ValueError(f"Could not fetch message UID {uid_text}")
                pieces = [item[1] for item in (message_data or []) if isinstance(item, tuple) and isinstance(item[1], bytes)]
                if not pieces:
                    raise ValueError(f"Message UID {uid_text} has no readable body")
                for item in message_data or []:
                    if isinstance(item, tuple) and isinstance(item[0], bytes):
                        size = re.search(rb"RFC822\.SIZE (\d+)", item[0], re.I)
                        if size and int(size.group(1)) > MAX_MAIL_BYTES:
                            raise ValueError(f"Message UID {uid_text} exceeds 10 MiB limit")
                source_url = f"imap-message://scholar/{uid_text}"
                candidates.extend(_parse_message(b"".join(pieces), seeds, source_url))
            except (imaplib.IMAP4.error, OSError, ValueError) as exc:
                errors.append({"source": "imap", "message": f"UID {uid_text}: {exc}"})
    except (imaplib.IMAP4.error, OSError, ValueError) as exc:
        # Do not echo server login responses, which may contain credentials.
        message = str(exc) if isinstance(exc, ValueError) else f"IMAP connection or authentication failed ({type(exc).__name__})"
        errors.append({"source": "imap", "message": message})
    finally:
        if client is not None:
            try:
                client.logout()
            except (imaplib.IMAP4.error, OSError):
                pass
    result = _merge_candidates(candidates)
    if errors:
        raise SourceError(errors, result)
    return result


class _ServiceRedirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        parsed = urllib.parse.urlsplit(newurl)
        if parsed.scheme != "https" or parsed.hostname not in {"api.semanticscholar.org", "export.arxiv.org", "arxiv.org"}:
            raise ValueError("Bibliographic service redirected to an unexpected host")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _fetch_bytes(url: str, headers: dict | None = None) -> bytes:
    global _ARXIV_LAST_REQUEST
    timeout = _env_int("PAPER_WATCH_HTTP_TIMEOUT", 20, 1, 60)
    request_headers = {"User-Agent": "PaperWatch/1.0 (research metadata monitor)", **(headers or {})}
    opener = urllib.request.build_opener(_ServiceRedirects())
    for attempt in range(2):
        if urllib.parse.urlsplit(url).hostname == "export.arxiv.org":
            # arXiv asks API clients to wait at least three seconds between calls.
            with _ARXIV_LOCK:
                delay = 3 - (time.monotonic() - _ARXIV_LAST_REQUEST)
                if delay > 0:
                    time.sleep(delay)
                _ARXIV_LAST_REQUEST = time.monotonic()
        try:
            with opener.open(urllib.request.Request(url, headers=request_headers), timeout=timeout) as response:
                body = response.read(MAX_RESPONSE_BYTES + 1)
                if len(body) > MAX_RESPONSE_BYTES:
                    raise ValueError("Bibliographic response exceeds 4 MiB limit")
                return body
        except urllib.error.HTTPError as exc:
            if attempt == 0 and exc.code in {429, 500, 502, 503, 504}:
                retry_after = exc.headers.get("Retry-After", "1") if exc.headers else "1"
                delay = min(5, max(1, int(retry_after))) if str(retry_after).isdigit() else 1
                time.sleep(delay)
                continue
            raise ValueError(f"Bibliographic service returned HTTP {exc.code}") from exc
    raise ValueError("Bibliographic request failed")


def _seed_api_id(seed: dict) -> str:
    if seed.get("semantic_scholar_id"):
        return str(seed["semantic_scholar_id"])
    arxiv_id = arxiv_id_from_url(seed.get("arxiv_id", "")) or arxiv_id_from_url(seed.get("paper_url", ""))
    if arxiv_id:
        return "ARXIV:" + arxiv_id
    doi = seed.get("doi") or _doi_from_url(seed.get("paper_url", ""))
    if doi:
        return "DOI:" + doi
    url = seed.get("paper_url", "")
    if normalize_paper_url(url):
        return "URL:" + url
    raise ValueError("Seed requires an arXiv ID, DOI, Semantic Scholar ID, or paper URL")


def _s2_headers() -> dict:
    headers = {"Accept": "application/json"}
    if os.environ.get("SEMANTIC_SCHOLAR_API_KEY"):
        headers["x-api-key"] = os.environ["SEMANTIC_SCHOLAR_API_KEY"]
    return headers


def _public_lookup_url(value: str) -> str:
    """Validate URL metadata lookup input without fetching or resolving it."""
    url = normalize_paper_url(value)
    if not url:
        return ""
    parsed = urllib.parse.urlsplit(url)
    host = (parsed.hostname or "").lower()
    if host in {"localhost", "localhost.localdomain"} or host.endswith((".local", ".localhost", ".internal")):
        return ""
    try:
        if not ipaddress.ip_address(host).is_global:
            return ""
    except ValueError:
        if "." not in host:
            return ""
    return url


def _normalized_doi(value: str) -> str:
    value = _compact(value)
    value = re.sub(r"^doi:\s*", "", value, flags=re.I)
    if value.startswith(("https://", "http://")):
        value = _doi_from_url(normalize_paper_url(value))
    return value.lower() if re.fullmatch(r"10\.\d{4,9}/\S+", value) else ""


def _enrich_semantic_scholar(paper: dict) -> dict:
    """Resolve a DOI, paper ID, or public URL with one bounded metadata call."""
    result = dict(paper)
    lookup_id = _compact(paper.get("semantic_scholar_id"))
    expected_doi = _normalized_doi(paper.get("doi", ""))
    expected_s2 = ""
    try:
        if lookup_id:
            if not re.fullmatch(r"[a-f\d]{40}", lookup_id, re.I):
                raise ValueError("Invalid Semantic Scholar paper ID")
            expected_s2 = lookup_id.lower()
        elif expected_doi:
            lookup_id = "DOI:" + expected_doi
        elif paper.get("doi"):
            raise ValueError("Invalid DOI for metadata lookup")
        else:
            url = _public_lookup_url(paper.get("paper_url", ""))
            if not url:
                return result
            expected_doi = _normalized_doi(_doi_from_url(url))
            lookup_id = "DOI:" + expected_doi if expected_doi else "URL:" + url
        fields = "title,abstract,authors,year,url,externalIds,openAccessPdf,publicationDate"
        endpoint = f"{S2_BASE}/paper/{urllib.parse.quote(lookup_id, safe='')}?" + urllib.parse.urlencode({"fields": fields})
        metadata = json.loads(_fetch_bytes(endpoint, _s2_headers()))
        if not isinstance(metadata, dict) or not _compact(metadata.get("title")) or not metadata.get("paperId"):
            raise ValueError("Semantic Scholar returned no matched paper metadata")
        resolved_id = _compact(metadata["paperId"])
        if not re.fullmatch(r"[a-f\d]{40}", resolved_id, re.I):
            raise ValueError("Semantic Scholar returned an invalid paper identifier")
        if expected_s2 and resolved_id.lower() != expected_s2:
            raise ValueError("Semantic Scholar returned a mismatched paper identifier")
        external = metadata.get("externalIds") or {}
        if not isinstance(external, dict):
            raise ValueError("Semantic Scholar returned invalid external identifiers")
        doi = _normalized_doi(external.get("DOI", ""))
        if expected_doi and doi != expected_doi:
            raise ValueError("Semantic Scholar returned a mismatched DOI")
        arxiv_id = arxiv_id_from_url(external.get("ArXiv", ""))
        values = {
            "title": _compact(metadata["title"]),
            "abstract": _compact(metadata.get("abstract")),
            "authors": ", ".join(_compact(author.get("name")) for author in metadata.get("authors") or [] if isinstance(author, dict) and author.get("name")),
            "year": metadata.get("year") or "", "published_date": _compact(metadata.get("publicationDate")),
            "semantic_scholar_id": resolved_id, "doi": doi, "arxiv_id": arxiv_id,
        }
        for field, value in values.items():
            if value:
                result[field] = value
        if arxiv_id:
            # A later refresh uses arXiv's primary API for versioned metadata.
            result["paper_url"] = f"https://arxiv.org/abs/{arxiv_id}"
        elif not _public_lookup_url(result.get("paper_url", "")):
            result["paper_url"] = _public_lookup_url(metadata.get("url", "")) or f"https://www.semanticscholar.org/paper/{resolved_id}"
        open_access = metadata.get("openAccessPdf")
        if isinstance(open_access, dict):
            open_access_url = _public_lookup_url(open_access.get("url", ""))
            if open_access_url:
                result["open_access_url"] = open_access_url
        source = {"kind": "semantic_scholar_metadata", "url": endpoint, "relation": "metadata", "evidence_url": endpoint}
        result["sources"] = list(paper.get("sources", []))
        if source not in result["sources"]:
            result["sources"].append(source)
        return result
    except (OSError, ValueError, TypeError) as exc:
        raise SourceError([{"source": "semantic_scholar_metadata", "message": str(exc)}], [dict(paper)]) from exc


def discover_citations(seeds: list[dict], limit: int = 25, since: str | None = None) -> list[dict]:
    """Read at most ``limit`` citation records per seed, across bounded pages.

    The service's ``next`` offset is followed. By default the publication window
    is the past 30 days (CITATION_LOOKBACK_DAYS); SEMANTIC_SCHOLAR_SINCE or an
    explicit ISO ``since`` date overrides that. An explicit empty ``since``
    requests historical discovery. Hitting the bound while pages remain is
    reported as incomplete, preserving all discovered candidates.

    The service treats a missing publication date as January 1 of the paper's
    year, so a recent date window can omit such papers. Mail is the complementary
    new-arrival source. This endpoint does not promise chronological ordering.
    """
    if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= 1000:
        raise SourceError([{"source": "semantic_scholar", "message": "limit must be an integer between 1 and 1000"}])
    try:
        if since is None:
            since = os.environ.get("SEMANTIC_SCHOLAR_SINCE")
            if since is None:
                days = _env_int("CITATION_LOOKBACK_DAYS", 30, 1, 3650)
                since = (datetime.now(timezone.utc) - timedelta(days=days)).date().isoformat()
        if since:
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", since):
                raise ValueError("Citation since date must use YYYY-MM-DD")
            datetime.strptime(since, "%Y-%m-%d")
    except (ValueError, TypeError) as exc:
        raise SourceError([{"source": "semantic_scholar", "message": str(exc)}]) from exc
    candidates, errors = [], []
    headers = _s2_headers()
    for seed in seeds:
        seed_id = str(seed.get("id", ""))
        try:
            if not seed_id:
                raise ValueError("Seed has no stable id")
            api_id = _seed_api_id(seed)
            offset, scanned, seen_offsets = 0, 0, set()
            while scanned < limit:
                if offset in seen_offsets:
                    raise ValueError("Citation service repeated a pagination offset")
                seen_offsets.add(offset)
                page_limit = min(100, limit - scanned)
                parameters = {
                    "fields": "title,abstract,authors,year,url,externalIds,publicationDate",
                    "offset": offset, "limit": page_limit,
                }
                if since:
                    parameters["publicationDateOrYear"] = since + ":"
                query = urllib.parse.urlencode(parameters)
                endpoint = f"{S2_BASE}/paper/{urllib.parse.quote(api_id, safe='')}/citations?{query}"
                response = json.loads(_fetch_bytes(endpoint, headers))
                if not isinstance(response, dict) or not isinstance(response.get("data"), list):
                    raise ValueError("Citation service returned an invalid response")
                rows = response["data"]
                for row in rows[:page_limit]:
                    scanned += 1
                    paper = row.get("citingPaper") if isinstance(row, dict) else None
                    if not isinstance(paper, dict) or not _compact(paper.get("title")):
                        continue
                    external = paper.get("externalIds") or {}
                    if not isinstance(external, dict):
                        raise ValueError("Citation service returned invalid external identifiers")
                    arxiv_id = arxiv_id_from_url(external.get("ArXiv", ""))
                    doi = _compact(external.get("DOI", ""))
                    url = normalize_paper_url(paper.get("url", ""))
                    if arxiv_id:
                        url = f"https://arxiv.org/abs/{arxiv_id}"
                    elif not url and doi:
                        url = "https://doi.org/" + doi
                    elif not url and paper.get("paperId"):
                        url = "https://www.semanticscholar.org/paper/" + urllib.parse.quote(paper["paperId"], safe="")
                    candidates.append({
                        "title": _compact(paper["title"]), "paper_url": url,
                        "arxiv_id": arxiv_id, "doi": doi,
                        "abstract": _compact(paper.get("abstract", "")),
                        "authors": ", ".join(_compact(author.get("name")) for author in paper.get("authors") or [] if isinstance(author, dict) and author.get("name")),
                        "year": paper.get("year") or "", "published_date": paper.get("publicationDate") or "",
                        "semantic_scholar_id": paper.get("paperId") or "", "seed_ids": [seed_id],
                        "sources": [{"kind": "semantic_scholar", "url": endpoint, "seed_id": seed_id, "relation": "cites", "evidence_url": endpoint}],
                    })
                next_offset = response.get("next")
                if next_offset is None:
                    break
                if isinstance(next_offset, bool) or not isinstance(next_offset, int) or next_offset <= offset:
                    raise ValueError("Citation service returned an invalid pagination offset")
                if scanned >= limit:
                    errors.append({
                        "source": "semantic_scholar", "seed_id": seed_id, "incomplete": True,
                        "since": since or "", "limit": limit,
                        "message": f"Citation scan reached its {limit}-record limit with more pages remaining; increase limit_per_seed or narrow the date window.",
                    })
                    break
                if not rows:
                    raise ValueError("Citation service returned an empty page with more pages remaining")
                offset = next_offset
        except (OSError, ValueError, TypeError, KeyError) as exc:
            errors.append({"source": "semantic_scholar", "seed_id": seed_id, "message": str(exc)})
    result = _merge_candidates(candidates)
    if errors:
        raise SourceError(errors, result)
    return result


def enrich_paper(paper: dict) -> dict:
    """Resolve metadata via primary APIs; never fetch an arbitrary paper page.

    arXiv identifiers use its Atom API. Other papers use a single Semantic
    Scholar DOI, paper-ID, or public-URL lookup; title search is never guessed.
    """
    result = dict(paper)
    arxiv_id = arxiv_id_from_url(paper.get("arxiv_id", "")) or arxiv_id_from_url(paper.get("paper_url", ""))
    if not arxiv_id:
        return _enrich_semantic_scholar(paper)
    endpoint = ARXIV_API + "?" + urllib.parse.urlencode({"id_list": arxiv_id, "max_results": 1})
    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    try:
        root = ET.fromstring(_fetch_bytes(endpoint, {"Accept": "application/atom+xml"}))
        entry = root.find("atom:entry", ns)
        if entry is None:
            raise ValueError("arXiv returned no entry for this identifier")
        identity = _compact(entry.findtext("atom:id", "", ns))
        title = _compact(entry.findtext("atom:title", "", ns))
        if arxiv_id_from_url(identity) != arxiv_id or not title or title.lower() == "error":
            raise ValueError("arXiv returned an error or mismatched identifier")
        published = _compact(entry.findtext("atom:published", "", ns))
        updated = _compact(entry.findtext("atom:updated", "", ns))
        version = re.search(r"v(\d+)$", identity)
        result.update({
            "arxiv_id": arxiv_id, "title": title, "paper_url": f"https://arxiv.org/abs/{arxiv_id}",
            "abstract": _compact(entry.findtext("atom:summary", "", ns)),
            "authors": ", ".join(_compact(author.findtext("atom:name", "", ns)) for author in entry.findall("atom:author", ns)),
            "published_date": published[:10], "updated_date": updated[:10],
            "year": int(published[:4]) if re.match(r"\d{4}-", published) else paper.get("year", ""),
            "arxiv_version": int(version.group(1)) if version else None,
        })
        doi = _compact(entry.findtext("arxiv:doi", "", ns))
        if doi:
            result["doi"] = doi
        primary_category = entry.find("arxiv:primary_category", ns)
        if primary_category is not None:
            result["arxiv_category"] = primary_category.attrib.get("term", "")
        source = {"kind": "arxiv_metadata", "url": endpoint, "relation": "metadata", "evidence_url": endpoint}
        result["sources"] = list(paper.get("sources", []))
        if source not in result["sources"]:
            result["sources"].append(source)
    except (OSError, ValueError, ET.ParseError) as exc:
        raise SourceError([{"source": "arxiv", "message": str(exc), "arxiv_id": arxiv_id}], [dict(paper)]) from exc
    return result
