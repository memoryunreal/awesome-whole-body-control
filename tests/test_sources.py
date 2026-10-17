"""Offline tests for discovery boundaries and citation provenance."""

import json
import os
import tempfile
import unittest
from email.message import EmailMessage
from pathlib import Path
from unittest.mock import patch
from urllib.parse import parse_qs, quote, urlsplit

from paper_watch import sources


SEEDS = [
    {"id": "egomimic", "title": "EgoMimic: Scaling Imitation Learning via Egocentric Video", "arxiv_id": "2410.24221", "aliases": ["EgoMimic"]},
    {"id": "vitra", "title": "Scalable Vision-Language-Action Model Pretraining", "arxiv_id": "2510.21571", "aliases": ["VITRA"]},
]


def mail(body, html=True, subject="New citations to EgoMimic"):
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = "scholaralerts-noreply@google.com"
    if html:
        message.set_content("Your Scholar alerts")
        message.add_alternative(body, subtype="html")
    else:
        message.set_content(body)
    return message.as_bytes()


def citation(title, arxiv_id="2601.12345"):
    return {"citingPaper": {"paperId": "s2-" + arxiv_id, "title": title, "externalIds": {"ArXiv": arxiv_id}, "authors": [{"name": "A Researcher"}], "year": 2026, "abstract": "A robotics paper.", "publicationDate": "2026-01-10"}}


class MailParsingTests(unittest.TestCase):
    def test_html_multiple_papers_nested_titles_redirects_and_controls(self):
        redirect = "https://scholar.google.com/scholar_url?url=" + quote("https://arxiv.org/pdf/2601.12345v2.pdf", safe="") + "&hl=en"
        body = f"""<html><h3><a href="{redirect}"><b>Robot Learning</b> from Human Videos</a></h3>
        <div>A Researcher - 2026</div><div>We learn a policy.</div>
        <a href="https://scholar.google.com/citations?user=abc">A Researcher</a>
        <a href="https://scholar.google.com/scholar?cites=123">Cited by 3</a>
        <h3><a href="https://openreview.net/forum?id=example">Ego Transfer for Robot Skills</a></h3>
        <a href="https://scholar.google.com/scholar_alerts?view_op=cancel_alert&id=1">Cancel alert</a>
        <a href="https://example.com/unsubscribe">Unsubscribe from these alerts</a>
        <a href="https://accounts.google.com/">Manage your account here</a></html>"""
        results = sources._parse_message(mail(body), SEEDS, "file:///alert.eml")
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["title"], "Robot Learning from Human Videos")
        self.assertEqual(results[0]["arxiv_id"], "2601.12345")
        self.assertEqual(results[0]["paper_url"], "https://arxiv.org/abs/2601.12345")
        self.assertEqual(results[0]["seed_ids"], ["egomimic"])
        self.assertTrue(all(source["relation"] == "mentions" for result in results for source in result["sources"]))
        self.assertEqual(results[0]["abstract"], "")
        self.assertIn("We learn a policy", results[0]["alert_snippet"])

    def test_plain_multiple_entries_and_google_q_redirect(self):
        first = "https://www.google.com/url?q=" + quote("https://arxiv.org/abs/2601.12345", safe="")
        body = f"""Robot Learning from Human Videos
{first}
Learning useful control with visual data.

[PDF] Dexterous Control from Egocentric Demonstrations <https://doi.org/10.1234/robot.42>
Another paper abstract here.

Unsubscribe
https://scholar.google.com/scholar_alerts?view_op=cancel_alert
"""
        results = sources._parse_message(mail(body, html=False), SEEDS, "file:///alert.eml")
        self.assertEqual(len(results), 2)
        self.assertEqual(results[1]["title"], "Dexterous Control from Egocentric Demonstrations")
        self.assertEqual(results[1]["doi"], "10.1234/robot.42")

    def test_empty_and_control_only_messages_never_create_fake_papers(self):
        body = """<h3>New papers</h3><a href="https://scholar.google.com/citations?user=1">My profile</a>
        <a href="https://example.com/paper.pdf">[PDF]</a>
        <a href="https://example.com/settings">Update your email preferences</a>"""
        self.assertEqual(sources._parse_message(mail(body), SEEDS, "file:///alert.eml"), [])
        self.assertEqual(sources._parse_message(mail("", html=False), SEEDS, "file:///alert.eml"), [])

    def test_html_preferred_over_plain_alternative_and_attachment_ignored(self):
        message = EmailMessage()
        message["Subject"] = "VITRA alerts"
        message.set_content("Robot Learning from Human Videos\nhttps://arxiv.org/abs/2601.12345")
        message.add_alternative('<h3><a href="https://arxiv.org/abs/2601.12345">Robot Learning from Human Videos</a></h3>', subtype="html")
        message.add_attachment(b"Other Robot Learning Paper\nhttps://arxiv.org/abs/2602.22222", maintype="text", subtype="plain", filename="ignore.txt")
        results = sources._parse_message(message.as_bytes(), SEEDS, "file:///alert.eml")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["seed_ids"], ["vitra"])

    def test_local_discovery_preserves_success_and_never_changes_mail(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "alert.eml"
            content = mail('<h3><a href="https://arxiv.org/abs/2601.12345">Robot Learning from Human Videos</a></h3>')
            path.write_bytes(content)
            with self.assertRaises(sources.SourceError) as caught:
                sources.discover_eml([path, path, Path(directory) / "missing.eml"], SEEDS)
            self.assertEqual(len(caught.exception.candidates), 1)
            self.assertEqual(len(caught.exception.errors), 1)
            self.assertEqual(path.read_bytes(), content)

    def test_identifier_and_redirect_validation(self):
        for value in ["2410.24221v3", "https://arxiv.org/pdf/2410.24221v3.pdf", "https://arxiv.org/html/2410.24221v2", "https://doi.org/10.48550/arXiv.2410.24221"]:
            self.assertEqual(sources.arxiv_id_from_url(value), "2410.24221")
        self.assertEqual(sources.arxiv_id_from_url("https://arxiv.org/abs/hep-th/9901001v2"), "hep-th/9901001")
        self.assertEqual(sources.arxiv_id_from_url("https://evil.example/abs/2410.24221"), "")
        self.assertEqual(sources.normalize_paper_url("javascript:alert(1)"), "")
        self.assertEqual(sources.normalize_paper_url("https://user:secret@example.com/paper"), "")


class FakeIMAP:
    def __init__(self, host, port, timeout):
        self.connection = (host, port, timeout)
        self.calls = []

    def login(self, user, password):
        self.calls.append(("login", user))
        return "OK", []

    def select(self, mailbox, readonly):
        self.calls.append(("select", mailbox, readonly))
        return "OK", [b"3"]

    def uid(self, operation, *args):
        self.calls.append((operation, *args))
        if operation == "search":
            return "OK", [b"1 2 3"]
        uid = args[0].decode()
        body = mail(f'<h3><a href="https://arxiv.org/abs/2601.1234{uid}">Robot Learning Paper Number {uid}</a></h3>')
        return "OK", [(f"{uid} (RFC822.SIZE {len(body)} BODY[] {{123}}".encode(), body), b")"]

    def logout(self):
        self.calls.append(("logout",))


class IMAPTests(unittest.TestCase):
    def test_gmail_default_bounded_readonly_peek_since_and_logout(self):
        instance = FakeIMAP("unused", 0, 0)
        settings = {"IMAP_USER": "reader@example.org", "IMAP_PASSWORD": "secret", "IMAP_MAX_MESSAGES": "2", "IMAP_SINCE": "2026-01-02", "IMAP_MAILBOX": "Scholar"}
        with patch.dict(os.environ, settings, clear=True), patch.object(sources.imaplib, "IMAP4_SSL", return_value=instance) as connect:
            results = sources.discover_imap(SEEDS)
        self.assertEqual(len(results), 2)
        self.assertEqual(connect.call_args.args, ("imap.gmail.com", 993))
        self.assertIn(("select", "Scholar", True), instance.calls)
        search = next(call for call in instance.calls if call[0] == "search")
        self.assertIn("02-Jan-2026", search)
        fetches = [call for call in instance.calls if call[0] == "fetch"]
        self.assertEqual([call[1] for call in fetches], [b"2", b"3"])
        self.assertTrue(all("BODY.PEEK[]" in call[2] for call in fetches))
        self.assertFalse(any(call[0].lower() in {"store", "expunge", "delete", "close"} for call in instance.calls))
        self.assertEqual(instance.calls[-1], ("logout",))

    def test_missing_credentials_and_invalid_bounds_are_visible(self):
        with patch.dict(os.environ, {}, clear=True), self.assertRaises(sources.SourceError):
            sources.discover_imap(SEEDS)
        with patch.dict(os.environ, {"IMAP_USER": "x", "IMAP_PASSWORD": "s", "IMAP_MAX_MESSAGES": "9999"}, clear=True), self.assertRaises(sources.SourceError) as caught:
            sources.discover_imap(SEEDS)
        self.assertIn("between 1 and 500", str(caught.exception))

    def test_failed_uid_does_not_lose_other_mail(self):
        instance = FakeIMAP("unused", 0, 0)
        original = instance.uid

        def uid(operation, *args):
            if operation == "fetch" and args[0] == b"2":
                return "NO", [b"unavailable"]
            return original(operation, *args)

        instance.uid = uid
        with patch.dict(os.environ, {"IMAP_USER": "x", "IMAP_PASSWORD": "s"}, clear=True), patch.object(sources.imaplib, "IMAP4_SSL", return_value=instance):
            with self.assertRaises(sources.SourceError) as caught:
                sources.discover_imap(SEEDS)
        self.assertEqual(len(caught.exception.candidates), 2)
        self.assertEqual(len(caught.exception.errors), 1)
        self.assertEqual(instance.calls[-1], ("logout",))


class CitationTests(unittest.TestCase):
    def test_paginates_to_limit_and_only_verified_endpoint_adds_cites(self):
        calls = []

        def fetch(url, headers):
            query = parse_qs(urlsplit(url).query)
            offset = int(query["offset"][0])
            limit = int(query["limit"][0])
            calls.append((offset, limit))
            rows = [citation(f"Robot Paper {number}", f"2601.{number:05d}") for number in range(offset, offset + limit)]
            result = {"offset": offset, "data": rows}
            if offset + limit < 205:
                result["next"] = offset + limit
            return json.dumps(result).encode()

        with patch.object(sources, "_fetch_bytes", side_effect=fetch):
            results = sources.discover_citations(SEEDS[:1], limit=205)
        self.assertEqual(calls, [(0, 100), (100, 100), (200, 5)])
        self.assertEqual(len(results), 205)
        self.assertEqual(results[0]["sources"][0]["relation"], "cites")
        self.assertIn("/citations?", results[0]["sources"][0]["evidence_url"])
        self.assertEqual(results[0]["published_date"], "2026-01-10")

    def test_date_window_and_truncation_are_explicit(self):
        payload = {"data": [citation("A Robot Research Paper")], "next": 1}
        with patch.object(sources, "_fetch_bytes", return_value=json.dumps(payload).encode()) as fetch:
            with self.assertRaises(sources.SourceError) as caught:
                sources.discover_citations(SEEDS[:1], limit=1, since="2026-01-01")
        query = parse_qs(urlsplit(fetch.call_args.args[0]).query)
        self.assertEqual(query["publicationDateOrYear"], ["2026-01-01:"])
        self.assertTrue(caught.exception.errors[0]["incomplete"])
        self.assertEqual(len(caught.exception.candidates), 1)

    def test_bad_since_date_fails_before_network(self):
        with patch.object(sources, "_fetch_bytes") as fetch, self.assertRaises(sources.SourceError):
            sources.discover_citations(SEEDS, since="2026-99-99")
        fetch.assert_not_called()

    def test_partial_failure_reports_seed_and_retains_success(self):
        def fetch(url, headers):
            if "2510.21571" in url:
                raise ValueError("Bibliographic service returned HTTP 429")
            return json.dumps({"data": [citation("A Robot Research Paper")]}).encode()

        with patch.object(sources, "_fetch_bytes", side_effect=fetch), self.assertRaises(sources.SourceError) as caught:
            sources.discover_citations(SEEDS)
        self.assertEqual(len(caught.exception.candidates), 1)
        self.assertEqual(caught.exception.errors[0]["seed_id"], "vitra")

    def test_same_citing_paper_for_multiple_seeds_preserves_both_edges(self):
        with patch.object(sources, "_fetch_bytes", return_value=json.dumps({"data": [citation("A Robot Research Paper")]}).encode()):
            results = sources.discover_citations(SEEDS)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["seed_ids"], ["egomimic", "vitra"])
        self.assertEqual(len(results[0]["sources"]), 2)

    def test_invalid_pagination_and_untitled_rows_do_not_become_papers(self):
        response = {"data": [{"citingPaper": {"paperId": "untitled"}}, citation("A Robot Research Paper")], "next": 0}
        with patch.object(sources, "_fetch_bytes", return_value=json.dumps(response).encode()), self.assertRaises(sources.SourceError) as caught:
            sources.discover_citations(SEEDS[:1], limit=10)
        self.assertEqual(len(caught.exception.candidates), 1)
        self.assertIn("pagination", str(caught.exception))


ATOM = b'''<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom"><entry>
<id>http://arxiv.org/abs/2410.24221v3</id><title>EgoMimic: Scaling Imitation Learning
via Egocentric Video</title><summary>We learn robot manipulation from human demonstrations.</summary>
<published>2024-10-31T17:59:55Z</published><updated>2025-02-01T01:02:03Z</updated>
<author><name>First Author</name></author><author><name>Second Author</name></author>
<arxiv:doi>10.1234/example</arxiv:doi><arxiv:primary_category term="cs.RO"/></entry></feed>'''


class EnrichmentTests(unittest.TestCase):
    def test_metadata_from_primary_api_preserves_existing_evidence(self):
        initial = {"title": "placeholder", "paper_url": "https://arxiv.org/pdf/2410.24221v3.pdf", "sources": [{"kind": "manual", "relation": "discovered"}], "status": "target"}
        with patch.object(sources, "_fetch_bytes", return_value=ATOM) as fetch:
            result = sources.enrich_paper(initial)
        self.assertTrue(fetch.call_args.args[0].startswith("https://export.arxiv.org/api/query?"))
        self.assertEqual(result["arxiv_id"], "2410.24221")
        self.assertEqual(result["arxiv_version"], 3)
        self.assertEqual(result["year"], 2024)
        self.assertEqual(result["published_date"], "2024-10-31")
        self.assertEqual(result["updated_date"], "2025-02-01")
        self.assertEqual(result["arxiv_category"], "cs.RO")
        self.assertEqual(result["authors"], "First Author, Second Author")
        self.assertEqual(result["status"], "target")
        self.assertEqual(len(result["sources"]), 2)
        self.assertEqual(initial["title"], "placeholder")

    def test_public_url_uses_only_s2_lookup_not_arbitrary_page(self):
        metadata = {"paperId": "a" * 40, "title": "Robot Learning", "abstract": "Verified abstract from bibliographic metadata."}
        with patch.object(sources, "_fetch_bytes", return_value=json.dumps(metadata).encode()) as fetch:
            result = sources.enrich_paper({"title": "Unknown", "paper_url": "https://example.org/paper"})
        self.assertEqual(fetch.call_count, 1)
        endpoint = fetch.call_args.args[0]
        self.assertTrue(endpoint.startswith(sources.S2_BASE + "/paper/URL%3Ahttps%3A%2F%2Fexample.org%2Fpaper?"))
        self.assertEqual(result["title"], "Robot Learning")
        self.assertEqual(result["abstract"], metadata["abstract"])
        self.assertEqual(result["sources"][0]["relation"], "metadata")

    def test_nonpublic_urls_are_not_looked_up(self):
        with patch.object(sources, "_fetch_bytes") as fetch:
            for url in ("https://localhost/paper", "http://127.0.0.1/", "file:///private/paper.pdf", "https://internal.local/paper"):
                result = sources.enrich_paper({"title": "Robot Learning", "paper_url": url})
                self.assertEqual(result["title"], "Robot Learning")
        fetch.assert_not_called()

    def test_doi_lookup_preserves_provenance_and_exposes_open_pdf(self):
        metadata = {"paperId": "a" * 40, "title": "Dexterous Robot Learning", "abstract": "We study robot learning with a complete experimental evaluation.",
                    "externalIds": {"DOI": "10.1234/ROBOT.42"}, "authors": [{"name": "A Researcher"}], "year": 2026,
                    "publicationDate": "2026-01-02", "openAccessPdf": {"url": "https://publisher.example/paper.pdf"}}
        initial = {"id": "title:existing", "title": "Email title", "doi": "10.1234/robot.42", "sources": [{"kind": "google_scholar_email", "relation": "mentions"}], "seed_ids": ["vitra"]}
        with patch.dict(os.environ, {"SEMANTIC_SCHOLAR_API_KEY": "sample-key"}), patch.object(sources, "_fetch_bytes", return_value=json.dumps(metadata).encode()) as fetch:
            result = sources.enrich_paper(initial)
        self.assertIn("/paper/DOI%3A10.1234%2Frobot.42?", fetch.call_args.args[0])
        self.assertEqual(fetch.call_args.args[1]["x-api-key"], "sample-key")
        self.assertEqual(result["id"], "title:existing")
        self.assertEqual(result["authors"], "A Researcher")
        self.assertEqual(result["published_date"], "2026-01-02")
        self.assertEqual(result["open_access_url"], "https://publisher.example/paper.pdf")
        self.assertEqual(result["seed_ids"], ["vitra"])
        self.assertEqual(len(result["sources"]), 2)
        self.assertEqual(initial["title"], "Email title")

    def test_s2_discovered_arxiv_identity_uses_primary_api_on_next_refresh(self):
        identity = "a" * 40
        metadata = {"paperId": identity, "title": "EgoMimic", "externalIds": {"ArXiv": "2410.24221"}}
        with patch.object(sources, "_fetch_bytes", side_effect=[json.dumps(metadata).encode(), ATOM]) as fetch:
            first = sources.enrich_paper({"title": "Unknown", "semantic_scholar_id": identity})
            second = sources.enrich_paper(first)
        self.assertEqual(first["arxiv_id"], "2410.24221")
        self.assertEqual(first["paper_url"], "https://arxiv.org/abs/2410.24221")
        self.assertEqual(second["arxiv_version"], 3)
        self.assertEqual(fetch.call_count, 2)
        self.assertTrue(fetch.call_args_list[1].args[0].startswith(sources.ARXIV_API))

    def test_s2_null_fields_never_erase_existing_abstract(self):
        metadata = {"paperId": "a" * 40, "title": "Robot Learning", "abstract": None, "authors": None, "externalIds": {}}
        with patch.object(sources, "_fetch_bytes", return_value=json.dumps(metadata).encode()):
            result = sources.enrich_paper({"title": "Robot Learning", "abstract": "Existing abstract", "semantic_scholar_id": "a" * 40})
        self.assertEqual(result["abstract"], "Existing abstract")

    def test_s2_failures_preserve_candidate_and_reject_identifier_mismatch(self):
        initial = {"title": "Email title", "doi": "10.1234/expected"}
        invalid_results = [
            {"error": "Paper not found"},
            {"paperId": "a" * 40, "title": "Wrong Paper", "externalIds": {"DOI": "10.1234/wrong"}},
            {"paperId": "a" * 40, "title": "No DOI", "externalIds": {}},
        ]
        for response in invalid_results:
            with self.subTest(response=response), patch.object(sources, "_fetch_bytes", return_value=json.dumps(response).encode()), self.assertRaises(sources.SourceError) as caught:
                sources.enrich_paper(initial)
            self.assertEqual(caught.exception.candidates, [initial])
        with patch.object(sources, "_fetch_bytes", side_effect=ValueError("HTTP 429")), self.assertRaises(sources.SourceError) as caught:
            sources.enrich_paper(initial)
        self.assertIn("HTTP 429", caught.exception.errors[0]["message"])
        metadata = {"paperId": "b" * 40, "title": "Other Paper"}
        with patch.object(sources, "_fetch_bytes", return_value=json.dumps(metadata).encode()), self.assertRaises(sources.SourceError):
            sources.enrich_paper({"title": "Original", "semantic_scholar_id": "a" * 40})

    def test_mismatched_or_malformed_atom_fails_without_false_metadata(self):
        for body in (ATOM.replace(b"2410.24221v3", b"2510.21571v3"), b"not xml"):
            with self.subTest(body=body[:20]), patch.object(sources, "_fetch_bytes", return_value=body), self.assertRaises(sources.SourceError) as caught:
                sources.enrich_paper({"title": "Original", "arxiv_id": "2410.24221"})
            self.assertEqual(caught.exception.candidates[0]["title"], "Original")


if __name__ == "__main__":
    unittest.main()
