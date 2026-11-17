---
name: team
description: Plan or review a team's sprint under the TRACER teams adaptation - cards with complexity and responsibility, repository profiles, expertise, cells of three with relay, progress checks, free margin and the speed or balance mode
argument-hint: "[plan, check, reassign or balance; defaults to plan]"
disable-model-invocation: true
---

Work under the teams adaptation of TRACER for "$ARGUMENTS". The rules are in
https://github.com/Rixmerz/tracer/blob/main/docs/adaptations/teams.md and the
templates in `${CLAUDE_PLUGIN_ROOT}/templates/team/`. State lives in
`docs/tracer/team/`: `people.md`, `repos.md`, `cards.md`, `balance/<sprint>.md`.

## plan

1. For each card: type (execution, diagnosis, analysis, exploration),
   complexity C, responsibility R from the rubric (set by the PO and the LT,
   never by the executor) and the repositories it touches. Split any card
   that mixes analysis and building: analysis is timeboxed and delivers a spec.
2. Read the people (capacity H, margin, role ceiling, budget, expertise per
   repository, speed per type) and the repository profiles (K, R floor,
   critical).
3. Call `team_balance` with the last sprint's slip and mode to set this
   sprint's mode and rotation share, then `team_assign` with it. If the tools
   are missing, follow `assignment.md` by hand.
4. Show each card: primary, relay, co-holder, rotation, expected time and
   checks. Nothing is planned into anyone's free margin. Wait for the PO and
   the LT to approve.

## check

At each check, ask for the evidence the card's type requires. Met: continue.
Not met: reassign at once to the next in the relay (A → B → C → LT, never
back to A), into that person's margin, and record the absorbed hours. Do not
penalize the person; recalibrate their factors.

## balance

At the end of the sprint, fill `balance-report.md`: nominal and worst-case
velocity, bus factors, rotation used, reassignments, margin consumed,
estimate accuracy, fatigue signals and the mode for the next sprint. A
fatigue signal is answered with less load, never with a penalty.
