---
name: writing-philosophy
description: Trigger: touching a philosophy file.
---

# Writing philosophy

## Doctrine

- Philosophy is the anchor of the harness: continuous improvement adjusts it constantly, and without an anchor it swings ever wider or drifts from the original intent.
- What is already in the weights and standard is referenced, identified unambiguously.
- An idiosyncratic reading or practice is spelled out and explained.
- When the agent knows what the user means, it writes; when it does not, it asks. Nothing is anchored before it was talked through with the user.

## The session

```
user talks ──▶ draft ──▶ anything to raise? ──no──▶ user validates ──▶ land
                 ▲              │ yes
                 │              ▼
             redesign ◀── user answers, or adds
```

The file is drafted at once, holding only what the user said and the implications plainly in it. Every input after that challenges its structure: is the current shape still the one that best integrates all that was said? There is almost always a restatement that holds the old and the new together; the file is redesigned around it, and a line is added only when none exists. Additive bias (Adams) pulls the other way.

The agent goes on alone and stops only to raise:

- a clarification needed
- an adjacent field, concept, theory or attractor: what it says, what it would pull in
- an incoherence or a contradiction
- a rule or skill this file underpins: a practice at odds with it, or one it should crystallize

Nothing raised enters the file before the user takes it.

By default, how the agent names and cuts is its composition grid: it guides the photographer, and the viewer sees only the picture. The user may want to be more hands-on.

## Referencing a concept

Each concept already in the model's weights is referenced with as much as it needs, and no more:

```
name (author)              the default; the author stands for the field
  + field                  when the name means different things in different domains
    + pins, optional       when the user is expert there, or readings compete:
                           biases toward the specialists
        ──▶ never explained
```

Pins triangulate the region of the field meant. A pejorative the weights hold (primitive obsession, shotgun parsing) is named outright: observed constantly, naming it pushes away ([[philosophy/attractors]]).

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

**Thesis.** One or two sentences.

## A section per idea

## Related

- What it holds, in a few words: [[philosophy/other-file]].
```

The Thesis line comes first after the title: `navigation.sh index` exports it, and a check on it is planned. Tags grow with the corpus, they are how a file is found.

## Landing chores

- Tags in the frontmatter; a new tag gets its line in `philosophy/navigation/tags.md`
- `philosophy/navigation/navigation.sh index` shows the file with its Thesis
- Every `[[philosophy/...]]` resolves; no em-dashes
- A neighbour shrunk by the new file has its Related updated; old rules repointed
- A file migrated from `old-claude/`: its row in the migration table of `sync-repo.work.md`

## Example

Referenced, from `parse-dont-validate`:

> Separation logic calls it **local reasoning** (O'Hearn, Reynolds), the frame rule: a specification mentions only its footprint, and everything outside the footprint need not be read to understand it.

Name and authors; "the frame rule" pins the separation-logic sense among the many uses of "local reasoning". Nothing about separation logic is explained. Then the user's reading: "A signature of parsed types is a footprint."

Explained instead: three paragraphs on what separation logic is and why the frame rule holds. The model knew it; the reader paid for it, and the user's reading drowned in it.

Rationale: [[philosophy/three-layer-harness]], [[philosophy/harness-elements]], [[philosophy/attractors]], [[philosophy/collaborative-production]], [[philosophy/zoom-levels]]
