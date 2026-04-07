# Thread Skills

Installable skills for running a repository-native thread system across Codex and Claude Code.

## Skill Suite

- `thread-intake`: classify one or many goals into existing threads, new threads, or one grouped clarification round
- `thread-repo-bootstrap`: initialize `threads/_template/`, create a git repo when missing, and lay down the minimum repo-level thread-system files in a fresh directory
- `thread-bootstrap`: allocate stable `slug-tNN` thread IDs and initialize new thread baselines from templates
- `thread-advance`: advance one runnable thread by one bounded round from the minimal continuation entry
- `thread-orchestrator`: intake, bootstrap, and advance at most one highest-priority runnable thread per directory

## Configuration

Copy `.env.example` to `.env` and adjust values for your workflow. The checked-in example sets conservative defaults:

- one runnable thread per directory
- repo bootstrap required before thread advance in a fresh directory
- repo bootstrap initializes git by default so commit-backed rounds can happen in the same round
- grouped clarification capped at five questions
- stop on dirty `interrupt.md`
- stop on dirty worktrees before an auto-committing round
- stop on pending `memory-proposal.md`
- auto-commit successful thread advances by default

## Canonical Model

- Canonical thread state lives under `threads/<thread-id>/`
- The default workflow is `main` plus thread directories, not branch-per-thread
- Dedicated `thread/<thread-id>` branches or worktrees are optional advanced infrastructure for teams that want stronger isolation

## Publish With GitHub CLI

Create a public repository and push the current branch:

```bash
gh repo create <owner>/thread-skills --public --source=. --push
```

## Install With `npx skills`

Preferred one-command install on macOS, Linux, or WSL:

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/texiwustion/thread-skills/main/scripts/install-thread-skills.sh)
```

If you already cloned the repo, run the local wrapper instead:

```bash
./scripts/install-thread-skills.sh
```

Useful variants:

```bash
./scripts/install-thread-skills.sh --agent codex
./scripts/install-thread-skills.sh --agent claude-code -g
./scripts/install-thread-skills.sh --skill thread-orchestrator --skill thread-advance
./scripts/install-thread-skills.sh --dry-run
```

Manual fallback if you do not want the wrapper script:

```bash
npx skills add texiwustion/thread-skills \
  --skill thread-repo-bootstrap \
  --skill thread-bootstrap \
  --skill thread-intake \
  --skill thread-advance \
  --skill thread-orchestrator \
  -a codex claude-code \
  -y --copy
```

The same GitHub path model works for both Codex and Claude Code.

Each skill now carries its own references and required scripts so path-based installation does not depend on repo-root `shared/` files.

When `THREAD_ORCHESTRATOR_ALLOW_AUTO_BOOTSTRAP=true`, a fresh directory without `threads/_template/` or `.git/` should be initialized in the same orchestration round before thread creation or advancement continues.

## Windows AI Rewrite Prompt

This repository does not ship a `.bat` installer. For Windows users, the supported path is WSL or asking an AI coding assistant to rewrite the shell wrapper into PowerShell for your environment. Use this prompt:

```text
Rewrite this Bash installer into an equivalent PowerShell script for Windows 11.

Requirements:
- Preserve behavior exactly from scripts/install-thread-skills.sh
- Keep support for: --repo, --agent (repeatable), --skill (repeatable), -g/--global, --dry-run, --no-copy, --no-yes, -h/--help
- Preserve env overrides: THREAD_SKILLS_REPO, THREAD_SKILLS_GLOBAL, THREAD_SKILLS_DRY_RUN
- Final command must call:
  npx skills add <repo> --skill ... -a ... [-g] [-y] [--copy]
- Output only one PowerShell script, no explanation
- Avoid Windows batch; PowerShell only
```

## License

This repository is licensed under Apache License 2.0. See [`LICENSE`](./LICENSE).
