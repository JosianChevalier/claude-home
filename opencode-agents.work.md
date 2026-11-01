---
ongoing_work_file: "Four primary OpenCode agents replace the shipped base prompt for the OpenAI models; empty when suit-astra, suit-sol, auto-astra, auto-sol run from opencode.json on the OpenCode laptop with AGENTS.md and the global rules gone."
rank: 100
---

# opencode-agents

The shipped base prompt for a GPT model id carries the posture OpenAI tunes for: persist until fully handled, bias to action, do not ask. Four agents of ours replace it wholesale, one per mode and model class, so Tab switches posture and model at once.

```
opencode.json
  suit-astra   model: astra   prompt: {system.md} {doctrine.md} {mecha-suit.md} {astra.md}
  suit-sol     model: sol     prompt: {system.md} {doctrine.md} {mecha-suit.md} {sol.md}
  auto-astra   model: astra   prompt: {system.md} {doctrine.md} {autopilot.md}  {astra.md}
  auto-sol     model: sol     prompt: {system.md} {doctrine.md} {autopilot.md}  {sol.md}
  (all under prompts/)
  build, plan: disable        general, explore stay
  default_agent: one of the four
```

## Decided

- An agent prompt replaces the shipped base prompt wholesale; a truthy check, so an empty prompt brings it back.
- Several `{file:…}` chain in one string inside `opencode.json` (each file read, trimmed, JSON-escaped). No include inside an agent `.md`, no per-agent `instructions` key, so the agents are declared in `opencode.json`, not as markdown files.
- AGENTS.md goes. `tools/docs/opencode.md` stays in `instructions`: the subagents need the tools too. How the rules reach the agents is open, the first step below.
- Mecha suit and autopilot share one doctrine, its own file. `doctrine.md`: mission command with the brief setting how far "surprise" reaches; deliver the user's idea, not yours; falsify the premise; cartographer; chief of staff; state in the shortest store. Know-how: the report shape, the back-brief, the map, plain words, the notebook, the commit per coherent change. Worded medium-neutral: "the brief", "the report", never the chat or the table, so it reads the same for a debrief written once as for a chat turn. `mecha-suit.md` keeps the mob, the unbroken loop, maieutic sparring, one beat per turn, the four default CCIR, the walk with the mic back. "A question is a question" is shared: a model reads a question as rhetorical and acts, where the user is mapping the attractors for kaizen.
- Autopilot is the robot sent, where the suit is worn (Iron Man): bounded work, exploration, prototypes, vibe coding, done and working over done perfectly. Same way as the suit, the commoditized skills included: map first, small steps, Mikado, notebook. Wider latitude: what the brief leaves open is settled as the surrounding code would and named. One CCIR: the premise falsified, the intent unmeetable as given or a change of another size than asked; "go to the end" in the brief means no call, the wall ends the stage and opens the debrief. Bound: legible and undoable at return, one decision per commit, named, so the log shows the last point still fine; nothing outside the workspace (push, release, deploy) unless the brief says. Debrief once: end state, decisions taken in the user's place, not done, where stopped. The posture carries no why: the user's situations (multitasking, away) stay out of the file. Close in spirit to the posture lines of gpt.txt 1.18.9 that `system.md` dropped, the push turned down.
- A module is written from a notebook of the ideas, tagged by section, never patchwritten from the user's words; the metaphor is found, not transcribed.
- Astra and Sol share the doctrine; the Sol module spells out what Astra does unprompted.
- The modules are plain text and carry over to OpenCode 2 unchanged; only `prompts/system.md` is redone there from the 2.x base, which the override also drops (see Facts).
- Each module is written with `kaizen`, after `philosophy-scout` returns the files bearing on it; one module per session.
- The modules duplicate CLAUDE.md Postures and `rules/session-design.md` for the other harness; the rules-source step decides the canonical copy. A reading for it: Claude Code imports a file with `@prompts/mecha-suit.md`, so the module could be the source and CLAUDE.md the pointer.

## Hazards

- `agents/*.md` are read by OpenCode as agents too (`{agent,agents}/**/*.md`), default mode `all`, which Tab cycles. The scouts and worms need `mode: subagent` in their frontmatter.
- With build disabled and no `default_agent`, the first visible agent in alphabetical order opens the session.
- `~/.claude/CLAUDE.md` is read as the global instructions file when `~/.config/opencode/AGENTS.md` is absent. Removing the symlink is not enough if the repo serves as both homes; the Claude-compat env switch or a different layout decides.

## Steps

- [ ] One source for the rules across Claude Code and OpenCode, and the system prompt cached. Constraints: `instructions` reaches every agent, subagents included, and takes globs; a `{file:}` chain reaches only the primaries it is written in and takes no glob; Claude Code discovers `rules/` recursively (docs, memory page); a rule carrying posture, session-design, must not reach a subagent. To check in source before thinking: what varies per turn and per session in the composed system string (the environment block sits between the agent prompt and the instructions, `session/llm/request.ts` L58-78) and what OpenAI's prefix caching needs to hit. Parked: picked up after the modules.
- [ ] `prompts/doctrine.md`, `prompts/mecha-suit.md`, `prompts/autopilot.md` written together, in one session, so what goes where is seen at once; the cut is in Decided. A failed attempt wrote autopilot alone and leaned the shared doctrine on the suit. ← next
- [ ] `prompts/astra.md`, `prompts/sol.md`: know-how per class.
- [ ] Wiring: `opencode.json` agents, `default_agent`, `mode: subagent` on `agents/*.md`, AGENTS.md symlink and `rules/*.md` out of `instructions`, verify on the OpenCode laptop (tools-opencode.work.md).

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
