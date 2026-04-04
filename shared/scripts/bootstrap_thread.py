#!/usr/bin/env python3
"""Initialize a thread directory from repository templates."""

from __future__ import annotations

import argparse
from pathlib import Path


MEMORY_TEMPLATE = "memory.md"
INTERRUPT_TEMPLATE = "interrupt.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--thread-id", required=True, help="Target thread ID")
    parser.add_argument("--goal", required=True, help="One-line goal for the new thread")
    parser.add_argument(
        "--threads-dir",
        default="threads",
        help="Path to the threads directory. Defaults to ./threads.",
    )
    return parser.parse_args()


def render_memory(template: str, thread_id: str, goal: str) -> str:
    return template.replace("<thread-id>", thread_id).replace("<中文，一句话目标>", goal)


def render_interrupt(template: str, thread_id: str) -> str:
    return template.replace("<thread-id>", thread_id)


def bootstrap_thread(threads_dir: Path, thread_id: str, goal: str) -> Path:
    template_dir = threads_dir / "_template"
    target_dir = threads_dir / thread_id
    target_dir.mkdir(parents=True, exist_ok=False)

    memory_template = (template_dir / MEMORY_TEMPLATE).read_text(encoding="utf-8")
    interrupt_template = (template_dir / INTERRUPT_TEMPLATE).read_text(encoding="utf-8")

    (target_dir / MEMORY_TEMPLATE).write_text(
        render_memory(memory_template, thread_id, goal),
        encoding="utf-8",
    )
    (target_dir / INTERRUPT_TEMPLATE).write_text(
        render_interrupt(interrupt_template, thread_id),
        encoding="utf-8",
    )

    return target_dir


def main() -> int:
    args = parse_args()
    bootstrap_thread(Path(args.threads_dir), args.thread_id, args.goal)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
