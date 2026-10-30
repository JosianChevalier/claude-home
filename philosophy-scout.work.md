---
ongoing_work_file: "philosophy-scout searches through navigation.sh explore, a cluster per call. Empty when the steps below are taken or dropped."
rank: 5
---

# philosophy-scout

The scout (`agents/philosophy-scout.md`) is called by `philosophy-guide` and by kaizen sessions, both with a loaded context: each splits a user question into sub-questions, one scout per sub-question, and reads whole the files it returns. A test calls it as the `philosophy-scout` subagent type.

## Runs, 2026-10-30

Question: "How should we use an agent to handle our gitflow?" Corpus: 52 files. ON: files a judge, reading them whole, says an answer would cite; six exist for this question (agentic-trunk-based-development, trunk-based-development, atomic-commit, continuous-delivery, batch-size-economics, agentic-extreme-programming).

| | model | files | ON of 6 | calls | time | tokens |
|---|---|---|---|---|---|---|
| index + Read, run 1 | Fable | 16 | | 31 | 75 s | 72k |
| index + Read, run 2 | Fable | 10 | | 6 | 42 s | 53k |
| explore | Fable | 9 | 3 | 6 | 36 s | 53k |
| explore, registered type | Fable | 9 | 3 | 6 | 27 s | 48k |
| explore, fog-of-war bullet, A | Fable | 9 | 5 | 10 | 58 s | 64k |
| explore, fog-of-war bullet, B | Fable | 10 | 4 | 9 | 50 s | 61k |
| explore, fog-of-war bullet | Opus | 6 | 3 | 12 | 21 s | 47k |
| explore, fog-of-war bullet | Sonnet | 5 | 4 | 8 | 12 s | 35k |

Where the time goes, run A: tool 7 s, model 50 s. Turns 1–4 take 2 s each; turns 5–10 take 5–11 s, each preceded by 450–750 output tokens of deliberation on which links bear. The pages are not the cost; the turns are, and what the scout writes before each call. Opus and Sonnet ran every command twice (relative path, then with a cd): their real calls are half the column.

Explore against the old index + Read scout on three questions, judged file by file: equal recall (11 against 12 of 14 ON files), 20 calls against 32. Half of every return is on the subject only, from both scouts; accepted, the cut from 52 is the point.

`continuous-delivery` is ON by inference (every commit releasable makes a release branch pointless) and came back in one run of eight (Sonnet): its thesis never names what it displaces. A philosophy edit if any, not a scout one.

A run is counted from the task notification (tokens, tool uses, duration) and from the subagent's transcript, the `output_file` the Agent tool names: one JSON object per line, the calls are the `tool_use` blocks of the `assistant` lines, a tool result opening with `<persisted-output>` is a call lost to the cap. Extracted by script, never read whole.

⚠️ Claude Code loads `agents/*.md` at session start: an edited scout is tested in the session that edited it as a general-purpose agent told to read the file and be it, the registered type only in a fresh session.

## Steps

- [ ] Explore serves the linked files whole, not as tags, thesis and headings. Hypothesis: the previews make the scout choose at every round, and the choosing is the time; whole files would mean fewer rounds. Against it: a neighbourhood whole is several pages under the cap, a turn each. Test: the gitflow question, same model as the row compared against, time and calls into the table. **← current**
- [ ] Pin the scout's model in the agent file. The step said Opus; the table says Sonnet, on one run. The frontmatter is shared with opencode (`provider/model-id`); Claude Code takes `sonnet`. Check both docs for a per-tool override.
- [ ] The corpus bullet's first command as `<harness-root>/philosophy/navigation/navigation.sh explore start`: the relative form cost Opus and Sonnet a retry per command.
- [ ] Angles step, the pull-request question: three runs today returned `zoom-levels` and `compounding-decisions` every time and `model-tiers` never, which a judge rated off the question. Drop the step, or its criterion becomes the two.
  > My agent keeps forcing itself to find feedback in pull requests. What do I do? (an agent asked to review a PR always produces findings, inventing nitpicks when there is nothing real). Files I already know bear on it: attractors.
- [ ] Kaizen group to take or drop: the guide showed the scout's whole haul, ideas off the reader's case included.
- Parked: `harness-design` is 21 files, 13k words, never a dump unit; a sub-tag cut only if a scout is seen dumping it whole.
