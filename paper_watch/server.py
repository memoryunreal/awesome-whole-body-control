"""Small loopback-only UI server. Static exports remain usable without it."""

import json
import os
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote, urlsplit

from .pipeline import build_site, ingest_url, run_pipeline, safe_error
from .store import bootstrap, now, public_state


def make_handler(store, config, site):
    running = threading.Lock()

    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(site), **kwargs)

        def log_message(self, *_):
            # Request paths may contain user data; avoid persisting them in logs.
            pass

        def reply(self, code, value):
            payload = json.dumps(value, ensure_ascii=False).encode()
            self.send_response(code)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(payload)

        def do_GET(self):
            path = urlsplit(self.path).path
            if path == "/api/state":
                return self.reply(200, public_state(store.load(), config))
            if path == "/api/health":
                return self.reply(200, {"status": "ok", "mode": "local", "running": running.locked(),
                    "gmail_configured": bool(os.getenv("IMAP_USER") and os.getenv("IMAP_PASSWORD")),
                    "imap_configured": bool(os.getenv("IMAP_USER") and os.getenv("IMAP_PASSWORD")),
                    "model_configured": bool(os.getenv("OPENAI_API_KEY"))})
            if path == "/api/config":
                return self.reply(200, public_state(store.load(), config)["config"])
            if path.startswith("/api/reports/"):
                identifier = unquote(path[len("/api/reports/"):])
                paper = next((p for p in public_state(store.load(), config)["papers"] if p["id"] == identifier), None)
                return self.reply(200, paper.get("report", {})) if paper else self.reply(404, {"error": "未找到论文"})
            if path.startswith("/api/"):
                return self.reply(404, {"error": "Unknown API route"})
            super().do_GET()

        def do_POST(self):
            # Browser forms on other sites must not trigger local writes or model calls.
            host = self.headers.get("Host", "")
            if urlsplit("http://" + host).hostname not in {"127.0.0.1", "localhost", "::1"}:
                return self.reply(403, {"error": "仅允许本机访问"})
            origin = self.headers.get("Origin")
            if origin and origin != "http://" + host:
                return self.reply(403, {"error": "请求来源不匹配"})
            if self.headers.get("Content-Type", "").split(";")[0].strip() != "application/json":
                return self.reply(415, {"error": "需要 application/json"})
            try:
                size = int(self.headers.get("Content-Length", "0"))
                if not 0 <= size <= 8192:
                    return self.reply(413, {"error": "请求过大"})
                payload = json.loads(self.rfile.read(size) or b"{}")
                if not isinstance(payload, dict):
                    raise ValueError("请求需要 JSON 对象")
                path = urlsplit(self.path).path
                if path == "/api/intake":
                    with store.lock():
                        state = store.load()
                        paper = ingest_url(state, str(payload.get("url", "")))
                        store.save(state)
                    build_site(store, config)
                    return self.reply(202, {"id": paper["id"], "status": paper["status"]})
                if path == "/api/decision":
                    decision = payload.get("decision")
                    if decision not in {"target", "review", "excluded"} or not payload.get("reason"):
                        raise ValueError("请选择筛选结果并填写理由")
                    with store.lock():
                        state = store.load()
                        paper = next((p for p in state["papers"] if p["id"] == payload.get("id")), None)
                        if not paper:
                            return self.reply(404, {"error": "未找到论文"})
                        paper["status"] = decision
                        paper["manual_decision"] = {"decision": decision, "reason": str(payload["reason"]), "at": now()}
                        paper["screening"] = {"decision": decision, "reason": str(payload["reason"]), "method": "manual", "evidence": []}
                        store.save(state)
                    build_site(store, config)
                    return self.reply(200, {"status": decision})
                if path == "/api/run":
                    if not running.acquire(blocking=False):
                        return self.reply(409, {"error": "已有任务正在运行"})

                    def work():
                        try:
                            run_pipeline(store, config)
                        except Exception as exc:
                            # Surface top-level failures in the UI, too.
                            try:
                                with store.lock():
                                    state = store.load()
                                    state["runs"].append({"id": now(), "started_at": now(), "finished_at": now(), "status": "failed", "errors": [{"source": "worker", "message": safe_error(exc)}]})
                                    store.save(state)
                            except RuntimeError:
                                pass
                        finally:
                            running.release()

                    threading.Thread(target=work, daemon=True).start()
                    return self.reply(202, {"status": "running"})
                return self.reply(404, {"error": "Unknown API route"})
            except (ValueError, OSError) as exc:
                return self.reply(400, {"error": safe_error(exc)})
            except RuntimeError as exc:
                return self.reply(409, {"error": safe_error(exc)})

    return Handler


def serve(store, config, port=8765):
    with store.lock():
        state = store.load()
        bootstrap(state, config)
        store.save(state)
    site = build_site(store, config)
    server = ThreadingHTTPServer(("127.0.0.1", port), make_handler(store, config, site))
    print(f"Paper Watch: http://127.0.0.1:{port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
