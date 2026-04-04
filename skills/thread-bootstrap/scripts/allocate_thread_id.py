#!/usr/bin/env python3
"""Allocate the next stable thread ID for a slug inside a threads directory."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


THREAD_ID_RE = re.compile(r"^(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)-t(?P<num>\d{2})$")


def normalize_slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)
    if not slug:
        raise ValueError("slug must contain at least one alphanumeric character")
    return slug


def allocate_thread_id(threads_dir: Path, raw_slug: str) -> str:
    slug = normalize_slug(raw_slug)
    max_suffix = 0

    if threads_dir.exists():
        for child in threads_dir.iterdir():
            if not child.is_dir() or child.name.startswith(".") or child.name == "_template":
                continue
            match = THREAD_ID_RE.match(child.name)
            if match and match.group("slug") == slug:
                max_suffix = max(max_suffix, int(match.group("num")))

    return f"{slug}-t{max_suffix + 1:02d}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slug", required=True, help="Goal slug or raw title to normalize")
    parser.add_argument(
        "--threads-dir",
        default="threads",
        help="Path to the threads directory. Defaults to ./threads.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        thread_id = allocate_thread_id(Path(args.threads_dir), args.slug)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    print(thread_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
