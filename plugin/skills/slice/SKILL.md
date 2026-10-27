---
description: Build one TRACER slice - check it is ready, implement it test-first, pass the gates and record its track (phase 3)
argument-hint: "[slice number or name; defaults to the next planned slice]"
disable-model-invocation: true
---

Build one TRACER slice: "$ARGUMENTS" (if empty, the first slice marked
planned in `docs/tracer/slices.md`). Follow the `tracer` skill's rules.

## 1. Definition of Ready

Check and report each item. If one fails, stop and say what is missing.

- Its requirements exist in the validated spec set, each with scenarios, and
  went through the empathy round.
- It lands on one capability in `docs/tracer/capabilities.md` and duplicates
  no existing one.
- Its audience, critical flows (success and failure paths, WORKS and CORRECT)
  and inherited component floors are written.
- It builds on the skeleton or earlier slices; it needs no new architecture.
  If it does, propose an ADR through `/tracer:scope` instead.
- It fits in 1 to 3 days. If not, propose a split.

Mark it "in progress" in `docs/tracer/slices.md`.

## 2. Build

1. Read the audience profile, the critical flows, the floors,
   `docs/tracer/identity.md` and the anti-pattern catalog before any code.
   Never fill an unspecified interface detail with the common default: if
   the specs do not say, ask or propose a spec change.
2. Turn each scenario into a test first, and each critical flow into an
   interface-driven end-to-end test that asserts its CORRECT lines; run them
   and confirm they fail.
3. Implement until they pass. Touch only what the slice's requirements need.
4. Link every new or changed symbol and test to its requirement (`@spec:`).
5. Self-check the screens against the anti-pattern catalog.
6. Anything you notice outside the slice: note it for `/tracer:scope`, do not
   build it.

## 3. Gates

Run and report each gate with its evidence:

| Gate | How |
| ---- | --- |
| Scenario tests | The slice's tests pass |
| Critical flows | Run by `/tracer:verify` (not by you): every flow passes end to end through the interface, success and failure paths, CORRECT lines included |
| Regression | The full suite and all earlier critical flows pass |
| Spec integrity | livespec `audit_coverage`: no untraced changed code, no requirement without a scenario |
| Impact | livespec `git_diff_impact` on the slice's diff; explain anything unexpected |
| UI and anti-patterns | Run by `/tracer:verify`: floors, accessibility, rendered text free of ids and paths, the anti-pattern catalog |
| Static quality | Duplication, complexity, vulnerabilities and secrets within the project's limits |
| Quality floor | The contract's thresholds still hold |
| Human review | Hand the diff and the gate results to the user; wait for approval |

A failed gate sends the slice back to step 3 and counts as rework: note it in
`docs/tracer/slices.md`. If verification finds something no spec covered,
add the CORRECT line and the catalog entry it proposes, and count an escaped
expectation.

## 4. Close

After the user approves and the slice is deployed:

- Mark it "done" with its cycle time in days and any rework.
- Record its track: which specs and symbols changed, and why.
- Report MEV coverage, slices remaining and the updated forecast.
