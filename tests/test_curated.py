import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from paper_watch.curated import apply_curated_reports
from paper_watch.store import public_state


class CuratedReportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.directory = self.root / "reports/curated"
        self.directory.mkdir(parents=True)
        content = "# Source-checked explanation\n\n" + "Method, evidence, interpretation and limitations.\n" * 30
        self.report = self.directory / "paper.md"
        self.report.write_text(content)
        self.entry = {"id": "arxiv:2602.16710", "arxiv_id": "2602.16710", "title": "Example paper",
                      "paper_url": "https://arxiv.org/abs/2602.16710", "report_file": "paper.md",
                      "sha256": hashlib.sha256(self.report.read_bytes()).hexdigest(),
                      "organization": "Verified organization", "summary": "What this explanation covers",
                      "selection_reason": "Relevant method with direct experimental evidence",
                      "review": {"status": "source_checked", "checked_at": "2026-10-17T00:00:00+00:00",
                                 "source_version": "v1", "sources": ["https://arxiv.org/html/2602.16710v1"]}}
        self.state = {"schema_version": 1, "papers": [], "edges": [], "runs": []}
        self.write_manifest()

    def write_manifest(self):
        (self.directory / "index.json").write_text(json.dumps({"schema_version": 1, "reports": [self.entry]}))

    def test_curated_report_is_ready_without_api_credentials(self):
        apply_curated_reports(self.state, self.root)
        report = self.state["papers"][0]["report"]
        self.assertEqual(report["status"], "ready")
        self.assertTrue(report["curated"])
        self.assertIn("未运行复现实验", report["reason"])
        public = public_state(self.state, {})
        self.assertEqual(public["stats"]["reports_ready"], 1)
        self.assertEqual(public["papers"][0]["report"]["organization"], "Verified organization")

    def test_reviewed_content_hash_is_enforced(self):
        self.report.write_text(self.report.read_text() + "\nChanged factual claim")
        with self.assertRaisesRegex(ValueError, "changed after source review"):
            apply_curated_reports(self.state, self.root)

    def test_unreviewed_content_is_not_published(self):
        self.entry["review"]["status"] = "draft"
        self.write_manifest()
        with self.assertRaisesRegex(ValueError, "source review"):
            apply_curated_reports(self.state, self.root)

    def test_path_escape_is_rejected(self):
        self.entry["report_file"] = "../private.md"
        self.write_manifest()
        with self.assertRaisesRegex(ValueError, "within"):
            apply_curated_reports(self.state, self.root)

    def test_existing_paper_and_edges_are_preserved(self):
        self.state["papers"] = [{"id": "arxiv:2602.16710", "arxiv_id": "2602.16710", "title": "Example paper",
                                 "is_seed": True, "status": "library", "sources": [], "seed_ids": []}]
        apply_curated_reports(self.state, self.root)
        apply_curated_reports(self.state, self.root)
        self.assertEqual(len(self.state["papers"]), 1)
        self.assertTrue(self.state["papers"][0]["is_seed"])
        self.assertEqual(self.state["papers"][0]["status"], "library")

    def test_verified_citation_is_directional_and_not_duplicated(self):
        target = "arxiv:2410.24221"
        self.state["papers"] = [{"id": target, "arxiv_id": "2410.24221", "title": "EgoMimic"}]
        self.entry["citations"] = [{"target": target, "evidence_url": "https://arxiv.org/html/2602.16710v1#bib.bib3",
                                    "evidence": "EgoMimic: scaling imitation learning via egocentric video."}]
        self.write_manifest()
        apply_curated_reports(self.state, self.root)
        apply_curated_reports(self.state, self.root)
        self.assertEqual(len(self.state["edges"]), 1)
        self.assertEqual(self.state["edges"][0]["source"], self.entry["id"])
        self.assertEqual(self.state["edges"][0]["target"], target)
        self.assertEqual(self.state["edges"][0]["provenance"], "paper_references")
        self.assertEqual(public_state(self.state, {})["edges"], self.state["edges"])

    def test_citation_without_source_excerpt_is_rejected(self):
        self.entry["citations"] = [{"target": self.entry["id"], "evidence_url": "https://arxiv.org/"}]
        self.write_manifest()
        with self.assertRaisesRegex(ValueError, "primary-source excerpt"):
            apply_curated_reports(self.state, self.root)

    def test_identifier_must_match_paper(self):
        self.entry["id"] = "arxiv:2410.24221"
        self.write_manifest()
        with self.assertRaisesRegex(ValueError, "match its arXiv"):
            apply_curated_reports(self.state, self.root)


if __name__ == "__main__":
    unittest.main()
