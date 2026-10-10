#!/usr/bin/env bash
# List ongoing work files, lowest rank first.
# Usage: list-work.sh [root]   (default: repo root or cwd)
set -euo pipefail
root="${1:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"

cd "$root" && find . -name '*.md' -not -path '*/.git/*' -print0 \
| xargs -0 awk '
  FNR==1 { inblock = ($0 == "---"); file = ""; rank = ""; next }
  !inblock { nextfile }
  $0 == "---" {
    if (file != "") printf "%s\t%s\t%s\n", (rank == "" ? "999999" : rank), substr(FILENAME, 3), file
    nextfile
  }
  /^ongoing_work_file:[[:space:]]*/ { sub(/^ongoing_work_file:[[:space:]]*/, ""); gsub(/^"|"$/, ""); file = $0 }
  /^rank:[[:space:]]*/ { sub(/^rank:[[:space:]]*/, ""); rank = $0 }
' \
| sort -n -k1,1 \
| awk -F'\t' '{ printf "%-4s %s\n     %s\n", $1, $2, $3 }'
