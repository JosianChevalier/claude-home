#!/usr/bin/env bash
# The philosophy corpus: the index, every file under one tag, or an exploration one cluster per call.
# Usage: navigation.sh index | navigation.sh tag <name> | navigation.sh explore start | navigation.sh explore <id> <file>… | navigation.sh explore <id> --more
# index: one line per file, name | tags | **Thesis.** line; no Thesis line shows "—": its tags are the index.
# tag: each file whose tags list holds <name> exactly, as <file name="philosophy/x.md">…</file>.
# explore: start prints a run id and the index, a link per file. <id> <file>… serves the files whole, up to ~24 KB,
#   never one already served in the run, then the files they link to as thesis, headings and link; a `more` link
#   while files are queued. The run id is in every link: copy the link.
set -euo pipefail
dir="$(cd "$(dirname "$0")/.." && pwd)"

usage() { sed -n '3p' "$0" | sed 's/^# //' >&2; exit 1; }
tags() { awk '/^---$/{n++; next} n==1 && /^tags:/{sub(/^tags: */, ""); print; exit}' "$1"; }
files() { for f in "$dir"/*.md; do case "$f" in *.work.md|*/README.md) ;; *) echo "$f" ;; esac; done; }

case "${1:-}" in
  index)
    files | while read -r f; do
      thesis="$(grep -m1 '^\*\*Thesis\.\*\*' "$f" | sed 's/^\*\*Thesis\.\*\* *//' || true)"
      printf '%s | %s | %s\n' "$(basename "$f" .md)" "$(tags "$f")" "${thesis:-—}"
    done ;;
  tag)
    [ -n "${2:-}" ] || usage
    hit=
    while read -r f; do
      tags "$f" | tr -d '[]' | tr ',' '\n' | sed 's/^ *//; s/ *$//' | grep -qxF -- "$2" || continue
      printf '<file name="philosophy/%s">\n' "$(basename "$f")"; cat "$f"; printf '</file>\n'
      hit=1
    done < <(files)
    [ -n "$hit" ] || { echo "no file tagged: $2" >&2; exit 1; } ;;
  explore) shift; exec python3 -I "$dir/navigation/explore.py" "$0" "$dir" "$@" ;;
  *) usage ;;
esac
