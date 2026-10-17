import copy
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from paper_watch.pipeline import run_pipeline, sync_library
from paper_watch.store import Store, load_config, merge_paper


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.store = Store(self.root / "state.json")
        self.config = load_config()

    def test_ready_report_revision_refreshes_once_and_keeps_history(self):
        state = self.store.load()
        paper, _ = merge_paper(state, {"title": "Egocentric Robot Learning from Human Videos", "arxiv_id": "2610.00001", "abstract": "Egocentric robot learning with human video. " * 8, "arxiv_version": 1})
        paper["status"] = "target"
        paper["report"] = {"status": "ready", "markdown": "version one"}
        self.store.save(state)
        updated = {**copy.deepcopy(paper), "arxiv_version": 2}
        with patch("paper_watch.pipeline.bootstrap"), patch("paper_watch.pipeline.build_site"), \
             patch("paper_watch.sources.enrich_paper", return_value=updated) as metadata, \
             patch("paper_watch.reports.generate_report", return_value={"status": "ready", "markdown": "version two"}) as generator:
            run_pipeline(self.store, self.config, citations=False, sync=False)
            run_pipeline(self.store, self.config, citations=False, sync=False)
        current = self.store.load()["papers"][0]
        self.assertEqual(current["report"]["markdown"], "version two")
        self.assertEqual(current["report_history"][0]["markdown"], "version one")
        self.assertEqual(generator.call_count, 1)
        self.assertEqual(metadata.call_count, 1)

    def test_export_to_curated_list_requires_current_ready_target(self):
        (self.root / "research_chunks").mkdir()
        state = self.store.load()
        for index, (status, report) in enumerate([
            ("target", {"status": "ready"}), ("target", {"status": "blocked"}),
            ("target", {"status": "ready", "stale": True}), ("excluded", {"status": "ready"})
        ]):
            paper, _ = merge_paper(state, {"title": f"Paper {index}", "arxiv_id": f"2610.0000{index}"})
            paper.update(status=status, report=report)
        with patch("paper_watch.pipeline.ROOT", self.root), patch("paper_watch.pipeline.subprocess.run") as build:
            self.assertTrue(sync_library(state))
            self.assertFalse(sync_library(state))
        content = (self.root / "research_chunks/09_watch.md").read_text()
        self.assertIn("Paper 0", content)
        self.assertIn("❓ Uncertain", content)
        for index in (1, 2, 3):
            self.assertNotIn(f"Paper {index}", content)
        build.assert_called_once()


if __name__ == "__main__":
    unittest.main()
