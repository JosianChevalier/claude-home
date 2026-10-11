#!/bin/bash
# Prototype commit: skips pre-commit hooks.
# Only works on prototype/* branches with 🧪 [PROTOTYPE] prefix.
# Usage: prototype-commit.sh <message>

set -euo pipefail

MESSAGE="${1:?Usage: prototype-commit.sh <message>}"

# Validate branch name
BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [[ "$BRANCH" != prototype/* ]]; then
  echo "ERROR: Prototype commits only allowed on prototype/* branches." >&2
  echo "  Current branch: $BRANCH" >&2
  exit 1
fi

# Validate commit message prefix
if [[ "$MESSAGE" != "🧪 [PROTOTYPE]"* ]]; then
  echo "ERROR: Prototype commit message must start with '🧪 [PROTOTYPE]'." >&2
  echo "  Got: $MESSAGE" >&2
  exit 1
fi

exec git commit --no-verify -m "$MESSAGE"
