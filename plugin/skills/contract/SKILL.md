---
description: Start a TRACER MEV - write the expectation contract, the complete spec set, the ADRs and the slice plan (phases 0 and 1)
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
5. The candidate items as a MoSCoW list. For each one ask: does it move the
   metric? Items that do not are *Could* and go to the post-MEV backlog.

Write `docs/tracer/contract.md` from the expectation contract template
(https://github.com/Rixmerz/tracer/blob/main/templates/expectation-contract.md)
and `docs/tracer/backlog.md`. Show the contract and wait for the user's
sign-off before phase 1.

## Phase 1: complete spec

1. Write every MEV requirement with at least one WHEN/THEN scenario, in the
   project's spec tool (OpenSpec by default:
   `### Requirement:` / `#### Scenario:`).
2. Record architecture decisions for the destination as ADRs: data model,
   persistence, integrations, deployment.
3. Validate strictly: no requirement without a scenario, no scenario without
   an observable outcome. With livespec available, `sync_openspec` then
   `validate_openspec`.
4. If a core assumption is risky (an AI capability, a third-party API),
   propose a timeboxed spike. Its code is deleted; its result updates the
   specs and ADRs.
5. Write `docs/tracer/slices.md`: the skeleton first (one flow end to end on
   the final architecture, with deployment, CI and tests), then slices of 1 to
   3 days, each listing the requirements it covers.
6. Give the first forecast: slice count × 2 days, as a wide range.

End with a summary: requirement and scenario counts, ADRs written, slice
count, forecast, and the next step (`/tracer:slice` for the skeleton).
