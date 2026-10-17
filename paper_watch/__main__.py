"""Run `python -m paper_watch --help` for the local workflow."""

import argparse
import json
import os
import sys
from pathlib import Path

from .pipeline import build_site, ingest_url, run_pipeline, safe_error
from .store import ROOT, Store, bootstrap, load_config, now, public_state


def load_env(path):
    """Read literal KEY=VALUE lines. Never source or execute a shell file."""
    path = Path(path)
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, separator, value = line.partition("=")
        if not separator or not key.strip().replace("_", "").isalnum():
            raise ValueError("Invalid environment file line")
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def main(argv=None):
    parser = argparse.ArgumentParser(description="论文订阅、筛选、深读报告与引用网络")
    parser.add_argument("--state", type=Path, default=ROOT / ".paper-watch/state.json")
    parser.add_argument("--config", type=Path, default=ROOT / "config/paper-watch.json")
    parser.add_argument("--env-file", type=Path, default=ROOT / ".env")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("init", help="导入既有清单并生成本地站点，不访问网络")
    run = commands.add_parser("run", help="采集、筛选、生成报告、更新清单和站点")
    run.add_argument("--eml", nargs="*", default=[], help="导入 Gmail 导出的 .eml 文件")
    run.add_argument("--imap", action="store_true", help="要求读取已配置的 Gmail/IMAP 邮箱")
    run.add_argument("--no-citations", action="store_true")
    run.add_argument("--no-network", action="store_true", help="仅本地导入与规则筛选")
    run.add_argument("--no-reports", action="store_true")
    run.add_argument("--no-sync", action="store_true")
    run.add_argument("--max-papers", type=int)
    site = commands.add_parser("build-site", help="导出静态网站，不包含原始邮件或凭据")
    site.add_argument("--output", type=Path)
    server = commands.add_parser("serve", help="启动仅限本机的交互站点")
    server.add_argument("--port", type=int, default=8765)
    intake = commands.add_parser("intake", help="添加一篇待处理论文")
    intake.add_argument("url")
    decision = commands.add_parser("decide", help="人工确认或排除候选论文")
    decision.add_argument("paper_id")
    decision.add_argument("decision", choices=["target", "review", "excluded"])
    decision.add_argument("--reason", required=True)
    commands.add_parser("status", help="显示已配置能力与任务状态，不显示密钥")
    args = parser.parse_args(argv)
    load_env(args.env_file)
    config = load_config(args.config)
    store = Store(args.state)
    if args.command in {"init", "intake", "decide"}:
        with store.lock():
            state = store.load()
            bootstrap(state, config)
            if args.command == "intake":
                result = ingest_url(state, args.url)
                print(json.dumps({"id": result["id"], "status": result["status"]}, ensure_ascii=False))
            if args.command == "decide":
                paper = next((p for p in state["papers"] if p["id"] == args.paper_id), None)
                if paper is None:
                    raise ValueError("Paper ID not found")
                paper["status"] = args.decision
                paper["manual_decision"] = {"decision": args.decision, "reason": args.reason, "at": now()}
                paper["screening"] = {"decision": args.decision, "reason": args.reason, "method": "manual", "evidence": []}
            store.save(state)
        print(build_site(store, config))
    elif args.command == "run":
        result = run_pipeline(store, config, eml=args.eml, imap=args.imap,
                              citations=not args.no_citations, network=not args.no_network,
                              reports=not args.no_reports, max_papers=args.max_papers, sync=not args.no_sync)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 2 if result["status"] == "partial" else 0
    elif args.command == "build-site":
        print(build_site(store, config, args.output))
    elif args.command == "serve":
        from .server import serve
        serve(store, config, args.port)
    elif args.command == "status":
        state = public_state(store.load(), config)
        print(json.dumps({"gmail_configured": bool(os.getenv("IMAP_USER") and os.getenv("IMAP_PASSWORD")),
                          "model_configured": bool(os.getenv("OPENAI_API_KEY")), "stats": state["stats"],
                          "last_run": state["runs"][-1] if state["runs"] else None}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, RuntimeError, OSError) as exc:
        print(safe_error(exc), file=sys.stderr)
        raise SystemExit(1)
