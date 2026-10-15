---
ongoing_work_file: "Every philosophy file carries a Thesis line, enforced. Empty when a pre-commit hook rejects a commit touching philosophy/ that leaves a file without one."
rank: 3
---

# philosophy-thesis-hook

Not a priority. The `philosophy-scout` agent indexes the corpus by its `**Thesis.**` lines (`philosophy/navigation/navigation.sh index`); a file without one falls back to its tags, a weaker index.

## Steps

- [ ] Give `model-tiers.md` and `zoom-levels.md` a Thesis line. **← current**
- [ ] Pre-commit hook: a commit touching `philosophy/*.md` fails if a touched file has no `**Thesis.**` line.
