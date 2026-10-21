#!/usr/bin/env bash
# The philosophy corpus: the index, every file under one tag, or files with those they link to.
# Usage: navigation.sh index | navigation.sh tag <name> | navigation.sh cluster <file>...
# index: one line per file, name | tags | **Thesis.** line; no Thesis line shows "—": its tags are the index.
# tag: each file whose tags list holds <name> exactly, as <file name="philosophy/x.md">…</file>.
# cluster: each <file> (name without .md) and every file it links to as [[philosophy/x]], once each, same format.
set -euo pipefail
dir="$(cd "$(dirname "$0")/.." && pwd)"

usage() { sed -n '3p' "$0" | sed 's/^# //' >&2; exit 1; }
tags() { awk '/^---$/{n++; next} n==1 && /^tags:/{sub(/^tags: */, ""); print; exit}' "$1"; }
files() { for f in "$dir"/*.md; do case "$f" in *.work.md|*/README.md) ;; *) echo "$f" ;; esac; done; }
show() { printf '<file name="philosophy/%s">\n' "$(basename "$1")"; cat "$1"; printf '</file>\n'; }

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
      show "$f"
      hit=1
    done < <(files)
    [ -n "$hit" ] || { echo "no file tagged: $2" >&2; exit 1; } ;;
  cluster)
    shift; [ $# -gt 0 ] || usage
    for n in "$@"; do
      [ -f "$dir/$n.md" ] || { echo "no file: $n" >&2; exit 1; }
      echo "$n"; grep -o '\[\[philosophy/[a-z0-9-]*\]\]' "$dir/$n.md" | sed 's/^\[\[philosophy\///; s/\]\]$//' || true
    done | awk '!seen[$0]++' | while read -r n; do
      if [ -f "$dir/$n.md" ]; then show "$dir/$n.md"; else echo "dangling link: $n" >&2; fi
    done ;;
  *) usage ;;
esac
