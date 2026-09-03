---
name: annotate-code-flow
description: Annotate and explain source code so its execution flow, data movement, state changes, and design logic are easy to follow. Use when a user asks to add educational comments, explain code inline, trace how code works, or make unfamiliar code easier to learn without changing its behavior.
---

# Annotate Code Flow

Make the code understandable as a connected process rather than a collection of syntax notes.

## Choose the output

- If the user asks to annotate or modify a file, add comments directly to the source.
- If the user asks only for an explanation or review, leave the source unchanged and provide an annotated excerpt or walkthrough.
- Match the user's apparent experience level. Define language-specific concepts briefly for a learner, but stay compact for an experienced developer.

## Build a mental model first

Inspect enough surrounding code to identify:

- the entry point and what triggers it;
- the main call sequence;
- where inputs originate and how data is transformed;
- branches, loops, early returns, and stopping conditions;
- state mutations and side effects;
- asynchronous boundaries, callbacks, events, or concurrency;
- error handling and important edge cases;
- the final output or externally visible result.

When relevant code crosses files, trace the important calls before annotating. Do not invent behavior that cannot be established from the code; label uncertain conclusions as assumptions.

## Write useful annotations

Prefer comments that explain intent, cause and effect, invariants, or why an operation occurs at that point. Place them at logical boundaries such as a function, processing phase, non-obvious branch, state transition, or error path.

Use short flow markers such as `Step 1`, `Step 2`, and `Step 3` only when they make a genuinely sequential path easier to follow. Keep numbering consistent across the annotated region.

Explain relationships that syntax alone does not reveal. For example, note that one value is cached for a later branch, that an early return prevents an invalid write, or that an awaited call pauses this function while other work may continue.

Do not:

- narrate obvious syntax or comment every line;
- restate names without adding meaning;
- claim a reason that the code does not support;
- add long tutorial blocks inside production code when a short comment and an external walkthrough are clearer;
- change behavior, public APIs, formatting conventions, or control flow merely to make annotation easier.

Preserve existing comment style and terminology. If comments already explain the same point, improve or consolidate them instead of duplicating them.

## Present the result

For a direct source edit, briefly summarize the execution path after making the annotations and report any verification performed. Run proportionate existing formatting or tests when comments could affect parsing, generated files, documentation tooling, or lint rules.

For a walkthrough, lead with a one- or two-sentence overview, then follow the runtime path in order. Use a compact flow diagram only when calls branch across several components and prose would obscure the relationship.
