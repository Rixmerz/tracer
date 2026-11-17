---
name: retro
description: Write a TRACER retrospective from the project's own records - decision log, slice plan, git or artifact history, verification results - marking every statement as fact, inference or hypothesis, and turn its lessons into floors and catalog entries
argument-hint: "[period, MEV or slice range; defaults to everything since the last retrospective]"
disable-model-invocation: true
---

Write a retrospective of "$ARGUMENTS". Follow the `tracer` skill's rules. No
production code is written in this command.

## 1. Gather the sources

Read, and list as available or missing:

- `docs/tracer/decisions.md` (the decision log) and `docs/tracer/slices.md`.
- The history: `git log` with its diffs, or the artifact's version list.
  Name every version or commit whose author is not known.
- `docs/tracer/content.md`, the contract, the audience profiles and the
  verification results or requests of each slice.
- The conversation or review comments, when the person shares them.

Never fill a gap from memory. What no source shows is written as missing.

## 2. Write it

Use `${CLAUDE_PLUGIN_ROOT}/templates/retrospective.md` and write
`docs/tracer/retros/<date>.md`. Mark each statement **[F]** fact, **[I]**
inference or **[H]** hypothesis. For each error, name the gate or step that
should have caught it and whether it ran. Find the pattern across errors:
several defects of one kind point to one missing gate.

## 3. Feed the method

For each lesson, propose the exact change and let the user accept each one:

- A CORRECT line for the spec it escaped from.
- An entry for `docs/tracer/floors.md`, or for `docs/tracer/anti-patterns.md`
  under the principle it breaks (a new family if none fits).
- A change to TRACER itself, written as an issue for its repository.

End with: sources read and missing, errors found, escaped expectations,
lessons accepted and where each one was written.
