# Thread Repo Bootstrap Rules

## Purpose

- Create the repo-level thread system in a fresh directory
- Establish `threads/_template/` before any thread bootstrap or thread advance

## Minimum Files

- `threads/_template/memory.md`
- `threads/_template/interrupt.md`
- `threads/_template/memory-proposal.md`
- `threads/_template/platform-memory-proposal.md`

## Guardrails

- If `threads/_template/` is missing, thread advancement must not start
- Initialize missing template files only; do not silently overwrite customized templates
- After repo bootstrap, hand off to `thread-bootstrap` for new threads

## Env Defaults

- `THREAD_ORCHESTRATOR_REQUIRE_REPO_BOOTSTRAP=true`

Fallback behavior:

- If env vars are absent, require repo bootstrap whenever the template root is missing.
