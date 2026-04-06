---
name: thread-repo-bootstrap
description: Initialize thread-system files in a fresh directory by creating threads/_template, initializing git when missing, and establishing the minimum repository-native thread templates before any thread advance.
---

# Thread Repo Bootstrap

Use this skill to make a fresh directory eligible for thread work.

## Core Rule

If `threads/_template/` does not exist or the directory is not yet a git repo, initialize the repo thread system first. When invoked by `thread-orchestrator` with auto bootstrap enabled, return control so the same round can continue into thread bootstrap or thread advance.

## Workflow

1. Check whether the target directory is already a git repo and already has `threads/_template/`.
2. If `.git/` is missing and git init is enabled, run `git init` with the configured default branch.
3. If `threads/_template/` is missing, create it.
4. Create the minimum template set:
   - `memory.md`
   - `interrupt.md`
   - `memory-proposal.md`
   - `platform-memory-proposal.md`
5. Confirm the directory now has repo-level thread capability and git-backed history for future advances.
6. Return control to `thread-orchestrator` or hand off to `thread-bootstrap`.

## Rules

- Never skip repo bootstrap in an empty directory and jump straight into thread advancement.
- Never rewrite existing templates silently; initialize only what is missing unless a human explicitly asks for migration.
- Treat repo bootstrap as the prerequisite layer below thread bootstrap.
- Treat git initialization as part of repo bootstrap unless `THREAD_REPO_BOOTSTRAP_INIT_GIT=false`.
- Do not convert missing repo bootstrap into a blocked outcome when the caller explicitly allows auto bootstrap.

## Env Defaults

- `THREAD_ORCHESTRATOR_REQUIRE_REPO_BOOTSTRAP=true`
- `THREAD_REPO_BOOTSTRAP_INIT_GIT=true`
- `THREAD_REPO_BOOTSTRAP_GIT_DEFAULT_BRANCH=main`

Fallback behavior:

- If env vars are absent, require repo bootstrap whenever `threads/_template/` is missing.

## When To Load Reference

Load [thread-repo-bootstrap-rules.md](./references/thread-repo-bootstrap-rules.md) when you need exact repo initialization rules.

## Scripts

- `scripts/init_thread_repo.py`
