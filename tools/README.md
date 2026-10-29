# tools

Scripts agents call instead of rewriting the same code each session. `docs/` is what tells agents they exist: one list per platform, loaded through that platform's own instruction channel, so `CLAUDE.md` / `AGENTS.md` stay untouched.

```
docs/claude.md     ─▶  Claude Code   settings.json, SessionStart hook `cat`,
                                     re-run after /clear, resume and compaction
docs/opencode.md   ─▶  OpenCode      opencode.json, `instructions`
```

The list is rooted at the home, a tool per item, its forms under it. A project with its own tools writes the same list rooted at the project.

A tool that compensates a habit of the current models carries a comment at its top:

```
# model-coupled: <model ids>. <what to check at a model change>
```

At a model change, `grep -r model-coupled tools/` lists what to recheck: keep, adjust or delete the tool and its lines in `docs/`.
