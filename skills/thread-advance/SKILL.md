---
name: thread-advance
description: Advance one runnable thread by one bounded round from the minimal continuation entry, stopping on dirty interrupt files, pending proposals, or contract overreach.
---

# Thread Advance

Use this skill to continue an existing thread by one bounded round.

## Core Rule

Read the minimal thread state, run one bounded contract, write back only the current baton, then stop.

## Workflow

1. Confirm the target `thread/<thread-id>` branch context.
2. Read `AGENTS.md`, `CLAUDE.md`, the thread `memory.md`, and the thread `interrupt.md`.
3. Check for dirty `interrupt.md` or pending `memory-proposal.md`.
4. Follow the active `NextStepContract`.
5. Advance exactly one round.
6. Rewrite `interrupt.md` with the new stop point.

## Stop Conditions

Stop immediately if:

- `interrupt.md` is dirty and `THREAD_ADVANCE_STOP_ON_DIRTY_INTERRUPT=true`
- `memory-proposal.md` is pending and `THREAD_ADVANCE_STOP_ON_PENDING_PROPOSAL=true`
- the contract would be exceeded
- verification fails
- a truth or boundary change is required

## Env Defaults

- `THREAD_ADVANCE_STOP_ON_DIRTY_INTERRUPT=true`
- `THREAD_ADVANCE_STOP_ON_PENDING_PROPOSAL=true`
- `THREAD_SELECTION_POLICY=highest-priority-runnable`
- `THREAD_PRIORITY_DEFAULT=P2`

Fallback behavior:

- If env vars are absent, use conservative stop-on-blocker defaults.

## When To Load Reference

Load [thread-advance-guards.md](./references/thread-advance-guards.md) when you need exact blocker semantics or continuation discipline.
