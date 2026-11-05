---
ongoing_work_file: "OpenCode's launcher sets TMPDIR=/tmp/opencode in place of HARNESS_TMPDIR, which nothing reads anymore. Empty when a fresh OpenCode session writes its notebook and exploration state under /tmp/opencode."
rank: 104
---

# opencode-tmpdir

The harness scripts that keep session state (`tools/grab-notebook`, `philosophy/navigation/explore.py`) read `TMPDIR`; unset, they fall back to plain `/tmp`, shared with every user. OpenCode's launcher, which lives outside this repo (container or terminal), still exports `HARNESS_TMPDIR=/tmp/opencode`, so OpenCode currently writes to `/tmp`. The local `opencode.json` already allows `/tmp/opencode`.

- [ ] In the OpenCode launcher, replace `HARNESS_TMPDIR=/tmp/opencode` with `TMPDIR=/tmp/opencode`. An export does not reach a running OpenCode: restart it. ← next
- [ ] In the fresh session, call `grab-notebook` twice and `philosophy/navigation/navigation.sh explore start`; both state files land under `/tmp/opencode` and the notebook path repeats. Then delete this file.
