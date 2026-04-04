---
name: thread-repo-bootstrap
description: Initialize thread-system files in a fresh directory by creating threads/_template and the minimum repository-native thread templates before any thread advance.
---

# Thread Repo Bootstrap

Use this skill to make a fresh directory eligible for thread work.

## Core Rule

If `threads/_template/` does not exist, initialize the repo thread system first. When invoked by `thread-orchestrator` with auto bootstrap enabled, return control so the same round can continue into thread bootstrap or thread advance.

## Workflow

1. Check whether `threads/_template/` already exists.
2. If not, create `threads/_template/`.
3. Create the minimum template set:
   - `memory.md`
   - `interrupt.md`
   - `memory-proposal.md`
   - `platform-memory-proposal.md`
4. Confirm the directory now has repo-level thread capability.
5. Return control to `thread-orchestrator` or hand off to `thread-bootstrap`.

## Rules

- Never skip repo bootstrap in an empty directory and jump straight into thread advancement.
- Never rewrite existing templates silently; initialize only what is missing unless a human explicitly asks for migration.
- Treat repo bootstrap as the prerequisite layer below thread bootstrap.
- Do not convert missing repo bootstrap into a blocked outcome when the caller explicitly allows auto bootstrap.

## Env Defaults

- `THREAD_ORCHESTRATOR_REQUIRE_REPO_BOOTSTRAP=true`

Fallback behavior:

- If env vars are absent, require repo bootstrap whenever `threads/_template/` is missing.

## When To Load Reference

Load [thread-repo-bootstrap-rules.md](./references/thread-repo-bootstrap-rules.md) when you need exact repo initialization rules.

## Scripts

- `scripts/init_thread_repo.py`
