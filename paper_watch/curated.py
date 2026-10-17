"""Load source-checked editorial reports without requiring a model API key."""

import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit

from .store import merge_paper


def apply_curated_reports(state, root):
    directory = Path(root) / "reports/curated"
    manifest = directory / "index.json"
    if not manifest.exists():
        return
    catalog = json.loads(manifest.read_text(encoding="utf-8"))
    if catalog.get("schema_version") != 1 or not isinstance(catalog.get("reports"), list):
        raise ValueError("Unsupported curated report manifest")
    seen = set()
    for entry in catalog["reports"]:
        identifier = entry["id"]
        if identifier != "arxiv:" + entry["arxiv_id"]:
            raise ValueError("Curated report ID must match its arXiv identifier")
        if identifier in seen:
            raise ValueError("Duplicate curated report ID")
        seen.add(identifier)
        path = (directory / entry["report_file"]).resolve()
        if not path.is_relative_to(directory.resolve()) or path.suffix != ".md":
            raise ValueError("Curated report path must remain within reports/curated")
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        if digest != entry.get("sha256"):
            raise ValueError(f"Curated report changed after source review: {entry['report_file']}")
        markdown = raw.decode("utf-8")
        if len(markdown.strip()) < 1000 or not markdown.startswith("# "):
            raise ValueError("Curated reports must contain a substantive Markdown explanation")
        review = entry.get("review", {})
        if review.get("status") != "source_checked" or not review.get("checked_at"):
            raise ValueError("Curated report has no completed source review")
        sources = review.get("sources", [])
        if not sources or any(urlsplit(url).scheme != "https" or not urlsplit(url).hostname for url in sources):
            raise ValueError("Curated report must cite public HTTPS primary sources")
        paper, _ = merge_paper(state, {
            "title": entry["title"], "arxiv_id": entry["arxiv_id"],
            "paper_url": entry["paper_url"], "project_url": entry.get("project_url", ""),
            "sources": [{"kind": "curated_report", "url": entry["paper_url"]}],
        }, "library", fill_missing=True)
        if paper.get("arxiv_id") != entry["arxiv_id"]:
            raise ValueError("Curated report identity does not match its paper")
        paper["report"] = {
            "status": "ready", "markdown": markdown, "generated_at": review["checked_at"],
            "evidence_level": "原文核查 · AI 辅助精读", "reason": "已对照论文与官方项目核查；未运行复现实验。",
            "curated": True, "organization": entry["organization"], "summary": entry["summary"],
            "selection_reason": entry["selection_reason"], "priority": entry.get("priority", 100),
            "source_version": review["source_version"], "source_urls": sources, "sha256": digest,
        }
        for citation in entry.get("citations", []):
            target = citation["target"]
            evidence_url = citation["evidence_url"]
            if not any(p["id"] == target for p in state["papers"]):
                raise ValueError("Curated citation target is missing from the library")
            if (urlsplit(evidence_url).scheme != "https" or not urlsplit(evidence_url).hostname
                    or not citation.get("evidence")):
                raise ValueError("Curated citations require a primary-source excerpt and URL")
            edge = {"source": paper["id"], "target": target, "kind": "cites",
                    "evidence_url": evidence_url, "provenance": "paper_references"}
            if not any(e["source"] == edge["source"] and e["target"] == target for e in state["edges"]):
                state["edges"].append(edge)
