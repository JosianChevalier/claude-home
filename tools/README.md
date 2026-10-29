# tools

Scripts agents call instead of rewriting the same code each session. `docs/` tells agents they exist: one doc for what both platforms have, one per platform for its home and its own tools. Each platform loads its pair through its native instruction channel, so no doc names the other platform and `CLAUDE.md` / `AGENTS.md` stay untouched.

```
docs/shared.md     ─┬─▶  OpenCode     opencode.json, `instructions`
docs/opencode.md   ─┘

docs/shared.md     ─┬─▶  Claude Code  settings.json, SessionStart hook: `cat` of both,
docs/claude.md     ─┘                 re-run after /clear, resume and compaction
```

| Tool | Platform | Does |
|---|---|---|
| `replace-text` | both | exact-text edits: one pair, a section between two anchors, or a batch across files |
| `grab-notebook` | Claude | this session's notebook path, the file created on the first call |

A tool that compensates a habit of the current models carries a comment at its top:

```
# model-coupled: <model ids>. <what to check at a model change>
```

At a model change, `grep -r model-coupled tools/` lists what to recheck: keep, adjust or delete the tool and its lines in `docs/`.
