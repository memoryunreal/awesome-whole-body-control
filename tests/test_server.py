"""Real loopback HTTP integration tests, isolated from network and user state."""

import http.client
import ipaddress
import json
import socket
import tempfile
import threading
import time
import unittest
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.parse import quote
from unittest.mock import patch

from paper_watch.server import make_handler
from paper_watch.store import Store, merge_paper


class LocalServerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.site = self.root / "site"
        self.site.mkdir()
        (self.site / "index.html").write_text("<!doctype html><title>Test research workspace</title>")
        self.store = Store(self.root / "state.json")
        self.config = {
            "seeds": [],
            "scope": {"description": "Robot imitation learning", "positive_terms": ["robot"]},
            "schedule": {"timezone": "Asia/Shanghai", "hour": 8, "minute": 0},
            "discovery": {"semantic_scholar": False},
            "llm": {"api_key": "private-config-key", "base_url": "https://private-model.example/v1"},
            "private_path": "/Users/private/research/key.json",
        }
        state = self.store.load()
        self.paper, _ = merge_paper(state, {
            "title": "Test robot imitation learning", "paper_url": "https://arxiv.org/abs/2601.00001",
            "abstract": "Test fixture abstract.",
            "sources": [{"kind": "mail", "url": "https://arxiv.org/abs/2601.00001", "mail_uid": "private-mail-uid", "raw_message": "private-raw-mail"}],
        }, "target")
        self.paper["report"] = {
            "status": "ready", "path": "/Users/private/reports/report.md", "markdown": "# Verified report\n\nSource-backed fixture.",
            "evidence_level": "fulltext-quote-checked", "reason": "Passed", "generated_at": "2026-01-01T00:00:00Z",
            "source": {"cache_path": "/Users/private/cache/fulltext.html"},
        }
        self.store.save(state)
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(self.store, self.config, self.site))
        self.server.daemon_threads = True
        self.port = self.server.server_address[1]
        self.server_thread = threading.Thread(target=self.server.serve_forever, kwargs={"poll_interval": 0.02}, daemon=True)
        self.server_thread.start()
        self.worker_events = []

    def tearDown(self):
        # Release any mocked worker even after an assertion fails.
        for release, finished in self.worker_events:
            release.set()
            finished.wait(timeout=2)
        self.server.shutdown()
        self.server.server_close()
        self.server_thread.join(timeout=2)
        self.temporary.cleanup()

    def request(self, method, path, body=None, headers=None):
        request_headers = dict(headers or {})
        if body is not None:
            body = json.dumps(body).encode("utf-8")
            request_headers.setdefault("Content-Type", "application/json")
        connection = http.client.HTTPConnection("127.0.0.1", self.port, timeout=3)
        try:
            connection.request(method, path, body=body, headers=request_headers)
            response = connection.getresponse()
            raw = response.read()
            payload = json.loads(raw) if raw else None
            return response.status, payload, dict(response.getheaders())
        finally:
            connection.close()

    def test_state_api_returns_stats_and_sanitized_reports(self):
        code, state, headers = self.request("GET", "/api/state")
        self.assertEqual(code, 200)
        self.assertEqual(state["schema_version"], 1)
        self.assertEqual(state["stats"]["papers"], 1)
        self.assertEqual(state["stats"]["target"], 1)
        self.assertEqual(state["stats"]["reports_ready"], 1)
        self.assertEqual(state["papers"][0]["report"]["markdown"], self.paper["report"]["markdown"])
        self.assertNotIn("path", state["papers"][0]["report"])
        self.assertNotIn("source", state["papers"][0]["report"])
        serialized = json.dumps(state)
        for secret in ("private-config-key", "private-model.example", "/Users/private", "private-mail-uid", "private-raw-mail"):
            self.assertNotIn(secret, serialized)
        self.assertEqual(headers["Cache-Control"], "no-store")
        self.assertEqual(headers["X-Content-Type-Options"], "nosniff")

    def test_config_api_returns_only_public_configuration(self):
        code, config, _ = self.request("GET", "/api/config")
        self.assertEqual(code, 200)
        self.assertEqual(config["scope"], self.config["scope"])
        self.assertEqual(config["schedule"]["hour"], 8)
        self.assertEqual(set(config.get("llm", {})), {"model"})
        self.assertNotIn("private_path", config)
        self.assertNotIn("private-config-key", json.dumps(config))

    def test_report_api_decodes_identifier_and_omits_local_paths(self):
        identifier = quote(self.paper["id"], safe="")
        code, report, _ = self.request("GET", "/api/reports/" + identifier)
        self.assertEqual(code, 200)
        self.assertEqual(report["status"], "ready")
        self.assertIn("Verified report", report["markdown"])
        self.assertNotIn("path", report)
        self.assertNotIn("source", report)
        self.assertNotIn("/Users/private", json.dumps(report))

    def test_unknown_api_and_report_routes_return_json_404(self):
        for path in ("/api/unknown", "/api/reports/missing"):
            with self.subTest(path=path):
                code, payload, headers = self.request("GET", path)
                self.assertEqual(code, 404)
                self.assertIn("error", payload)
                self.assertTrue(headers["Content-Type"].startswith("application/json"))
        code, payload, _ = self.request("POST", "/api/unknown", {})
        self.assertEqual(code, 404)
        self.assertIn("error", payload)

    def test_local_arxiv_intake_accepts_and_persists_without_network(self):
        url = "https://arxiv.org/abs/2602.12345v2"
        origin = "http://127.0.0.1:" + str(self.port)
        resolve = socket.getaddrinfo

        def local_only(host, *args, **kwargs):
            try:
                loopback = ipaddress.ip_address(host).is_loopback
            except ValueError:
                loopback = host == "localhost"
            if not loopback:
                raise AssertionError("Intake must not need external DNS for an official arXiv URL")
            return resolve(host, *args, **kwargs)

        with patch("paper_watch.server.build_site", return_value=self.site) as rebuild, patch("socket.getaddrinfo", side_effect=local_only):
            code, result, _ = self.request("POST", "/api/intake", {"url": url}, {"Origin": origin})
        self.assertEqual(code, 202)
        self.assertEqual(result["id"], "arxiv:2602.12345")
        self.assertEqual(result["status"], "pending")
        added = next(row for row in self.store.load()["papers"] if row["id"] == result["id"])
        self.assertEqual(added["paper_url"], url)
        rebuild.assert_called_once_with(self.store, self.config)

    def test_cross_origin_post_cannot_start_worker_or_write(self):
        with patch("paper_watch.server.run_pipeline") as run:
            code, result, _ = self.request("POST", "/api/run", {}, {"Origin": "https://unrelated.example"})
        self.assertEqual(code, 403)
        self.assertIn("error", result)
        run.assert_not_called()
        self.assertEqual(len(self.store.load()["papers"]), 1)

    def test_untrusted_host_post_is_rejected(self):
        with patch("paper_watch.server.run_pipeline") as run:
            code, _, _ = self.request("POST", "/api/run", {}, {"Host": "research.attacker.example"})
        self.assertEqual(code, 403)
        run.assert_not_called()

    def test_parallel_run_returns_conflict_and_health_tracks_worker(self):
        entered, release, finished = threading.Event(), threading.Event(), threading.Event()
        self.worker_events.append((release, finished))

        def worker(store, config):
            entered.set()
            try:
                release.wait(timeout=3)
            finally:
                finished.set()

        with patch("paper_watch.server.run_pipeline", side_effect=worker) as run:
            code, result, _ = self.request("POST", "/api/run", {})
            self.assertEqual(code, 202)
            self.assertEqual(result["status"], "running")
            self.assertTrue(entered.wait(timeout=2), "Background worker did not start")
            code, health, _ = self.request("GET", "/api/health")
            self.assertEqual(code, 200)
            self.assertTrue(health["running"])
            code, result, _ = self.request("POST", "/api/run", {})
            self.assertEqual(code, 409)
            self.assertIn("error", result)
            run.assert_called_once_with(self.store, self.config)
            release.set()
            self.assertTrue(finished.wait(timeout=2))
            deadline = time.monotonic() + 2
            while time.monotonic() < deadline:
                _, health, _ = self.request("GET", "/api/health")
                if not health["running"]:
                    break
                time.sleep(0.005)
            self.assertFalse(health["running"], "Worker lock was not released")


if __name__ == "__main__":
    unittest.main()
