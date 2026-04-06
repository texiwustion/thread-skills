# Thread Repo Bootstrap Rules

## Purpose

- Create the repo-level thread system in a fresh directory
- Establish `threads/_template/` before any thread bootstrap or thread advance
- Initialize git when missing so branch operations can happen in the same round

## Minimum Files

- `threads/_template/memory.md`
- `threads/_template/interrupt.md`
- `threads/_template/memory-proposal.md`
- `threads/_template/platform-memory-proposal.md`
- `.git/` when `THREAD_REPO_BOOTSTRAP_INIT_GIT=true`

## Guardrails

- If `threads/_template/` is missing, thread advancement must not start
- If `.git/` is missing and git init is enabled, repo bootstrap must create it before any branch-oriented thread action
- Initialize missing template files only; do not silently overwrite customized templates
- After repo bootstrap, hand off to `thread-bootstrap` for new threads

## Env Defaults

- `THREAD_ORCHESTRATOR_REQUIRE_REPO_BOOTSTRAP=true`
- `THREAD_REPO_BOOTSTRAP_INIT_GIT=true`
- `THREAD_REPO_BOOTSTRAP_GIT_DEFAULT_BRANCH=main`

Fallback behavior:

- If env vars are absent, require repo bootstrap whenever the template root is missing.
