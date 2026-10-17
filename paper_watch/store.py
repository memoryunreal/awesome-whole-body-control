"""Atomic local state and conservative identity / citation handling."""

import copy
import csv
import hashlib
import ipaddress
import json
import os
import re
import tempfile
import unicodedata
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit

from .sources import arxiv_id_from_url


ROOT = Path(__file__).resolve().parents[1]


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def normalized_title(title):
    return " ".join(re.findall(r"\w+", unicodedata.normalize("NFKC", title).casefold()))


def arxiv_id(value):
    """Only trust explicit identifiers and recognized arXiv/DOI URLs."""
    return arxiv_id_from_url(value).lower()


def _doi_id(value):
    value = str(value or "").strip().lower()
    if value.startswith("doi:"):
        value = value[4:].strip()
    if value.startswith(("https://", "http://")):
        try:
            parsed = urlsplit(value)
        except ValueError:
            return ""
        if parsed.hostname not in {"doi.org", "dx.doi.org"} or parsed.username or parsed.password:
            return ""
        value = unquote(parsed.path.lstrip("/"))
    return value if re.fullmatch(r"10\.\d{4,9}/\S+", value) else ""


def _identifiers(paper):
    return (
        arxiv_id(paper.get("arxiv_id", "")) or arxiv_id(paper.get("paper_url", "")),
        _doi_id(paper.get("doi", "")) or _doi_id(paper.get("paper_url", "")),
    )


def _find_existing(state, incoming):
    aid, doi = _identifiers(incoming)
    identity = paper_id(incoming)
    title = normalized_title(incoming["title"])
    title_matches = []
    for paper in state["papers"]:
        current_aid, current_doi = _identifiers(paper)
        # A matching bibliographic identifier is stronger than the title.
        if ((aid and current_aid == aid) or (doi and current_doi == doi) or
                (identity.startswith(("arxiv:", "doi:")) and paper["id"] == identity)):
            return paper
        conflicting = ((aid and current_aid and aid != current_aid) or
                       (doi and current_doi and doi != current_doi))
        if not conflicting and normalized_title(paper["title"]) == title:
            title_matches.append(paper)
    # Do not attach an identifier-free alert arbitrarily when its title names
    # multiple known papers. A unique title match still promotes old local IDs.
    if len(title_matches) == 1:
        return title_matches[0]
    unidentified = [paper for paper in title_matches if not any(_identifiers(paper))]
    return unidentified[0] if len(unidentified) == 1 else None


def paper_id(paper):
    aid, doi = _identifiers(paper)
    if aid:
        return "arxiv:" + aid
    if doi:
        return "doi:" + doi
    return "title:" + hashlib.sha256(normalized_title(paper["title"]).encode()).hexdigest()[:16]


def load_config(path=None):
    return json.loads(Path(path or ROOT / "config/paper-watch.json").read_text())


def atomic_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".state-", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


class Store:
    def __init__(self, path=None):
        self.path = Path(path or ROOT / ".paper-watch/state.json")

    @contextmanager
    def lock(self):
        import fcntl
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.with_suffix(".lock").open("a") as lock:
            try:
                fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError as exc:
                raise RuntimeError("已有论文任务正在运行，请稍后重试。") from exc
            try:
                yield
            finally:
                fcntl.flock(lock.fileno(), fcntl.LOCK_UN)

    def load(self):
        if self.path.exists():
            state = json.loads(self.path.read_text(encoding="utf-8"))
            if state.get("schema_version") != 1:
                raise ValueError("Unsupported state schema; refusing to overwrite it")
            return state
        return {"schema_version": 1, "papers": [], "edges": [], "runs": []}

    def save(self, state):
        state["updated_at"] = now()
        atomic_json(self.path, state)


def merge_paper(state, incoming, status="pending", *, fill_missing=False, existing_id=None):
    """Merge by stable IDs, DOI or whole normalized title, preserving reports."""
    incoming = copy.deepcopy(incoming)
    if not str(incoming.get("title", "")).strip():
        raise ValueError("Paper title is required")
    aid, doi = _identifiers(incoming)
    if aid:
        incoming["arxiv_id"] = aid
    if doi:
        incoming["doi"] = doi
    identity = paper_id(incoming)
    current = _find_existing(state, incoming)
    original = next((p for p in state["papers"] if p["id"] == existing_id), None) if existing_id else None
    if original is not None and current is None:
        current = original
    elif original is not None and current is not original:
        # Two different intake URLs can resolve to the same canonical paper.
        # Consolidate their local state and redirect graph edges to one ID.
        for key, value in original.items():
            if key not in {"id", "sources", "seed_ids"} and not current.get(key):
                current[key] = copy.deepcopy(value)
        for key in ("sources", "seed_ids"):
            for value in original.get(key, []):
                if value not in current[key]:
                    current[key].append(value)
        for edge in state["edges"]:
            for key in ("source", "target"):
                if edge[key] == original["id"]:
                    edge[key] = current["id"]
        state["edges"] = list({json.dumps(edge, sort_keys=True): edge for edge in state["edges"]}.values())
        state["papers"].remove(original)
    created = current is None
    if created:
        current = {"id": identity, "status": status, "seed_ids": [], "sources": [],
                   "screening": {}, "report": {}, "first_seen": now()}
        if any(p["id"] == identity for p in state["papers"]):
            # An ambiguous title-only candidate must not reuse an ID already
            # attached to an identified paper with the same title.
            current["id"] = "title:" + hashlib.sha256((normalized_title(incoming["title"]) + "\0unresolved").encode()).hexdigest()[:16]
        state["papers"].append(current)
    if fill_missing and not created:
        incoming = {key: value for key, value in incoming.items()
                    if key in {"id", "sources", "seed_ids", "is_seed"} or
                    current.get(key) in (None, "", [])}
    # Only new metadata invalidates a negative/review screen. A repeated mail does not.
    changed = any(incoming.get(k) and incoming[k] != current.get(k)
                  for k in ("abstract", "title", "arxiv_version"))
    for key, value in incoming.items():
        if key in {"id", "status", "report", "screening", "sources", "seed_ids"}:
            continue
        if value not in (None, "", []):
            current[key] = value
    for key in ("sources", "seed_ids"):
        for value in incoming.get(key, []):
            if value not in current[key]:
                current[key].append(value)
    if status == "pending" and not current.get("is_seed") and not current.get("manual_decision"):
        if current["status"] == "library" or (changed and current["status"] in {"review", "excluded"}):
            current["status"] = "pending"
    if changed and not created and current.get("report", {}).get("status") == "ready":
        current["report"]["stale"] = True
    current["last_seen"] = now()
    return current, created


def bootstrap(state, config, csv_path=None):
    path = Path(csv_path or ROOT / "papers.csv")
    if path.exists():
        with path.open(encoding="utf-8", newline="") as stream:
            for row in csv.DictReader(stream):
                merge_paper(state, {**row, "sources": [{"kind": "library", "url": row.get("paper_url", "")}]}, "library", fill_missing=True)
    for seed in config["seeds"]:
        merge_paper(state, {**seed, "is_seed": True, "sources": [{"kind": "seed", "url": seed["paper_url"]}]}, "library", fill_missing=True)


def add_verified_edges(state, paper, config):
    seeds = {seed["id"]: seed for seed in config["seeds"]}
    for source in paper.get("sources", []):
        seed_id = source.get("seed_id")
        # A topical match or an unqualified email mention never creates an edge.
        if (source.get("relation") != "cites" or seed_id not in seeds or
                source.get("kind") not in {"semantic_scholar", "scholar_citation_alert"} or
                not source.get("evidence_url") or paper["id"] == seed_id):
            continue
        seed = next((p for p in state["papers"] if p.get("arxiv_id") == seeds[seed_id]["arxiv_id"]), None)
        if not seed:
            continue
        edge = {"source": paper["id"], "target": seed["id"], "kind": "cites",
                "evidence_url": source["evidence_url"], "provenance": source["kind"]}
        if not any(e["source"] == edge["source"] and e["target"] == edge["target"] for e in state["edges"]):
            state["edges"].append(edge)


def public_state(state, config):
    """Export an allowlist; never export raw messages, mailbox IDs, secrets or paths."""
    result = {"schema_version": 1, "updated_at": state.get("updated_at"), "papers": [],
              "edges": [], "runs": [], "config": copy.deepcopy(config)}
    for edge in state["edges"]:
        public_edge = {key: copy.deepcopy(edge[key]) for key in ("source", "target", "kind", "provenance") if key in edge}
        if _public_url(edge.get("evidence_url")):
            public_edge["evidence_url"] = edge["evidence_url"]
        result["edges"].append(public_edge)
    # Config is public by contract, but still only expose supported sections.
    result["config"] = {k: result["config"][k] for k in ("seeds", "scope", "schedule", "discovery", "publication") if k in config}
    result["config"]["llm"] = {"model": os.getenv("OPENAI_MODEL") or config.get("llm", {}).get("model", "")}
    for paper in state["papers"]:
        fields = ("id", "title", "authors", "year", "category", "paper_url", "project_url", "code_url",
                  "code_status", "summary", "abstract", "arxiv_id", "doi", "status", "seed_ids", "is_seed",
                  "first_seen", "last_seen", "robot_platform", "arxiv_version", "venue", "tags", "real_robot", "dataset_url")
        row = {k: copy.deepcopy(paper[k]) for k in fields if k in paper}
        for field in ("paper_url", "project_url", "code_url", "dataset_url"):
            if field in row and not _public_url(row[field]):
                del row[field]
        row["sources"] = [{k: src[k] for k in ("kind", "url", "seed_id", "relation", "evidence_url") if k in src and
                           (k not in {"url", "evidence_url"} or _public_url(src[k]))}
                          for src in paper.get("sources", [])]
        row["screening"] = {k: copy.deepcopy(paper.get("screening", {})[k])
                            for k in ("decision", "score", "reason", "evidence", "method") if k in paper.get("screening", {})}
        row["report"] = {k: copy.deepcopy(paper.get("report", {})[k])
                         for k in ("status", "markdown", "evidence_level", "reason", "generated_at", "stale",
                                   "curated", "organization", "summary", "selection_reason", "priority",
                                   "source_version", "source_urls", "sha256") if k in paper.get("report", {})}
        result["papers"].append(row)
    for run in state["runs"][-30:]:
        public_run = {k: copy.deepcopy(run[k]) for k in ("id", "started_at", "finished_at", "status", "discovered", "added", "screened", "reports_ready", "discovery_attempted") if k in run}
        public_run["errors"] = []
        for error in run.get("errors", []):
            public_error = {key: copy.deepcopy(error[key]) for key in ("source", "seed_id", "paper_id", "incomplete", "since", "limit") if key in error}
            if "message" in error:
                public_error["message"] = _public_error_message(error["message"])
            public_run["errors"].append(public_error)
        result["runs"].append(public_run)
    result["stats"] = {"papers": len(result["papers"]), "seeds": sum(bool(p.get("is_seed")) for p in result["papers"]),
                       "citations": len(result["edges"])}
    for status in ("library", "pending", "target", "review", "excluded"):
        result["stats"][status] = sum(p.get("status") == status for p in result["papers"])
    result["stats"]["reports_ready"] = sum(p.get("report", {}).get("status") == "ready" and not p.get("report", {}).get("stale") for p in result["papers"])
    return result


def _public_url(value):
    """Validate a public link without resolving DNS or exposing local URIs."""
    try:
        parsed = urlsplit(str(value or ""))
        host = (parsed.hostname or "").lower()
        if (parsed.scheme not in {"http", "https"} or not host or parsed.username or parsed.password or
                host in {"localhost", "localhost.localdomain"} or host.endswith((".localhost", ".local"))):
            return False
        try:
            return ipaddress.ip_address(host).is_global
        except ValueError:
            return True
    except ValueError:
        return False


def _public_error_message(value):
    text = str(value)
    for name in ("IMAP_USER", "IMAP_PASSWORD", "OPENAI_API_KEY", "SEMANTIC_SCHOLAR_API_KEY"):
        secret = os.getenv(name)
        if secret:
            text = text.replace(secret, "[redacted]")
    text = re.sub(r"(?:file|imap-message|imaps?)://[^\s'\";]+", "[local source]", text, flags=re.I)
    text = re.sub(r"(?<![\w:/])/(?:Users|home|private|tmp|var|Volumes|opt|mnt)/[^\s'\";,]+", "[local path]", text)
    return re.sub(r"\b[A-Za-z]:\\[^\s'\";,]+", "[local path]", text)
