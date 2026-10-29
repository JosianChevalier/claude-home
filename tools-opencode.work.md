---
ongoing_work_file: "OpenCode runs the harness tools through run. Empty when a fresh OpenCode session shows the tools' help at start and run grab-notebook prints a path keyed by its session id."
rank: 1
---

# OpenCode verification

First pull on the OpenCode laptop, nothing checked yet: `run` appears as a tool, its help block in context at start, `run grab-notebook` prints `/tmp/notebook-<opencode session id>.md`.

If it breaks, two suspects: OpenCode loading every file of `tools/`, not only `run.ts`, and choking on the bash scripts; `Bun.$`'s `.env()` dropping the inherited environment.
