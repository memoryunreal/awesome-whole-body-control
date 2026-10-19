import copy
import json
import tempfile
import unittest
from pathlib import Path

from paper_watch.curated import apply_curated_reports
from paper_watch.focus import validate_focus_subset
from paper_watch.publish import prepare_snapshot
from paper_watch.store import ROOT, load_config


class FocusSubsetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / "web/focus.json").read_text())
        cls.state = prepare_snapshot(ROOT / "data/paper-watch.json", ROOT / "papers.csv", load_config())
        apply_curated_reports(cls.state, ROOT)

    def validate(self, catalog=None, state=None):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "web").mkdir()
            (root / "web/focus.json").write_text(json.dumps(catalog or self.catalog))
            validate_focus_subset(state or self.state, root)

    def test_reviewed_subset_fits_budgets_and_has_all_completed_reports(self):
        self.validate()
        self.assertEqual(len(self.catalog["entries"]), 39)
        deep = [entry for entry in self.catalog["entries"] if entry["deep_read"]]
        self.assertEqual(len(deep), 8)
        self.assertEqual({entry["short_name"] for entry in deep},
                         {"HOMIE", "FALCON", "ULC", "SkillBlender", "VIRAL", "WholeBodyVLA", "GRAIL", "OpenHLM"})
        self.assertLessEqual(sum(entry["tier"] == "支撑" for entry in self.catalog["entries"]), 5)

    def test_missing_library_paper_prevents_publication(self):
        state = copy.deepcopy(self.state)
        target = self.catalog["entries"][0]["paper_id"]
        state["papers"] = [paper for paper in state["papers"] if paper["id"] != target]
        with self.assertRaisesRegex(ValueError, "missing from the published library"):
            self.validate(state=state)

    def test_blocked_or_stale_report_cannot_count_as_focus_deep_reading(self):
        for report in ({"status": "blocked"}, {"status": "ready", "stale": True}):
            state = copy.deepcopy(self.state)
            paper = next(p for p in state["papers"] if p["id"] == self.catalog["entries"][0]["paper_id"])
            paper["report"].update(report)
            with self.assertRaisesRegex(ValueError, "no completed, current"):
                self.validate(state=state)

    def test_duplicate_paper_and_wrong_source_are_rejected(self):
        catalog = copy.deepcopy(self.catalog)
        catalog["entries"][1]["paper_id"] = catalog["entries"][0]["paper_id"]
        with self.assertRaisesRegex(ValueError, "Duplicate focus"):
            self.validate(catalog=catalog)
        catalog = copy.deepcopy(self.catalog)
        catalog["entries"][0]["source_url"] = "https://arxiv.org/abs/0000.00000"
        with self.assertRaisesRegex(ValueError, "verified arXiv source"):
            self.validate(catalog=catalog)

    def test_more_report_labels_do_not_satisfy_the_reading_budget(self):
        catalog = copy.deepcopy(self.catalog)
        catalog["entries"][8]["deep_read"] = True
        with self.assertRaisesRegex(ValueError, "deep reading selection"):
            self.validate(catalog=catalog)


if __name__ == "__main__":
    unittest.main()
