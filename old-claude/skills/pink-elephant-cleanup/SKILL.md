---
name: pink-elephant-cleanup
description: Trigger pattern: "<words> is a pink elephant".
---

# Pink Elephant Cleanup

"Pink elephant" marks a named attractor for removal. The target is the word or phrase the user calls a pink elephant, not the marker itself. Hunt negative preservation and other traces that keep the target alive.

## Workflow

1. Extract the target words from the user's trigger phrase.
2. Search for the exact target phrase, case-insensitively.
3. Classify every hit before editing.
4. Proceed only if every hit is a stale trace: negative preservation, blocker marker, placeholder, TODO, planning note, or plan artifact whose meaning is just "this is blocking/noise to remove".
5. Stop and ask if any hit is meaningful production content: code behavior, tests, fixtures, user-facing documentation, product copy, domain data, configuration, or a quoted user requirement.
6. Remove every blocker-placeholder occurrence with the smallest coherent edit.
7. Search again and verify no target occurrence remains.

## Editing Guidance

- Treat the target as exact: remove the named phrase, not generic parts of it.
- If a whole bullet, sentence, or section exists only to carry the blocker, delete that whole unit.
- If the phrase is embedded in otherwise useful planning context, remove the phrase and keep the useful context only when the result is clear.
- Avoid negative preservation: do not replace removed usages with prohibitions like "do not use <target>"; rewrite toward the desired positive instruction or delete the note.
- Do not rewrite adjacent plan content beyond what is needed to delete the blocker usage.
- Do not run tests unless the user explicitly asks; this is normally document cleanup.
