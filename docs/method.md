# The TRACER Method

TRACER is a development method for building software with AI agents. In one
sentence: **agree up front on the value the product must deliver, specify all
of it, then build it in thin slices that are already part of the final
product.**

This document explains the method from the ground up. Each concept is
introduced before it is used.

## 1. The problem

AI agents build for what they are asked today, not for where the product is
going.

Ask an agent for a proof of concept and it stores data in a JSON file. Ask it
for a minimum viable product next and it adds a database. The proof-of-concept
code is then thrown away or duplicated, and the product ships half-built.

The classic answer is to write a complete specification and hand it to the
agent in one go. That recreates waterfall: huge changes, frozen specs and late
surprises.

TRACER keeps the good half of each approach. From specification-first
development it takes knowing the destination before building. From iterative
development it takes small, verified steps. What it drops is throwaway code
and big-bang delivery.

## 2. The target: Minimum Expected Value

Everything in TRACER points at one deliverable, so it needs a name first.

The **Minimum Expected Value (MEV)** is the smallest scope that delivers the
value the business already expects. It is defined by an outcome, not by a
feature list: a measurable result, a target for that result, and a quality
floor below which the result does not count.

An example: *customer email queries are answered within 1 day instead of 8,
with fewer than 2% wrong answers, validated by the customer care lead.*

The MEV is easiest to understand next to the better-known minimum viable
product (MVP):

|           | MVP                          | MEV                                              |
| --------- | ---------------------------- | ------------------------------------------------ |
| Question  | Does anyone want this?       | Did we deliver the value the business expects?   |
| Demand    | Uncertain                    | Already confirmed                                |
| Code      | Disposable if the idea fails | Final from the first slice                       |
| Done when | Enough has been learned      | The metric reaches its target                    |

An MVP is an experiment. An MEV is a delivery. TRACER is for the second case
only.

## 3. Two horizons

With the MEV defined, the core idea of TRACER fits in one table. The method
separates the horizon you **design** for from the horizon you **execute** in:

| Horizon       | Scope                                                  | Why                                                                         |
| ------------- | ------------------------------------------------------ | --------------------------------------------------------------------------- |
| **Design**    | The complete MEV: every requirement, from the start    | Architecture (data, persistence, integrations) is decided once, for the real destination |
| **Execution** | Thin slices of 1 to 3 days, on the final architecture  | The agent never works all-or-nothing, and every slice is tested as it lands |

Designing for the whole MEV removes throwaway code. Executing in slices
removes waterfall.

## 4. The name

A tracer bullet is a thin but real round that shows the path to the target.
Unlike a prototype, it is kept. Each slice in TRACER works the same way.

The acronym also states the method:

- **T**raceable: every requirement is linked to the code and tests that
  implement it.
- **R**equirement-complete: the MEV is fully specified before building starts.
- **A**rchitected for the destination: no temporary architecture, ever.
- **C**ontinuously validated: every slice passes the validation gates.
- **E**xecuted in slices: 1 to 3 days each, each one deployable.
- **R**eleased at MEV: delivery happens when the expected value is complete
  and verified.

## 5. When to use it

Use TRACER when:

- The business already knows the value it expects. The goal is to deliver it,
  not to discover whether anyone wants it.
- AI agents write a large share of the code.
- Specifications and code must stay aligned over time.

Do not use it when:

- Demand itself is uncertain. Run a real MVP or experiment first, and expect
  to throw it away.
- The work is pure research with no definable outcome.

## 6. Principles

Seven rules that cannot be negotiated away. Drop any of them and it is no
longer TRACER.

1. **Design for the destination.** Architecture decisions are made for the
   MEV, never for an intermediate prototype.
2. **No throwaway code.** Every slice is part of the final product. If
   something is not needed for the MEV, it is not built.
3. **Spec before code.** Any change in behaviour starts as a change to the
   specification, then reaches the code.
4. **Every slice is deployable** and leaves the system working.
5. **Every slice passes the gates.** Tests and checks run on each slice, not
   at the end.
6. **All code is traced.** Code without a linked requirement is an alert, not
   a detail.
7. **Scope is filtered by the expected value.** A new idea enters the MEV
   only if it moves the MEV's metric.

## 7. Vocabulary

The rest of this document uses these terms. Most have already appeared; this
is the reference list.

| Term                     | Definition |
| ------------------------ | ---------- |
| **MEV**                  | Minimum Expected Value: the smallest scope that delivers the expected outcome (section 2). |
| **Expectation contract** | The written definition of the MEV's success: metric, current value, target, quality floor, validation window and who validates it. |
| **Requirement**          | One behaviour the system must have, written so it can be checked. |
| **Scenario**             | A concrete WHEN/THEN example of a requirement. Every scenario can become a test. |
| **Spec**                 | A requirement together with its scenarios. The full set of specs describes the MEV. |
| **ADR**                  | Architecture Decision Record: one architecture decision, written once, for the destination. |
| **Slice**                | A vertical piece of 1 to 3 days that implements a few requirements and can be deployed on its own. Also called a tracer. |
| **Skeleton**             | The first slice: one flow end to end on the final architecture, with deployment, CI and tests in place. |
| **Spec change**          | A proposal that adds, modifies or removes requirements before any code changes. |
| **Validation gate**      | An automated or human check that every slice must pass before it counts as done. |
| **Track**                | The recorded history of a slice: which specs and code symbols changed, and why. |
| **MEV coverage**         | Verified scenarios divided by all scenarios in the MEV. The real progress bar. |
| **Post-MEV backlog**     | Ideas that do not move the MEV's metric, kept for after the first delivery. |

## 8. Defining the MEV

An MEV is defined in five steps. Together they form the expectation contract.

### 8.1 The metric

One metric, its current value, the target, and who validates it. If no metric
can be named, the work is not ready for TRACER.

### 8.2 The cut

Start from a MoSCoW list (Must, Should, Could, Won't) and apply one test to
every item: **does it move the metric?** Items that do not are *Could*, even
if the client asked for them.

The MEV is every *Must* plus the *Shoulds* that pass the test. *Could* items
go to the post-MEV backlog.

### 8.3 The quality floor

The minimum quality the outcome needs: error rate, performance, accessibility,
or, for AI features, an accuracy threshold measured on real samples (for
example, 45 correct answers out of 50).

### 8.4 The validation window

How long the MEV runs in production before the metric is measured. Usually 2
to 4 weeks.

### 8.5 The exit decision

Decided in advance, applied at the end of the window:

| Result         | Decision |
| -------------- | -------- |
| Target reached | Close the MEV. Post-MEV items become a new MEV if they justify one. |
| Partly reached | Open a new MEV focused on the gap. |
| Not reached    | Stop, record what was learned, and decide whether to retire the feature. |

## 9. Lifecycle

An MEV goes through six phases. Phases 0 and 1 happen once. Phase 3 repeats
until every scenario is verified, and phase 4 runs alongside it.

```
Design horizon                    Execution horizon
──────────────────────────────    ─────────────────────────────────────────────
0 Expectation → 1 Complete   →    2 Skeleton → 3 Slices (repeat) → 5 Release
  contract       spec                             ↑
                                               4 Scope control (in parallel)
```

### Phase 0 · Expectation contract

Agree the metric, target, quality floor, validation window and validator.

**Exit:** a signed-off contract.

### Phase 1 · Complete spec

1. Write every MEV requirement, each with at least one scenario.
2. Record the architecture decisions as ADRs for the destination: data model,
   persistence, integrations, deployment.
3. Validate the spec set strictly: no requirement without a scenario, no
   scenario without an observable outcome.
4. Order the requirements into a slice plan: which flow goes into the
   skeleton, which slices follow.

**Exit:** a validated spec set and its ADRs. No code yet, except a timeboxed
spike when a risky assumption must be checked first.

### Phase 2 · Skeleton

One flow, end to end, on the final architecture: real database, real
deployment, CI, test harness and validation gates wired up.

**Exit:** the skeleton is deployed and its scenarios pass.

### Phase 3 · Tracer slices

Each slice takes a few requirements from the plan, turns their scenarios into
tests, has the agent implement them, passes the gates, links the code to the
specs and records its track.

**Exit per slice:** deployed and traced.
**Exit for the phase:** MEV coverage reaches 100%.

### Phase 4 · Scope control

Runs in parallel with phase 3. See section 12.

### Phase 5 · MEV release

Release, run the validation window, measure the metric and take the exit
decision.

## 10. Slices

A slice is the unit of execution: small enough that an agent never works
all-or-nothing, real enough that nothing gets rebuilt later.

### Sizing

| Rule     | Value |
| -------- | ----- |
| Size     | 1 to 3 days of work |
| Shape    | Vertical: data, logic and interface for the requirements it covers |
| Content  | A few related requirements, never a whole module at once |
| Too big  | Split it before it starts. A slice that needs more than 3 days is two slices. |

### Definition of Ready

- Its requirements exist in the validated spec set, each with scenarios.
- It builds on the skeleton or on earlier slices. No new architecture appears
  inside a slice.
- Its validation gates are known.

### Definition of Done

- Every scenario it covers has a passing test.
- It passed every validation gate.
- A person reviewed and approved the change.
- It is deployed and the system still works.
- Its code is linked to its specs, and its track is recorded with the reason
  for each change.

### Inside the slice

Extreme Programming practices: test-first from the scenarios, continuous
integration, small commits, collective code ownership, and pair programming
(human with human, or human with agent) on risky work.

The agent writes the code. A person owns the result.

## 11. Validation gates

Gates are what make TRACER fast without being reckless: every slice is checked
as it lands, so errors never pile up until the end.

| Gate               | Checks | Typical tooling |
| ------------------ | ------ | --------------- |
| **Scenario tests** | Every scenario in the slice passes | Unit, integration and end-to-end tests generated from WHEN/THEN |
| **Regression**     | Earlier slices still pass | Full test suite in CI |
| **Spec integrity** | No requirement without a scenario; no new code without a linked spec | Spec validator, traceability audit |
| **Impact**         | What else the change touches | Call-graph and diff impact analysis |
| **UI**             | Layout, responsiveness and visual regressions | Layout inspection and screenshot checks |
| **Quality floor**  | The MEV's thresholds still hold: accuracy, performance, cost per use | Benchmarks on real samples |
| **Human review**   | A person approves the change | Pull request review |

A team chooses its own tools for each gate; the gates themselves are fixed. A
slice that fails a gate goes back to implementation, and the failure counts as
rework.

## 12. Scope control during delivery

Specifying the whole MEV up front invites scope creep. This phase is the
counterweight. New ideas are welcome, but none of them reaches the code
without passing the same filter.

### The filter

1. **Write it as a spec change:** what it adds, modifies or removes.
2. **Test it against the metric:** does it move the MEV's outcome?
3. **Decide:**

| Answer                         | Result |
| ------------------------------ | ------ |
| Moves the metric, small        | Enters the MEV. The slice plan and forecast are updated. |
| Moves the metric, large        | Enters only by swapping out a *Should* of similar size, or by accepting a new forecast. |
| Does not move the metric       | Post-MEV backlog. |
| Changes an architecture decision | New ADR first, then impact analysis on built slices before accepting. |

### Learnings from building

Some changes are not new ideas but corrections: a scenario was wrong, a
constraint appeared. These go straight in as spec changes, since they keep the
spec true, but they still update the forecast and are recorded in the track.

## 13. Traceability

TRACER needs one unbroken chain:

**MEV → requirements → scenarios → code → tests → tracks**

Any toolchain that keeps that chain alive works. The reference stack is
[OpenSpec](https://github.com/Fission-AI/OpenSpec) for authoring specs and
livespec for keeping specs linked to code.

| Need | Reference tool | What it provides |
| ---- | -------------- | ---------------- |
| Author requirements and scenarios | OpenSpec | `### Requirement:` / `#### Scenario:` (WHEN/THEN) per capability |
| Validate the spec set | OpenSpec / livespec | Strict validation: every requirement has at least one scenario |
| Propose spec changes | OpenSpec changes | ADD / MODIFY / REMOVE deltas, applied then archived |
| Link code and tests to specs | livespec | `@spec:` annotations and scenario-level links, rescanned on every index |
| Detect drift | livespec | Body and signature hashes per symbol; code with no linked spec |
| Analyse impact | livespec | Call graph and diff impact before each review |
| Record history | livespec tracks | Per range: which specs and symbols changed, and why |
| Measure progress | livespec | Per-scenario verified flag, coverage audit |

### How each phase uses it

- **Phase 1:** author the whole MEV as specs, record ADRs as specs of their
  own kind, validate strictly.
- **Phase 3:** link every slice's code and tests to its scenarios, run impact
  analysis before review, record the slice's track.
- **Phase 4:** every new idea is a spec change before it is anything else.
- **Phase 5:** MEV coverage comes straight from the verified scenarios.

### Representing the MEV itself

Model the MEV as a spec at the top of the graph, holding the expectation
contract, with its requirements linked beneath it. MEV coverage is then a
query rather than a spreadsheet, and any change can be traced back to the
outcome it serves.

## 14. Forecasting

Because the whole MEV is specified up front, its size in slices is known from
day one. Dates come from how fast slices actually close, always as a range.

1. **Count the slices** in the slice plan after phase 1.
2. **Until there is data** (the first 5 to 10 slices), forecast with 2 days per
   slice and give a wide range.
3. **With data**, use the measured cycle time per slice and the number of
   slices finished per week:

```
Weeks to MEV ≈ Remaining slices ÷ Slices finished per week
```

Always give two dates: **likely** (met half the time) and **safe** (met 85
times in 100). Recompute every week and after every accepted scope change.

The gap between the slice count planned in phase 1 and the count at release is
itself a signal: it measures how much the spec missed.

## 15. Metrics

| Metric | What it measures | Healthy signal |
| ------ | ---------------- | -------------- |
| **MEV coverage** | Verified scenarios ÷ all MEV scenarios | Rises every week |
| Cycle time per slice | Days from start to deployed | 3 days or less, 85% of the time |
| Rework | Slices that failed a gate | Under 15% |
| Untraced code | Changed code with no linked spec | Zero at release |
| Drift | Specs whose linked code changed without a spec change | Resolved within the slice |
| Spec growth | Slices at release ÷ slices planned in phase 1 | Under 1.3 |
| Throwaway | Code deleted because it was built for a temporary shape | Zero |
| Outcome | The MEV metric after the validation window | Target reached |

### Calibration

- **Rework above 15%:** scenarios are too vague or slices too big. Tighten
  both.
- **Spec growth above 1.3:** phase 1 was too shallow. Spend longer on
  scenarios and spikes.
- **Cycle time above 3 days:** split slices further.
- **Any throwaway:** an architecture decision was skipped. Add the missing
  ADR.

## 16. Roles and cadence

### Roles

| Role | Owns | Does not |
| ---- | ---- | -------- |
| **Outcome owner** | The expectation contract, the cut, scope decisions, the exit decision | Add scope without passing the filter |
| **Spec lead** | The spec set, ADRs, the slice plan, spec integrity | Let code change behaviour before the spec does |
| **Builders** (people and their agents) | Slices, tests, links and tracks | Mark a slice done that skipped a gate |
| **Reviewer** | Human approval of each slice | Approve without seeing gate results |

One person can hold several roles. On a solo project, one person holds all
four.

### Cadence

| Event | When | Purpose |
| ----- | ---- | ------- |
| Expectation workshop | Once per MEV | Phase 0 |
| Spec sessions | During phase 1 | Write and validate the whole spec set and its ADRs |
| Slice review | Every slice | Gates, review, deploy, track |
| Scope triage | Weekly, or when an idea arrives | Run the filter on spec changes |
| Progress check | Weekly | MEV coverage, forecast, rework |
| Outcome review | End of the validation window | Exit decision and retrospective |

## 17. Edge cases

| Situation | TRACER response |
| --------- | --------------- |
| No metric can be named for the MEV | Not ready for TRACER. Clarify the outcome first, or run an experiment if demand is unknown. |
| A core assumption is risky (an AI capability, a third-party API) | Timeboxed spike in phase 1. Its code is not kept; its result decides the spec and the ADRs. |
| The agent builds something outside the slice | It fails the spec-integrity gate as untraced code. Remove it, or turn it into a spec change and filter it. |
| A scenario turns out to be wrong | Spec change first, then code. Record it in the track as a learning. |
| An ADR turns out to be wrong after several slices | Write the new ADR, run impact analysis on built slices, plan migration slices. Count the cost as spec growth. |
| A slice cannot fit in 3 days (migration, heavy refactor) | Spike for a split. If it is truly atomic, mark it as such and protect it from interruption. |
| The quality floor is not reached (AI accuracy below threshold) | No release. Improve the approach in more slices, or revisit the contract with the outcome owner. |
| Stakeholders want a demo before the MEV | Show the deployed slices; they are real. Never build a separate demo. |
| Work starts on existing code with no specs | Reverse-engineer specs from the code first, curate them, link them, then define the MEV as a delta on top. |
| The metric is reached with *Shoulds* still open | Release anyway. Remaining items go through the filter as post-MEV work. |

## 18. FAQ

**Isn't specifying everything up front just waterfall?**
Waterfall failed by doing three things together: planning everything, freezing
the spec and delivering everything at once. TRACER does only the first. Specs
change through spec changes, and delivery happens slice by slice on a deployed
system.

**Why not start with a proof of concept and grow it into an MVP?**
Agents build for what they are asked. A proof of concept gets a
proof-of-concept architecture, which the MVP then throws away or duplicates.
TRACER's skeleton is as fast to reach as a proof of concept but already has
the final shape.

**What if we learn something that invalidates part of the spec?**
That is expected. It becomes a spec change, goes through the filter, updates
the forecast and is recorded in the track. The spec stays true; it just is not
frozen.

**How long should phase 1 take?**
As long as it takes to give every requirement concrete scenarios, typically 10
to 20% of the MEV's total time. A short phase 1 shows up later as spec growth
and rework.

**Does TRACER require OpenSpec and livespec?**
No. It requires the chain MEV → requirements → scenarios → code → tests →
tracks to stay alive. Those tools are the reference way to keep it.

**Can stakeholders see progress before release?**
Yes. Every slice is deployed, and MEV coverage shows how much of the expected
value is verified.

**What does the agent do, and what do people do?**
Agents write code and tests inside a slice. People own the contract, the spec,
the architecture decisions, the review and the exit decision.

## 19. Adapting TRACER

TRACER says how to build one MEV. It says nothing about which MEV goes first,
or who builds it with how much capacity. Those questions depend on the
organization, and answering them is the job of an adaptation.

An adaptation keeps the invariants, tunes the parameters and adds the rules
its context needs. It never redefines the base method.

### Invariants

The seven principles. An adaptation that breaks one of them is a different
method.

### Tunable parameters

| Parameter | Default | Change it when |
| --------- | ------- | -------------- |
| Slice size | 1 to 3 days | Research-heavy work (up to 5) or very operational work (under 1) |
| Phase 1 share | 10 to 20% of MEV time | High-risk domains need more; well-known domains need less |
| Validation window | 2 to 4 weeks | The metric needs a longer cycle to show |
| Rework threshold | 15% | Stricter in regulated domains |
| Gates | All seven | Never fewer; the tooling per gate is free |

### Common questions adaptations answer

| Context | Typical additions |
| ------- | ----------------- |
| In-house team with shifting priorities | Priority scoring between MEVs; switching only at a slice boundary, never mid-slice; notification rules for internal stakeholders |
| Agency or team serving several clients | Capacity reserved per client; estimating and quoting in slices; time tracking per slice |
| Regulated domain | Extra compliance gate; stricter rework threshold; audit trail built from tracks |

Every adaptation plugs into the same two points of TRACER: the moment to
switch work is the end of a slice, and the unit of work is the slice.

### Writing an adaptation

1. Name the context and the question TRACER leaves open there.
2. List the rules that answer it, and check each against the seven principles.
3. Map its vocabulary to TRACER's: what a slice, an MEV and a gate are called
   there.
4. Set the parameters for that context.
5. Keep it short: an adaptation documents only what it adds.

## 20. Templates

Ready-to-copy templates live in [`../templates`](../templates):

- [Expectation contract](../templates/expectation-contract.md)
- [Requirement with scenarios](../templates/requirement.md)
- [Slice](../templates/slice.md)
- [Scope change](../templates/scope-change.md)
