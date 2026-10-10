#!/usr/bin/env bash
# Create a work file.
# Usage: new-work.sh <path.md> "<what must empty, and when it counts as empty>" [rank]
# Rank defaults to last (max + 1).
set -euo pipefail
path="$1"; what="$2"; rank="${3:-}"
here="$(cd "$(dirname "$0")" && pwd)"
root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

[ -e "$path" ] && { echo "exists: $path" >&2; exit 1; }

if [ -z "$rank" ]; then
  max="$("$here/list-work.sh" "$root" | awk 'NR%2==1 && $1 != 999999 {print $1}' | sort -n | tail -1)"
  rank=$(( ${max:-0} + 1 ))
fi

mkdir -p "$(dirname "$path")"
printf -- '---\nongoing_work_file: "%s"\nrank: %s\n---\n\n# %s\n\n- [ ] \n' "${what//\"/\\\"}" "$rank" "$(basename "$path" .md)" > "$path"
echo "$rank  $path"
