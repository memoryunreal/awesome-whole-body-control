"""Build a public, offline site from a checked-in snapshot and the current CSV.

Unlike the interactive CLI, this entry point never opens the private local store,
loads an environment file, fetches papers, or contacts a mailbox.  The snapshot
retains citation/report evidence while the CSV supplies weekly library updates.
"""

import argparse
import copy
import csv
import json
import sys
from pathlib import Path

from .pipeline import build_site
from .store import ROOT, atomic_json, bootstrap, load_config, merge_paper, now, public_state


# These are maintained by the weekly library review.  In particular, an empty
# code URL must remove an older claim when a repository is no longer verified.
CURATED_FIELDS = (
    "summary", "code_status", "code_url", "project_url", "dataset_url",
    "category", "tags", "real_robot", "robot_platform", "year", "venue",
)


def prepare_snapshot(snapshot_path, csv_path, config):
    """Merge current curated metadata without overwriting research evidence."""
    snapshot_path, csv_path = Path(snapshot_path), Path(csv_path)
    if not csv_path.is_file():
        raise ValueError("The current papers.csv is required to publish the library")
    if snapshot_path.exists():
        state = json.loads(snapshot_path.read_text(encoding="utf-8"))
        if (not isinstance(state, dict) or state.get("schema_version") != 1 or
                any(not isinstance(state.get(key), list) for key in ("papers", "edges", "runs"))):
            raise ValueError("The public snapshot has an unsupported schema")
        if any(not isinstance(paper, dict) or not paper.get("id") or not paper.get("title")
               for paper in state["papers"]):
            raise ValueError("The public snapshot contains an invalid paper")
        identities = [paper["id"] for paper in state["papers"]]
        if len(identities) != len(set(identities)):
            raise ValueError("The public snapshot contains duplicate paper IDs")
        if any(not isinstance(edge, dict) or edge.get("source") not in identities or
               edge.get("target") not in identities for edge in state["edges"]):
            raise ValueError("The public snapshot contains an invalid citation edge")
        # Discard unknown/private fields before doing any work with the snapshot.
        state = public_state(state, config)
    else:
        state = {"schema_version": 1, "papers": [], "edges": [], "runs": []}

    bootstrap(state, config, csv_path)
    with csv_path.open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            paper, _ = merge_paper(state, row, "library", fill_missing=True)
            for field in CURATED_FIELDS:
                if field in row:
                    paper[field] = row[field]
    state["updated_at"] = now()
    return public_state(state, config)


class SnapshotStore:
    """The site builder needs only load(); no private state file is involved."""

    def __init__(self, state):
        self.state = state

    def load(self):
        return copy.deepcopy(self.state)


def publish(*, root=ROOT, snapshot=None, output=None, write_snapshot=False):
    """Export the complete static site, optionally updating its public snapshot."""
    root = Path(root)
    snapshot = Path(snapshot) if snapshot is not None else root / "data/paper-watch.json"
    output = Path(output) if output is not None else root / "_site"
    if write_snapshot and snapshot.resolve() == (root / ".paper-watch/state.json").resolve():
        raise ValueError("Publication must not overwrite the private local state")
    config = load_config(root / "config/paper-watch.json")
    state = prepare_snapshot(snapshot, root / "papers.csv", config)
    build_site(SnapshotStore(state), config, output)
    (output / ".nojekyll").touch()
    if write_snapshot:
        atomic_json(snapshot, state)
    return state


def main(argv=None):
    parser = argparse.ArgumentParser(description="离线构建可公开部署的论文网站")
    parser.add_argument("--output", type=Path, default=ROOT / "_site")
    parser.add_argument("--snapshot", type=Path, default=ROOT / "data/paper-watch.json",
                        help="公开快照：保留引用关系与深读报告")
    parser.add_argument("--write-snapshot", action="store_true",
                        help="构建成功后更新公开快照，不写入本地私有状态")
    args = parser.parse_args(argv)
    if not args.snapshot.exists():
        print("No public snapshot found; publishing the CSV library without stored citations or reports.", file=sys.stderr)
    state = publish(snapshot=args.snapshot, output=args.output, write_snapshot=args.write_snapshot)
    print(json.dumps({"output": str(args.output), "stats": state["stats"],
                      "snapshot_updated": args.write_snapshot}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError) as exc:
        print(f"Publication failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
