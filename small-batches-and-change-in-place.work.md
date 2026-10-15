---
ongoing_work_file: "Relocate the ideas of the old notes small-batches and change-in-place one by one, then recenter both. Empty when both are gone from old-claude/rationale/, their two recentered files stand in philosophy/, and every link to them is re-pointed."
rank: 1
---

# small-batches and change-in-place

Split out of `sync-repo.work.md`, step 3.2; its migration flow (MO) applies. Old notes in `old-claude/rationale/`, reference copy in `old-claude-reference/`.

## State

- Both notes at once: relocate their ideas one by one to the homes below, then recenter what is left.
- `change-in-place`, recentered on its purpose: counterbalance the AI bias toward rewriting from scratch and plugging the flow in at the end, which nullifies small steps and atomic commits. `make-the-change-easy` uses it as its MO.
- `small-batches`, recentered on how to split work: elephant carpaccio (Cockburn). Open: technical stages as the exception, when no thinner functional cut exists, or as a normal level of the plan, as the old note has it. The name follows.
- Little's law: dropped.
- Holding cost (Reinertsen's term, now in `batch-size-economics`) stays one file: a reader needs why holding cost is high to get the economics. Split a part out only when another path needs it without the rest; likeliest first: unvalidated work, for planning.
- Holding cost, heaviest first: cost of delay (missed gain, manque à gagner), unvalidated work (built on an untested hypothesis, written off if it fails; fast feedback is what shrinks it), then risk. Entry name: unvalidated work, leaning; alternative late feedback.
- Unseen: a line in `batch-size-economics`, about the whole holding cost: the economics are not obvious because holding cost is unseen.

| Idea | From | Home |
|---|---|---|
| Reinertsen frame; risk lands at once at the big-bang integration | both | `batch-size-economics`, already there |
| Cost of delay | small-batches | `batch-size-economics`, Holding cost, entry Delay |
| Fast feedback | small-batches | `batch-size-economics`, Holding cost, entry Unvalidated work |
| Inventory piling up unseen | small-batches | `batch-size-economics`, one line on holding cost as a whole |
| Just in time, the why: a piece built early waits unvalidated | change-in-place | the same, Unvalidated work |
| Just in time, the rule: each piece built with what consumes it | change-in-place | `small-batches`, recentered |
| Option value: forecast disposable, state precious | small-batches | `planning-is-everything`, at its migration |
| Every stage ends working and deployed | small-batches | `continuous-delivery`, at its migration |
| Dark code: new behavior dark then keystone, existing behavior in place | change-in-place | `continuous-delivery`, at its migration |
| Refactor and redesign alternated, recursively | small-batches | `make-the-change-easy`, already there |
| Atomic commit below the plan | small-batches | `atomic-commit`, already there |
| In place as the MO | change-in-place | `make-the-change-easy` points at `change-in-place` |

## Next

1. Relocate, one idea per turn, down the table.
2. Recenter `change-in-place`.
3. Recenter `small-batches`, and name it.
4. Re-point the links to `small-batches`: `make-the-change-easy`, `trunk-based-development`, `atomic-commit`, `guest-codebase`, `batch-size-economics`; the skills `write-plan`, `refactoring-moves` at 3.4.
5. Mapping rows in `sync-repo.work.md`; delete this file.
