---
ongoing_work_file: "Every philosophy file carries a Thesis line, enforced, and tags at a granularity that picks a dump. Empty when a pre-commit hook rejects a commit touching philosophy/ that leaves a file without a Thesis line, and the tags are consolidated."
rank: 3
---

# philosophy-thesis-hook

Not a priority. The `philosophy-scout` agent indexes the corpus by its `**Thesis.**` lines (`philosophy/navigation/navigation.sh index`); a file without one falls back to its tags, a weaker index. `navigation.sh tag <name>` dumps every file under one tag, chosen from `philosophy/navigation/tags.md`.

## Steps

- [ ] Give `model-tiers.md` and `zoom-levels.md` a Thesis line. **← current**
- [ ] Tag granularity: 24 of 50 tags sit on one file (no use for choosing a dump), `harness-design` on 17 of 34 (half the corpus). Merge the duplicate clusters (`ddd`/`domain-modeling`/`tactical-ddd`, `batch-size`/`small-batches`/`flow`, `trunk-based-development`/`continuous-integration`, `consistency`/`invariants`/`aggregates`), drop single-file tags, fix `attractors.md` tagged `vocabulary` instead of `attractors`; then rewrite `tags.md`. Merges proposed in conversation, decided by Josian.
- [ ] Pre-commit hook: a commit touching `philosophy/*.md` fails if a touched file has no `**Thesis.**` line.
