#!/bin/bash
# Commit wrapper: validates the message then commits.
# Usage: commit.sh <message> [git-commit-flags...]
#   Supports \n in <message> for multi-line commit messages.

set -euo pipefail

RAW="${1:?Usage: commit.sh <message> [git-commit-flags...]}"
MESSAGE=$(printf '%b' "$RAW")
shift

# Block --no-verify
for arg in "$@"; do
  if [[ "$arg" == "--no-verify" ]]; then
    echo "ERROR: --no-verify is not allowed." >&2
    exit 1
  fi
done

# Validate subject line length (first line, ≤72 chars)
SUBJECT=$(echo "$MESSAGE" | head -n1)
SUBJECT_LENGTH=${#SUBJECT}
if (( SUBJECT_LENGTH > 72 )); then
  echo "ERROR: Subject line is ${SUBJECT_LENGTH} chars (max 72)." >&2
  echo "  Subject: $SUBJECT" >&2
  exit 1
fi

# Validate commit message structure
LINE_COUNT=$(echo "$MESSAGE" | wc -l)
if (( LINE_COUNT > 1 )); then
  SECOND_LINE=$(echo "$MESSAGE" | sed -n '2p')
  if [[ -n "$SECOND_LINE" ]]; then
    echo "ERROR: Line 2 must be empty (blank line between subject and body)." >&2
    exit 1
  fi

  # Check for footer: scan from the end for key: value lines
  IN_FOOTER=false
  FOUND_FOOTER_BLANK=true
  while IFS= read -r line; do
    if [[ "$line" =~ ^[A-Za-z-]+:\ .+ ]]; then
      IN_FOOTER=true
    elif $IN_FOOTER; then
      # First non-footer line going backwards — must be blank
      if [[ -n "$line" ]]; then
        FOUND_FOOTER_BLANK=false
      fi
      break
    fi
  done < <(echo "$MESSAGE" | tail -n +3 | tac)

  if $IN_FOOTER && ! $FOUND_FOOTER_BLANK; then
    echo "ERROR: Footer must be preceded by a blank line." >&2
    exit 1
  fi
fi

git commit -m "$MESSAGE" "$@"

# Rebase on main after commit when working on a branch (trunk-based development)
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [[ "$CURRENT_BRANCH" != "main" ]]; then
  echo "Rebasing on main..."
  if ! timeout 20 git fetch origin main 2>/dev/null; then
    echo "WARNING: Could not fetch origin/main (network unreachable or VPN off). Rebasing on local main." >&2
  fi
  git rebase main
fi
