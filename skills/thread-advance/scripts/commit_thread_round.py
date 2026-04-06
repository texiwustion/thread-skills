#!/usr/bin/env python3
"""Commit one completed thread round when the repo has changes."""

from __future__ import annotations

import argparse
import os
import subprocess
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root where the round should be committed.",
    )
    parser.add_argument("--thread-id", required=True, help="Thread ID for the commit message.")
    parser.add_argument(
        "--summary",
        default="advance one bounded round",
        help="Short round summary used in the commit message.",
    )
    return parser.parse_args()


def git(repo_root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )


def has_changes(repo_root: Path) -> bool:
    result = git(repo_root, "status", "--short")
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git status failed")
    return bool(result.stdout.strip())


def build_message(thread_id: str, summary: str) -> str:
    template = os.getenv(
        "THREAD_ADVANCE_COMMIT_MESSAGE_TEMPLATE",
        "thread({thread_id}): {summary}",
    )
    return template.format(thread_id=thread_id, summary=summary)


def commit_round(repo_root: Path, thread_id: str, summary: str) -> bool:
    if not has_changes(repo_root):
        return False

    add_result = git(repo_root, "add", "-A")
    if add_result.returncode != 0:
        raise RuntimeError(add_result.stderr.strip() or "git add failed")

    commit_result = git(repo_root, "commit", "-m", build_message(thread_id, summary))
    if commit_result.returncode != 0:
        raise RuntimeError(commit_result.stderr.strip() or "git commit failed")

    return True


def main() -> int:
    args = parse_args()
    commit_round(Path(args.repo_root), args.thread_id, args.summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
