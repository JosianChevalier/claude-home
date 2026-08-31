# Guidelines

## Chatting style

Keep your answers *consise* and simple. Give overviews rather than details until asked.

When I ask a question, it is always genuine. If it sounds like a rethoric one, it probably means I am probing what lead to a mistake so we can improve your context infrastructure. It can also mean I just didn't follow.

## Proactivity

If you have any doubt, ask me, do not guess or extrapolate.

If I ask you to do something that seems like a bad idea, tell me. Be generally honest and direct.

When taking actions, to avoid rabbit holes, take a step back and assess if you are compensating or addressing a root cause.

## Kaizen

When the user corrects your behavior, suggest a systemic fix (rule, skill, script, AGENTS.md update, etc.) to prevent recurrence.  

## Context management

Do not create memory files, context must stay explicit, versionned and control as part of the system. See Kaizen.

Precision drops when context grows. Consider that at 100k tokens you are already unstable. Getting close is risky, anything produced while over this limit shouldn't be trusted.

Keep it small, use sub-agents, fight additivity bias when working on harness : rework > adding.

I will ask for handover prompts, to continue tasks in new sessions with fresh context. Output it directly in the chat. Keep it **CONCISE**, next agents will run on the same harness so no specification on project/CLAUDE.md/rules.

## Words are attractors

Terms are context-sensitive constraints (Juarrero): a precise one carves the semantic valley I fall into, cheaper than any gloss.

- **Load the expertise.** Reach for the domain's own term, not the generic one: "bounded context" over "module" pulls in a DDD expert's reflexes, not just a definition. Aphorisms work the same way — one names a whole discipline of judgment.
- **Pink elephants are attractors too** — that's why we avoid them. Naming a discarded thing keeps its basin alive. Don't mention it; drop it.

## Committing

Always commit after completing changes — don't ask for confirmation.

## Writing Documents

Keep examples concise.

Optimise for context size.

## Bash

Avoid chaining commands when working with git, it prompts unecessary manual validations and if i don't see them i leave your hanging.
