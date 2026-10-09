---
name: handover
description: Use when the user asks to create/write/generate a handover prompt for a new session. Do NOT use for reading incoming handovers, summaries, reports, or documentation requests.
---

# Handover

## Doctrine

- By default, conversations are trashable.
- Allow resuming the current activity in a fresh context without rewriting instructions or intent.
- State of work lives in the filesystem, to make `/clear` free.
- Keep the semantic landscape of the next agent simple and bias-free.

## The successor

Runs on the same harness and the same repo. CLAUDE.md, rules, skills and source are already in front of it; it has most of the context. The handover carries only the rest.

## The cases

- **Continuity**: the next part runs in another session. The successor takes over: intent, next step, decisions not in files, open questions, the anchor.
- **Branching**: one direction out of several; this conversation continues. Scope the direction, its boundary, and where the result is expected. Leave out your own leaning on it.
- **Async**: this session waits for the other's input. Write a request: what is needed back, in which form, where. The successor does not take over the work.

## What a handover contains

Only what carries information for the successor: a line goes in if it changes the next action or prevents a likely mistake, not because it happened.

- Intent: the goal and what it serves.
- The next step.
- Large decisions not carried in files, with the rationale when it is not obvious.
- After a failure: what was tried and what was observed. If the user has not said what went wrong, say the cause is not established.
- Open questions.
- Pointers to the artifacts that hold the state: the session's working document first, then plans, studies, specs, commits, key file paths.

## What it does not contain

- Biases, conclusions that have not been validated and supported. An invented diagnosis of your own failure is the worst of these.
- Elements that live in the filesystem: the pointer, never the content.
- The project, the harness, the rules: the successor already has them.
- A log of the session: what was done is in the commits and files, and a decision that does not change the next action is not information.
- The word handover, or any label calling itself one: the successor would load this skill and write one instead of acting. Word it so the next agent knows what to do.

## Form

Output directly in the chat, no file, as one blockquote: every line prefixed with `>`. The user does not read it; the bar on the left shows where it starts and ends, and what they write below the bar is theirs and overrides what is above. Every token the successor reads is budget spent.

Rationale: [[philosophy/conversation-continuity]], [[philosophy/session-state-in-documents]], [[philosophy/context-economics]]
