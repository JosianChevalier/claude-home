#!/usr/bin/env bash
# Usage: bash scripts/grab-kaizen-file.sh [absolute-kaizen-file-path]
# Create a private Kaizen file, or reopen one passed from another session.
#   Print its path. Without TMPDIR, fail rather than create state in public /tmp.
set -euo pipefail
umask 077

if (( $# > 1 )) || [[ -z "${TMPDIR:-}" || "$TMPDIR" == /tmp ]]; then
  printf 'usage: TMPDIR=<private-directory> bash scripts/grab-kaizen-file.sh [absolute-kaizen-file-path]\n' >&2
  exit 2
fi

here="$(cd "$(dirname "$0")" && pwd)"
root="$(python3 -I "$here/../../../tools/private_temp_dir.py" "$TMPDIR")"

if (( $# == 0 )); then
  mktemp "$root/kaizen-XXXXXXXX.md"
  exit
fi

file="$1"
name="${file##*/}"
if [[ ! "$name" =~ ^kaizen-[a-zA-Z0-9_-]+\.md$ || "$file" != "$root/$name" || -L "$file" || ! -f "$file" || ! -O "$file" || "$(python3 -I -c 'import os, stat, sys; print(oct(stat.S_IMODE(os.lstat(sys.argv[1]).st_mode))[2:])' "$file")" != 600 ]]; then
  printf 'unsafe or missing Kaizen file: %s\n' "$file" >&2
  exit 1
fi
printf '%s\n' "$file"
