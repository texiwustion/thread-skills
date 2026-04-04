# Thread Orchestrator Policy

## Dispatch Order

1. Intake goals
2. Group by directory
3. Classify attach vs bootstrap
4. Select one highest-priority runnable thread per directory
5. Dispatch the action
6. Summarize results compactly

## Runnable Thread Selection

- Respect `THREAD_SELECTION_POLICY=highest-priority-runnable`
- Respect `THREAD_ORCHESTRATOR_MAX_THREADS_PER_DIR=1`
- If the directory has no runnable thread, bootstrap only if allowed and needed

## Reporting

Return only:

- new threads created
- existing threads advanced
- blocked threads and reasons

## Env Defaults

- `THREAD_ORCHESTRATOR_MAX_DIRS_PER_RUN=3`
- `THREAD_ORCHESTRATOR_MAX_THREADS_PER_DIR=1`
- `THREAD_ORCHESTRATOR_ALLOW_AUTO_BOOTSTRAP=true`
- `THREAD_ORCHESTRATOR_ALLOW_AUTO_ATTACH=true`
- `THREAD_SELECTION_POLICY=highest-priority-runnable`

Fallback behavior:

- If env vars are absent, do not fan out aggressively.

