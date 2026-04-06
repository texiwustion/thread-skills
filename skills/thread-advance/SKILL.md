---
name: thread-advance
description: Advance one runnable thread by one bounded round from the minimal continuation entry, stopping on dirty interrupt files, pending proposals, or contract overreach, then auto-commit a successful round by default.
---

# Thread Advance

Use this skill to continue an existing thread by one bounded round.

## Core Rule

Read the minimal thread state, run one bounded contract, write back only the current baton, auto-commit the successful round when enabled, then stop.

## Workflow

1. Confirm the target `thread/<thread-id>` branch context.
2. Read `AGENTS.md`, `CLAUDE.md`, the thread `memory.md`, and the thread `interrupt.md`.
3. Check for dirty `interrupt.md`, dirty worktree when auto-commit is enabled, or pending `memory-proposal.md`.
4. Follow the active `NextStepContract`.
5. Advance exactly one round.
6. Rewrite `interrupt.md` with the new stop point.
7. If verification passed and no proposal is pending, commit the round by default with `scripts/commit_thread_round.py`.

## Stop Conditions

Stop immediately if:

- `interrupt.md` is dirty and `THREAD_ADVANCE_STOP_ON_DIRTY_INTERRUPT=true`
- the worktree is dirty before the round starts and `THREAD_ADVANCE_STOP_ON_DIRTY_WORKTREE=true`
- `memory-proposal.md` is pending and `THREAD_ADVANCE_STOP_ON_PENDING_PROPOSAL=true`
- the contract would be exceeded
- verification fails
- a truth or boundary change is required

## Env Defaults

- `THREAD_ADVANCE_STOP_ON_DIRTY_INTERRUPT=true`
- `THREAD_ADVANCE_STOP_ON_DIRTY_WORKTREE=true`
- `THREAD_ADVANCE_STOP_ON_PENDING_PROPOSAL=true`
- `THREAD_ADVANCE_AUTO_COMMIT=true`
- `THREAD_ADVANCE_COMMIT_MESSAGE_TEMPLATE=thread({thread_id}): {summary}`
- `THREAD_SELECTION_POLICY=highest-priority-runnable`
- `THREAD_PRIORITY_DEFAULT=P2`

Fallback behavior:

- If env vars are absent, use conservative stop-on-blocker defaults.

## When To Load Reference

Load [thread-advance-guards.md](./references/thread-advance-guards.md) when you need exact blocker semantics or continuation discipline.

## Scripts

- `scripts/commit_thread_round.py`
