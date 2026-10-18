---
tags: [harness-design, vocabulary]
---

# Attractors

**Thesis.** What is in context pulls what comes next; the sharpest pull per token is a precise term.

Terms are context-sensitive constraints (Juarrero): they do not label, they constrain what follows. In the model's semantic landscape a precise term carves the semantic valley the trajectory falls into, cheaper and more reliable than any amount of glossing. The same holds for everything else in context: a copied file, a named option, a stale note. Each is a basin.

```
in context          basin carved
a precise term      the field's reflexes: heuristics, failure modes, taste
an aphorism         a whole discipline of judgment
a copy              nearer than the canonical it duplicates
a negation          the thing negated, kept alive
a name              a posture: what the whole flow falls into
```

## Load the expertise

Reach for the domain's own term, not the generic one: "bounded context" over "module" pulls in a DDD expert's reflexes, not just a definition. An aphorism works the same way: one names a whole discipline of judgment ("make it work, make it right, make it fast").

This is why doctrine is written as a few attractors ([[philosophy/harness-shape]]): each precise term is compressed context. A vague rule needs paragraphs of clarification; a well-named one needs a sentence. Philosophy is written in the field's own terms for the same reason.

## Finding an aphorism

A doctrine line is looked for before it is written. In order:

1. **The rationale's own terms.** A skill's doctrine quotes the attractors of the philosophy it points to (the horizon, the disappointment, the belt): the file and the skill then pull the same way.
2. **A known saying.** The idea is stated plainly, then the discipline that already has a line for it is searched: Freud's cigar for "trivial is an answer", "horses, not zebras" its rival. Several candidates side by side; the one wins whose basin is the meaning intended, not the nearest-sounding.
3. **Coined.** When nothing fits exactly. A coined line pulls only what it says, so it says the whole thing: short, concrete, a verb.

The pull is the author's, not the writer's: a name quoted for a meaning it does not carry pulls its own meaning anyway. A saying that fits only loosely is dropped and the line coined. Misused often enough, a saying's basin moves: the harness ends up teaching its own meaning of the name, and the name no longer loads the discipline it stood for.

## Pink elephants

Attractors are indifferent to negation. Naming a discarded thing, "don't use X", the rejected option, keeps its basin alive and raises the probability of falling into it. Do not mention it; drop it. When removing a behavior from the harness, delete its vocabulary rather than prohibit it.

The exception is a basin already in the weights. When the model goes to a behavior unprompted, the pull is there whether or not we name it; naming the violation does not carve a basin, it compensates one. A violation is named only when observed; a violation named unobserved is a pink elephant.

Then it is named by its own pejorative name, as the field names it: "primitive obsession", not "don't apply KISS to types, it causes issues". Both qualify the same behavior; the connotation is what pushes away from it. Sometimes the violation is shown as it will appear, a counter-example, for the same reason.

An artifact is a pink elephant the same way: a finished work file, a handover's list of what was not done, is read as a premise by a fresh context ([[philosophy/session-state-in-documents]]).

## Copies

A copy is a nearer attractor than the canonical it duplicates. Restating a rule or a file in the prompt adds weight to what the receiver already holds, and the copy, not the canonical, is now what pulls. A pointer keeps one version in the landscape.

## Reorient before compensating

Naming a violation fights the stream. Two cheaper moves come first, in order:

- **Rename.** A skill named for executing a plan pulled weaker models to finish the whole step without a word; renamed for mobbing from the plan, they stayed conversational. One word changed, no boundary added.
- **Reshape the flow.** A skill that writes an artifact fired on reading one. A boundary in its description would still leave the word in the landscape; the flow was changed instead, so the artifact never carries the trigger word, which is said at creation time only.

Sometimes the change is bigger than a word: a posture, the direction of the whole thing. Going against a stream is the signal to change direction, not to push harder. Compensation is the last resort, and it is called that.

## Skill descriptions

A description is pure attractor engineering: it is matched against the session's content at trigger time. Use the exact words the session will contain. A don't-invoke boundary is a compensation: the moves above come first, and when it stays it names the trigger the model mis-fires on, and only that one.

## Related

- Doctrine as a few attractors, rationalization lists as pink elephants: [[philosophy/harness-shape]].
- Everything shown is shown for metis; attractors govern how: [[philosophy/transmission-belt]].
- A finished work file as a pink elephant: [[philosophy/session-state-in-documents]].
- Skill descriptions and philosophy in the field's terms: [[philosophy/harness-elements]].
