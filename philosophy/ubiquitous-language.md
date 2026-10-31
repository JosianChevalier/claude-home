---
tags: [ddd, domain-modeling, vocabulary, bounded-contexts, cognitive-load, clean-code]
---

# Ubiquitous language

**Thesis.** The language is the model in its default expression, and its substance is verbs: true sentences about who does what. Code is where those sentences are best kept, read as a domain expert would say them.

## The language is the model

A **ubiquitous language** (Evans) is the model in words. The model exists only as expressed (φmodel-expressions), and language is the expression used by default: whenever we speak of the domain, we speak it.

Every other expression reuses its terms: code, schema, contract, UI. The reuse runs both ways and the line is fluid; what holds is that a term stays the same term across all of them.

Ubiquitous means in every expression of one model. It does not mean one language across the whole codebase and organisation: that would be a single model, which nobody wants.

Its limit is the **bounded context** (Evans), a linguistic boundary: where the language stops applying.

## Verbs, not the glossary

A ubiquitous language is usually read as a glossary, a list of nouns. What matters is the sentences that are true, and in each the verb: who does what, and how. Those sentences are the business rules and the invariants.

Structure without movement is dead. A domain understood through its nouns alone gives the **anemic domain model** (Fowler). The domain is **process over substance** (Whitehead):

> A process cannot be understood by stopping it. Understanding must move with the flow of the process, must join it and flow with it.
> (Herbert, *Dune*, the First Law of Mentat)

**EventStorming** (Brandolini) relies on events as the language relies on verbs: events are the symptoms and signals of behaviour.

## Language carries process

Natural language is rich at process. Most diagrams show structure; the ones that show process are hard to read. A sequence diagram costs far more **extraneous load** (Sweller) than the same flow in plain English.

## The code reads as the sentence

Behaviour and rules are best represented in code. So the language stays close to the domain code, and the domain code keeps a **single level of abstraction** (Beck, Composed Method): each function reads as a plain English sentence of the language.

The aim: read the code as a sentence refined by a domain expert.

## Related

- The model as its expressions, the language one of them: φmodel-expressions.
- The type the engineer holds, the concepts the code holds: φmodel-phenomenology.
