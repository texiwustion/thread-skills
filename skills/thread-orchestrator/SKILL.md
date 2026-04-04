---
name: thread-orchestrator
description: Dispatch multi-goal requests across directories by intaking, bootstrapping, or advancing at most one highest-priority runnable thread per directory.
---

# Thread Orchestrator

Use this skill to run the thread system as a thin scheduler.

## Core Rule

Group work by directory first, then choose at most one highest-priority runnable thread per directory.

## Workflow

1. Intake incoming goals.
2. Group them by directory or repo.
3. Decide for each goal whether to bootstrap or advance.
4. Select one runnable thread per directory.
5. Dispatch the chosen action.
6. Return a compact result summary.

## Scheduling Rule

- Default selection policy: `highest-priority-runnable`
- Default per-directory concurrency: `1`
- Use multiple worktrees for same-repo parallelism, not multiple active threads in one worktree

## Env Defaults

- `THREAD_ORCHESTRATOR_MAX_DIRS_PER_RUN=3`
- `THREAD_ORCHESTRATOR_MAX_THREADS_PER_DIR=1`
- `THREAD_ORCHESTRATOR_ALLOW_AUTO_BOOTSTRAP=true`
- `THREAD_ORCHESTRATOR_ALLOW_AUTO_ATTACH=true`
- `THREAD_SELECTION_POLICY=highest-priority-runnable`

Fallback behavior:

- If env vars are absent, keep the orchestrator thin and conservative.

## When To Load Reference

Load [thread-orchestrator-policy.md](../../shared/references/thread-orchestrator-policy.md) when you need exact dispatch and reporting rules.

