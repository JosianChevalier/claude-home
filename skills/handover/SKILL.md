---
name: handover
description: Use when the user asks to create/write/generate a handover prompt for a new session. Do NOT use for reading incoming handovers, summaries, reports, or documentation requests.
---

# Handover

## Doctrine

- A handover is a map for the next agent, not a record of this session: only what changes the next action or prevents a likely mistake.
- The next agent runs on the same harness and repo. Do not re-specify project, CLAUDE.md, rules, or copied source content.
- Pointers over contents: plans, studies, specs, philosophy docs, commits, key file paths. Copying an artifact spends the next agent's context twice.
- Every token the next agent reads is budget spent. Optimise for context size.

## Procedure

Output the prompt directly in the chat, no file.

- It does not need to identify itself as a handover; word it so the next agent understands what to do from it.
- Cover, in order: goal, current state, decisions made (with rationale if non-obvious), immediate next steps, open questions.
- Make it self-sufficient through artifact pointers, not copied artifact contents.
