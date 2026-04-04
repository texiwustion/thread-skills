# Thread Advance Guards

## Minimal Continuation Entry

- Confirm the target thread branch first
- Read only `AGENTS.md`, `CLAUDE.md`, thread `memory.md`, and thread `interrupt.md`
- Do not widen reads unless those files explicitly point to more context

## Blockers

- Dirty `interrupt.md`
- Pending `memory-proposal.md`
- Failed verification
- Contract overreach
- Need to change approved truth or scope boundaries

## Env Defaults

- `THREAD_ADVANCE_STOP_ON_DIRTY_INTERRUPT=true`
- `THREAD_ADVANCE_STOP_ON_PENDING_PROPOSAL=true`
- `THREAD_SELECTION_POLICY=highest-priority-runnable`
- `THREAD_PRIORITY_DEFAULT=P2`

Fallback behavior:

- If env vars are absent, stop on any ambiguity rather than guessing.

