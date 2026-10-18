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

## Steps

- [ ] From 2026-10-20, recount inline-Python edits in the transcripts (Bash calls with `python` and `write(`) against the baseline above, split per model. Since the rule rewrite of 2026-10-18, also check: batches used instead of single calls chained with `&&`, `--between` used, `git diff` no longer run after an edit. Feed what `replace-text` misses back into it. **← current**
