import copy
import csv
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from paper_watch.publish import prepare_snapshot, publish


class PublishTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / "config").mkdir()
        self.config = {"seeds": [{"id": "arxiv:2410.24221", "title": "Seed paper",
                                  "arxiv_id": "2410.24221", "paper_url": "https://arxiv.org/abs/2410.24221"}]}
        (self.root / "config/paper-watch.json").write_text(json.dumps(self.config))
        self.snapshot = self.root / "data/paper-watch.json"
        self.csv = self.root / "papers.csv"
        self.state = {"schema_version": 1, "papers": [
            {"id": "arxiv:2610.00001", "title": "Enriched official title", "arxiv_id": "2610.00001",
             "abstract": "Verified full abstract", "paper_url": "https://arxiv.org/abs/2610.00001",
             "status": "target", "summary": "Old summary", "code_status": "❓ Uncertain",
             "code_url": "https://github.com/old/repo", "seed_ids": ["arxiv:2410.24221"],
             "sources": [{"kind": "semantic_scholar", "message_id": "private-message",
                          "url": "https://api.semanticscholar.org/graph/v1/paper/ARXIV:2610.00001"}],
             "screening": {"decision": "target", "reason": "Relevant human demonstrations"},
             "report": {"status": "ready", "markdown": "Verified report", "path": "/private/report.md"},
             "raw_email": "PRIVATE EMAIL BODY"},
            {"id": "arxiv:2410.24221", "title": "Seed paper", "arxiv_id": "2410.24221",
             "status": "library", "is_seed": True, "sources": [], "seed_ids": [], "report": {}}
        ], "edges": [{"source": "arxiv:2610.00001", "target": "arxiv:2410.24221", "kind": "cites",
                      "evidence_url": "https://api.semanticscholar.org/graph/v1/paper/ARXIV:2410.24221/citations"}],
            "runs": []}
        self.write_snapshot(self.state)
        self.write_csv([{"title": "Older CSV title", "paper_url": "https://arxiv.org/abs/2610.00001",
                         "summary": "Weekly corrected summary", "code_status": "❌ No Code", "code_url": "",
                         "project_url": "https://example.org/project", "category": "Whole-body Control",
                         "year": "2026", "robot_platform": "G1"}])

    def write_snapshot(self, state):
        self.snapshot.parent.mkdir(exist_ok=True)
        self.snapshot.write_text(json.dumps(state))

    def write_csv(self, rows):
        fields = list(dict.fromkeys(key for row in rows for key in row))
        with self.csv.open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

    def test_weekly_metadata_replaces_old_claims_and_preserves_evidence(self):
        state = prepare_snapshot(self.snapshot, self.csv, self.config)
        paper = next(p for p in state["papers"] if p["id"] == "arxiv:2610.00001")
        self.assertEqual(paper["title"], "Enriched official title")
        self.assertEqual(paper["abstract"], "Verified full abstract")
        self.assertEqual(paper["summary"], "Weekly corrected summary")
        self.assertEqual(paper["code_status"], "❌ No Code")
        self.assertNotIn("code_url", paper)
        self.assertEqual(paper["category"], "Whole-body Control")
        self.assertEqual(paper["robot_platform"], "G1")
        self.assertEqual(paper["status"], "target")
        self.assertEqual(paper["report"], {"status": "ready", "markdown": "Verified report"})
        self.assertEqual(paper["screening"], self.state["papers"][0]["screening"])
        self.assertEqual(state["edges"], self.state["edges"])

    def test_weekly_new_paper_and_seed_are_added_without_fabricated_evidence(self):
        self.write_csv([{"title": "A new weekly paper", "paper_url": "https://arxiv.org/abs/2610.00002"}])
        state = prepare_snapshot(self.snapshot, self.csv, self.config)
        self.assertEqual(len(state["papers"]), 3)
        new = next(p for p in state["papers"] if p["id"] == "arxiv:2610.00002")
        self.assertEqual(new["status"], "library")
        self.assertEqual(new["report"], {})
        self.assertEqual(state["stats"]["citations"], 1)

    def test_export_never_reads_environment_mailbox_or_private_store(self):
        private = self.root / ".paper-watch/state.json"
        private.parent.mkdir()
        private.write_text("PRIVATE LOCAL STORE")
        (self.root / ".env").write_text("OPENAI_API_KEY=PRIVATE KEY")
        original = self.snapshot.read_bytes()
        with patch("imaplib.IMAP4_SSL") as mailbox, patch("urllib.request.urlopen") as network:
            state = publish(root=self.root)
        mailbox.assert_not_called()
        network.assert_not_called()
        self.assertEqual(private.read_text(), "PRIVATE LOCAL STORE")
        self.assertEqual(self.snapshot.read_bytes(), original)
        output = self.root / "_site"
        self.assertTrue((output / "index.html").is_file())
        self.assertTrue((output / "app.js").is_file())
        self.assertTrue((output / ".nojekyll").is_file())
        exported = (output / "data/state.json").read_text()
        for secret in ("PRIVATE", "private-message", "/private/report.md", "raw_email"):
            self.assertNotIn(secret, exported)
        self.assertEqual(json.loads(exported), state)

    def test_explicit_snapshot_update_remains_sanitized_and_repeatable(self):
        first = publish(root=self.root, write_snapshot=True)
        second = publish(root=self.root, write_snapshot=True)
        self.assertEqual(first["stats"], second["stats"])
        self.assertEqual(first["edges"], second["edges"])
        self.assertEqual(len(second["papers"]), 2)
        self.assertEqual(json.loads(self.snapshot.read_text()), second)
        self.assertNotIn("raw_email", self.snapshot.read_text())

    def test_missing_snapshot_can_build_a_fresh_csv_library(self):
        self.snapshot.unlink()
        state = publish(root=self.root)
        self.assertEqual(state["stats"]["papers"], 2)
        self.assertEqual(state["stats"]["citations"], 0)
        self.assertEqual(state["stats"]["reports_ready"], 0)
        self.assertFalse(self.snapshot.exists())

    def test_invalid_snapshot_fails_without_exporting_or_overwriting(self):
        for transform in (
                lambda state: state.update(schema_version=2),
                lambda state: state["papers"].append(copy.deepcopy(state["papers"][0])),
                lambda state: state["edges"][0].update(target="missing")):
            state = copy.deepcopy(self.state)
            transform(state)
            self.write_snapshot(state)
            original = self.snapshot.read_bytes()
            with self.assertRaises(ValueError):
                publish(root=self.root, write_snapshot=True)
            self.assertEqual(self.snapshot.read_bytes(), original)
            self.assertFalse((self.root / "_site").exists())

    def test_private_local_state_cannot_be_overwritten(self):
        private = self.root / ".paper-watch/state.json"
        with self.assertRaisesRegex(ValueError, "private local state"):
            publish(root=self.root, snapshot=private, write_snapshot=True)
        self.assertFalse(private.exists())


if __name__ == "__main__":
    unittest.main()
