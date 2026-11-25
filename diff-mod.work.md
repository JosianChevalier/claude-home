---
ongoing_work_file: "A plugin that redraws a change shown in the chat as a rich git diff, red and green, the changed words stronger inside the line; one for Claude Code, one for opencode. Empty when both are adopted and the writing rule's three diff lines are one."
rank: 106
---

# diff-mod

A change shown in the chat should read like a rich git diff: red and green, the changed words stronger inside the line. Strikethrough beats CriticMarkup and git word-diff visually; plain `+`/`-` colouring is refused. The road is a plugin that redraws the output.

The Claude Code spike is `/tmp/claude/diff-mod-spike/`, `hooks/register.tsx` being the whole mod. It is in a temporary folder: a restart loses it. It works on a sub-agent's report, colour codes read, no screen seen:

- The hook `ui.render` on `AssistantMessage` gets the reply's raw Markdown.
- The mod returns its own tree; the text around the diff goes through `<Markdown>`.
- Nested `Text` gives two backgrounds on one line.
- The colours are the theme's `diffAdded`, `diffRemoved`, `diffAddedWord`, `diffRemovedWord`.
- Word highlights only on a `-` line directly followed by a `+` line.

To try it: `claude --plugin-dir /tmp/claude/diff-mod-spike` from a trusted folder.

- [ ] Look at the spike on a real screen: the look, the background width (text only), a reply still streaming, wrapped lines, several blocks, the alignment of a last one-line change. ← next
- [ ] The opencode plugin.
- [ ] Once adopted, the three diff lines of the chat section of `output-styles/writing.md` become one: a change is shown in a `diff` block, the old line directly above the new one.
- [ ] To weigh: colouring headings only, through the same kind of mod.
