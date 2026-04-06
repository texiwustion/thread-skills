---
name: thread-bootstrap
description: Bootstrap a new thread from a goal, allocate a stable slug-tNN thread id, initialize thread files from templates, and honor env-driven defaults for thread creation.
---

# Thread Bootstrap

Use this skill to create a new thread when a goal should not be attached to an existing thread.

## Core Rule

Allocate a stable `thread-id` once, initialize from `threads/_template/`, and stop before doing any goal work.

## Workflow

1. Confirm `threads/_template/` already exists and repo bootstrap has established git state when branch checkout is expected.
2. If the template root or `.git/` is missing, stop and hand off to `thread-repo-bootstrap`.
3. Decide whether the goal belongs in an existing thread.
4. If new thread is required, generate `<topic-slug>-tNN`.
5. Create or checkout `thread/<thread-id>`.
6. Copy `threads/_template/memory.md` and `threads/_template/interrupt.md`.
7. Fill only the minimum bootstrap fields.
8. Write the first stop point into `interrupt.md`.

## Rules

- Use `THREAD_BOOTSTRAP_ID_STYLE=slug-tNN` by default.
- Use `THREAD_BOOTSTRAP_AUTO_CHECKOUT=true` to decide whether to switch branches automatically.
- Use `THREAD_BOOTSTRAP_TEMPLATE_ROOT=threads/_template` when set; otherwise use the repo default.
- Repo bootstrap is a hard prerequisite; do not invent template files ad hoc during thread bootstrap.
- If branch creation or checkout is part of the bootstrap round, require `.git/` first.
- Never rename a thread after creation.
- Never add proposal or execution content beyond bootstrap state.

## When To Load Reference

Load [thread-bootstrap-rules.md](./references/thread-bootstrap-rules.md) when you need exact ID allocation, template, or branch rules.

## Scripts

- `scripts/allocate_thread_id.py`
- `scripts/bootstrap_thread.py`
