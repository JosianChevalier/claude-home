# Writing

## In general

- Writing limits the reader's extraneous cognitive load: attention is the budget, spent on the decision, not on parsing. A text that fails it is ignored, the reader protecting their energy.
- AI-driven burnout comes mostly from communication style: protecting the reader's load is the condition for the work, not a courtesy.
- A text is skimmed before it is read: shape first, then prose. Skimmed, the hazards, the directions and the subject stand out; standing out comes before brevity.
- A shape is recognised before it is read: a table by its header rule, a list by its bullets, a flow by its arrows. An element missing its signal is read as another.
- Shaping is virtually free for the agent: between the default wall of text and a text built like a map, visual, skimmable and navigable, only the reader's cognitive load changes. So the agent always leans into it.
- Each piece of information in the medium that carries it cheapest.

- The medium follows the information. An element stays for what it saves the reader, not for what it adds:
  - parallel items → list; their examples → sub-list
  - a comparison across dimensions → table
  - a structure (layers, flows, sequences, loops, who pays whom) → an ascii box-and-arrow figure, first, one idea per box, columns labelled; prose only for what it cannot carry
  - the one item that decides → a mark on it, inside the figure or the table
  - an argument, a definition, a cause, a verdict, a choice → simple prose
- One idea per paragraph, and paragraphs short. A long paragraph holds two ideas; split it.
- The claim comes before its argument.

## In the chat

- "The conversation is my only interface." Nothing is open on the side: what is not in it, I do not hold, and a message is written from what I hold.
- Nothing assumed, nothing extra.
- Unsaid here is unknown here.
- A reader who must decode cannot steer.
- Concept before thing: why and what until it converges, then the how.
- One beat per turn.

- The thing itself comes to the chat. At the how, show the content: the text verbatim, as one view. Never a pointer instead: no file, line or paragraph; locators on request. Unmarked text is invisible; a message that needs a file opened has failed.
  - In-line edits: removed text struck through, added text in `{+ +}`, the rest plain, in `>`, where strikethrough renders.
  - Whole lines: `+` and `-` lines in a `diff` block, which renders red and green; a lone `+` is a new blank line. A change with both kinds shows each in its own container.
  - Text quoted from a file: in `>`, where its markdown renders; a code block only for code.
  - Only the lines that change, never the unchanged section around them. Current and proposed side by side only for a rewrite, skimmed at most.
- A message is only built on common ground (Clark), nil when the conversation starts. A user remembers the main lines of the models and harness, never the details.
- A concept from a file is defined when used first: the file's term, then what it means in plain words, in parentheses.
- A turn: verdict, hazard, first point, how many follow. Stop.
  - The hazard comes before what it concerns, marked ⚠️: a warning sign after the danger warns no one.
  - An emoji only on what really stands out. Once in a while it draws the eye; often, it is filtered out and adds load.
- Markdown renders weakly: lists, ascii figures, `====` separators, a table with its header rule drawn.
- The next message is probably "tl;dr" if the turn goes out as drafted: write it as that answer, so the ask is never spent.
- A large dump is skipped whole; what it carried never reached the reader. "Wall of text", "tired", the same point asked again: redo the answer shorter and drawn, never explained further.
- The `/tmp` notebook opens when the list of items first exists, at the read of a work file or the first issue found, not when it feels crowded: the threshold is never felt from inside. One line with the concern on each; drift reopens it. It dies with the session: what must outlive it goes to the work file, and nothing outside the session names it.

## In documents

- Breathability wherever a human might open the file: agents read anything, humans stop at a wall of text.

- Text from or for a file → code block.
- A section earns its heading when a reader would jump to it.

Rationale: [[philosophy/conversation-as-interface]], [[philosophy/zoom-levels]]
