---
name: tracer
description: >-
  Work under the TRACER development method: a Minimum Expected Value (MEV)
  fully specified up front, then built in 1-3 day slices on the final
  architecture, each one tested, traced to its specs and deployable. Use when
  the repository has a docs/tracer/ folder or an MEV spec, when the user
  mentions TRACER, MEV, slices, tracer slices, expectation contract or scope
  filter, or asks to plan, build or review work "the TRACER way".
---

# TRACER

The full method is in the handbook: https://github.com/Rixmerz/tracer/blob/main/docs/method.md.
This skill is the operational summary an agent follows.

## Where things live

Keep TRACER state in the repository, so it survives sessions:

- `docs/tracer/contract.md`: the expectation contract (metric, target, quality
  floor, validation window, validator, Must/Should/post-MEV backlog).
- `docs/tracer/slices.md`: the slice plan, one line per slice with status
  (planned, in progress, done) and the requirements it covers.
- `docs/tracer/backlog.md`: the post-MEV backlog.
- Specs and ADRs: wherever the project's spec tool keeps them (OpenSpec
  `openspec/` by default).

If these files are missing, the project has not started TRACER. Suggest
`/tracer:contract` instead of improvising.

## Rules you never break

1. **Design for the destination.** Never pick a temporary architecture (JSON
   file instead of the planned database, a mock instead of the planned
   integration) to go faster. If the ADRs do not cover a decision you need,
   stop and propose an ADR.
2. **No throwaway code.** Do not build anything the MEV does not need.
3. **Spec before code.** Any change in behaviour starts as a spec change. If
   asked to change behaviour with no spec change, write the spec change first
   and show it.
4. **Stay inside the slice.** Implement only the requirements of the current
   slice. Something else worth doing goes to `/tracer:scope`, not into the
   diff.
5. **Every slice passes the gates** before it counts as done: scenario tests,
   regression, spec integrity, impact, UI (if there is UI), quality floor,
   human review. Never mark a slice done on your own; a person approves.
6. **All code is traced.** Every new or changed symbol is linked to a
   requirement.
7. **Scope is filtered by the metric.** A new idea enters the MEV only if it
   moves the contract's metric.

## Traceability with livespec

livespec is installed with this plugin. Use it for the chain
MEV → requirements → scenarios → code → tests → tracks:

- Cold open per repo: `index_project`, then `get_project_overview`.
- If the repo has `openspec/`, run `sync_openspec` before reading specs and
  `validate_openspec` after editing them.
- Link code and tests to specs with `@spec:` annotations (see livespec's
  `agent_playbook` prompt).
- Before review: `git_diff_impact` for the impact gate, `audit_coverage` for
  spec integrity and MEV coverage.

If the livespec MCP server is not available in this session, say so once and
keep the chain by hand: `@spec:` comments in code and tests, and a coverage
count in `docs/tracer/slices.md`.

## Commands

- `/tracer:contract`: phase 0 and phase 1. Write the contract, the specs, the
  ADRs and the slice plan.
- `/tracer:slice`: phase 3. Start, build and close one slice.
- `/tracer:scope`: phase 4. Run a new idea or correction through the filter.

## Reporting progress

When asked how the MEV is going, report: MEV coverage (verified scenarios ÷
all scenarios), slices done and remaining, the likely and safe forecast dates
(section 14 of the handbook), rework rate and any untraced code.
