# Thread Bootstrap Rules

## ID Allocation

- Format: `<topic-slug>-tNN`
- `topic-slug` should be stable, lowercase, and hyphen-delimited
- `NN` is the next available two-digit suffix for that slug
- Never rename a thread after creation

## Branching

- Preferred branch: `thread/<thread-id>`
- If `THREAD_BOOTSTRAP_AUTO_CHECKOUT=true`, switch to the branch after creating it
- Do not create run branches here

## Template Initialization

- Source templates from `threads/_template/`
- Require repo bootstrap first; do not create the template root ad hoc here
- Copy only the minimum thread files
- Keep `memory.md` typed and short
- Keep `interrupt.md` focused on the first stop point

## Env Defaults

- `THREAD_BOOTSTRAP_ID_STYLE=slug-tNN`
- `THREAD_BOOTSTRAP_AUTO_CHECKOUT=true`
- `THREAD_BOOTSTRAP_TEMPLATE_ROOT=threads/_template`

Fallback behavior:

- If env vars are absent, use the repo template root, slug-tNN IDs, and conservative branch switching.
