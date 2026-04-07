#!/usr/bin/env bash

set -euo pipefail

REPO_DEFAULT="texiwustion/thread-skills"
AGENTS_DEFAULT=("codex" "claude-code")
SKILLS_DEFAULT=(
  "thread-repo-bootstrap"
  "thread-bootstrap"
  "thread-intake"
  "thread-advance"
  "thread-orchestrator"
)

repo="${THREAD_SKILLS_REPO:-$REPO_DEFAULT}"
global_install="${THREAD_SKILLS_GLOBAL:-false}"
dry_run="${THREAD_SKILLS_DRY_RUN:-false}"
copy_mode=true
yes_mode=true
agents=("${AGENTS_DEFAULT[@]}")
skills=("${SKILLS_DEFAULT[@]}")

print_help() {
  cat <<'EOF'
Install the full thread-skills suite with npx skills.

Usage:
  ./scripts/install-thread-skills.sh [options]

Options:
  --repo <owner/repo>     Override the GitHub repo. Default: texiwustion/thread-skills
  --agent <name>          Add one target agent. Repeatable. Defaults: codex claude-code
  --skill <name>          Install only the named skill. Repeatable.
  -g, --global            Install globally instead of project-local.
  --dry-run               Print the npx command without running it.
  --no-copy               Do not pass --copy to npx skills.
  --no-yes                Do not pass -y to npx skills.
  -h, --help              Show this help text.

Env overrides:
  THREAD_SKILLS_REPO
  THREAD_SKILLS_GLOBAL=true|false
  THREAD_SKILLS_DRY_RUN=true|false
EOF
}

is_true() {
  case "$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]')" in
    1|true|yes|on) return 0 ;;
    *) return 1 ;;
  esac
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo)
      repo="${2:?missing value for --repo}"
      shift 2
      ;;
    --agent)
      if [[ ${agents[0]:-} == "${AGENTS_DEFAULT[0]}" && ${#agents[@]} -eq ${#AGENTS_DEFAULT[@]} ]]; then
        agents=()
      fi
      agents+=("${2:?missing value for --agent}")
      shift 2
      ;;
    --skill)
      if [[ ${skills[0]:-} == "${SKILLS_DEFAULT[0]}" && ${#skills[@]} -eq ${#SKILLS_DEFAULT[@]} ]]; then
        skills=()
      fi
      skills+=("${2:?missing value for --skill}")
      shift 2
      ;;
    -g|--global)
      global_install=true
      shift
      ;;
    --dry-run)
      dry_run=true
      shift
      ;;
    --no-copy)
      copy_mode=false
      shift
      ;;
    --no-yes)
      yes_mode=false
      shift
      ;;
    -h|--help)
      print_help
      exit 0
      ;;
    *)
      printf 'Unknown option: %s\n' "$1" >&2
      print_help >&2
      exit 1
      ;;
  esac
done

cmd=(npx skills add "$repo")

for skill in "${skills[@]}"; do
  cmd+=(--skill "$skill")
done

if [[ ${#agents[@]} -gt 0 ]]; then
  cmd+=(-a "${agents[@]}")
fi

if is_true "$global_install"; then
  cmd+=(-g)
fi

if is_true "$yes_mode"; then
  cmd+=(-y)
fi

if is_true "$copy_mode"; then
  cmd+=(--copy)
fi

printf 'Running:'
for arg in "${cmd[@]}"; do
  printf ' %q' "$arg"
done
printf '\n'

if is_true "$dry_run"; then
  exit 0
fi

exec "${cmd[@]}"
