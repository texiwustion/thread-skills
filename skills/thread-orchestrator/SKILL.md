---
name: thread-orchestrator
description: Dispatch multi-goal requests across directories by intaking, bootstrapping, or advancing at most one highest-priority runnable thread per directory.
---

# Thread Orchestrator

Use this skill to run the thread system as a thin scheduler.

## Core Rule

Group work by directory first. If `threads/_template/` is missing and auto bootstrap is allowed, perform repo bootstrap in the same round before choosing the runnable thread. Only report blocked when repo bootstrap is required but not allowed.

## Workflow

1. Intake incoming goals.
2. Group them by directory or repo.
3. If a directory lacks `threads/_template/`:
   - when `THREAD_ORCHESTRATOR_ALLOW_AUTO_BOOTSTRAP=true`, run `thread-repo-bootstrap` immediately in the same round
   - when auto bootstrap is disabled, report blocked and stop for that directory
4. After repo bootstrap, decide for each goal whether to bootstrap or advance.
5. Select one runnable thread per directory.
6. Dispatch the chosen action.
7. Return a compact result summary.

## Scheduling Rule

- Default selection policy: `highest-priority-runnable`
- Default per-directory concurrency: `1`
- Default repo prerequisite: `threads/_template/` must exist before any thread advance
- Use multiple worktrees for same-repo parallelism, not multiple active threads in one worktree

Missing `threads/_template/` is not itself a blocker when auto bootstrap is enabled. It is a prerequisite action to perform first.

## Env Defaults

- `THREAD_ORCHESTRATOR_MAX_DIRS_PER_RUN=3`
- `THREAD_ORCHESTRATOR_MAX_THREADS_PER_DIR=1`
- `THREAD_ORCHESTRATOR_ALLOW_AUTO_BOOTSTRAP=true`
- `THREAD_ORCHESTRATOR_ALLOW_AUTO_ATTACH=true`
- `THREAD_ORCHESTRATOR_REQUIRE_REPO_BOOTSTRAP=true`
- `THREAD_SELECTION_POLICY=highest-priority-runnable`

Fallback behavior:

- If env vars are absent, stay conservative but still treat missing repo bootstrap as a prerequisite action rather than an immediate blocked outcome.

## When To Load Reference

Load [thread-orchestrator-policy.md](./references/thread-orchestrator-policy.md) when you need exact dispatch and reporting rules.
