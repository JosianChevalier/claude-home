---
ongoing_work_file: "OpenCode can use the harness editing and session-notebook tools without Claude-specific paths or assumptions"
rank: 1
---

# OpenCode tool portability


## Current step

First run on OpenCode, none installed here: `run` appears as a tool and `run doc opencode` through it prints the list; `run grab-notebook` prints a path keyed by OpenCode's session id. If `run` is missing: OpenCode may load every file of `tools/`, not only `*.ts`, and choke on the bash scripts; or `Bun.$`'s `.env()` may drop `process.env`.


Keep Claude's existing scripts working. Do not include `wake-and-run`, status widgets, or compaction policy in this work.
