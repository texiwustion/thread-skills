# Thread Intake Policy

## Classification

- Attach when the goal materially overlaps an existing thread goal and scope
- Bootstrap when the goal is distinct enough to need its own state container
- Ask one grouped clarification round only when attachment vs bootstrap is still ambiguous

## Question Format

Each question should include:

- why it matters
- recommended default
- conservative fallback if unanswered

## Env Defaults

- `THREAD_ORCHESTRATOR_MAX_QUESTIONS=5`
- `THREAD_ORCHESTRATOR_ALLOW_AUTO_ATTACH=true`
- `THREAD_ORCHESTRATOR_ALLOW_AUTO_BOOTSTRAP=true`

Fallback behavior:

- If env vars are absent, classify conservatively and keep the question count low.
