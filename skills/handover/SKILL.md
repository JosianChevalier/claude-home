---
name: handover
description: Use when the user asks to create/write/generate a handover prompt for a new session. Do NOT use for reading incoming handovers, summaries, reports, or documentation requests.
---

# Handover

## Doctrine

- By default, conversations are trashable.
- Allow resuming the current activity in a fresh context without rewriting instructions or intent.
- State of work lives in the work file, to make `/clear` free. The handover carries what is not state: pointers, the next action, the posture.
- Keep the semantic landscape of the next agent simple and bias-free.

## The successor

Runs on the same harness and the same repo. CLAUDE.md, rules, skills and source are already in front of it; it has most of the context. The handover carries only the rest.

## The cases

- **Continuity**: the next part runs in another session. The successor takes over the activity.
- **Branching**: one direction out of several; this conversation continues. Scope the direction, its boundary, and where the result is expected. Leave out your own leaning on it.
- **Async**: this session waits for the other's input. Write a request: what is needed back, in which form, where. The successor does not take over the work.

## Building it

Start from nothing; each line has to earn its place.

0. Save first. What the conversation decided about the work, and the file does not hold yet: how it runs, what was decided, what is open. Distilled into the work file, then the quote is written against the file. What is in the file is never in the quote.
1. Orient: point to the resources that carry the state of this activity, the work file first, one line each on what the successor finds there.
2. Next step: state it only if the resources do not already show it.
3. Survival: what the successor needs and nothing anchors. Where it goes is a matter of nature.
   - A file: impactful, not consumed by the immediate next action, and sensitive to a restart. Invoking this skill is the request to write it.
   - A line: consumed by the immediate next action, or the posture of the next agent, which lives in session. After a failure, no story: name the dial and set it the other way. Too long becomes "verdict first, three lines"; too deep becomes "map, no detail"; the wrong idea in focus becomes "the question is X, not Y". A posture instruction, not a diagnosis.
   - Not a word: what was considered and not done, what is done and over, an approach among several still being tried, an unvalidated conclusion, above all a diagnosis of your own failure. Named, it becomes a pink elephant.

Then check: can the successor act, from the pointers and the lines? What this serves, what to do next, what was decided, what is open. A gap is a line.

## Form

In the chat, no file, shaped like this:

```
Handover: the review

> Resume the review from review.work.md. Verdict first, three lines, then wait.
> --- end of agent generated instruction
```

The label names the topic when there are several. The quote is a direct prompt to the successor, second person. The last line closes it: the user pastes the quote and writes below that line, and what is below overrides what is above. Every token the successor reads is budget spent.

Never the word handover inside the quote, nor any label calling itself one: the successor would load this skill and write one instead of acting.

Rationale: [[philosophy/conversation-continuity]], [[philosophy/session-state-in-documents]], [[philosophy/context-economics]]
