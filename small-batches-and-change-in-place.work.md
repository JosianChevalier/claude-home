---
ongoing_work_file: "Write batch-slicing, pulling from the old notes small-batches and change-in-place what it needs, then recenter change-in-place. Empty when both are gone from old-claude/rationale/, batch-slicing and the recentered change-in-place stand in philosophy/, and every link to them is re-pointed."
rank: 1
---

# small-batches and change-in-place

Split out of `sync-repo.work.md`, step 3.2; its migration flow (MO) applies. Old notes in `old-claude/rationale/`, reference copy in `old-claude-reference/`.

## State

- Pull, not push: start with `batch-slicing` and pull from the two old notes what it needs. The rows below with other homes wait for those homes.
- `small-batches` becomes `philosophy/batch-slicing`; elephant carpaccio (Cockburn) names its top level only. Core idea (2026-10-15): finding the next hypothesis to validate, and cutting the smallest slice that can test it. First the hypotheses of value, about the domain and the user: functional increments only production verifies. Under them, technical hypotheses. Just in time is a line in passing (written).
- Crossing the valley (`make-the-change-easy`): one line, as how to slice deeper. Not the main idea. Intermediate models are more or less coherent; the point is going from one hill to another.
- A reshape is a slice at the technical level, not a value hypothesis.
- Technical slices are a normal level under each functional increment, not an exception (user, 2026-10-15). Hence the rename from `elephant-carpaccio`.
- What defines a step: a north star that guides tiny sub-agents. It is the human's unit of thought.
- Little's law: dropped.
- Holding cost (Reinertsen's term, now in `batch-size-economics`) stays one file: a reader needs why holding cost is high to get the economics. Split a part out only when another path needs it without the rest; likeliest first: speculative work, for planning.

| Idea | From | Home |
|---|---|---|
| Reinertsen frame; risk lands at once at the big-bang integration | both | `batch-size-economics`, already there |
| Cost of delay | small-batches | `batch-size-economics`, Holding cost, entry Delay |
| Fast feedback | small-batches | `batch-size-economics`, Holding cost, entry Speculative work |
| Inventory piling up unseen | small-batches | `batch-size-economics`, one line on holding cost as a whole |
| Just in time, the why: a piece built early waits unvalidated | change-in-place | the same, Speculative work |
| Just in time, the rule: each piece used as soon as it lands | change-in-place | `batch-slicing`, a line in passing |
| Option value: forecast disposable, state precious | small-batches | `planning-is-everything`, at its migration |
| Last responsible moment (Poppendieck): when to commit to a decision; optionality, so architecture | change-in-place | a philosophy of designing architecture, later |
| Nested feedback loops: any change a hypothesis, one loop per level | new | its own philosophy, later; home open |
| Pull (Lean, Ohno): a piece built because its user asks for it; push the failure mode | new | later, one layer up; home open |
| Every stage ends working and deployed | small-batches | `continuous-delivery`, at its migration |
| Dark code: new behavior dark then keystone, existing behavior in place | change-in-place | `continuous-delivery`, at its migration |
| Refactor and redesign alternated, recursively | small-batches | `make-the-change-easy`, already there |
| Atomic commit below the plan | small-batches | `atomic-commit`, already there |
| In place as the MO | change-in-place | `make-the-change-easy` points at `change-in-place` |

## Next

1. Re-point the links to `small-batches` at `batch-slicing`: `make-the-change-easy`, `trunk-based-development`, `atomic-commit`, `guest-codebase`, `batch-size-economics`; the skills `write-plan`, `refactoring-moves` at 3.4.
2. Mapping rows in `sync-repo.work.md`; delete this file.
