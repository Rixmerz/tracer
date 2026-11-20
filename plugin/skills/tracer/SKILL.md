---
name: tracer
description: >-
  Work under the TRACER development method: a Minimum Expected Value (MEV)
  seen from the client's side, specified in two rounds (base and empathy),
  then built in 1-3 day slices on the final architecture, each one verified
  through critical end-to-end flows, checked for UI/UX anti-patterns, traced
  to its specs and deployable. Use when the repository has a docs/tracer/
  folder or an MEV spec, when the user mentions TRACER, MEV, slices, tracer
  slices, expectation contract, audience profile, empathy round, critical
  flows or scope filter, or asks to plan, build, verify or review work "the
  TRACER way".
---

# TRACER

This skill is how an agent follows the method, step by step. The handbook
explains the reasons: https://github.com/Rixmerz/tracer/blob/main/docs/method.md.
Templates: `${CLAUDE_PLUGIN_ROOT}/templates/` (copy them; never write them from memory).

The core idea: agree the value the product must deliver, see it from the side
of the people who will use it, specify all of it, then build it in thin
slices that are already final. "Done" means correct for those people, checked
through the interface they use, never just "the tests are green".

## Where things live

Keep TRACER state in the repository, so it survives sessions:

| File | Holds |
| ---- | ----- |
| `docs/tracer/contract.md` | Expectation contract: metric, target, quality floor, audiences, validation window, validator, Must/Should |
| `docs/tracer/audiences.md` | One audience profile per audience |
| `docs/tracer/content.md` | The client's content inventory: every text they gave, literal or free, and the open questions |
| `docs/tracer/decisions.md` | Decision log: one entry per slice, publish or version, with trigger, change, alternative dropped, reason and the version it was based on |
| `docs/tracer/capabilities.md` | The capability map: what the user can do, each entry linked to its requirements |
| `docs/tracer/empathy/<capability>.md` | The empathy review of each capability |
| `docs/tracer/flows/<capability>.md` | Critical flows with success and failure paths and WORKS / CORRECT criteria |
| `docs/tracer/floors.md` | Component floors for this project (start from the template) |
| `docs/tracer/anti-patterns.md` | Anti-pattern catalog for this project (start from the template) |
| `docs/tracer/design-system.md` | The documented design system the product is built on, its style and the brand overlay that adapts it |
| `docs/tracer/identity.md` | Identity guideline chosen from variants |
| `docs/tracer/deferred.md` | Expectations left out on purpose, each with its reason |
| `docs/tracer/slices.md` | Slice plan: status, capability, requirements, flows, rework |
| `docs/tracer/backlog.md` | Post-MEV backlog |
| `docs/tracer/baselines/` | Reference screenshots of each closed slice, at each width of the profile |
| `docs/tracer/retros/` | Retrospectives (`/tracer:retro`) |

Specs and ADRs live wherever the project's spec tool keeps them (OpenSpec
`openspec/` by default). If `docs/tracer/` is missing, the project has not
started TRACER: suggest `/tracer:contract` instead of improvising.

## Rules you never break

1. **Design for the destination.** Never pick a temporary architecture (a
   JSON file instead of the planned database, a stub instead of the planned
   integration) to go faster. If the ADRs do not cover a decision, stop and
   propose an ADR.
2. **No throwaway code.** Build nothing the MEV does not need.
3. **Spec before code.** Any change in behaviour starts as a spec change.
4. **Every slice is deployable** and leaves the system working.
5. **Every slice passes the gates** before it counts as done.
6. **All code is traced.** Every new or changed symbol links to a requirement.
7. **Scope is filtered by the metric.** A new idea enters the MEV only if it
   moves the contract's metric.
8. **See the product from the client's side.** Before writing or building
   anything with an interface, read the audience profile. Never fill an
   unspecified detail with the most common solution you know; write it as an
   expectation and let the outcome owner decide.
9. **Done means correct, not just working.** A slice is done when its critical
   flows pass end to end through the interface, its CORRECT criteria hold for
   its audience, and it shows no catalogued anti-pattern. Never mark your own
   slice done: verification is done by someone else, and a person approves.
10. **Mock first, then straight to the MEV.** Before production code, build a
    mock of the interface with every detail the client expects and iterate
    it until the outcome owner validates it **and** three to five real
    members of each audience complete its critical flows without help in an
    audience test. The sponsor (who commissions) is not the audience (who
    uses): their approval alone never validates a mock. Then development goes from the
    validated mock straight to the MEV: there is no proof of concept and no
    MVP.
11. **The client's words are requirements.** Text the client gave as fixed
    (calls to action, headlines, claims, service names) is shown as given,
    and you never add a statement of fact the client did not provide. A
    missing fact is a question to the client, not text on screen. A request
    for a different tone changes hierarchy, order and design, not the facts.
12. **Not verified is said, never hidden.** If the environment cannot render
    or measure the interface, or forbids it, the slice is "built, not
    verified" and you hand the person the verification request; you never
    report it as done.
13. **Never publish over what you did not read.** Before a publish, push or
    save, check the live version is the one you started from; if not, read
    it and merge.
14. **Every iteration leaves its reason.** Each slice, publish or version
    gets an entry in `decisions.md`.

## Size of the project

A small product (a one-page site, a landing page, an institutional site)
runs the same method in light mode, with the institutional-site profile of
the handbook (section 22): the metric is the right person contacting by the
right channel, the critical flows are the urgent contact from a phone and
checking the credentials, and a slice is a section. Light mode shortens the
documents, never the order: audience profiles and the empathy round come
before the first mock, the client's content is inventoried before any
design, and every slice is verified or declared not verified.

## How to follow the method

### Phase 0 · Expectation contract (`/tracer:contract`)

1. Ask, one question at a time: outcome owner; metric, current value and
   target (no metric means not ready for TRACER); quality floor; validation
   window and validator.
2. **Client content.** Inventory every text the client gave in
   `docs/tracer/content.md` (template `client-content.md`): literal or free,
   where it goes, and the questions for what is missing or cut. A truncated
   source is a question, never something to complete.
3. **Audience profile, for each audience:** who they are, what they are
   trying to get done, what they know and do not know, their words, their
   devices and context, accessibility needs (default WCAG 2.2 AA), what they
   must never see, and the product genre they recognise. Name the sponsor
   and, per audience, three to five representatives (real users, not their
   managers) and the date of the first audience test. If nobody can
   describe the audience, stop: talk to someone who knows them first.
4. MoSCoW list; for each item ask whether it moves the metric. Items that do
   not are *Could* and go to the backlog.
5. Write the contract, the profiles and the content inventory. Wait for sign-off.

### Phase 1 · Complete spec (`/tracer:contract`, then `/tracer:empathy`)

1. **Base round.** Write every MEV requirement with WHEN/THEN scenarios: what
   is sought, from the request and the contract.
2. **Capability map.** Group the requirements by what the user can do.
   Before adding a capability, search the existing ones (livespec
   `search_similar` over specs and code). If one already covers it, extend it.
3. **Empathy round.** For every capability, through its audience profile:
   - What are they trying to get done, in their words?
   - What do they know, and what do they not?
   - Where would they get stuck or frustrated?
   - What do they take for granted?
   - What has the product genre taught them to expect?

   List the expectations you find and classify each: **basic** (its absence
   makes the product feel broken), **performance** (more is better) or
   **differentiator** (not expected, valued). Propose them as a list for the
   outcome owner to accept or reject; do not decide silently.
4. **Apply the MEV rule.** For each capability in the cut: every basic
   expectation enters; performance expectations enter if they move the
   metric; the product carries at least one deliberate differentiator.
   Everything else goes through the scope filter or to `deferred.md` with its
   reason.
5. **Improve and add specs** from the accepted expectations. Mark each one as
   born in the empathy round.
6. **Critical flows.** For every capability, write at least one flow a person
   from its audience makes through the real interface, with its success path
   and its failure paths (invalid input, network or server error, no
   permission, empty data, and any domain-specific one). Every criterion has
   two halves:
   - **WORKS:** the technical result (stored, status, record).
   - **CORRECT:** what the person sees and can do, line by line, each line
     checkable. A CORRECT line you cannot check is badly written: rewrite it.
7. **Component floors.** List the components each capability uses and copy
   their floors from `floors.md`, tuned to the audience.
8. **Design system and identity.** Choose the base with
   `/tracer:design-system`: a documented design system from the design
   catalog (or the company's own documented one), never one invented for the
   project. For the screens that define the product, produce two or three
   variants as brand overlays of that base, test them as sketches with each
   audience's representatives (template `audience-test.md`), let the
   outcome owner choose among those the audience could use, and
   record the choice in `design-system.md` and `identity.md`. A look
   asked for by the client (a law firm's, a hotel's) is a style from the
   catalog worn as an overlay, never an aesthetic invented for the occasion,
   and `identity.md` names where each choice comes from in the client's
   world. Check the variants with `check_genericity`.
9. **ADRs** for the destination: data model, persistence, integrations,
   deployment.
10. **Validate strictly:** no requirement without a scenario, no scenario
    without an observable outcome, no capability without a critical flow, no
    uncheckable CORRECT line. With livespec: `sync_openspec`, then
    `validate_openspec`.
11. **Slice plan:** the skeleton first, then slices of 1 to 3 days, each on
    one capability. Forecast: slice count × 2 days, as a wide range.

### Audience gate (blocking)

Before writing any production interface code (the skeleton's screens or any
slice), check, for every audience whose screens you will touch, that
`docs/tracer/audience-tests/` holds a test of the current mock with result
**met**, or that `docs/tracer/decisions.md` holds a **waiver** signed by the
outcome owner covering that audience and those screens (template
`decision-log.md`). If neither exists, **stop**: say which audience and
screens are blocked and ask for a test or a waiver. Never infer one from
"the client approved the mock", a deadline, or silence, and never write the
waiver yourself: you draft it, a person signs it.

### Phase 2 · Skeleton

One flow end to end on the final architecture: real database, real
deployment, CI, tests and gates, including the end-to-end runner that drives
the interface for critical flows.

### Phase 3 · Slices (`/tracer:slice`)

**Ready** only when: its requirements are validated and went through the
empathy round; it lands on a capability and duplicates none; its audience,
critical flows and inherited floors are written; it needs no new
architecture; it fits in 1 to 3 days.

**Build:**

1. Read the audience profile, the flows, the floors, `design-system.md` and
   `identity.md` first. Use the base system's components and tokens.
2. Turn scenarios and critical flows into failing tests: unit and integration
   for the WORKS halves, interface-driven end-to-end tests for the flows and
   their CORRECT halves.
3. Implement until they pass. Touch only what the slice needs; anything else
   goes to `/tracer:scope`.
4. Link code and tests to requirements (`@spec:`).
5. Self-check against the anti-pattern catalog before handing over,
   including `check_genericity` on each page and a check that every selector
   you wrote matches an element of the render.
6. Before publishing, compare the live version with the one you read
   (rule 13), then write the decision-log entry.

**Gates** (all nine, each with evidence):

| Gate | How |
| ---- | --- |
| Scenario tests | The slice's tests pass |
| Critical flows | Every flow it touches passes end to end through the interface, success and failure paths, CORRECT lines included |
| Regression | Full suite and all earlier critical flows pass |
| Spec integrity | livespec `audit_coverage`: no untraced code, no requirement without a scenario |
| Impact | livespec `git_diff_impact`; explain anything unexpected |
| UI and anti-patterns | Layout and accessibility inspection, component floors, rendered text scanned for ids and paths, walkthrough as the audience |
| Static quality | Duplication, complexity, vulnerabilities and secrets within limits |
| Quality floor | The contract's thresholds still hold |
| Human review | A person approves, with the gate results in front of them |

The critical-flow and anti-pattern gates are run by a **verifier who is not
the builder** (`/tracer:verify`, or a separate agent or person), working from
the specs, profiles and catalogs, never from the builder's report. A failed
gate sends the slice back and counts as rework.

**Close:** mark it done with cycle time and rework, store its visual
baseline (screenshots at each width of the profile in
`docs/tracer/baselines/<slice>/`), record its track, report MEV coverage and
the updated forecast. The next slice compares its screens against the
baselines of the slices it touches.

### Phase 4 · Scope control (`/tracer:scope`)

Every new idea or correction becomes a spec change, is tested against the
metric, sized and decided by the outcome owner.

### Phase 5 · Release

Release, run the validation window, measure the metric, take the exit
decision.

### Learning loop

Whenever a basic expectation or an anti-pattern is found after a slice was
marked done: reopen it as rework, add the missing CORRECT line to its spec,
and add the cause to `floors.md`, or to `anti-patterns.md` under the
principle it breaks, so it cannot escape again. Count it as an escaped expectation.

## Without the plugin

The method does not need the plugin. When its tools are missing, say once
which ones, and keep going by hand:

| Needs the plugin or its servers | Works in any agent |
| --- | --- |
| Commands (`/tracer:*`) | The same steps, read from this skill or the handbook |
| livespec links and audits | Requirement ids written next to the code and in the slice, checked by hand |
| layout-inspector measures | The verification request (`verification-request.md`) handed to the person, and the visual rubric (`visual-rubric.md`) for a separate verifier reading screenshots |
| `tracer-design-catalog` tools | `catalog/systems.json` and `styles.json` read directly; contrast computed by script |
| | Contract, profiles, content inventory, empathy reviews, flows, decision log: markdown files in the repository, or in the artifact when there is no repository |

When the host forbids rendering or checking the result (some artifact
types do), that rule wins, and the slice is "built, not verified": say so and
hand over the verification request with each publish. Ask the person whether
a render check may be run; their permission lifts the host's rule for that
slice.

## Briefing an orchestrator or another agent

When you hand a slice to another agent or an orchestrator, its brief carries
the audience profile, the critical flows with their WORKS and CORRECT lines,
the inherited floors, the anti-pattern catalog, `design-system.md` and `identity.md`. Its
acceptance criteria are the CORRECT lines and the flows, not only the test
command. Tests passing is necessary and never sufficient.

## The design catalog

The plugin's `tracer-design-catalog` server answers from a catalog of
documented design systems (owner, documentation, packages and licenses read
from the npm registry) and of visual styles (traits, accessibility risks and
the systems that carry them): `search_design_systems`, `get_design_system`,
`search_styles`, `get_style`, `design_system_brief`, `check_overlay`,
`check_contrast` and `check_genericity` (the traits of the "Identity, not
template" family in a page's HTML and CSS). A style is never a design system: it is a brand overlay on
one. An overlay only changes what its base defines, and never weakens focus,
contrast, target size, labels, motion or error behaviour.

## Traceability with livespec

livespec is installed with this plugin:

- Cold open per repo: `index_project`, then `get_project_overview`.
- With `openspec/`: `sync_openspec` before reading specs, `validate_openspec`
  after editing them.
- Duplicate capabilities: `search_similar` before adding one.
- Links: `@spec:` annotations in code and tests (livespec's `agent_playbook`).
- Before review: `git_diff_impact` for impact, `audit_coverage` for integrity
  and MEV coverage.

If livespec is not available, say so once and keep the chain by hand.

## Reporting progress

Report MEV coverage, slices done and remaining, likely and safe forecast
dates, rework rate, change fail rate, escaped expectations, empathy yield and
any untraced code.

## Commands

| Command | Phase | Does |
| ------- | ----- | ---- |
| `/tracer:contract` | 0-1 | Contract, audience profiles, base round, capability map, ADRs, slice plan |
| `/tracer:empathy` | 1 | Empathy round on one capability or all: expectations, improved and new specs, critical flows |
| `/tracer:slice` | 3 | One slice: ready check, test-first build, gates, track |
| `/tracer:verify` | 3 | Independent verification: critical flows, CORRECT lines, floors and anti-patterns |
| `/tracer:scope` | 4 | Runs an idea or correction through the scope filter |
| `/tracer:team` | 3 | Teams adaptation: assignment, checks, relay, speed or balance |
| `/tracer:retro` | any | Retrospective from the decision log and the history; its lessons become floors and catalog entries |
