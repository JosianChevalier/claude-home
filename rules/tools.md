# Tools

## `~/.claude/tools/replace-text`

Edits text by exact match, in place of an inline Python script. A whole file is rewritten with the Write tool. Every old text must match exactly once; if any edit fails, no file is written.

- One edit: `replace-text FILE 'old' 'new'`. `''` as new deletes.
- Several edits, in one or more files: one call, pairs on stdin in a heredoc, so they land all together or not at all, with no shell quoting:

  ```
  replace-text <<'EOF'
  @@@ path/a.md
  old text
  @@@
  new text
  @@@ path/b.md
  ...
  EOF
  ```

- A whole section: `replace-text FILE --between 'START' 'END' < new`, from START up to END, END kept.

It prints `FILE:LINE -REMOVED +ADDED` per edit: no `git diff` needed to check where it landed. `-h` for the details.
