---
ongoing_work_file: "philosophy-scout answers in a few calls: an explore command serves a cluster per call, paginated, a file never twice. Empty when the command is in navigation.sh, the scout searches through it, and a gitflow run beats the baseline below."
rank: 5
---

# philosophy-scout

The scout (`agents/philosophy-scout.md`) is called by `philosophy-guide` and by kaizen sessions, both with a loaded context: each splits a user question into sub-questions, one scout per sub-question, and reads whole the files it returns. A test calls it as the `philosophy-scout` subagent type.

## Baseline, 2026-10-30

Question: "How should we use an agent to handle our gitflow?"

| | |
|---|---|
| Subagent tokens | 72k, 31 tool calls, 30 turns, 75 s |
| Return | 16 files of 52: 8 on the question, 8 on its subject |

The time is the turns: a shell cat of nine files hit the tool's output cap (~30 KB), then one Read per turn for 27 files. The return size is accepted: the cut from 52 is the point, a near file riding along is not blocking.

## The explore command

HATEOAS: each response carries the next calls, the scout copies one, the state stays in the tool.

- `navigation.sh explore start` → a run id, a served list and a queue created empty, the index with a link per file.
- `navigation.sh explore <id> <file>…` → the files queued; the queue served up to ~24 KB of whole files, marked served; then the `[[links]]` of what was served, minus served and queued, each as tags, thesis, `##` headings, link; a `more` link while the queue is not empty.
- `navigation.sh explore <id> --more` → the same with nothing new queued.
- The run id is in every link: several scouts run in parallel in one session and the session id cannot tell them apart (probed 2026-10-30: a subagent's shell carries the parent's session id and pid).

## Steps

- [ ] Write the command, in `philosophy/navigation/`. **← current**
- [ ] The scout's search section: start, open the entry points of each mechanism in one call, then the links whose thesis and headings bear, several per call, `more` when shown; stop at the round that adds no file that applies. The "read several files per turn" bullet goes.
- [ ] Rerun the gitflow question, compare with the baseline.
- [ ] Validate the angles step: scout on the bare question, no hint of angles. Passes if `zoom-levels`, `compounding-decisions` and `model-tiers` come back.
  > My agent keeps forcing itself to find feedback in pull requests. What do I do? (an agent asked to review a PR always produces findings, inventing nitpicks when there is nothing real). Files I already know bear on it: attractors.
- [ ] Pin the scout to Opus whatever the session model. The agent file is shared with opencode (`provider/model-id`); Claude Code takes `opus`. Check both docs for a fallback list or a per-tool override.
- [ ] Kaizen group to take or drop: the guide showed the scout's whole haul, ideas off the reader's case included.
- Parked: `harness-design` is 21 files, 13k words, never a dump unit; a sub-tag cut only if a scout is seen dumping it whole.
