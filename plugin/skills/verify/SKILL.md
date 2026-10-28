---
description: Independently verify a TRACER slice or an existing screen - drive its critical flows through the interface, check every CORRECT line, the component floors and the anti-pattern catalog (phase 3)
argument-hint: "[slice number, capability or URL; defaults to the slice in progress]"
disable-model-invocation: true
---

Verify "$ARGUMENTS" (if empty, the slice marked in progress in
`docs/tracer/slices.md`). Follow the `tracer` skill's rules.

You are the verifier, not the builder. Work from the specs, the audience
profile, the critical flows, `docs/tracer/floors.md`,
`docs/tracer/anti-patterns.md` and `docs/tracer/identity.md`. Do not read or
trust the builder's report. Do not fix anything: report what you find.

## 1. Become the audience

Read the audience profile of the capability. For the rest of this command,
judge every screen as that person would: their words, their knowledge, their
devices, their accessibility needs.

## 2. Drive the critical flows

For every critical flow the target touches, run it end to end through the
real interface (a browser driver such as rastro or Playwright, against the
deployed or production-like system):

- First prove you are on the target: the screen of the slice, signed in as
  its audience, with real data from the system (not fixtures). Evidence of
  any other screen, such as a login page, does not count.
- The success path, checking the WORKS half and every CORRECT line.
- Every failure path: trigger it and check what the person sees and how they
  recover. A failure with no clear message and no way out is a failure of
  the flow, whatever the API returned.
- Interruptions: start each long operation (an upload, a save) and navigate
  away, switch tabs or repeat it. Nothing may be lost without a warning.

## 3. Check floors and anti-patterns

- Every component on the screens meets its floor.
- Accessibility: keyboard use, focus, accessible names, contrast, target
  sizes (layout-inspector or an equivalent).
- Rendered text scanned for UUIDs, storage keys, ids, file paths and stack
  traces.
- Every entry of the anti-pattern catalog, one by one; then each family's
  principle against the screen as a whole. A case that breaks a principle
  fails even if no entry names it.
- The same action solved differently elsewhere (compare with the capability
  map).
- Consistency with `identity.md`.
- Every value, count or flag on screen comes from data the system really
  provides.
- Common actions are recognizable at a glance: icon plus label, one meaning
  per icon, no state told by color alone.
- The testing anti-patterns: the builder's last full run is clean, or its
  failures match the base list.

## 4. Report

One table: each flow, CORRECT line, floor and anti-pattern as passed or
failed, with evidence (a screenshot, the rendered text, the step). Then the
verdict: **pass** only if every line passes.

If something fails that no spec, floor or catalog entry covered, say so: it
is an escaped expectation. Propose the CORRECT line to add to the spec and
the entry to add to `floors.md`, or to `anti-patterns.md` under the
principle it breaks.

On an existing product with no TRACER specs (a screen, a URL), derive the
audience from the user first, then run steps 2 to 4 using the templates'
floors and catalog.
