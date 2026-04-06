# Thread Orchestrator Policy

## Dispatch Order

1. Intake goals
2. Group by directory
3. If `threads/_template/` or `.git/` is missing:
   - run repo bootstrap first when auto bootstrap is enabled
   - otherwise report blocked for that directory
4. Classify attach vs bootstrap
5. Select one highest-priority runnable thread per directory
6. Dispatch the action
7. Summarize results compactly

## Runnable Thread Selection

- Respect `THREAD_SELECTION_POLICY=highest-priority-runnable`
- Respect `THREAD_ORCHESTRATOR_MAX_THREADS_PER_DIR=1`
- Respect `THREAD_ORCHESTRATOR_REQUIRE_REPO_BOOTSTRAP=true`
- Respect `THREAD_ORCHESTRATOR_ALLOW_AUTO_BOOTSTRAP=true` as permission to perform repo bootstrap inline rather than stopping early
- Treat missing `.git/` as part of missing repo bootstrap, not as a separate blocked state when auto bootstrap is enabled
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
- `THREAD_ORCHESTRATOR_REQUIRE_REPO_BOOTSTRAP=true`
- `THREAD_SELECTION_POLICY=highest-priority-runnable`

Fallback behavior:

- If env vars are absent, do not fan out aggressively, but still treat missing repo bootstrap as setup work before reporting blocked.
