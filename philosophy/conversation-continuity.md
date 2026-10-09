---
tags: [handover, conversation-continuity, context-economics, attractors]
---

# Rationale: Conversation Continuity

Why a conversation can be left, resumed or branched at any point, and why the handover that does it carries intent and pointers, and nothing that would shape the receiving agent's judgment before it has looked.

A handover is the communication layer between sessions ([[philosophy/session-design]]). It points at the session's working document instead of carrying the state.

## The cases

The rules differ slightly by what the receiving agent is for. There may be more cases than these.

- **Continuity.** The next part of the work runs in another session; the author's context ends. The receiver takes over: intent, next step, decisions not yet in files, open questions, pointer to the anchor.
- **Branching.** The conversation should go in several directions at once; the author continues. The handover scopes one direction: the question, its boundary, and where the result is expected so the author can pick it up. The author's leaning on that direction is the bias to leave out.
- **Async.** The current session is waiting for the input of another one. The handover is a request: what is needed back, in which form, where. The receiver does not take over the work.

## The author has a stake in the story

Whatever the case, the author writes about its own work. After a failure it does not write "cause unknown"; it invents a cause, in the same register as its facts. Mid-work it leans toward its own direction. The author's model of the situation is the most suspect content a handover can carry, and the one the receiver can least check.

## The receiver cannot weigh what it is told

A fresh context takes its prompt as given. It cannot tell a validated conclusion from a hunch: both become premises. An unvalidated conclusion is not information, it is an anchor; the receiver reasons from it instead of toward it. Decisions the user made go in, with their rationale when it is not obvious. What was tried and what was observed go in. Why it failed stays out unless the user established it. Let the receiver look.

## The session log is not information

The author's most available material is its own session, so the default handover narrates it: every decision, every step done. Nearly none of it changes what the receiver does next; what was done is in the commits and the anchor, and a decision the receiver would make the same way or never faces is noise. Information is what changes the next action or prevents a likely mistake. Everything else spends the receiver's budget and crowds the landscape.

## Everything in the prompt is in the landscape

What is in context pulls ([[philosophy/attractors]]). Restating the project, the rules, or a copied file adds weight to things the receiver already holds in canonical form, and the copy, not the canonical, is now the nearest. A pointer keeps one version in the landscape ([[philosophy/context-economics]], one canonical home per fact).

## The receiver is a peer on the same harness

Same CLAUDE.md, rules, skills, repo. The handover is the delta: what the filesystem does not carry.

## The handover passes through a human, unread

It goes from one terminal to the next through the user's clipboard. The user should not need to read it: they must see where it starts and ends, and be able to write below it, since what they add is the steering of the moment and overrides what is above ([[philosophy/zoom-levels]], attention is the scarce budget). One visually delimited block follows.

## Words are triggers

The harness loads skills on words. A text that calls itself a handover makes the receiver load the handover skill and write one instead of acting. An artifact's name is a side effect in the receiver's harness; the handover says what to do, not what it is.
