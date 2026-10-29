---
tags: [session-state, artifacts, planning, context-economics]
---

# Session state lives in documents

**Thesis.** A session is a process that can die at any moment. The state of the work lives in a work file and the conversation is its echo; the file itself dies with the work, once what outlives it has graduated to its home.

```
conversation ──▶ notebook ──▶ work file ──▶ commits · harness · documentation
 a turn           a session     the work      the project
 thinking         derived       remembering   graduated
```

## Agents are ephemeral processes

Treat an agent session like a backend process: it can crash, be killed, hit context rot, or simply end. Backend engineering solved this long ago: **crash-only design** and 12-factor **statelessness**. A process holds no irreplaceable state; everything durable lives in a backing store, so any instance can restart and pick up. The conversation window is the process memory; the repo is the backing store. Anything that exists only in the conversation is state we have already decided to lose.

Cloud-native systems prove it with a chaos monkey: instances are killed at random, in production, and the system must not notice. `/clear` is the monkey you run yourself. If clearing costs something, the state was not in the file.

## The conversation is for thinking; the repo is for remembering

(Pierrain, *A good harness makes /clear free*.) People don't clear sessions because resuming hurts: decisions, discarded alternatives, the real next step, all of it lives in the one place clearing destroys. The fix is structural, not disciplinary: the **work file is the single source of truth for the state of the work**, with the conversation as its echo. Then the session is disposable *by construction*, and clearing stops being a cost you avoid and becomes an option you exercise freely.

The quality check: *if this session dies right now, what is lost?* If the answer isn't "nothing", the state isn't fully externalized.

Plans and studies are not final or permanent by default. They are working artifacts: temporary state containers that survive the session while the task is alive. They can be skeletal, partial, and still useful; the point is that the next agent can resume from the current shared model instead of reconstructing it from chat.

## The session is anchored in a working document

Unless explicitly not required, a session gets anchored in a working document in the repository: an existing study or plan, or a work file, committed or not, depending on the nature of the work and above all on its longevity. Some sessions do not need one: three questions, each closed in its round, and the conversation carries them. Past a handful of open threads the conversation starts dropping some; a file the session comes back to as a checklist drops none. That is the moment to ask whether to anchor.

A work file is a backlog, distributed: the tasks of a project sit next to the work they concern, one file per piece of work, in place of a tracker.

Conversation, notebook, working document, repo: four stores ordered by inertia ([[philosophy/change-inertia]]). The conversation lasts a turn. The notebook, a `/tmp` file of the agent's own, lasts the session ([[philosophy/conversation-as-interface]]). The working document lasts the work. The repo keeps what graduated. What survives the conversation reaches the document; what survives the document is committed.

## Save at hand-back, not at stage end

Checkboxes don't capture everything. The state must be written explicitly **every time control returns to the user**: each such moment is a potential session boundary. What the state contains: decisions, findings, open threads, the real next step.

In a mob session the mic returns every turn, and the navigators hold the state too; a hand-back there is a mob decision about the plan (a split, a lift, a reorder, a stage done, a constraint discovered) or a turn that could end the session, not every move. The artifact is opened at checkpoints, not during the exchange ([[philosophy/collaborative-production]]).

The cost model is the point: an unpredictable, compounding resume cost is replaced by a tiny, systematic write cost, paid by the agent, not the user.

This write is a distillation step, not an append step. Keep the state, delete or replace stale detail as the model improves. Otherwise the artifact becomes another context debt instead of a session-survival mechanism.

## The work file is the handoff mechanism

The next session has **no memory of this one**; the work file is the only channel through which learning crosses the session boundary. Updating it is therefore not bookkeeping: it *is* the deliverable of a stage, alongside the commits. A session that drives perfectly but leaves the file stale has stranded its learning in a dying process.

## The work file dies with the work

The work file is the canonical home for one thing only, the work in progress ([[philosophy/context-economics]], one canonical home per fact), and it is deleted when the work is done. Everything discovered along the way that deserves to outlive it must graduate to its own home first:

- code and design → **commits**
- conventions, workflows, corrected agent behavior → **the harness** (rules, skills, philosophy)
- domain and system knowledge → **documentation**

Learning left in the file at deletion time is lost; learning kept in the file *instead of* its home is a copy waiting to diverge.

A finished work file left in the repo is a pink elephant ([[philosophy/attractors]]). A fresh context takes whatever it reads as a premise ([[philosophy/conversation-continuity]]); it cannot tell a closed thread from an open one, and the stale file becomes an anchor. Deleting is not losing: the history is git's job.

## Related

- [[philosophy/process-units]]: the process units; the session is the one where a human is required.
- [[philosophy/change-inertia]]: why the four stores are cut where they are.
- [[philosophy/conversation-as-interface]]: the notebook, the store below the work file.
- [[philosophy/conversation-continuity]]: what crosses a session boundary and what must not.
- [[philosophy/context-economics]]: one canonical home per fact.
- [[philosophy/attractors]]: the finished work file as a pink elephant.
