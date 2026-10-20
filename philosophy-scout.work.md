---
ongoing_work_file: "philosophy-scout returns what a loaded kaizen context can afford. Empty when its return rule is decided, written in agents/philosophy-scout.md, and a test run confirms it."
rank: 5
---

# philosophy-scout

The scout (`agents/philosophy-scout.md`) is called by `philosophy-guide` and by kaizen sessions, both with a loaded context: each splits a user question into sub-questions, one scout per sub-question. Its posture: explore until a round adds nothing, return passages verbatim. Not yet registered as a subagent type: a test runs it as a general-purpose agent told to read the file and be it, with `<harness-root>` = the checkout.

## Baseline

Question: "How should we use an agent to handle our gitflow?" Run on the current `agents/philosophy-scout.md`.

| | |
|---|---|
| Subagent tokens | 81k, 10 tool calls, 60 s |
| Rounds | 5 link-following, stopped at the first dry one |
| Return | ~4k tokens, 10 files quoted |

- Near, not on the question: `model-tiers`. Every other file returned is on it.
- Off procedure: read `process-units` on speculation (no file cited it); grepped five files instead of reading them.

Size is acceptable (Josian); a near passage riding along is the defect.

## Return doctrine, decided

- `description: Finds the philosophy passages that bear on one question. Call with the question.` What it does and how to call it; call sites carry the detail.
- Opening line: "one kaizen question" → "one question".
- Posture, added: "**Search wide, carry light.** What you read costs your context; what you return costs the caller's, already loaded. The two bills are apart: exhaust the first, keep the second to what the question needs."
- The return, opening: "A passage comes back when it speaks to the question itself. One that speaks to the question's subject stays where you found it: having read it is what tells you the rest is enough."
- The return, removed: "No passage that only sits near the question."

## Steps

- [ ] Decide what to do with the off-procedure moves (speculative reads, grep): forbid, or allow and write them in. **← current**
- [ ] Write the doctrine and that decision in `agents/philosophy-scout.md`, rerun the gitflow question, compare with the baseline.
- Parked: `harness-design` is 21 files, 13k words, never a dump unit; a sub-tag cut only if a scout is seen dumping it whole.
