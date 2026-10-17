"""Scope and full-text evidence regression tests; no network or paid API calls."""

import copy
import hashlib
import json
import os
import socket
import tempfile
import urllib.error
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from paper_watch.reports import (
    NOT_REPORTED,
    SECTIONS,
    ReportError,
    _candidate_urls,
    _chat_json,
    _download,
    _fetch_fulltext,
    _public_addresses,
    _validate_report,
    generate_report,
)
from paper_watch.screening import screen_paper


CONFIG = {
    "scope": {
        "description": "Robotics, imitation and egocentric learning",
        "positive_terms": ["robot", "imitation learning", "egocentric"],
        "negative_terms": ["medical imaging"],
        "target_threshold": 45,
        "review_threshold": 15,
    },
    "llm": {"model": "test-model", "base_url": "https://api.example.com/v1"},
    "seeds": [],
}
PAPER = {
    "id": "arxiv:2601.00001",
    "title": "Robot imitation learning from egocentric data",
    "arxiv_id": "2601.00001v2",
    "abstract": "We develop robot imitation learning from egocentric demonstrations. " * 4,
}
QUOTE = "We train a robot imitation learning policy with 100 demonstrations and evaluate it on 5 tasks."


def source_fixture():
    return {
        "url": "https://arxiv.org/html/2601.00001v2",
        "kind": "html", "version": "v2", "sha256": "a" * 64,
        "blocks": [{
            "id": "B0001", "text": QUOTE, "section": "Experiments", "anchor": "S4",
            "url": "https://arxiv.org/html/2601.00001v2#S4",
        }],
        "truncated": False, "characters": 12000, "fetched_at": "2026-01-01T00:00:00+00:00",
    }


def report_fixture():
    sections = {key: [{"status": "not_reported", "text": "Not reported", "evidence": []}] for key in SECTIONS}
    for key in ("overview", "problem", "method", "evaluation"):
        sections[key] = [{
            "status": "reported", "text": "使用 100 个示范训练机器人策略，在 5 项任务中评估。",
            "evidence": [{"block_id": "B0001", "quote": QUOTE}],
        }]
    sections["relevance"] = [{
        "status": "inferred", "text": "推断：该方法可为本组的模仿学习研究提供比较对象。",
        "evidence": [{"block_id": "B0001", "quote": QUOTE}],
    }]
    return {"sections": sections}


def verification_fixture(report=None):
    report = report or report_fixture()
    return {"verdicts": [
        {"id": f"{section}:{index}", "supported": True, "reason": "Supported by source"}
        for section, rows in report["sections"].items()
        for index, row in enumerate(rows) if row["status"] != "not_reported"
    ]}


class ScreeningTests(unittest.TestCase):
    def test_target_requires_multiple_scope_matches_and_metadata(self):
        result = screen_paper(PAPER, CONFIG)
        self.assertEqual(result["decision"], "target")
        self.assertGreaterEqual(result["score"], 45)
        self.assertTrue(result["evidence"])
        self.assertEqual(result["method"], "scope-rules-v2")

    def test_missing_abstract_goes_to_review_even_with_matching_title(self):
        self.assertEqual(screen_paper(dict(PAPER, abstract=""), CONFIG)["decision"], "review")

    def test_conflicting_scope_goes_to_review(self):
        result = screen_paper(dict(PAPER, abstract=PAPER["abstract"] + " Applied to medical imaging."), CONFIG)
        self.assertEqual(result["decision"], "review")
        self.assertTrue(any(row["polarity"] == "negative" for row in result["evidence"]))

    def test_a_citation_alone_does_not_establish_relevance(self):
        paper = {"title": "Galactic population models", "abstract": "We study the formation of distant galaxies using spectroscopic population analysis. " * 3, "seed_ids": ["vitra"]}
        self.assertEqual(screen_paper(paper, CONFIG)["decision"], "excluded")

    def test_keyword_boundaries_prevent_incidental_substrings(self):
        config = {"scope": {"positive_terms": ["arm"]}}
        paper = {"title": "Charm physics", "abstract": "A study of charm physics and particle interactions in high energy collisions. " * 2}
        self.assertEqual(screen_paper(paper, config)["evidence"], [])

    def test_empty_scope_never_auto_accepts(self):
        self.assertEqual(screen_paper(PAPER, {"scope": {}})["decision"], "review")

    def test_priority_terms_increase_score_but_still_need_multiple_matches(self):
        normal = screen_paper(PAPER, CONFIG)
        priority = copy.deepcopy(CONFIG)
        priority["scope"]["priority_terms"] = ["egocentric"]
        weighted = screen_paper(PAPER, priority)
        self.assertGreater(weighted["score"], normal["score"])
        only_one = {"title": "Egocentric research", "abstract": "Egocentric visual sensing provides a useful representation for embodied environments. " * 2}
        self.assertEqual(screen_paper(only_one, priority)["decision"], "review")


class EvidenceTests(unittest.TestCase):
    def test_unknown_source_location_rejected(self):
        report = report_fixture()
        report["sections"]["method"][0]["evidence"][0]["block_id"] = "B9999"
        with self.assertRaises(ReportError):
            _validate_report(report, source_fixture())

    def test_fabricated_quote_rejected(self):
        report = report_fixture()
        report["sections"]["method"][0]["evidence"][0]["quote"] = "The method achieves state of the art success on all tasks."
        with self.assertRaises(ReportError):
            _validate_report(report, source_fixture())

    def test_numeric_claim_must_be_in_its_own_evidence(self):
        report = report_fixture()
        report["sections"]["evaluation"][0]["text"] = "成功率为 99%。"
        with self.assertRaises(ReportError):
            _validate_report(report, source_fixture())

    def test_missing_claim_evidence_rejected(self):
        report = report_fixture()
        report["sections"]["method"][0]["evidence"] = []
        with self.assertRaises(ReportError):
            _validate_report(report, source_fixture())

    def test_missing_core_results_rejected(self):
        report = report_fixture()
        report["sections"]["evaluation"] = [{"status": "not_reported", "text": "None", "evidence": []}]
        with self.assertRaises(ReportError):
            _validate_report(report, source_fixture())

    def test_not_reported_text_cannot_hide_a_claim(self):
        report = report_fixture()
        report["sections"]["ablations"][0]["text"] = "The authors never conducted ablations."
        valid = _validate_report(report, source_fixture())
        self.assertEqual(valid["sections"]["ablations"][0]["text"], NOT_REPORTED)

    def test_unknown_section_rejected(self):
        report = report_fixture()
        report["sections"]["invented"] = []
        with self.assertRaises(ReportError):
            _validate_report(report, source_fixture())


class ReportFlowTests(unittest.TestCase):
    def test_missing_key_is_blocked_without_reading_or_writing(self):
        with patch.dict(os.environ, {}, clear=True), patch("paper_watch.reports._fetch_fulltext") as fetch, tempfile.TemporaryDirectory() as output:
            result = generate_report(PAPER, CONFIG, output)
            self.assertEqual(result["status"], "blocked")
            self.assertEqual(result["markdown"], "")
            self.assertEqual(list(Path(output).iterdir()), [])
            fetch.assert_not_called()

    def test_missing_model_is_blocked(self):
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}, clear=True), tempfile.TemporaryDirectory() as output:
            self.assertEqual(generate_report(PAPER, {"llm": {}}, output)["status"], "blocked")

    def test_missing_fulltext_never_generates_an_abstract_report(self):
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}), patch("paper_watch.reports._fetch_fulltext", side_effect=ReportError("No full text")), patch("paper_watch.reports._chat_json") as model, tempfile.TemporaryDirectory() as output:
            self.assertEqual(generate_report(PAPER, CONFIG, output)["status"], "blocked")
            model.assert_not_called()

    def test_valid_report_is_written_with_auditable_source_and_labels(self):
        report = report_fixture()
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}), patch("paper_watch.reports._fetch_fulltext", return_value=source_fixture()), patch("paper_watch.reports._chat_json", side_effect=[report, verification_fixture(report)]), tempfile.TemporaryDirectory() as output:
            result = generate_report(dict(PAPER, id="../../../escape"), CONFIG, output)
            self.assertEqual(result["status"], "ready", result["reason"])
            self.assertEqual(Path(result["path"]).parent, Path(output))
            self.assertEqual(Path(result["path"]).read_text(), result["markdown"])
            self.assertIn("原文事实 reported", result["markdown"])
            self.assertIn("分析推断 inferred", result["markdown"])
            self.assertIn("未报告 not_reported", result["markdown"])
            self.assertIn("版本：v2", result["markdown"])
            self.assertIn("B0001", result["markdown"])
            self.assertNotIn("test-key", result["markdown"])

    def test_rejected_entailment_cannot_be_saved_as_ready(self):
        review = verification_fixture()
        review["verdicts"][0]["supported"] = False
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}), patch("paper_watch.reports._fetch_fulltext", return_value=source_fixture()), patch("paper_watch.reports._chat_json", side_effect=[report_fixture(), review]), tempfile.TemporaryDirectory() as output:
            result = generate_report(PAPER, CONFIG, output)
            self.assertEqual(result["status"], "failed")
            self.assertEqual(list(Path(output).iterdir()), [])

    def test_incomplete_verification_is_rejected(self):
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}), patch("paper_watch.reports._fetch_fulltext", return_value=source_fixture()), patch("paper_watch.reports._chat_json", side_effect=[report_fixture(), {"verdicts": []}]), tempfile.TemporaryDirectory() as output:
            self.assertEqual(generate_report(PAPER, CONFIG, output)["status"], "failed")

    def test_malformed_generation_is_rejected(self):
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}), patch("paper_watch.reports._fetch_fulltext", return_value=source_fixture()), patch("paper_watch.reports._chat_json", return_value={"markdown": "invented report"}), tempfile.TemporaryDirectory() as output:
            self.assertEqual(generate_report(PAPER, CONFIG, output)["status"], "failed")


class FullTextTests(unittest.TestCase):
    def test_arxiv_version_is_preserved_in_both_source_attempts(self):
        self.assertEqual(_candidate_urls(PAPER), ["https://arxiv.org/html/2601.00001v2", "https://arxiv.org/pdf/2601.00001v2"])

    def test_abs_page_is_not_used_as_fulltext(self):
        paper = dict(PAPER, arxiv_id="", paper_url="https://arxiv.org/abs/2601.00001v3")
        self.assertEqual(_candidate_urls(paper)[0], "https://arxiv.org/html/2601.00001v3")

    def test_substantive_html_extracts_locators_and_concrete_version(self):
        paragraph = QUOTE + " " + ("The policy uses egocentric visual observations for robot imitation learning. " * 10)
        paragraphs = "".join(f'<p id="p{i}">{paragraph}</p>' for i in range(12))
        html = f'<html><head><link rel="canonical" href="https://arxiv.org/html/2601.00001v2"></head><body><article><h1>{PAPER["title"]}</h1><h2>Introduction</h2>{paragraphs}<h2>Methods and Experiments</h2><p>{paragraph}</p></article></body></html>'
        with patch("paper_watch.reports._download", return_value=(html.encode(), "https://arxiv.org/html/2601.00001", "text/html")):
            source = _fetch_fulltext(PAPER)
        self.assertEqual(source["version"], "v2")
        self.assertEqual(source["sha256"], hashlib.sha256(html.encode()).hexdigest())
        self.assertGreater(source["characters"], 6000)
        self.assertTrue(any(block["url"].endswith("#p1") for block in source["blocks"]))

    def test_arxiv_header_version_and_article_filtering(self):
        paragraph = QUOTE + " " + ("The policy uses egocentric visual observations for robot imitation learning. " * 10)
        paragraphs = "".join(f'<p id="p{i}">{paragraph}</p>' for i in range(12))
        html = f'<html><body><p>Report GitHub Issue</p><a href="/abs/2601.00001v2">Abstract</a><article><h1>{PAPER["title"]}</h1><h2>Introduction</h2>{paragraphs}<h2>Experiments</h2><p>{paragraph}</p></article><p>Page footer</p></body></html>'
        with patch("paper_watch.reports._download", return_value=(html.encode(), "https://arxiv.org/html/2601.00001", "text/html")):
            source = _fetch_fulltext(dict(PAPER, arxiv_id="2601.00001"))
        self.assertEqual(source["version"], "v2")
        self.assertNotIn("Report GitHub Issue", [row["text"] for row in source["blocks"]])
        self.assertEqual(source["blocks"][0]["text"], PAPER["title"])

    def test_abstract_landing_page_is_rejected(self):
        html = f'<html><article><h1>{PAPER["title"]}</h1><h2>Abstract</h2><p>{PAPER["abstract"]}</p></article></html>'
        with patch("paper_watch.reports._download", return_value=(html.encode(), "https://arxiv.org/abs/2601.00001", "text/html")):
            with self.assertRaises(ReportError):
                _fetch_fulltext(PAPER)

    def test_private_dns_resolution_is_rejected(self):
        addresses = [(socket.AF_INET, socket.SOCK_STREAM, 6, "", ("127.0.0.1", 443))]
        with patch("socket.getaddrinfo", return_value=addresses):
            with self.assertRaises(ReportError):
                _public_addresses("https://attacker.example/paper")

    def test_mixed_public_and_private_dns_is_rejected(self):
        addresses = [(socket.AF_INET, socket.SOCK_STREAM, 6, "", (ip, 443)) for ip in ("8.8.8.8", "10.0.0.1")]
        with patch("socket.getaddrinfo", return_value=addresses):
            with self.assertRaises(ReportError):
                _public_addresses("https://attacker.example/paper")

    def test_trusted_official_host_can_use_vpn_fake_dns_range(self):
        addresses = [(socket.AF_INET, socket.SOCK_STREAM, 6, "", ("198.18.1.73", 443))]
        with patch("socket.getaddrinfo", return_value=addresses):
            self.assertEqual(_public_addresses("https://arxiv.org/html/2601.00001"), addresses)
            self.assertEqual(_public_addresses("https://export.arxiv.org/api/query"), addresses)

    def test_fake_dns_exception_never_applies_to_arbitrary_host_or_subdomain(self):
        addresses = [(socket.AF_INET, socket.SOCK_STREAM, 6, "", ("198.18.1.73", 443))]
        with patch("socket.getaddrinfo", return_value=addresses):
            for hostname in ("publisher.example", "evil.arxiv.org", "arxiv.org.attacker.example"):
                with self.subTest(hostname=hostname), self.assertRaises(ReportError):
                    _public_addresses("https://" + hostname + "/paper")

    def test_trusted_host_cannot_resolve_to_other_private_addresses(self):
        for ip in ("127.0.0.1", "10.0.0.1", "169.254.169.254", "::1"):
            addresses = [(socket.AF_INET, socket.SOCK_STREAM, 6, "", (ip, 443))]
            with patch("socket.getaddrinfo", return_value=addresses), self.subTest(ip=ip), self.assertRaises(ReportError):
                _public_addresses("https://arxiv.org/html/2601.00001")

    def test_redirect_from_trusted_proxy_to_private_source_is_rejected(self):
        def resolve(host, *args, **kwargs):
            ip = "198.18.1.73" if host == "arxiv.org" else "127.0.0.1"
            return [(socket.AF_INET, socket.SOCK_STREAM, 6, "", (ip, 443))]
        opener = Mock()
        opener.open.side_effect = urllib.error.HTTPError(
            "https://arxiv.org/html/2601.00001", 302, "Redirect", {"Location": "https://localhost/secret"}, None
        )
        with patch("socket.getaddrinfo", side_effect=resolve), patch("urllib.request.build_opener", return_value=opener):
            with self.assertRaises(ReportError):
                _download("https://arxiv.org/html/2601.00001")
        self.assertEqual(opener.open.call_count, 1)

    def test_credentials_plain_http_and_nonstandard_ports_are_rejected(self):
        for url in ("http://example.com/paper", "https://user:pass@example.com/paper", "https://example.com:8443/paper", "file:///etc/passwd"):
            with self.subTest(url=url), self.assertRaises(ReportError):
                _public_addresses(url)


class ApiTests(unittest.TestCase):
    def test_compatible_api_uses_json_output_and_configured_model(self):
        response = Mock()
        response.read.return_value = json.dumps({"choices": [{"finish_reason": "stop", "message": {"content": '{"sections":{}}'}}]}).encode()
        response.__enter__ = Mock(return_value=response)
        response.__exit__ = Mock(return_value=False)
        opener = Mock()
        opener.open.return_value = response
        with patch.dict(os.environ, {}, clear=True), patch("urllib.request.build_opener", return_value=opener):
            self.assertEqual(_chat_json([], CONFIG["llm"], "test-key"), {"sections": {}})
        request = opener.open.call_args.args[0]
        self.assertEqual(request.full_url, "https://api.example.com/v1/chat/completions")
        self.assertEqual(json.loads(request.data)["model"], "test-model")
        self.assertEqual(json.loads(request.data)["response_format"], {"type": "json_object"})

    def test_base_url_environment_override_is_used(self):
        response = Mock()
        response.read.return_value = json.dumps({"choices": [{"finish_reason": "stop", "message": {"content": '{}'}}]}).encode()
        response.__enter__ = Mock(return_value=response)
        response.__exit__ = Mock(return_value=False)
        opener = Mock()
        opener.open.return_value = response
        with patch.dict(os.environ, {"OPENAI_BASE_URL": "https://llm.example.org/v1"}), patch("urllib.request.build_opener", return_value=opener):
            _chat_json([], CONFIG["llm"], "test-key")
        self.assertEqual(opener.open.call_args.args[0].full_url, "https://llm.example.org/v1/chat/completions")


if __name__ == "__main__":
    unittest.main()
