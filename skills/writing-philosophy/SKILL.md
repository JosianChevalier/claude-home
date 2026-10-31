---
name: writing-philosophy
description: "Trigger: working on the philosophy layer: planning, drafting or editing a philosophy/ file."
---

# Writing philosophy

## Doctrine

- Philosophy is the anchor of the harness: continuous improvement adjusts it constantly, and without an anchor it swings ever wider or drifts from the original intent.
- What is already in the weights and standard is identified unambiguously.
- A reading laid on an existing concept is overloaded: the concept identified, the change written next to it.
- An idiosyncratic reading or practice is detailed: spelled out and explained.
- When the agent knows what the user means, it writes; when it does not, it asks. Nothing is anchored before it was talked through with the user.

## The session

```
user talks ──▶ draft ──▶ anything to raise? ──no──▶ user validates ──▶ land
                 ▲              │ yes
                 │              ▼
             redesign ◀── user answers, or adds
```

The file is drafted from the first input, holding only what the user said and the implications plainly in it.

Each round sediments: one question, its answer, its impact written, then the next question. Questions are never batched before writing.

Any step may be prepared first, long or in the background, such as scouting `philosophy/` for the concept's home and its neighbours.

Every input challenges the structure: is the current shape still the one that best integrates all that was said? There is almost always a restatement that holds the old and the new together; the file is redesigned around it, and a line is added only when none exists. Additive bias (Adams) pulls the other way.

The agent goes on alone and stops only to raise:

- a clarification needed
- an adjacent field, concept, theory or attractor: what it says, what it would pull in
- an incoherence or a contradiction
- a cut: the input brings a concept the file reads without, or one another file would build on
- a rule or skill this file underpins: a practice at odds with it, or one it should crystallize

Nothing raised enters the file before the user takes it.

By default, how the agent names and cuts is its composition grid: it guides the photographer, and the viewer sees only the picture. The user may want to be more hands-on.

## Referencing a concept

A concept enters identified, overloaded or detailed (φfield-terms). Identified, it takes as much as it needs, and no more:

```
name (author)              the default; the author stands for the field
  + field                  when the name means different things in different domains
    + pins, optional       when the user is expert there, or readings compete:
                           biases toward the specialists
        ──▶ never explained
```

Pins triangulate the region of the field meant. A pejorative the weights hold (primitive obsession, shotgun parsing) is named outright: observed constantly, naming it pushes away (φattractors).

## Where a concept lives

One source of truth per concept, DRY (Hunt & Thomas).

Using a concept is taking a dependency:

- named from the weights, it pulls a package
- linked to a philosophy file, it pulls our own module

A concept the user adds nothing to already lives in the weights: no file.

A file exists for what the user brings on top. Other files depend on it, never restate it.

A link is proposed after reading the target file, never from a keyword match.

## Grow, then cut

An idea goes into the closest file until there is enough material to build on; the file is cut when it gets big. Agents load philosophy file by file, through the rationale lines of rules and skills: a file holding more than one concept makes every reference to it load the rest.

- **Several paths.** A concept several files build on, or that solves several files' problems, gets its own file, reachable from each.
- **Readable without it.** When part of a file reads without the details of one aspect, that aspect goes to its own file. A problem with several detailed solutions becomes a file per solution, unless they are one-liners.

`parse-dont-validate` and `always-valid-domain` are the second case: one could hold both, and each reads on its own.

## Shape of the file

```markdown
---
tags: [ddd, vocabulary]
---

# Title

**Thesis.** One sentence: the scout loads every thesis, as a skill description is loaded whole.

## A section per idea

## Related

- What it holds, in a few words: φother-file.
```

The Thesis line comes first after the title, the governing thought before its support (Minto): `navigation.sh index` exports it. Tags grow with the corpus, they are how a file is found.

## Landing chores

- Tags in the frontmatter; a new tag gets its line in `philosophy/navigation/tags.md`
- `philosophy/navigation/navigation.sh index` shows the file with its Thesis
- Every `φ<name>` resolves to `philosophy/<name>.md`; no em-dashes
- A neighbour shrunk by the new file has its Related updated; old rules repointed

## Examples

**Identified.**

> The old system is replaced by a **strangler fig** (Fowler).

Named and nothing more. A paragraph on growing the new system around the old one would cost the reader what the model already knew.

**Identified precisely.**

> Each **aggregate** (Evans), the consistency boundary, is saved whole.

Alone, "aggregate" could be a SQL function. Evans fixes the field; "the consistency boundary" pins the reading meant among DDD's. Nothing about DDD is explained.

**Overloaded.**

> Terms are **attractors** (Juarrero), context-sensitive constraints: they do not label, they constrain what follows. In the model's semantic landscape a precise term carves the basin the next tokens fall into, and the basin is indifferent to negation: "don't use X" carves X's.

Juarrero's context-sensitive constraints are referenced. That a term in a model's context acts as one, and that negation feeds the basin, is the user's reading: spelled out.

**Detailed.**

> The **spork**: two complete readings of one concept fit, and one artifact is made to hold both, the union of their state, the intersection of their behaviour.

Nothing in the weights carries it: the whole reading is written out.

Rationale: φthree-layer-harness, φharness-elements, φattractors, φfield-terms, φcollaborative-production, φzoom-levels
