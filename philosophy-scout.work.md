---
ongoing_work_file: "philosophy-scout searches through navigation.sh explore, a cluster per call. Empty when a fresh session's registered philosophy-scout runs the gitflow question through explore in about five calls, and the steps below are taken or dropped."
rank: 5
---

# philosophy-scout

The scout (`agents/philosophy-scout.md`) is called by `philosophy-guide` and by kaizen sessions, both with a loaded context: each splits a user question into sub-questions, one scout per sub-question, and reads whole the files it returns. A test calls it as the `philosophy-scout` subagent type.

## Runs, 2026-10-30

Question: "How should we use an agent to handle our gitflow?" Corpus: 52 files.

| | files | calls | time | tokens |
|---|---|---|---|---|
| index + Read, run 1 | 16 | 31 | 75 s | 72k |
| index + Read, run 2 | 10 | 6 | 42 s | 53k |
| explore | 9 | 6 | 36 s | 53k |

Same instructions, runs 1 and 2: that much spread. One run compares nothing; a change is judged on several.

The return size is accepted: the cut from 52 is the point, a near file riding along is not blocking. The time was the turns: one file per turn once a shell cat hit the tool's output cap (~30 KB). Explore holds the whole response, links included, under 24 KB.

⚠️ Claude Code loads `agents/*.md` at session start: an edited scout is tested in the session that edited it as a general-purpose agent told to read the file and be it, the registered type only in a fresh session.

## Steps

- [ ] Fresh session: the registered `philosophy-scout` on the gitflow question goes through explore, about five calls. **← current**
- [ ] Validate the angles step: scout on the bare question, no hint of angles. Passes if `zoom-levels`, `compounding-decisions` and `model-tiers` come back.
  > My agent keeps forcing itself to find feedback in pull requests. What do I do? (an agent asked to review a PR always produces findings, inventing nitpicks when there is nothing real). Files I already know bear on it: attractors.
- [ ] Pin the scout to Opus whatever the session model. The agent file is shared with opencode (`provider/model-id`); Claude Code takes `opus`. Check both docs for a fallback list or a per-tool override.
- [ ] Kaizen group to take or drop: the guide showed the scout's whole haul, ideas off the reader's case included.
- Parked: `harness-design` is 21 files, 13k words, never a dump unit; a sub-tag cut only if a scout is seen dumping it whole.
