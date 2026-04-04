---
name: thread-intake
description: Intake one or many goals, classify them into existing threads or new threads, and ask one grouped Socratic round when needed.
---

# Thread Intake

Use this skill to turn a multi-goal request into a thread plan.

## Core Rule

Prefer attachment over bootstrap when goals overlap materially; ask at most one grouped round of questions when clarification is required.

## Workflow

1. Read the incoming goals.
2. Scan existing thread summaries and stops.
3. Classify each goal:
   - attach to an existing thread
   - create a new thread
   - ask one grouped clarification round
4. Return a compact recommendation set.

## Question Rule

- Ask one grouped round only.
- Keep each question necessary and concrete.
- For each question, include why it matters, the recommended default, and the conservative fallback if unanswered.

## Env Defaults

- `THREAD_ORCHESTRATOR_MAX_QUESTIONS=5`
- `THREAD_ORCHESTRATOR_ALLOW_AUTO_ATTACH=true`
- `THREAD_ORCHESTRATOR_ALLOW_AUTO_BOOTSTRAP=true`

Fallback behavior:

- If env vars are absent, prefer attachment when safe and ask fewer questions, not more.

## When To Load Reference

Load [thread-intake-policy.md](./references/thread-intake-policy.md) when you need exact classification or question formats.
