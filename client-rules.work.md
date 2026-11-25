---
ongoing_work_file: "Each rule loaded where its reader needs it: Claude's main session, Claude's subagents, or OpenCode. Empty when the steps below are done."
rank: 9
---

# Client rules

```
 rule                              home                         reaches
 writing (Extended mind)     ✔     output-styles/extended-mind.md main sessions: Claude + forks, OpenCode primary agents
 delegation                  ✔     CLAUDE.md, one section       main + general/custom subagents (not Explore, Plan)
 subtraction + no decision logs    rules/                       main + general/custom subagents
 OpenCode                          AGENTS.md or prompts         OpenCode only
```

## Steps

- [ ] 3. A rule for writing documents, in `rules/`, written for both Claude and GPT: against additive bias and decision logs, reusing `rules/subtraction.md` and the kickstart-harness wording: not a secret diary, not a bureaucrat's record, not the trial; write the conclusion. Also the cognitive walkthrough from the reader's place, an obstacle costing more than it carries, patchwriting (Howard) undone through the notebook. Repeating the main session's prompts is fine.
- [ ] 4. Drawing. Part 3 of `extended-mind.md`: the user trims it and adds a list of shapes. For GPT only, `prompts/back-of-the-napkin.md` holds Roam's doctrine written out (the 6×6, SQVID's change-or-current-state, look/see/imagine/show), with `~/Projects/kickstart-harness/prompts/draw.md` as a source, and both OpenCode primary agents load it by `{file:}`. Claude keeps `extended-mind.md` alone.

## Decided

- Rules differ per client: the models answer differently. Prompts may be shared where they fit both.
- Caching does not decide placement: system prompt, CLAUDE.md and rules all sit in the cached prefix, shared across sessions in the same folder within the TTL (docs: code.claude.com/docs/en/prompt-caching).
- Restarting to load an edited rule costs nothing.

## Parked

- The git status snapshot at startup differs between sessions and cuts the cross-session cache. Ideally it comes after CLAUDE.md and rules.
