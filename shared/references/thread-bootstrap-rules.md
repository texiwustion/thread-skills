# Thread Bootstrap Rules

## ID Allocation

- Format: `<topic-slug>-tNN`
- `topic-slug` should be stable, lowercase, and hyphen-delimited
- `NN` is the next available two-digit suffix for that slug
- Never rename a thread after creation

## Execution Context

- Canonical thread state lives in `threads/<thread-id>/`
- Dedicated `thread/<thread-id>` branches are optional advanced infrastructure, not a default requirement
- If a wrapper honors `THREAD_BOOTSTRAP_AUTO_CHECKOUT=true`, use it only in repos that explicitly adopt branch-per-thread execution
- Do not create run branches here

## Template Initialization

- Source templates from `threads/_template/`
- Require repo bootstrap first; do not create the template root ad hoc here
- Copy only the minimum thread files
- Keep `memory.md` typed and short
- Keep `interrupt.md` focused on the first stop point

## Env Defaults

- `THREAD_BOOTSTRAP_ID_STYLE=slug-tNN`
- `THREAD_BOOTSTRAP_AUTO_CHECKOUT=false`
- `THREAD_BOOTSTRAP_TEMPLATE_ROOT=threads/_template`

Fallback behavior:

- If env vars are absent, use the repo template root, slug-tNN IDs, and directory-first execution.
