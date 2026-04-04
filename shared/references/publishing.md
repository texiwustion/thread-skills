# Publishing

## GitHub

Create a public repository from the current directory:

```bash
gh repo create <owner>/thread-skills --public --source=. --push
```

If the repo already exists, push the current branch with normal git remotes instead.

## `npx skills`

Install a skill from the GitHub repo path:

```bash
npx skills add <owner>/thread-skills --path skills/thread-intake
npx skills add <owner>/thread-skills --path skills/thread-bootstrap
npx skills add <owner>/thread-skills --path skills/thread-advance
npx skills add <owner>/thread-skills --path skills/thread-orchestrator
```

Use the same repo/path model for Codex and Claude Code.

## Release Discipline

- Keep `.env.example` checked in.
- Keep `.env` local and untracked.
- Publish only after local scaffold, scripts, and skill metadata pass validation.
- Smoke-test at least one installed skill before announcing the repo.
