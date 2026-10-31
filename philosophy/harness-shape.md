---
tags: [harness-design, kaizen]
---

# Harness shape

**Thesis.** A rule or skill is a doctrine and know-how, then a pointer to its rationale. The doctrine is a few attractors that hold everywhere, fat tail included; the know-how is the head of the Pareto distribution, commodified into steps; the pointer keeps the reasons out of the file. The layers themselves: φthree-layer-harness.

```
 ## Doctrine          what must always be true   a few attractors; holds in the fat tail; at the top, or per section
 ## <know-how>…       what worked                the head, commodified; left on the doctrine's word
 Rationale: [[…]]     why                        lives in the rationale; only the pointer stays
```

## Doctrine

Doctrine is what must always be true: the intent, the result wanted, the posture, in a few attractors (φattractors). A heuristic belongs here when it holds in every case, and it is written as a maxim or an aphorism: a known saying when one fits, a coined one otherwise. A line that carries a condition or a step ("only what would…", "before X, do Y") is know-how, whatever header it sits under.

- "Make the change easy, then make the easy change."
- "Mecha suit, not robot."
- "One change, one commit."

How it is written:

- **Quoted or coined.** Both are doctrine. How one is found: φfield-terms.
- **Spread out.** The doctrine heads the file, or sits with the part of the know-how it governs, and moves with that part.
- **Identifiable.** Wherever it sits, a reader tells at once which lines hold always. Every rule and skill carries a doctrine marked so; the mark is the file's choice: a blank line before the know-how, a section of its own, "Doctrine:" before a list, whatever fits.
- **Agents differ.** In an agent, and in `CLAUDE.md`, the doctrine is the posture and the objective, under their own names (`Postures`). A skill or rule is know-how with a little doctrine; an agent is doctrine with little know-how, the steps living in the skills it composes.
- **Reasons stay in the rationale.** The file points to it.

## Know-how

What worked in the usual case: the head of the Pareto distribution, commodified into steps. Procedures, heuristics, checklists, knowledge, in whatever form fits; it is not always a procedure and takes no fixed header. It is the main part of the artifact, split into sections when useful.

Where the situation departs from what a step assumed, the agent may leave the step, on the strength of the doctrine. A doctrine that seems not to fit mid-execution is still obeyed, and flagged; rare with mature doctrine.

## The split

The know-how is written for the head of the distribution. The doctrine guides the fat tail. Know-how that tries to cover the tail grows without end and still misses a case; a doctrine alone leaves the head to be reinvented each time.

Two consequences for how know-how is written:

- **Heuristics over orders.** A step says what usually works and what it is for, so the agent can tell when it has stopped working.
- **The limit of applicability must be felt.** What the steps assume shows somewhere: in the wording of the steps, or in the doctrine. No dedicated section is required. Its absence everywhere is a defect: an agent that cannot tell where the steps stop applying applies them everywhere.

The split is also a proportion rule. A short file is a doctrine and a few lines of know-how; sections are added when the body has grown enough to need them.

## Rewriting a file

1. Gather what must always be true, at the top or with the part it governs, identifiable.
2. The rest is know-how: keep it after the doctrine, sectioned if useful.
3. Move reasons to the rationale and leave the pointer.
4. Keep a list of rationalizations only for temptations the current models produce unprompted. Any other temptation named is a pink elephant (φattractors).

```markdown
# <Skill>

## Doctrine

- "Make the change easy, then make the easy change."

## <Know-how section>

1. …

Rationale: φmake-the-change-easy
```

## Related

- The three layers and why they stay apart: φthree-layer-harness.
- What each harness element is for: φharness-elements.
- What happens after a failed run: φkaizen.
- Why a precise term does the work of a paragraph: φfield-terms.
