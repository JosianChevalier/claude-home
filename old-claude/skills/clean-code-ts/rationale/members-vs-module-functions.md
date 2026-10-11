---
tags: [typescript, code-structure]
---

# Rationale: Members vs Module Functions

Two forces decide placement: **encapsulation** and **composition**.

## The module is the real privacy boundary

TypeScript's `private` is a compile-time annotation; non-export is enforced by the module system itself, at runtime, in plain JavaScript. A pure helper gains nothing from living inside the class — it only gains an unnecessary `this` context and a longer file to scroll inside. Public API and state-touching behavior stay members because they *are* the object's contract and DSL.

## Point-free composition, without the `this` quirk

JavaScript methods are unbound functions: `this` is resolved at the **call site**, not at definition (late binding — closer to dynamic scoping, where closure variables are lexically captured). So `array.map(this.myFunction)` detaches the method and silently loses its receiver, while `array.map(myFunction)` on a pure module function just works.

Pure module functions are `this`-free by construction, so they compose point-free in pipelines with the idiomatic dot-free form. The rule **avoids** the language quirk instead of managing it — no `.bind(this)`, no arrow-property workarounds, no per-call vigilance. A quirk you cannot encounter is cheaper than one you handle correctly every time.
