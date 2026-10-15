#!/usr/bin/env bash
# The philosophy index: one line per file, name | tags | **Thesis.** line.
# Usage: navigation.sh index
# A file without a Thesis line shows "—": its tags are the index.
set -euo pipefail
dir="$(cd "$(dirname "$0")" && pwd)"

[ "${1:-}" = index ] || { sed -n '3p' "$0" >&2; exit 1; }
for f in "$dir"/*.md; do
  case "$f" in *.work.md) continue ;; esac
  tags="$(awk '/^---$/{n++; next} n==1 && /^tags:/{sub(/^tags: */, ""); print; exit}' "$f")"
  thesis="$(grep -m1 '^\*\*Thesis\.\*\*' "$f" | sed 's/^\*\*Thesis\.\*\* *//' || true)"
  printf '%s | %s | %s\n' "$(basename "$f" .md)" "$tags" "${thesis:-—}"
done
