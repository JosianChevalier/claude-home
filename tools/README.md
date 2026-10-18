# tools

Scripts agents call instead of rewriting the same code each session. The rule where each is needed tells agents it exists.

| Tool | Does |
|---|---|
| `replace-text` | exact-text edits: one pair, a section between two anchors, or a batch across files |

A tool that compensates a habit of the current models carries a comment at its top:

```
# model-coupled: <model ids>. <what to check at a model change>
```

At a model change, `grep -r model-coupled tools/` lists what to recheck: keep, adjust or delete the tool and its line in `rules/tools.md`.
