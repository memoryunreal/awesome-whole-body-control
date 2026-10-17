import csv
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from paper_watch import pipeline
from paper_watch.store import ROOT, Store, add_verified_edges, arxiv_id, bootstrap, load_config, merge_paper, public_state


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.store = Store(self.root / "state.json")
        self.config = load_config()
        self.state = self.store.load()

    def test_arxiv_versions_deduplicate_without_losing_report(self):
        first, created = merge_paper(self.state, {"title": "A robot paper", "paper_url": "https://arxiv.org/abs/2410.24221v1"})
        first["report"] = {"status": "ready", "markdown": "kept"}
        second, duplicate = merge_paper(self.state, {"title": "Revised robot title", "arxiv_id": "2410.24221v2", "abstract": "New abstract"})
        self.assertTrue(created)
        self.assertFalse(duplicate)
        self.assertEqual(first["id"], second["id"])
        self.assertEqual(len(self.state["papers"]), 1)
        self.assertEqual(second["report"]["markdown"], "kept")
        self.assertTrue(second["report"]["stale"])

    def test_whole_titles_not_prefixes_and_unicode_identity(self):
        for title in ("Learning Robots From Human Videos One", "Learning Robots From Human Videos Two", "机器人学习"):
            merge_paper(self.state, {"title": title})
        merge_paper(self.state, {"title": "机器人学习"})
        self.assertEqual(len(self.state["papers"]), 3)

    def test_same_title_promotes_identity_without_losing_local_id(self):
        first, _ = merge_paper(self.state, {"title": "A paper"})
        identity = first["id"]
        second, created = merge_paper(self.state, {"title": "A paper", "arxiv_id": "2410.24221"})
        self.assertFalse(created)
        self.assertEqual(second["id"], identity)
        third, created = merge_paper(self.state, {"title": "New title", "arxiv_id": "2410.24221"})
        self.assertFalse(created)
        self.assertEqual(third["id"], identity)

    def test_same_title_with_conflicting_arxiv_or_doi_remains_separate(self):
        for identifiers in (({"arxiv_id": "2601.11111"}, {"arxiv_id": "2601.22222"}),
                            ({"doi": "10.1234/first"}, {"doi": "10.1234/second"})):
            state = self.store.load()
            first, _ = merge_paper(state, {"title": "A Survey of Robot Learning", **identifiers[0]})
            second, created = merge_paper(state, {"title": "A Survey of Robot Learning", **identifiers[1]})
            self.assertTrue(created)
            self.assertNotEqual(first["id"], second["id"])
            self.assertEqual(len(state["papers"]), 2)
            for key, value in identifiers[0].items():
                self.assertEqual(first[key], value)

    def test_ambiguous_title_only_discovery_is_stable_without_reusing_known_id(self):
        original, _ = merge_paper(self.state, {"title": "Same Title"})
        old_id = original["id"]
        merge_paper(self.state, {"title": "Same Title", "arxiv_id": "2601.11111"})
        merge_paper(self.state, {"title": "Same Title", "arxiv_id": "2601.22222"})
        unidentified, created = merge_paper(self.state, {"title": "Same Title"})
        repeated, created_again = merge_paper(self.state, {"title": "Same Title"})
        self.assertTrue(created)
        self.assertFalse(created_again)
        self.assertEqual(unidentified["id"], repeated["id"])
        self.assertNotEqual(unidentified["id"], old_id)
        self.assertEqual(original["id"], old_id)
        self.assertEqual(len({paper["id"] for paper in self.state["papers"]}), 3)

    def test_arxiv_url_requires_official_host_and_supports_legacy_identifiers(self):
        self.assertEqual(arxiv_id("https://example.org/abs/2410.24221"), "")
        self.assertEqual(arxiv_id("https://arxiv.org.evil.org/abs/2410.24221"), "")
        self.assertEqual(arxiv_id("https://arxiv.org/pdf/hep-th/9901001v2.pdf"), "hep-th/9901001")
        self.assertEqual(arxiv_id("arxiv:hep-th/9901001v1"), "hep-th/9901001")
        seed, _ = merge_paper(self.state, {"title": "Real seed", "arxiv_id": "2410.24221"})
        unrelated, created = merge_paper(self.state, {"title": "Other title", "paper_url": "https://example.org/abs/2410.24221"})
        self.assertTrue(created)
        self.assertNotEqual(seed["id"], unrelated["id"])
        self.assertEqual(seed["title"], "Real seed")
        self.assertNotIn("arxiv_id", unrelated)

    def test_only_verified_citations_create_edges(self):
        bootstrap(self.state, self.config, self.root / "missing.csv")
        paper, _ = merge_paper(self.state, {"title": "A follow-up", "arxiv_id": "2610.00001", "sources": [
            {"kind": "scholar_email", "relation": "mentions", "seed_id": "arxiv:2410.24221", "evidence_url": "https://scholar.google.com"},
            {"kind": "semantic_scholar", "relation": "cites", "seed_id": "arxiv:2410.24221", "evidence_url": "https://api.semanticscholar.org/graph/v1/paper/ARXIV:2410.24221/citations"}
        ]})
        add_verified_edges(self.state, paper, self.config)
        add_verified_edges(self.state, paper, self.config)
        self.assertEqual(len(self.state["edges"]), 1)
        self.assertEqual(self.state["edges"][0]["source"], paper["id"])
        self.assertEqual(self.state["edges"][0]["target"], "arxiv:2410.24221")

    def test_atomic_storage_and_process_lock(self):
        self.store.save(self.state)
        self.assertEqual(self.store.load()["schema_version"], 1)
        with self.store.lock():
            with self.assertRaises(RuntimeError):
                with Store(self.store.path).lock():
                    pass
        with self.store.lock():
            pass

    def test_public_export_strips_mail_and_local_paths(self):
        paper, _ = merge_paper(self.state, {"title": "A paper", "raw_email": "private", "sources": [
            {"kind": "scholar_email", "message_id": "private-id", "mailbox": "me@example.com", "url": "https://arxiv.org/abs/2410.24221"}
        ]})
        paper["report"] = {"status": "ready", "path": "/private/report.md", "markdown": "public report"}
        public = json.dumps(public_state(self.state, self.config))
        for value in ("private-id", "me@example.com", "/private/report.md", "raw_email", "message_id"):
            self.assertNotIn(value, public)
        self.assertIn("public report", public)

    def test_public_export_removes_local_source_urls_and_error_paths(self):
        paper, _ = merge_paper(self.state, {"title": "A paper", "project_url": "file:///Users/research/private/notes", "sources": [
            {"kind": "google_scholar_email", "url": "file:///Users/research/private/alert.eml", "evidence_url": "imap-message://scholar/345", "relation": "mentions"},
            {"kind": "manual", "url": "https://reader:password@example.org/paper"},
            {"kind": "metadata", "url": "http://127.0.0.1/private"},
            {"kind": "arxiv_metadata", "url": "https://export.arxiv.org/api/query?id_list=2410.24221"},
        ]})
        self.state["runs"].append({"id": "1", "errors": [{"source": "eml", "message": "Cannot read /Users/research/private/alert.eml", "path": "/tmp/raw"}]})
        public = json.dumps(public_state(self.state, self.config))
        for secret in ("/Users/", "imap-message:", "reader:password", "127.0.0.1", "/tmp/raw"):
            self.assertNotIn(secret, public)
        self.assertIn("export.arxiv.org", public)
        self.assertEqual(len(public_state(self.state, self.config)["papers"][0]["sources"]), 4)
        self.assertEqual(paper["sources"][0]["evidence_url"], "imap-message://scholar/345")

    def test_ready_report_count_excludes_stale_reports(self):
        first, _ = merge_paper(self.state, {"title": "Current report"})
        second, _ = merge_paper(self.state, {"title": "Old report"})
        first["report"] = {"status": "ready", "markdown": "Current"}
        second["report"] = {"status": "ready", "markdown": "Old", "stale": True}
        self.assertEqual(public_state(self.state, self.config)["stats"]["reports_ready"], 1)

    def test_bootstrap_preserves_decision(self):
        path = self.root / "papers.csv"
        with path.open("w") as handle:
            writer = csv.DictWriter(handle, fieldnames=["title", "paper_url"])
            writer.writeheader()
            writer.writerow({"title": "A paper", "paper_url": "https://arxiv.org/abs/2610.00001"})
        bootstrap(self.state, self.config, path)
        self.state["papers"][0]["status"] = "excluded"
        bootstrap(self.state, self.config, path)
        self.assertEqual(self.state["papers"][0]["status"], "excluded")

    def test_bootstrap_only_fills_missing_metadata_and_merges_sources(self):
        paper, _ = merge_paper(self.state, {"title": "Updated official title", "arxiv_id": "2601.12345", "authors": "Verified Author", "abstract": "Verified abstract", "arxiv_version": 2,
                                           "sources": [{"kind": "arxiv_metadata", "url": "https://export.arxiv.org/api/query?id_list=2601.12345"}]}, "target")
        paper["report"] = {"status": "ready", "markdown": "Verified report"}
        old_id = paper["id"]
        path = self.root / "papers.csv"
        with path.open("w") as handle:
            writer = csv.DictWriter(handle, fieldnames=["title", "arxiv_id", "authors", "summary", "paper_url"])
            writer.writeheader()
            writer.writerow({"title": "Old title", "arxiv_id": "2601.12345", "authors": "Old Author", "summary": "Curated summary", "paper_url": "https://arxiv.org/abs/2601.12345"})
        for _ in range(2):
            bootstrap(self.state, {"seeds": []}, path)
        self.assertEqual(paper["id"], old_id)
        self.assertEqual(paper["title"], "Updated official title")
        self.assertEqual(paper["authors"], "Verified Author")
        self.assertEqual(paper["summary"], "Curated summary")
        self.assertEqual(paper["status"], "target")
        self.assertNotIn("stale", paper["report"])
        self.assertEqual(len(paper["sources"]), 2)

    def test_existing_corpus_is_idempotent_on_repeat_bootstrap(self):
        bootstrap(self.state, {"seeds": []}, ROOT / "papers.csv")
        count = len(self.state["papers"])
        self.assertGreater(count, 0)
        identities = [paper["id"] for paper in self.state["papers"]]
        self.assertEqual(len(set(identities)), count)
        bootstrap(self.state, {"seeds": []}, ROOT / "papers.csv")
        self.assertEqual([paper["id"] for paper in self.state["papers"]], identities)

    def test_manual_intake_rejects_local_http_and_credentials(self):
        for url in ("http://arxiv.org/abs/2610.00001", "https://user:secret@arxiv.org/", "https://127.0.0.1/"):
            with self.assertRaises(ValueError):
                pipeline.ingest_url(self.state, url)

    def test_no_network_pipeline_and_resume(self):
        candidate = {"title": "Egocentric Human Video Robot Learning", "arxiv_id": "2610.00001", "abstract": "We study egocentric robot learning from human video. " * 8}
        with patch("paper_watch.sources.discover_eml", return_value=[candidate]), \
             patch("paper_watch.sources.discover_citations") as remote, \
             patch("paper_watch.sources.enrich_paper") as enrich, \
             patch("paper_watch.pipeline.bootstrap"), \
             patch("paper_watch.pipeline.build_site"):
            first = pipeline.run_pipeline(self.store, self.config, eml=["unused"], network=False, sync=False)
            second = pipeline.run_pipeline(self.store, self.config, eml=["unused"], network=False, sync=False)
        remote.assert_not_called()
        enrich.assert_not_called()
        self.assertEqual(first["added"], 1)
        self.assertEqual(second["added"], 0)
        self.assertEqual(len(self.store.load()["papers"]), 1)
        self.assertEqual(first["reports_ready"], 0)

    def test_failed_source_keeps_partial_discoveries(self):
        from paper_watch.sources import SourceError
        error = SourceError([{"source": "test", "message": "unavailable"}], [{"title": "A paper"}])
        with patch("paper_watch.sources.discover_eml", side_effect=error), \
             patch("paper_watch.pipeline.bootstrap"), patch("paper_watch.pipeline.build_site"):
            result = pipeline.run_pipeline(self.store, self.config, eml=["unused"], network=False, sync=False)
        self.assertEqual(result["status"], "partial")
        self.assertEqual(result["added"], 1)
        self.assertEqual(len(self.store.load()["papers"]), 1)

    def test_credentials_redacted_from_failure(self):
        with patch.dict(os.environ, {"IMAP_PASSWORD": "sample-private-password", "IMAP_USER": "me@example.com"}):
            result = pipeline.safe_error(ValueError("login me@example.com sample-private-password"))
        self.assertNotIn("me@example.com", result)
        self.assertNotIn("sample-private-password", result)

    def test_metadata_update_preserves_manual_exclusion(self):
        paper, _ = merge_paper(self.state, {"title": "A paper", "arxiv_id": "2610.00001"})
        paper["status"] = "excluded"
        paper["manual_decision"] = {"decision": "excluded", "reason": "out of scope"}
        merge_paper(self.state, {"title": "A paper", "arxiv_id": "2610.00001", "abstract": "New abstract"})
        self.assertEqual(paper["status"], "excluded")

    def test_plural_videos_and_vlas_are_in_scope(self):
        from paper_watch.screening import screen_paper
        paper = {"title": "Learning VLAs from Human Videos", "abstract": "We use human videos for cross-embodiment robot learning. " * 4}
        result = screen_paper(paper, self.config)
        self.assertEqual(result["decision"], "target")
        self.assertIn("human video", [e["term"] for e in result["evidence"]])

    def test_enrichment_corrects_url_placeholder_without_duplicate(self):
        paper, _ = merge_paper(self.state, {"title": "https://publisher.example/paper", "paper_url": "https://publisher.example/paper"})
        updated, created = merge_paper(self.state, {"title": "Resolved paper", "arxiv_id": "2610.00001"}, existing_id=paper["id"])
        self.assertFalse(created)
        self.assertEqual(len(self.state["papers"]), 1)
        self.assertEqual(updated["title"], "Resolved paper")

    def test_two_intake_urls_merge_when_resolved_to_one_paper(self):
        canonical, _ = merge_paper(self.state, {"title": "Known paper", "arxiv_id": "2610.00001"})
        placeholder, _ = merge_paper(self.state, {"title": "https://publisher.example/paper"})
        merged, created = merge_paper(self.state, {"title": "Known paper", "arxiv_id": "2610.00001"}, existing_id=placeholder["id"])
        self.assertEqual(len(self.state["papers"]), 1)
        self.assertEqual(merged["id"], canonical["id"])
        self.assertFalse(created)


if __name__ == "__main__":
    unittest.main()
