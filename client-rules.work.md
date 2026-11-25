---
ongoing_work_file: "Each rule loaded where its reader needs it: Claude's main session, Claude's subagents, or OpenCode. Empty when the steps below are done."
rank: 9
---

# Client rules

```
 rule                              home                         reaches
 writing (Extended mind)     ✔     output-styles/extended-mind.md main sessions: Claude + forks, OpenCode primary agents
 delegation                  ✔     CLAUDE.md, one section       main + general/custom subagents (not Explore, Plan)
 documents, compensation     ✔     rules/                       main + general/custom subagents
 OpenCode                          AGENTS.md or prompts         OpenCode only
```

## Steps

- [ ] 4. Drawing. Part 3 of `extended-mind.md`: the user trims it and adds a list of shapes. For GPT only, `prompts/back-of-the-napkin.md` holds Roam's doctrine written out (the 6×6, look/see/imagine/show), with `~/Projects/kickstart-harness/prompts/draw.md` as a source, and both OpenCode primary agents load it by `{file:}`. Claude keeps `extended-mind.md` alone.

## Decided

- Rules differ per client: the models answer differently. Prompts may be shared where they fit both.
- Caching does not decide placement: system prompt, CLAUDE.md and rules all sit in the cached prefix, shared across sessions in the same folder within the TTL (docs: code.claude.com/docs/en/prompt-caching).
- Restarting to load an edited rule costs nothing.

## Parked

- Claude's subagents have no answer-shape rule: Cartographer lives only in Extended mind, which reaches the main session and forks. Step 3's rule could carry the report's shape, if their reports sprawl.
- The git status snapshot at startup differs between sessions and cuts the cross-session cache. Ideally it comes after CLAUDE.md and rules.
