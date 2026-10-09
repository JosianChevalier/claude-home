---
tags: [harness-design, kaizen]
---

# Rationale: Harness Shape

The shape every rule and skill is written toward: a doctrine, then know-how. The layers themselves: [[philosophy/three-layer-harness]].

## Doctrine

Doctrine is what must always be true: the intent, whatever should stay true in every case. It expresses the result wanted, the posture, the mindset, in a few attractors. Heuristics belong here when they hold in all cases; a saying is the compact form.

- "Make the change easy, then make the easy change."
- "Mecha suit, not robot."
- "One change, one commit."

How it is written:

- **Quoted or coined.** Both are doctrine.
- **One header.** Today's labels in rules and skills (`Core principle`, `Iron Law`, `Prime Directive`, `Principles`, `Standing rule`, `Rule of thumb`) all become `Doctrine`.
- **Every rule and skill carries it.** The `Doctrine` header is the one fixed element of the shape.
- **Agents differ.** In an agent, and in `CLAUDE.md`, layer 2 is the posture and the objective, under their own names (`Postures`). A skill or rule is know-how with a little doctrine; an agent is doctrine with little know-how, the steps living in the skills it composes.
- **Reasons stay in philosophy.** The file points to them.
- **Doctrine inside a philosophy file** is fine when its reason and what would falsify it sit next to it.

## Know-how

What is true in the usual case: the main body of the Pareto distribution. Procedures, heuristics, checklists, knowledge, in whatever form fits; it is not always a procedure and takes no fixed header. It is the main part of the artifact, split into sections when useful. Where the situation departs from what a step assumed, the agent may leave the step, on the strength of the doctrine.

A doctrine that seems not to fit mid-execution is still obeyed, and flagged. This is expected to be rare with mature doctrine.

## The 80/20 split

The know-how is written for the usual case, roughly four out of five. The doctrine guides the fifth. Know-how that tries to cover every case grows without end and still misses one; a doctrine alone leaves the usual case to be reinvented each time.

Two consequences for how know-how is written:

- **Heuristics over orders.** A step says what usually works and what it is for, so the agent can tell when it has stopped working.
- **The limit of applicability must be felt.** What the steps assume shows somewhere: in the wording of the steps, or in the doctrine. No dedicated section is required. Its absence everywhere is a defect: an agent that cannot tell where the steps stop applying applies them everywhere.

The split is also a proportion rule. A short file is a `Doctrine` header and a few lines of know-how; sections are added when the body has grown enough to need them.

## Rewriting a file

1. Gather what must always be true under `## Doctrine`.
2. The rest is know-how: keep it after the doctrine, sectioned if useful.
3. Move reasons to philosophy and leave the pointer.
4. Keep a list of rationalizations only for temptations the current models produce unprompted. For any other temptation, the list is the pink elephant.

```markdown
# <Skill>

## Doctrine

- "Make the change easy, then make the easy change."

## <Know-how section>

1. …

Rationale: [[philosophy/workflow-rhythm]]
```

## Related

- What each harness element is for: [[philosophy/harness-elements]].
- What happens after a failed run: [[philosophy/kaizen]].

Where the rewritten harness lives: `sync-repo.md`.
