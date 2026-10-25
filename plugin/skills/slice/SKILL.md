---
description: Build one TRACER slice - check it is ready, implement it test-first, pass the gates and record its track (phase 3)
argument-hint: "[slice number or name; defaults to the next planned slice]"
disable-model-invocation: true
---

Build one TRACER slice: "$ARGUMENTS" (if empty, the first slice marked
planned in `docs/tracer/slices.md`). Follow the `tracer` skill's rules.

## 1. Definition of Ready

Check and report each item. If one fails, stop and say what is missing.

- Its requirements exist in the validated spec set, each with scenarios.
- It builds on the skeleton or earlier slices; it needs no new architecture.
  If it does, propose an ADR through `/tracer:scope` instead.
- It fits in 1 to 3 days. If not, propose a split.

Mark it "in progress" in `docs/tracer/slices.md`.

## 2. Build

1. Turn each scenario into a test first; run them and confirm they fail.
2. Implement until they pass. Touch only what the slice's requirements need.
3. Link every new or changed symbol and test to its requirement (`@spec:`).
4. Anything you notice outside the slice: note it for `/tracer:scope`, do not
   build it.

## 3. Gates

Run and report each gate with its evidence:

| Gate | How |
| ---- | --- |
| Scenario tests | The slice's tests pass |
| Regression | The full suite passes |
| Spec integrity | livespec `audit_coverage`: no untraced changed code, no requirement without a scenario |
| Impact | livespec `git_diff_impact` on the slice's diff; explain anything unexpected |
| UI | Only if the slice has UI: layout and responsive checks |
| Quality floor | The contract's thresholds still hold |
| Human review | Hand the diff and the gate results to the user; wait for approval |

A failed gate sends the slice back to step 2 and counts as rework: note it in
`docs/tracer/slices.md`.

## 4. Close

After the user approves and the slice is deployed:

- Mark it "done" with its cycle time in days and any rework.
- Record its track: which specs and symbols changed, and why.
- Report MEV coverage, slices remaining and the updated forecast.
