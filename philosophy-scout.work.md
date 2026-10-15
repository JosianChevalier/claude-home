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
- Relevant too: `agentic-extreme-programming`, `batch-size-economics` (first labelled near; Josian: both relevant).
- Near, not on it: `model-tiers`. The "no passage that only sits near the question" rule did not hold it back.
- Off procedure: read `process-units` on speculation (no file cited it); grepped five files instead of reading them.

4k is acceptable (Josian). The issue is the load, not the size: a near passage rides along with the core ones.

## Trial, 2026-10-15: return doctrine

Same question, scratch copy of the scout with the wording below. One run each: variance not ruled out.

| | First run | Trial |
|---|---|---|
| Subagent tokens | 81k, 10 tool calls, 60 s | 69k, 6 tool calls, 27 s |
| Files quoted | 10 | 6 |
| Return | ~4k tokens | ~2k tokens (estimate) |
| `model-tiers` | returned | dropped |

All six files returned are on the question.

## Steps

- [x] Write the return doctrine. Exhaust the scent, bring back only what the question needs (central-place foraging, Orians & Pearson). Callers: `philosophy-guide` and kaizen, each splitting a user question into sub-questions, one scout per sub-question. Wording, tried above:
  - `description: Finds the philosophy passages that bear on one question. Call with the question.` The description says what it does and how to call it; call sites carry the detail.
  - Opening line: "one kaizen question" → "one question".
  - Posture, added: "**Search wide, carry light.** What you read costs your context; what you return costs the caller's, already loaded. The two bills are apart: exhaust the first, keep the second to what the question needs."
  - The return, opening: "A passage comes back when it speaks to the question itself. One that speaks to the question's subject stays where you found it: having read it is what tells you the rest is enough."
  - The return, removed: "No passage that only sits near the question."
- [ ] Decide what to do with the off-procedure moves (speculative reads, grep): forbid, or allow and write them in. **← current**
- [ ] Write it in `agents/philosophy-scout.md`, rerun the gitflow question, compare with the table above.
