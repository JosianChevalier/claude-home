---
name: ongoing-work
description: Tracking ongoing work, anchoring conversation work in a file, looking for next tasks.
---

# ongoing-work

## Doctrine

- The conversation is for thinking; the file is for remembering. What exists only in the conversation is state already decided to be lost, so a piece of work that outlives its turn is anchored in a work file: what must empty, the current step. Cloud-native with a chaos monkey: any instance can be killed at any moment, so no instance holds irreplaceable state. `/clear` is the monkey you run yourself; if it costs something, the state was not in the file.
- Saved at hand-back, distilled not appended. Every return of control to the user is a potential session boundary. The write keeps decisions, open threads, the real next step, and replaces stale detail.
- The sweep is the truth. One key marks a work file and nothing else ever matches, so "what's next" is one script, not a search.
- A work file is a backlog, not a changelog. A line says what is left, nothing else; what was done goes in the commit message.
- A finished work file is a pink elephant. A fresh context takes whatever it reads as a premise; stale work pollutes it. The file is deleted when the work ends. History is git's job.
- A new session, topic or file: the reader holds nothing of the work but what this conversation has said. The first message on it says what we are on, in plain words, before anything else.
- Only the text after the last tool call reaches the reader. What comes before is a progress note at most. Anything meant for the reader goes in the final message, whole, not as a recap; and the final message assumes nothing before it was read.

## Keys

A work file is named `<topic>.work.md`, next to the work it concerns. The suffix is for git, which cannot read frontmatter: one whitelist pattern covers them all. The key is for the sweep.

Frontmatter only, read only inside the opening `---` block. Never write them at line start outside one.

    ongoing_work_file: "<what must empty, and when it counts as empty>"
    rank: 3

Lowest rank first. Gaps are fine; renumber only when reordering.

## Scripts

- `scripts/list-work.sh [root]` — the sweep, sorted. Two lines per item: rank and path, then the sentence.
- `scripts/new-work.sh <topic.work.md> "<what must empty>" [rank]` — creates the work file with the keys and a title. Rank defaults to last.

## Asks

- **What's next:** the coming item, said as below.
- **Next, move on, and the like:** the coming item, said as below, then start.
- **Anchor this / new work file:** `new-work.sh`, next to the work it concerns; rank last unless told. Steps as checkboxes, a current-step marker, so a zero-context session resumes without the conversation.
- **Deprioritize, put it last, and the like:** rank 99. No renumbering.
- **Done:** delete the work file. No renumbering.
- **Reorder:** renumber, then show the sweep.

## Saying the coming item

From the current-step marker in the work file. A breadcrumb, one level per line, from the first level the reader lacks (the project if we are out of context) down to the item. Each level says what it is in a few plain words, not only its name: the reader has not read the work file. The item is session-sized: a vague or large one is broken down and its first piece is the item. Clear at a glance where we are; never prose.

    Migration of the old `.claude/` into this repo, file by file
    └ 3.2 philosophy backlog: old notes become `philosophy/` files after a review in conversation
      └ next: `aggregates`, the note on what must be saved together in a model; three issues open

## The test of the first message

- The first message on anything new is read by someone who holds nothing: no file, no previous session, no line of what I read before writing.
- If the user does not understand it on first reading, they hand it as is to another agent that cannot read any file. That agent must understand it immediately, with nothing but the message.
- If it does not, the user spends their time fixing the harness instead of doing the actual work, all the agent's work is killed, and the session is trashed. Write every first message so this never has to be run.

Rationale: [[philosophy/session-state-in-documents]], [[philosophy/conversation-continuity]], [[philosophy/context-economics]]
