---
description: Start a TRACER MEV - write the expectation contract and audience profiles, the base round of specs, the capability map, the ADRs and the slice plan (phases 0 and 1)
argument-hint: "[short name of the MEV]"
disable-model-invocation: true
---

Start a TRACER Minimum Expected Value named "$ARGUMENTS". Follow the `tracer`
skill's rules. No production code is written in this command.

## Phase 0: expectation contract

Ask the user, one question at a time, until each field has a concrete answer:

1. The outcome owner.
2. The metric, its current value and its target. If no metric can be named,
   stop: the work is not ready for TRACER (suggest an experiment instead).
3. The quality floor (error rate, performance, accessibility, or accuracy on
   real samples for AI features).
4. The validation window (default 2 to 4 weeks) and who validates.
5. The audiences. For each one, fill the audience profile template
   (https://github.com/Rixmerz/tracer/blob/main/templates/audience-profile.md):
   who they are, what they are trying to get done, what they know and do not
   know, their words, context, accessibility needs (default WCAG 2.2 AA),
   what they must never see, and the product genre. If nobody can describe
   an audience, stop until someone who knows them can.
6. The candidate items as a MoSCoW list. For each one ask: does it move the
   metric? Items that do not are *Could* and go to the post-MEV backlog.

Write `docs/tracer/contract.md` from the expectation contract template
(https://github.com/Rixmerz/tracer/blob/main/templates/expectation-contract.md)
`docs/tracer/audiences.md` and `docs/tracer/backlog.md`. Copy the component
floors and anti-pattern catalog templates into `docs/tracer/floors.md` and
`docs/tracer/anti-patterns.md`. Show the contract and wait for the user's
sign-off before phase 1.

## Phase 1: complete spec

1. **Base round.** Write every MEV requirement with at least one WHEN/THEN
   scenario, in the project's spec tool (OpenSpec by default:
   `### Requirement:` / `#### Scenario:`), using the requirement template.
2. **Capability map.** Group requirements by what the user can do and write
   `docs/tracer/capabilities.md`. Before adding a capability, search the
   existing ones (livespec `search_similar`); extend instead of duplicating.
3. **Empathy round.** Run the `/tracer:empathy` procedure on every
   capability: expectations, the MEV rule, improved and new specs, critical
   flows, inherited floors and the deferred list. Then fix the identity of
   the defining screens through two or three variants chosen by the user.
4. Record architecture decisions for the destination as ADRs: data model,
   persistence, integrations, deployment.
5. Validate strictly: no requirement without a scenario, no scenario without
   an observable outcome, no capability without a critical flow, no CORRECT
   line that cannot be checked. With livespec available, `sync_openspec` then
   `validate_openspec`.
6. If a core assumption is risky (an AI capability, a third-party API),
   propose a timeboxed spike. Its code is deleted; its result updates the
   specs and ADRs.
7. Write `docs/tracer/slices.md`: the skeleton first (one flow end to end on
   the final architecture, with deployment, CI and tests), then slices of 1 to
   3 days, each on one capability, listing its requirements and critical
   flows.
8. Give the first forecast: slice count × 2 days, as a wide range.

End with a summary: requirement and scenario counts (base and empathy),
critical flows, deferred expectations, ADRs written, slice
count, forecast, and the next step (`/tracer:slice` for the skeleton).
