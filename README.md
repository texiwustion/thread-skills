# Thread Skills

Installable skills for running a repository-native thread system across Codex and Claude Code.

## Skill Suite

- `thread-intake`: classify one or many goals into existing threads, new threads, or one grouped clarification round
- `thread-bootstrap`: allocate stable `slug-tNN` thread IDs and initialize new thread baselines from templates
- `thread-advance`: advance one runnable thread by one bounded round from the minimal continuation entry
- `thread-orchestrator`: intake, bootstrap, and advance at most one highest-priority runnable thread per directory

## Configuration

Copy `.env.example` to `.env` and adjust values for your workflow. The checked-in example sets conservative defaults:

- one runnable thread per directory
- grouped clarification capped at five questions
- stop on dirty `interrupt.md`
- stop on pending `memory-proposal.md`

## Publish With GitHub CLI

Create a public repository and push the current branch:

```bash
gh repo create <owner>/thread-skills --public --source=. --push
```

## Install With `npx skills`

Install one skill at a time from the GitHub repo path:

```bash
npx skills add <owner>/thread-skills --path skills/thread-intake
npx skills add <owner>/thread-skills --path skills/thread-bootstrap
npx skills add <owner>/thread-skills --path skills/thread-advance
npx skills add <owner>/thread-skills --path skills/thread-orchestrator
```

The same GitHub path model works for both Codex and Claude Code.

## License

This repository is licensed under Apache License 2.0. See [`LICENSE`](./LICENSE).
