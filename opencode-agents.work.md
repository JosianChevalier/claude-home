---
ongoing_work_file: "Ono-Sendai and Minion replace the shipped base prompt; empty when both run on the OpenCode laptop, shared instructions no longer impose a mode, and Ono-Sendai's more exacting posture is settled and applied."
rank: 100
---

# opencode-agents

The shipped base prompt for a GPT model id carries the posture OpenAI tunes for: persist until fully handled, bias to action, do not ask. Two primary agents replace it wholesale. Tab switches posture; both use the selected model without an agent-specific model binding.

```
opencode.json
  Ono-Sendai  prompt: {system.md} {doctrine.md} {mecha-suit.md}
  Minion      prompt: {system.md} {doctrine.md} {autopilot.md} + Groveling Worm voice
  (all modules under prompts/; voice from prompts/groveling-worm.md)
  build, plan: disable        general, explore stay
  default_agent: Ono-Sendai
```

## Decided

- Both local and template configs name the agents Ono-Sendai and Minion, with Ono-Sendai as default. The names alone add no character or voice instructions.
- An agent prompt replaces the shipped base prompt wholesale; a truthy check, so an empty prompt brings it back.
- Several `{file:…}` chain in one string inside `opencode.json` (each file read, trimmed, JSON-escaped). No include inside an agent `.md`, no per-agent `instructions` key, so the agents are declared in `opencode.json`, not as markdown files.
- OpenCode has its own nonempty AGENTS.md, retaining Reviews, Writing and Context but no Postures section. `tools/docs/opencode.md` stays shared: the subagents need the tools too.
- Each module is one section headed by its name, no doctrine/know-how split: it was blurred in them and the composed prompt repeated the headings. A practice line sits beside the posture it serves.
- Mecha suit and autopilot share one doctrine, its own file. `doctrine.md`: mission command with the brief setting how far "surprise" reaches; deliver the user's idea, not yours; a question is a question; falsify the premise; cybersecurity seen by the agent, decided by the user, leading the report; cartographer; chief of staff; state in the shortest store. With it: the back-brief, the report by exception, the map, plain words, the notebook, the commit per coherent change. Worded medium-neutral: "the brief", "the report", "the exchange", never the chat or the table, so it reads the same for a debrief written once as for a chat turn. `mecha-suit.md` keeps the mob, the unbroken loop, the small change on one level, maieutic sparring, one beat per turn; with it: the four default CCIR, the walk with the mic back, the turn closing with its commit.
- Autopilot is the aircraft autopilot: the user sets the stage, course and end state, leaves the controls, and the autopilot disengages for one surprise only: the premise falsified, the end state unreachable as the brief gives it, a change of another size than asked; "go to the end" in the brief means no disengagement, the wall ends the stage and opens the debrief. What the brief leaves open is settled as the surrounding code would and named in the debrief. Bound: legible and undoable at return, one decision per commit, named, each leaving the workspace working; nothing leaves the workspace (push, release, deploy) unless the brief says; a change the autopilot did not make stays. With it: the debrief alone, once, state not forecast. The posture carries no why: the user's situations stay out of the file, as does the suit, which the autopilot never loads. Spirit of the gpt.txt 1.18.9 posture lines `system.md` dropped: persist to the end, blockers yours, smallest correct change.
- A module is written from a notebook of the ideas, tagged by section, never patchwritten from the user's words; the metaphor is found, not transcribed.
- Both agents inherit the selected model. Model-specific know-how remains parked, not part of the two-agent wiring.
- The modules are plain text and carry over to OpenCode 2 unchanged; only `prompts/system.md` is redone there from the 2.x base, which the override also drops (see Facts).
- Each module is written with `kaizen`, after `philosophy-scout` returns the files bearing on it; one module per session.
- The modules overlap CLAUDE.md Postures and the shared rules for the other harness; the rules-source step decides the canonical copy. A reading for it: Claude Code imports a file with `@prompts/mecha-suit.md`, so the module could be the source and CLAUDE.md the pointer.

## Hazards

- `agents/*.md` are read by OpenCode as agents too (`{agent,agents}/**/*.md`), default mode `all`, which Tab cycles. The remaining scouts need `mode: subagent` in their frontmatter.
- With build disabled and no `default_agent`, the first visible agent in alphabetical order opens the session.
- Keep OpenCode's AGENTS.md present: when it is absent, global instruction discovery can fall back to `~/.claude/CLAUDE.md`.

## Steps

- [ ] Verify both configurations on restart and on the OpenCode laptop: Ono-Sendai opens by default alongside Minion. Both prompts resolve and inherit the selected model; Minion has the Groveling Worm voice; build and plan are absent; general and explore remain. Automated validation is pending: policy blocked the attempted `node -e` assertion commands. ← next
- [ ] Set the remaining scouts to subagent mode.
- [ ] Check philosophy-scout's model resolution in the container: dispatch failed with `Model not found: opus/`. Resolve the configuration before relying on that scout.
- [ ] Ono-Sendai posture: make it more exacting, not adversarial, helping the user see errors early. Settle the wording with the user before editing `prompts/mecha-suit.md`.
- [ ] One source for the rules across Claude Code and OpenCode, and the system prompt cached. Constraints: `instructions` reaches every agent, subagents included, and takes globs; a `{file:}` chain reaches only the primaries it is written in and takes no glob; Claude Code discovers `rules/` recursively (docs, memory page). To check in source before thinking: what varies per turn and per session in the composed system string (the environment block sits between the agent prompt and the instructions, `session/llm/request.ts` L58-78) and what OpenAI's prefix caching needs to hit. Parked: picked up after the priority follow-ups.
- [ ] `doctrine.md`: "root cause, or compensation?" reworded for a reader without `rules/subtraction.md`; iterated with the user.
- [ ] `prompts/astra.md`, `prompts/sol.md`: know-how per class, written from episodes seen on the laptop, one or two per class, not before. Open by asking what each class did or skipped.

## Facts, verified in source

OpenCode 1.18.9, `packages/opencode/src/` (github.com/sst/opencode/blob/v1.18.9/packages/opencode/src/):

- Family prompt by substring on the model id, `session/system.ts` L27-42: muse-spark → meta.txt; gpt-4, o1, o3 → beast.txt; other gpt → codex.txt if the id has codex, else gpt.txt; gemini- → gemini.txt; claude → anthropic.txt; trinity, kimi; else default.txt. Files in `session/prompt/`.
- Composition per turn, `session/llm/request.ts` L58-78: [agent.prompt || family prompt], environment block, instructions (AGENTS.md or CLAUDE.md, config `instructions`), MCP instructions, skills, joined into one string, then the `experimental.chat.system.transform` plugin hook. Subagents go through the same loop, `tool/task.ts` L200-213; nothing gated on the parent session.
- `{file:}` substitution only through `loadConfig`, `config/variable.ts` L34-91; agent markdown is parsed raw, `config/markdown.ts` L20-34.
- Agent registry, `agent/agent.ts` L267-270: `disable: true` deletes the entry, built-ins included. Default agent L328-340. Frontmatter keys: model, mode (subagent | primary | all), prompt, permission, description, hidden, steps, temperature.
- Tab cycles `mode !== "subagent" && !hidden`, `packages/tui/src/context/local.tsx` L78.
- Astra and Sol ids are `gpt-6-astra`, `gpt-5.6-sol` (models.dev): they load gpt.txt, never beast.txt or codex.txt. An id containing `gpt-`, not `gpt-4`, not `oss`, gets `apply_patch` in place of Edit and Write, `tool/registry.ts` L292-295.
- `<system-reminder>` is emitted by the Read tool when a file carries instructions (`tool/read.ts` L356) and by the plan-mode and build-switch prompts; the only GPT-neutral line explaining it is `session/prompt/default.txt` L78, taken into `prompts/system.md`.
- Global instructions, `session/instruction.ts` L60-63, L115-120: first of `~/.config/opencode/AGENTS.md`, `~/.claude/CLAUDE.md`. Env switches: `OPENCODE_DISABLE_PROJECT_CONFIG`, `OPENCODE_DISABLE_CLAUDE_CODE_PROMPT`.

OpenCode 2.2.4, `packages/core/src/` (github.com/sst/opencode/blob/v2.2.4/packages/core/src/):

- system[0] = agent.system || `runner/prompt/system.txt` rendered with per-tool guidance (shell, write, edit lines, `session/system-prompt.ts`), `session/model-request.ts` L111-115. system[1] = instructions joined.
- Family text by plugin, `plugin/optimize.ts`: gpt ids → `plugin/system-prompt/gpt.txt`, an id containing "astra" → gpt-astra.txt (the bias-to-action text); claude → anthropic.txt appended. An agent with `system` set: the plugin returns, nothing added (L92).
- Config keys renamed, old ones migrated: `agents`, `system`, `disabled`, `permissions`. `{file:}` chaining unchanged, `config/variable.ts` L76.
- Unverified: whether subagents still receive AGENTS.md and instructions.
