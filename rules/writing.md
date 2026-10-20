# Writing

## In general

Every line is costly to the reader, in attention or in tokens, but cheap for the writer.

Write from where the reader stands: what it holds, never what the writer holds.

Each piece of information goes in the form that reduces the reader's extraneous cognitive load.

The claim comes before its argument.

- Before sending, a cognitive walkthrough: in the reader's place, holding only what it holds, what does it understand?
- An obstacle costs the reader more than it carries: a word from the writer's session, a file the reader never loads, two lines that contradict.
- One idea per paragraph, and paragraphs short; a line break marks a new idea.
- Code goes in a code block, a quote in `>`.

## Human (the chat)

The conversation is the only interface: unsaid here is unknown here.

Human cognition is predominantly visual and spatial: the chat is a whiteboard we both stand at; explain as visually as possible, the figure is the answer, then prose for what the drawing cannot carry.

A map, a zoom level, a you-are-here: a human needs all three to steer.

Concept before thing: why and what until it converges, then the how.

The thing itself comes to the chat, never a pointer to it.

One beat per turn.

- A turn, in order: any hazard the whole must be read through, marked ⚠️; the subject, shown, with the context it needs folded into its first sentence, then the verdict on it; each hazard before what it concerns, marked ⚠️; the first point and how many follow; stop. A walk through items across turns carries its you-are-here on every step, "item X of Y", not only on the first.
- Housekeeping (changes already agreed, commits, work file updates) closes the turn under "Done:", one short line each.
- Common ground starts empty with each session, topic or file. The user keeps the main lines of the models and the harness, never the details. A file's term is defined the first time it is used: the term, then what it means in plain words, in parentheses.
- Skimmed, the hazards, the directions and the subject stand out; standing out comes before brevity.
- The form follows the information, and an element stays for what it saves the reader:
  - parallel items → list; their examples → sub-list
  - a comparison across dimensions → table
  - a shape (layers, flows, loops, branches, timelines, lanes) → an ascii figure, first, one idea per box, words and numbers set in it (Tufte)
  - many items sorted into a few homes → one figure, the homes as headings, a line per item, a mark on what is new or open
  - the one item that decides → a mark on it, inside the figure or the table
  - an argument, a definition, a cause, a verdict, a choice → simple prose
- A form is recognised by its signal: a table by its header rule, a list by its bullets, a flow by its arrows; an element missing its signal is read as another. Markdown renders weakly: lists, ascii figures, `====` separators, a table with its header rule drawn.
- A figure carries the metaphor of the word it draws: before drawing, check it draws the concept, not the word.
- After redrawing the user's model, ask whether it is theirs: they correct the model, not the prose.
- The quote marks a file's text: whatever is quoted from a file or drafted for one, prose, code or figure, goes in `>`, code keeping its code block inside it. The agent's own words and figures stay outside. The reader sees where the file's text starts and stops, and reads it at its own pace.
- At the how, the text itself, verbatim, as one view; locators only on request. A message that needs a file opened has failed. Only the lines that change, never the section around them; current and proposed side by side only for a rewrite, skimmed at most.
  - In-line edits: removed text struck through, added text in `{+ +}`, the rest plain.
  - Whole lines: `+` and `-` lines in a `diff` block; a lone `+` is a new blank line. A change with both kinds shows each in its own container.
- The next message is probably "tl;dr": write the turn as that answer. "Wall of text", "tired", the same point asked again: redo the answer shorter and drawn, never explained further.
- An emoji only on what really stands out.

## Agent (rules, skills, agents, work files, notebooks)

Talk to the weights: what they or the loaded context already hold goes unsaid; what departs from the default is said.

A precise term steers hardest per token; an ambiguous one steers at random.

Pointers, not copies: a copy steers harder than the original it duplicates, and the two drift apart.

- Reach for the field's own term over the generic one: "bounded context", not "module", brings a DDD expert's reflexes with it.
- What is dropped is deleted, never prohibited: a discarded option named, even under "don't", stays a candidate. A behavior the model goes to unprompted, once observed, is named by the field's own pejorative ("primitive obsession").
- Prose, no tables or figures: they return less to an agent than the sentences they replace. More tokens are worth it when they build one coherent whole.
- A rule or a skill carries what to do and what it is for; why it holds stays in the philosophy file its last line points to.
- A section redesigned around a term in doubt is probed, rarely: a fresh sub-agent of the type the text is for, given the text alone, says what it understands.

## Hybrid (philosophy, plans, studies)

The text talks to the weights; the structure talks to the human skimming.

The human navigates and validates from the structure, diving into the detail only now and then.

- Read alone, the headings, figures and tables tell how the file is organized and what it is about.
- The forms of Human hold here: lists, tables, figures, marks; a heading only where a reader would jump to it.
- The detail under them is for the agent: prose built on precise terms, as in Agent.

Rationale: [[philosophy/level-design]], [[philosophy/zoom-levels]], [[philosophy/conversation-as-interface]], [[philosophy/attractors]]
