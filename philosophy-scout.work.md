---
ongoing_work_file: "philosophy-scout returns what a loaded kaizen context can afford. Empty when its return rule is decided, written in agents/philosophy-scout.md, and a test run confirms it."
rank: 5
---

# philosophy-scout

The scout (`agents/philosophy-scout.md`) is called from a kaizen session whose context is already loaded. Its posture: explore until a round adds nothing, return passages verbatim. Not yet registered as a subagent type: a test runs it as a general-purpose agent told to read the file and be it, with `<harness-root>` = the checkout.

## Test run, 2026-10-15

Question: "How should we use an agent to handle our gitflow?"

| | |
|---|---|
| Subagent tokens | 81k, 10 tool calls, 60 s |
| Rounds | 5 link-following, stopped at the first dry one |
| Return | ~4k tokens, 10 files quoted |
| Tag dump | not used (`trunk-based-development` is on 2 files, read directly) |

- Core, on the question: `agentic-trunk-based-development`, `trunk-based-development`, `atomic-commit`, `compounding-decisions`.
- Near, not on it: `agentic-extreme-programming`, `batch-size-economics`, `model-tiers`. The "no passage that only sits near the question" rule did not hold them back.
- Off procedure: read `process-units` on speculation (no file cited it); grepped five files instead of reading them.

The hazard: a 4k return into an already loaded context costs about what reading the 3 right files directly would.

## Steps

- [ ] Decide the return rule: exhaustive search kept, return ranked (core first, near ones apart), or return capped at the core. **← current**
- [ ] Decide what to do with the off-procedure moves (speculative reads, grep): forbid, or allow and write them in.
- [ ] Write it in `agents/philosophy-scout.md`, rerun the gitflow question, compare with the table above.
