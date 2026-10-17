"""Idempotent orchestration. Every stage can be resumed after failure."""

import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from datetime import datetime, timedelta, timezone
from urllib.parse import urlsplit

from .store import ROOT, Store, add_verified_edges, atomic_json, bootstrap, merge_paper, now, public_state


def safe_error(exc):
    text = str(exc)
    for name in ("IMAP_PASSWORD", "OPENAI_API_KEY", "SEMANTIC_SCHOLAR_API_KEY", "IMAP_USER"):
        value = os.getenv(name)
        if value:
            text = text.replace(value, "[redacted]")
    return text[:700]


def ingest_url(state, url):
    import ipaddress
    import socket
    parts = urlsplit(url)
    if parts.scheme != "https" or not parts.hostname or parts.username or parts.password:
        raise ValueError("请输入公开论文的 HTTPS 链接。")
    if parts.port not in (None, 443):
        raise ValueError("论文链接不能使用非标准端口。")
    # These immutable official entry points also work through fake-IP VPN DNS.
    if parts.hostname not in {"arxiv.org", "www.arxiv.org", "export.arxiv.org", "doi.org"}:
        addresses = socket.getaddrinfo(parts.hostname, 443, type=socket.SOCK_STREAM)
        if not addresses or any(not ipaddress.ip_address(item[4][0]).is_global for item in addresses):
            raise ValueError("论文链接必须指向公开互联网地址。")
    paper, _ = merge_paper(state, {"title": url, "paper_url": url,
                                    "sources": [{"kind": "manual", "url": url}]})
    return paper


def build_site(store, config, destination=None):
    destination = Path(destination or ROOT / ".paper-watch/site")
    destination.mkdir(parents=True, exist_ok=True)
    for path in (ROOT / "web").iterdir():
        if path.is_file():
            shutil.copy2(path, destination / path.name)
    atomic_json(destination / "data/state.json", public_state(store.load(), config))
    return destination


def sync_library(state):
    """Generate a separate source chunk; never rewrite a curated source chunk."""
    selected = [p for p in state["papers"] if p.get("status") == "target" and
                p.get("report", {}).get("status") == "ready" and not p["report"].get("stale")]
    path = ROOT / "research_chunks/09_watch.md"
    if not selected and not path.exists():
        return False
    lines = ["# Paper Watch — accepted papers", "", "Generated from validated target reports by `python -m paper_watch run`.", ""]
    for paper in sorted(selected, key=lambda p: p["id"]):
        values = {"title": paper["title"], "authors": paper.get("authors", ""), "year": paper.get("year", ""),
                  "arxiv_id": paper.get("arxiv_id", ""), "paper_url": paper.get("paper_url", ""),
                  "project_url": paper.get("project_url", ""), "category": paper.get("category") or "Foundation / VLA",
                  # Discovery never verifies official implementation files.
                  "code_status": paper.get("code_status") or "❓ Uncertain",
                  "code_url": paper.get("code_url", ""), "robot_platform": paper.get("robot_platform", ""),
                  "one_line": paper.get("summary") or paper.get("abstract", "")[:600]}
        for key, value in values.items():
            value = " ".join(str(value).split())
            lines.append(("- " if key == "title" else "  ") + key + ": " + value)
        lines.append("")
    content = "\n".join(lines)
    if path.exists() and path.read_text() == content:
        return False
    path.write_text(content, encoding="utf-8")
    subprocess.run([sys.executable, str(ROOT / "build.py")], cwd=ROOT, check=True, capture_output=True, text=True)
    return True


def run_pipeline(store, config, *, eml=(), imap=False, citations=True, network=True,
                 reports=True, max_papers=None, sync=True):
    from . import sources
    from .reports import generate_report
    from .screening import SCREENING_VERSION, screen_paper

    with store.lock():
        state = store.load()
        bootstrap(state, config)
        run = {"id": now(), "started_at": now(), "status": "running", "discovered": 0,
               "added": 0, "screened": 0, "reports_ready": 0, "errors": []}
        run["discovery_attempted"] = bool(eml or (network and (citations or imap or os.getenv("IMAP_USER"))))
        state["runs"].append(run)
        state["runs"] = state["runs"][-90:]
        store.save(state)
        candidates = []

        def discover(name, fn):
            try:
                candidates.extend(fn())
            except Exception as exc:
                candidates.extend(getattr(exc, "candidates", []))
                details = getattr(exc, "errors", None)
                if details:
                    for detail in details:
                        source = str(detail.get("source", name))
                        if detail.get("seed_id"):
                            source += " / " + str(detail["seed_id"])
                        run["errors"].append({"source": source, "message": safe_error(detail.get("message", "Discovery failed"))})
                else:
                    run["errors"].append({"source": name, "message": safe_error(exc)})

        if eml:
            discover("eml", lambda: sources.discover_eml(eml, config["seeds"]))
        if network and citations and config.get("discovery", {}).get("semantic_scholar", True):
            discover("semantic_scholar", lambda: sources.discover_citations(
                config["seeds"], limit=int(config.get("discovery", {}).get("limit_per_seed", 50))))
        if network and (imap or (os.getenv("IMAP_USER") and os.getenv("IMAP_PASSWORD"))):
            os.environ.setdefault("IMAP_HOST", config.get("discovery", {}).get("imap_host", "imap.gmail.com"))
            os.environ.setdefault("IMAP_MAILBOX", config.get("discovery", {}).get("imap_mailbox", "INBOX"))
            os.environ.setdefault("IMAP_LOOKBACK_DAYS", str(config.get("discovery", {}).get("lookback_days", 14)))
            discover("gmail", lambda: sources.discover_imap(config["seeds"]))
        for candidate in candidates:
            try:
                paper, created = merge_paper(state, candidate)
                add_verified_edges(state, paper, config)
                run["discovered"] += 1
                run["added"] += int(created)
            except Exception as exc:
                run["errors"].append({"source": "intake", "message": safe_error(exc)})
        store.save(state)

        limit = max_papers if max_papers is not None else int(config.get("discovery", {}).get("max_papers_per_run", 20))
        scope_hash = hashlib.sha256((SCREENING_VERSION + json.dumps(config.get("scope", {}), sort_keys=True)).encode()).hexdigest()
        # Pending first; already-complete reports never consume the run budget.
        queue = [p for p in state["papers"] if not p.get("is_seed") and (
            p.get("status") == "pending" or
            (p.get("status") == "target" and (p.get("report", {}).get("status") != "ready" or p["report"].get("stale"))) or
            (p.get("status") == "review" and not p.get("abstract")) or
            (p.get("status") in {"target", "review", "excluded"} and not p.get("manual_decision") and
             p.get("screening", {}).get("scope_hash") != scope_hash))]
        # Recheck a bounded number of completed targets, too: a new arXiv
        # revision may keep the title/abstract unchanged and be absent from mail.
        refresh_cutoff = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
        refresh = sorted([p for p in state["papers"] if not p.get("is_seed") and
                          p.get("status") == "target" and p.get("report", {}).get("status") == "ready" and
                          not p["report"].get("stale") and p.get("metadata_checked_at", "") < refresh_cutoff],
                         key=lambda p: p.get("metadata_checked_at", ""))[:5]
        queued_ids = {p["id"] for p in queue}
        queue.extend(p for p in refresh if p["id"] not in queued_ids)
        queue.sort(key=lambda p: (p.get("status") != "pending", p.get("last_processed", "")))
        for paper in queue[:max(0, limit)]:
            if network:
                try:
                    enriched = sources.enrich_paper(paper)
                    if enriched:
                        enriched.setdefault("title", paper["title"])
                        paper, _ = merge_paper(state, enriched, existing_id=paper["id"])
                        paper["metadata_checked_at"] = now()
                except Exception as exc:
                    run["errors"].append({"source": "metadata", "paper_id": paper["id"], "message": safe_error(exc)})
            if not paper.get("manual_decision"):
                paper["screening"] = screen_paper(paper, config)
                paper["screening"]["scope_hash"] = scope_hash
                paper["status"] = paper["screening"]["decision"]
            add_verified_edges(state, paper, config)
            run["screened"] += 1
            needs_report = paper.get("report", {}).get("status") != "ready" or paper.get("report", {}).get("stale")
            if (paper["status"] == "target" and reports and needs_report and not network and
                    paper.get("report", {}).get("status") != "ready" and not os.getenv("OPENAI_API_KEY")):
                paper["report"] = {"status": "blocked", "reason": "未配置 OPENAI_API_KEY，补齐后可重试生成报告。",
                                   "evidence_level": "none", "generated_at": now()}
            if paper["status"] == "target" and reports and network and needs_report:
                try:
                    result = generate_report(paper, config, store.path.parent / "reports")
                    if paper.get("report", {}).get("status") == "ready":
                        history = paper.setdefault("report_history", [])
                        history.append(paper["report"])
                        paper["report_history"] = history[-5:]
                    paper["report"] = result
                    run["reports_ready"] += int(result.get("status") == "ready")
                    if result.get("status") == "failed":
                        run["errors"].append({"source": "report", "paper_id": paper["id"], "message": result.get("reason", "Report failed")})
                except Exception as exc:
                    paper["report"] = {"status": "failed", "reason": safe_error(exc), "generated_at": now()}
                    run["errors"].append({"source": "report", "paper_id": paper["id"], "message": safe_error(exc)})
            paper["last_processed"] = now()
            store.save(state)
        if sync and config.get("sync_library", True):
            try:
                run["library_updated"] = sync_library(state)
            except Exception as exc:
                run["errors"].append({"source": "library", "message": safe_error(exc)})
        run["finished_at"] = now()
        run["status"] = "partial" if run["errors"] else "completed"
        store.save(state)
    build_site(store, config)
    return run
