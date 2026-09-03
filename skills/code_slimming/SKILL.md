---
name: code-slimming
description: Simplify existing code by removing unnecessary logic, duplication, abstractions, and dependencies while preserving required behavior. Use for refactoring, cleanup, reducing complexity, or making an implementation smaller and clearer; do not use when the user wants new features or code-golf at the expense of readability.
---

# Code Slimming

Make the codebase smaller, clearer, and easier to maintain without changing its intended behavior.

## Working approach

1. Establish the required behavior from the request, existing tests, call sites, public interfaces, and documentation.
2. Identify code that adds no justified value, including:
   - unreachable or unused code, imports, variables, parameters, and dependencies;
   - duplicated logic that can be expressed once without obscuring intent;
   - wrappers, helpers, classes, configuration, and indirection used only once without a concrete benefit;
   - redundant branches, conversions, temporary values, comments, and defensive checks already guaranteed by validated invariants;
   - obsolete compatibility paths and feature flags when repository evidence shows they are no longer required.
3. Prefer the simplest conventional implementation that remains readable and fits the surrounding code.
4. Make focused edits. Do not broaden the refactor into unrelated files merely to achieve stylistic consistency.
5. Run the most relevant existing tests, linters, type checks, or build commands after editing. If coverage is weak, perform a targeted behavioral check.

## Constraints

- Preserve observable behavior, public APIs, data formats, error semantics, and supported compatibility unless the user explicitly authorizes a change.
- Treat apparent dead code cautiously. Check references, dynamic loading, reflection, framework conventions, configuration, and external entry points before removing it.
- Do not optimize for line count alone. Reject compressed expressions, clever one-liners, and over-generalized helpers when they reduce readability or debuggability.
- Do not replace clear repetition with an abstraction unless it removes meaningful maintenance cost.
- Avoid adding dependencies to reduce a small amount of local code. Remove a dependency only after confirming it has no remaining use.
- Preserve useful comments that explain intent, constraints, or surprising behavior; remove comments that merely restate the code or describe deleted behavior.
- Keep performance and security properties intact. Do not remove validation, authorization, escaping, synchronization, resource cleanup, or error handling without evidence that it is redundant.
- Respect generated or vendored code boundaries; change their source or generator rather than hand-editing outputs when applicable.

## Completion report

Summarize what was simplified, call out any behavior-affecting choices, and report the verification performed. If suspected code could not be safely removed, identify it and explain the uncertainty briefly.
