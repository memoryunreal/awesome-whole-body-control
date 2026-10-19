"""Validate the editorial reading subset before publishing its public assets."""

import json
from pathlib import Path

from .sources import arxiv_id_from_url


def validate_focus_subset(state, root):
    path = Path(root) / "web/focus.json"
    if not path.exists():
        return
    catalog = json.loads(path.read_text(encoding="utf-8"))
    if catalog.get("schema_version") != 1 or not isinstance(catalog.get("entries"), list):
        raise ValueError("Unsupported focus subset schema")
    fraction, deep_fraction = catalog["target_fraction"], catalog["deep_fraction"]
    if not 0 < fraction < 1 or not 0 < deep_fraction < 1:
        raise ValueError("Focus fractions must be between zero and one")
    entries = catalog["entries"]
    if len(entries) != round(catalog["library_size_at_review"] * fraction):
        raise ValueError("Focus selection does not match its reviewed library budget")
    if sum(entry.get("deep_read") is True for entry in entries) != round(len(entries) * deep_fraction):
        raise ValueError("Focus deep reading selection does not match its budget")
    groups = {group["id"] for group in catalog["groups"]}
    papers = {paper["id"]: paper for paper in state["papers"]}
    ids, arxiv_ids, ranks = set(), set(), set()
    for entry in entries:
        identifier, aid = entry["paper_id"], entry["arxiv_id"]
        if identifier in ids or aid in arxiv_ids or entry["rank"] in ranks:
            raise ValueError("Duplicate focus paper, arXiv ID or reading rank")
        ids.add(identifier)
        arxiv_ids.add(aid)
        ranks.add(entry["rank"])
        paper = papers.get(identifier)
        if paper is None:
            raise ValueError("Focus paper is missing from the published library")
        if (arxiv_id_from_url(paper.get("arxiv_id", "")) or
                arxiv_id_from_url(paper.get("paper_url", ""))) != aid:
            raise ValueError("Focus paper identity differs from its verified source")
        if entry["source_url"] != "https://arxiv.org/abs/" + aid:
            raise ValueError("Focus entries require the verified arXiv source")
        if (entry["group"] not in groups or entry["tier"] not in {"主线", "支撑"}
                or not all(entry.get(key) for key in ("short_name", "verified_title", "reason", "source_level"))
                or not isinstance(entry["deep_read"], bool)):
            raise ValueError("Focus entry lacks its selection rationale or classification")
        if entry["deep_read"]:
            report = paper.get("report", {})
            if (report.get("status") != "ready" or report.get("stale") or
                    not report.get("curated") or len(report.get("markdown", "")) < 1000):
                raise ValueError("Focus deep reading has no completed, current source-checked report")
    if ranks != set(range(1, len(entries) + 1)):
        raise ValueError("Focus reading ranks must be consecutive")
