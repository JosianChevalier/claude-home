---
ongoing_work_file: "A pre-made `replace-text` script replaces the inline Python agents write to edit text. Empty when the recount shows agents calling `replace-text` instead of writing the script, or `replace-text` is dropped."
rank: 7
---

# replace-text

A small token optimization, not a fix: agents edit text well with inline Python (`python3 - <<'EOF' … open(p,'w').write(s)`), but rewrite the same few lines each time. `replace-text` is those lines, pre-made, called in one line; `rules/tools.md` points agents to it; its `model-coupled` comment marks it for recheck at a model change.

## Evidence (transcripts, 2026-10-08 → 17)

- 292 inline-Python edits in 68 sessions, against 102 Edit-tool calls and 96 `sed -i`. 286 of them in `~/.claude`, so mostly markdown.
- Scaffolding is ~20% of a call's characters; the rest is anchors and new text.
- What the scripts do:

| Form | Calls |
|---|---|
| Exact replacement(s), one file | ~121 |
| Several files in one call | ~81 |
| Insert before/after an anchor (`old+new`) | ~25 |
| Section between two anchors | ~23 |
| Delete a span (`replace(old,'')`) | ~15 |
| Other: JSON, regex, moves, patch staging | ~27, out of scope |

- ~2/3 already guard with `assert s.count(old)==1`; some define their own `def rep(p, pairs)`.
- Transcripts mix Fable 5.1 and Opus 5.5; the split per model is not done.

## First check (2026-10-18, one day after release)

- 125 `replace-text` calls. Since the rule: 61 calls against 12 inline-Python edits, 10 of these from one session started before the rule, 2 a structural rewrite out of scope.
- 3 failures, all `0 matches` on a wrong anchor: nothing written, retried. No tool bug.
- Friction: single calls chained with `&&` (all-or-nothing lost), `--between` never used, `git diff` after ~9 calls. Answered by the rule rewrite and the `FILE:LINE -REMOVED +ADDED` output.

## Steps

- [ ] From 2026-10-20, rerun the check, split per model, and feed what `replace-text` misses back into it. **← current**
  - The data: `~/.claude/projects/*/*.jsonl`, Bash `tool_use` items matched to their `tool_result` by `tool_use_id`; leave out the session doing the check and `-private-var-folders-` projects (headless tests).
  - Count per session: `replace-text` calls, inline-Python edits (`python` and `write(`), Edit; note whether the session started before the rule.
  - Failures: results with `nothing written` or a traceback, and what the agent did next.
  - Friction, from each call with ~6 events before and 2 after, read by a scout: single calls chained with `&&` instead of a batch, `--between` used, `git diff` still run after an edit, quoting workarounds, inline Python the tool could have done.
