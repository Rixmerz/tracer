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

A second failure hides behind the first. Agents are very good at producing
work that *looks* finished: tests are green, the pipeline passes, the screen
renders. Yet a navigation bar ships without icons or keyboard support, a file
picker asks a non-technical user for a full CDN path, and files are listed by
UUID instead of by name. Nobody asked for those things to be right, because
nobody thought they needed asking. An agent fills every gap with the most
common solution it has seen, an orchestrator verifies only what was written,
and the last 10% that separates "works" from "correct for the people using
it" never happens.

The problem is not only how tasks are written. It starts earlier: between an
informal request ("a training platform", "a navbar") and the task, no step
makes explicit what the client takes for granted.

TRACER keeps the good half of each approach. From specification-first
development it takes knowing the destination before building. From iterative
development it takes small, verified steps. What it drops is throwaway code
and big-bang delivery. And it adds what neither had: the product is seen from
the client's side before it is specified, and "done" means correct for that
client, checked through the interface they will actually use.

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

Ten rules that cannot be negotiated away. Drop any of them and it is no
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
8. **See the product from the client's side.** Every capability is specified
   twice: once for what is sought, once for how the people using it will live
   it. What they take for granted is written down, never assumed.
9. **Done means correct, not just working.** A slice is done when its critical
   flows pass end to end through the real interface, its correctness criteria
   hold for its audience, and it shows none of the known anti-patterns.
10. **Mock first, then straight to the MEV.** Before any production code, the
    interface is built as a mock with every detail the client expects. The
    mock is iterated until the outcome owner validates it as what they
    expect. Only then does the definitive development start, and it goes
    from the validated mock straight to the MEV. There is no proof of
    concept and no MVP in between.

## 7. Vocabulary

The rest of this document uses these terms. Most have already appeared; this
is the reference list.

| Term                     | Definition |
| ------------------------ | ---------- |
| **MEV**                  | Minimum Expected Value: the smallest scope that delivers the expected outcome (section 2). |
| **Expectation contract** | The written definition of the MEV's success: metric, current value, target, quality floor, audience profile, validation window and who validates it. |
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
| **Audience profile**     | Who uses the system: their goals, what they know and do not know, their words, devices, accessibility needs, and what they must never see. Part of the contract. |
| **Base round**           | The first round of specs: what is sought, from the request and the contract. |
| **Empathy round**        | The second round of specs: every capability re-read as its audience lives it, producing improved and new specs. |
| **Expectation**          | Something the audience takes for granted or wants from a capability, classified as basic, performance or differentiator (section 9). |
| **Component floor**      | The minimum a kind of interface component must provide for a given audience: a navbar, a file picker, a table, a form. |
| **Capability map**       | The spec set organized by what the user can do, used to stop the same capability from being built twice. |
| **Critical flow**        | One user journey through the real interface, from the front end to the API and back, with its success path and its failure paths. |
| **Works / Correct**      | The two halves of every acceptance criterion: *works* is the technical result; *correct* is what the audience must see and be able to do. |
| **Anti-pattern**         | Something an interface must not show or do, even if no requirement forbids it. Kept in a shared catalog. |
| **Deferred list**        | Expectations left out of the MEV on purpose, each with its reason. |

## 8. Defining the MEV

An MEV is defined in six steps. Together they form the expectation contract.

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

The quality floor is a set of numbers. It cannot say that files must be
listed by name or that a navbar needs icons; those expectations come from the
audience profile and the empathy round (section 9).

### 8.4 The audience profile

Who will use the system, written before any spec:

- **Who they are** and what they are trying to get done.
- **What they know and do not know.** A human resources team does not know
  what a CDN, a UUID or an endpoint is.
- **Their words.** The labels and terms the interface must use.
- **Their context:** devices, frequency of use, connection, time pressure.
- **Accessibility needs,** with WCAG 2.2 AA as the default floor.
- **What they must never see:** internal identifiers, file paths, stack
  traces, technical jargon.
- **The product genre** the system belongs to (a learning platform, a store,
  a back office) and the conventions people bring from it.

If a system has several audiences (learners and administrators), write one
profile each. Every capability later names the audience it serves.

### 8.5 The validation window

How long the MEV runs in production before the metric is measured. Usually 2
to 4 weeks.

### 8.6 The exit decision

Decided in advance, applied at the end of the window:

| Result         | Decision |
| -------------- | -------- |
| Target reached | Close the MEV. Post-MEV items become a new MEV if they justify one. |
| Partly reached | Open a new MEV focused on the gap. |
| Not reached    | Stop, record what was learned, and decide whether to retire the feature. |

## 9. Seeing the product from the client's side

An informal request is a valid starting point. Nobody has to write a formal
product document first. TRACER's job is to turn that request into specs that
hold what the client meant, including what they never said.

### Three layers of every request

| Layer | What it holds | Example: "a training platform" |
| ----- | ------------- | ------------------------------ |
| **Explicit** | What was said | Upload training material, assign it to people |
| **Implicit** | What any member of the audience expects without asking | Find a file by its title, see a preview, real file names, no URLs |
| **Latent** | What the owner has in mind but did not say | Brand identity, plans for certificates next year |

Tasks written from the explicit layer alone produce work that looks finished
and is not. An agent fills the implicit layer with the most common solution
it has seen, whether it fits this audience or not. The two rounds of specs
exist to make the implicit and latent layers explicit before any code is
written.

### 9.1 Round one: the base

The first round writes what is sought: every capability the MEV needs, with
its business rules and scenarios, taken from the request and the contract.
This is the spec set as TRACER has always written it.

### 9.2 Round two: empathy

The second round reads every capability again, through the audience profile.
For each one, answer:

1. **Who** uses it, from which profile.
2. **What they are trying to get done,** in their words.
3. **What they know and what they do not.**
4. **Where they would get stuck or frustrated.**
5. **What they take for granted.**
6. **What the product genre has taught them to expect.**

The answers produce two kinds of output:

- **Improved specs:** existing requirements gain scenarios and correctness
  criteria. "Upload material" becomes: the file keeps its real name, shows a
  thumbnail, can be picked by title, and no URL is ever shown or asked for.
- **New specs:** capabilities the base round missed entirely, such as search
  over the material list or an empty state that explains what to do first.

Every spec born in this round is marked as such, so the round's yield can be
measured (section 18).

The agent proposes; the outcome owner decides. An AI agent knows the average
product of a genre very well, and that knowledge is useful here as a list to
accept or reject item by item, instead of a decision the agent makes silently
while coding.

### 9.3 Expectation levels

Each expectation found in round two is classified, following the Kano model:

| Level | Meaning | Absence | Examples |
| ----- | ------- | ------- | -------- |
| **Basic** | Taken for granted | The product feels broken, even if nobody asked | Icons with labels, real file names, previews, keyboard use, clear errors |
| **Performance** | More is better | Users are less satisfied | Speed, filters, bulk actions |
| **Differentiator** | Not expected, valued when present | Nothing; it is what makes the product its own | A distinctive visual identity, a well-judged shortcut |

**The MEV rule:** for every capability inside the cut, the MEV includes all of
its basic expectations, the performance expectations that move the metric,
and at least one deliberate differentiator for the product as a whole.

Basic expectations are not scope creep. They are part of the capability
itself: a file list without a way to find a file is not a smaller file list,
it is a broken one.

### 9.4 Component floors

Interface components repeat across products, and so do their minimum
expectations. TRACER keeps a catalog of component floors, tuned per audience.
Two examples:

- **Navigation bar:** icons with text labels, a visible active section,
  full keyboard use, landmarks and accessible names, a collapsed version on
  small screens.
- **File picker or file list:** search by title, real names (never storage
  keys), a thumbnail or type icon, size and date, an empty state, clear
  upload errors.
- **Buttons and actions:** common actions carry a recognizable icon next to
  their label, because people find an icon faster than they read a word;
  icon-only buttons only for universal icons, with a tooltip and an
  accessible name; one icon keeps one meaning across the product.

A slice that builds or changes a component inherits its floor. The catalog
grows every time an expectation is discovered late (section 18).

### 9.5 The capability map

Organize the spec set by what the user can do ("find training material",
"track a learner's progress"), not by screens or modules. Every new task must
land on a capability:

- If the capability exists, the task extends it.
- If it does not, the task creates it, through a spec change.

This is what stops the same function from being built twice in two places,
which is a duplication of behaviour, not of code, and which code-level
duplicate detection does not catch.

### 9.6 Identity and variants

The differentiator is where taste lives. For the screens that define the
product, generate two or three variants before committing to one, compare
them side by side, and record the choice as an identity guideline (palette,
type, tone, motion). Later slices follow the guideline instead of returning
to the average.

### 9.7 The deferred list

Every expectation left out of the MEV goes to a deferred list with its
reason. Leaving something out on purpose and forgetting it look the same in
the code. They must not look the same in the spec.

## 10. Critical flows and correctness

APIs are rarely where products fail. They are usually documented, tested and
working. The real failures appear where the interface ties the parts
together: a flow that technically completes but leaves the user lost, a
screen that renders data the user cannot read, an error that is swallowed.
That is why TRACER validates flows, not only functions.

### 10.1 Critical flows

Every capability has at least one **critical flow**: a journey a person from
its audience makes through the real interface, from the front end through the
API to the data and back to what the person sees.

- It is tested end to end, by driving the interface the way a person would.
- It asserts what the person sees and can do, not what a function returns.
- It runs against the deployed or production-like system, with real
  persistence.

### 10.2 Success and failure paths

Each critical flow has its success path and its failure paths. For each
failure, the spec states what the person must see and how they recover:

| Failure | The person must see |
| ------- | ------------------- |
| File too large or wrong format | Which limit was hit and what is allowed, before the upload is lost |
| Network or server error | That it failed, that nothing was saved twice, and a way to retry |
| No permission | Why, in their words, and who can grant it |
| Empty data | What this screen is for and the first action to take |

**A failure path with no clear message and no way out is a failed test,**
even if the API returned the right status code.

### 10.3 Works and correct

Every acceptance criterion is written in two halves:

- **Works:** the technical result. *The file is stored and the API returns
  201.*
- **Correct:** what the audience must see and be able to do. *The file
  appears under its real name with a thumbnail, can be found by searching its
  title, can be selected with the keyboard, and a screen reader announces it.*

Something can work and still be incorrect. The *correct* half is written with
care, line by line, because it is the half agents and orchestrators skip and
the half the verifier enforces. A *correct* criterion that cannot be checked
is badly written and goes back to the empathy round.

## 11. UI/UX anti-patterns

Validations check what must happen. Anti-patterns catch what must not exist,
even though no requirement forbids it. TRACER keeps a shared catalog, and
every slice with an interface is checked against it. Its core entries:

| Anti-pattern | Example |
| ------------ | ------- |
| Internal data on screen | UUIDs, storage keys, database ids, file paths, stack traces |
| Asking for what the system knows | A field asking for a URL or an id the system already holds |
| Lists without a way in | No search, no preview, no sorting, no empty state |
| Icons without labels, or text without hierarchy | An icon-only navbar; a wall of same-weight text |
| Destructive actions without a net | Delete with no confirmation and no undo |
| Errors that explain nothing | "Something went wrong" with no cause and no next step |
| The same action solved two ways | Uploading a file works differently on two screens |
| Inaccessible controls | No keyboard focus, missing accessible names, contrast below WCAG AA, targets too small |
| Jargon in the interface | Technical terms the audience profile says they do not know |
| Silent states | No loading, success or error feedback |
| Words where a picture reads faster | A toolbar of text-only buttons; a status written as plain words; a table of numbers where a chart would show the trend |
| State shown only by color | A red or green dot with no icon, shape or text |
| Interface built on data nobody provides | A "used in" count or a delete lock that depends on a field no API fills |
| Work lost by moving on | Switching a tab cancels an upload in progress without a warning |
| Changes out of sight | "Add row" appends the row off screen and the view stays where it was; saving a field reloads the whole page |
| Information the audience cannot read | A "JSON" tab in a form used by human resources; a download of raw records for a sales team |

Part of the catalog can be checked automatically: layout and accessibility
inspection, reading the rendered text for internal identifiers. The rest is
checked by the verifier, walking the interface as the audience would. Every
anti-pattern found after a slice was marked done joins the catalog, so the
method improves from one project to the next.

## 12. Lifecycle

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

Agree the metric, target, quality floor, audience profile, validation window
and validator.

**Exit:** a signed-off contract.

### Phase 1 · Complete spec

1. **Base round:** write every MEV requirement, each with at least one
   scenario (section 9.1).
2. **Empathy round:** read every capability through the audience profile;
   improve the specs, add the missing ones, classify expectations and apply
   the MEV rule (sections 9.2 and 9.3). Record the deferred list.
3. **Organize by capability** and check the map for duplicated behaviour
   (section 9.5).
4. **Write the critical flows** of each capability, with success and failure
   paths and *works / correct* criteria (section 10).
5. **Fix the identity** of the defining screens through variants (section
   9.6).
6. **Build the mock and get it validated.** A clickable mock of every screen,
   with all the details the client expects: real wording, states, empty and
   error cases, the anti-pattern catalog already applied. Iterate it with the
   outcome owner until they confirm it is what they expect. The mock is the
   reference the slices are verified against; it is not grown into the
   product.
7. Record the architecture decisions as ADRs for the destination: data model,
   persistence, integrations, deployment.
8. Validate the spec set strictly: no requirement without a scenario, no
   scenario without an observable outcome, no capability without a critical
   flow, no *correct* criterion that cannot be checked.
9. Order the requirements into a slice plan: which flow goes into the
   skeleton, which slices follow.

**Exit:** a validated spec set, its critical flows, its ADRs and the mock,
all signed off by the outcome owner. No code yet, except a timeboxed
spike when a risky assumption must be checked first.

### Phase 2 · Skeleton

One flow, end to end, on the final architecture: real database, real
deployment, CI, test harness and validation gates wired up, including the
end-to-end runner that drives the interface for critical flows.

**Exit:** the skeleton is deployed and its scenarios pass.

### Phase 3 · Tracer slices

Each slice takes a few requirements from the plan, turns their scenarios into
tests, has the agent implement them, passes the gates, links the code to the
specs and records its track.

**Exit per slice:** deployed and traced.
**Exit for the phase:** MEV coverage reaches 100%.

### Phase 4 · Scope control

Runs in parallel with phase 3. See section 15.

### Phase 5 · MEV release

Release, run the validation window, measure the metric and take the exit
decision.

## 13. Slices

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

- Its requirements exist in the validated spec set, each with scenarios, and
  have been through the empathy round.
- It lands on a capability in the capability map; no existing capability
  already covers it.
- Its audience is named, and its critical flows are written with success and
  failure paths and *works / correct* criteria.
- The component floors it inherits are listed.
- It builds on the skeleton or on earlier slices. No new architecture appears
  inside a slice.
- Its validation gates are known.
- Its target is confirmed: the repository, the screen and, for any external
  action that cannot be undone (a ticket, a release, a deletion), its exact
  destination. Never copied from an earlier task.
- Its test environment runs: the full suite runs on the base commit, and the
  tests that already fail there are recorded, so no later red is guessed.

### Definition of Done

- Every scenario it covers has a passing test.
- Every critical flow it touches passes end to end through the real
  interface, success and failure paths alike.
- Every *correct* criterion was verified as its audience would experience it,
  not only every *works* criterion.
- It meets the floors of the components it builds and shows none of the
  catalogued anti-patterns.
- It passed every validation gate, with one clean full run of the suite
  after the last change.
- A person reviewed and approved the change.
- It is deployed and the system still works.
- Its code is linked to its specs, and its track is recorded with the reason
  for each change.

### Inside the slice

Extreme Programming practices: test-first from the scenarios, continuous
integration, small commits, collective code ownership, and pair programming
(human with human, or human with agent) on risky work.

The agent writes the code. A person owns the result.

## 14. Validation gates

Gates are what make TRACER fast without being reckless: every slice is checked
as it lands, so errors never pile up until the end.

| Gate               | Checks | Typical tooling |
| ------------------ | ------ | --------------- |
| **Scenario tests** | Every scenario in the slice passes | Unit, integration and end-to-end tests generated from WHEN/THEN |
| **Critical flows** | Each flow the slice touches passes end to end through the interface, on its success and failure paths, with its *correct* criteria | Browser-driven end-to-end tests against a production-like system |
| **Regression**     | Earlier slices and their critical flows still pass | Full test suite in CI |
| **Spec integrity** | No requirement without a scenario; no new code without a linked spec | Spec validator, traceability audit |
| **Impact**         | What else the change touches | Call-graph and diff impact analysis |
| **UI and anti-patterns** | Layout, responsiveness, accessibility, component floors and the anti-pattern catalog | Layout and accessibility inspection, rendered-text scans for internal identifiers, a walkthrough as the audience |
| **Static quality** | Duplication, complexity, known vulnerabilities and leaked secrets stay within limits | Duplicate detection, cyclomatic complexity, dependency and secret scanners |
| **Quality floor**  | The MEV's thresholds still hold: accuracy, performance, cost per use | Benchmarks on real samples |
| **Human review**   | A person approves the change | Pull request review |

A team chooses its own tools for each gate; the gates themselves are fixed. A
slice that fails a gate goes back to implementation, and the failure counts as
rework.

**The verifier is not the builder.** The agent that built a slice already
believes it is right. The critical-flow and anti-pattern gates are run by a
separate agent or person, working from the specs, the audience profile and
the catalogs, never from the builder's report. A builder's claim of success is
not evidence.

**Evidence must show the target.** A screenshot of the login page, a measure
of the wrong screen or a run in the wrong project proves nothing. Every piece
of evidence names the screen, the signed-in audience and the data it ran on.

### Testing anti-patterns

A green run can still be a false one. The catalog keeps a second list for
tests, checked with the gates:

| Anti-pattern | Example |
| ------------ | ------- |
| A red explained away | Timeouts blamed on machine load, or failures called pre-existing, with no run on the base commit |
| Done without a clean full run | Committing after a partial suite or one that ended in timeouts |
| Evidence of the wrong target | Layout measured on the unauthenticated login page instead of the screen in the slice |
| Fixtures that hide the contract | Tests pass on a field the real API never returns |
| Tests that leak the machine | A test passes only because a binary or path exists on the author's machine |
| Only the happy path | Nothing interrupts, cancels or repeats the operation |
| Claims from reading code | "It already works there" without running it where the audience uses it |
| Broken test setup | A test module configured twice; tests that pass only in one order |

The rule behind them: a failure is only pre-existing if it also fails on the
base commit, and a slice is only done after one clean full run.

## 15. Scope control during delivery

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

## 16. Traceability

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

## 17. Forecasting

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

## 18. Metrics

| Metric | What it measures | Healthy signal |
| ------ | ---------------- | -------------- |
| **MEV coverage** | Verified scenarios ÷ all MEV scenarios | Rises every week |
| Cycle time per slice | Days from start to deployed | 3 days or less, 85% of the time |
| Rework | Slices that failed a gate | Under 15% |
| Untraced code | Changed code with no linked spec | Zero at release |
| Drift | Specs whose linked code changed without a spec change | Resolved within the slice |
| Spec growth | Slices at release ÷ slices planned in phase 1 | Under 1.3 |
| Throwaway | Code deleted because it was built for a temporary shape | Zero |
| Change fail rate | Deployed slices that caused a failure in production | Low and falling |
| Deployment rework rate | Deployed work that had to be redone because it was wrong for its users, broken down by expectation level | Under 10%, near zero for basic expectations |
| Escaped expectations | Basic expectations or anti-patterns found after a slice was marked done | Zero; each one joins a catalog |
| Empathy yield | Specs improved or added by the empathy round ÷ base specs | Above zero; a yield of zero means the round was skipped |
| Outcome | The MEV metric after the validation window | Target reached |

Throughput (how fast slices close) and stability (how often they fail or come
back) are read together. Agents raise throughput easily; only stability shows
whether what they built was right.

### Calibration

- **Rework above 15%:** scenarios are too vague or slices too big. Tighten
  both.
- **Spec growth above 1.3:** phase 1 was too shallow. Spend longer on
  scenarios and spikes.
- **Cycle time above 3 days:** split slices further.
- **Any throwaway:** an architecture decision was skipped. Add the missing
  ADR.
- **Escaped expectations or rework on basic expectations:** the empathy round
  or the floors were too shallow. Add what escaped to the component floors or
  the anti-pattern catalog, and re-run the empathy round on the capabilities
  it touched.
- **Change fail rate rising:** critical flows miss failure paths. Add them.

## 19. Roles and cadence

### Roles

| Role | Owns | Does not |
| ---- | ---- | -------- |
| **Outcome owner** | The expectation contract, the audience profile, the cut, scope decisions, the exit decision | Add scope without passing the filter |
| **Spec lead** | The spec set in both rounds, critical flows, ADRs, the slice plan, spec integrity | Let code change behaviour before the spec does |
| **Builders** (people and their agents) | Slices, tests, links and tracks | Mark a slice done that skipped a gate |
| **Verifier** (a person or a separate agent) | Critical flows, *correct* criteria and the anti-pattern check, walked as the audience | Verify their own work, or accept the builder's report as evidence |
| **Reviewer** | Human approval of each slice | Approve without seeing gate results |

One person can hold several roles, except that no one verifies their own
slice. On a solo project, one person holds every role and a separate agent
acts as verifier.

### Cadence

| Event | When | Purpose |
| ----- | ---- | ------- |
| Expectation workshop | Once per MEV | Phase 0 |
| Spec sessions | During phase 1 | Write the base round, the empathy round, critical flows and ADRs; validate them |
| Slice review | Every slice | Gates, independent verification, review, deploy, track |
| Catalog update | Whenever an expectation escapes | Add it to the component floors or the anti-pattern catalog |
| Scope triage | Weekly, or when an idea arrives | Run the filter on spec changes |
| Progress check | Weekly | MEV coverage, forecast, rework |
| Outcome review | End of the validation window | Exit decision and retrospective |

## 20. Edge cases

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
| Nobody can describe the audience | Not ready for TRACER. Talk to someone from the audience, or to whoever serves them, before the empathy round. |
| A task duplicates an existing capability | Extend the capability instead. If the two must differ, the difference is a spec change and goes through the filter. |
| A slice works but is found incorrect after it was marked done | Reopen it as rework, add the missing *correct* criterion to its spec, and add the cause to a catalog so it cannot escape again. |
| The empathy round produces more than the MEV can hold | Basic expectations of capabilities in the cut stay. Everything else goes through the filter or to the deferred list. |
| An orchestrator marks tasks done on tests alone | Give it the critical flows, *correct* criteria and catalogs as its acceptance criteria, and run the verification gates with a separate verifier. |

## 21. FAQ

**Isn't the empathy round just scope creep?**
No. Basic expectations are part of a capability, not additions to it: a file
list nobody can search is broken, not small. Performance expectations and
new ideas from the round still pass the scope filter, and what does not enter
goes to the deferred list with its reason.

**Why validate through the interface when the API is already tested?**
Because that is where products fail. An API can return the right data while
the screen shows a UUID, hides the error or traps keyboard users. The user
only ever meets the interface.


**Isn't specifying everything up front just waterfall?**
Waterfall failed by doing three things together: planning everything, freezing
the spec and delivering everything at once. TRACER does only the first. Specs
change through spec changes, and delivery happens slice by slice on a deployed
system.

**Why not start with a proof of concept and grow it into an MVP?**
Agents build for what they are asked. A proof of concept gets a
proof-of-concept architecture, which the MVP then throws away or duplicates.
TRACER's skeleton is as fast to reach as a proof of concept but already has
the final shape. What a proof of concept is usually asked to show, how the
product will look and behave, is settled by the mock instead: once the client
validates it, development goes from the mock straight to the MEV, with no
proof of concept and no MVP.

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

## 22. Adapting TRACER

TRACER says how to build one MEV. It says nothing about which MEV goes first,
or who builds it with how much capacity. Those questions depend on the
organization, and answering them is the job of an adaptation.

An adaptation keeps the invariants, tunes the parameters and adds the rules
its context needs. It never redefines the base method.

### Invariants

The ten principles. An adaptation that breaks one of them is a different
method.

### Tunable parameters

| Parameter | Default | Change it when |
| --------- | ------- | -------------- |
| Slice size | 1 to 3 days | Research-heavy work (up to 5) or very operational work (under 1) |
| Phase 1 share | 10 to 20% of MEV time | High-risk domains need more; well-known domains need less |
| Validation window | 2 to 4 weeks | The metric needs a longer cycle to show |
| Rework threshold | 15% | Stricter in regulated domains |
| Gates | All nine | Never fewer; the tooling per gate is free |

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
2. List the rules that answer it, and check each against the ten principles.
3. Map its vocabulary to TRACER's: what a slice, an MEV and a gate are called
   there.
4. Set the parameters for that context.
5. Keep it short: an adaptation documents only what it adds.

## 23. Templates

Ready-to-copy templates live in [`../plugin/templates`](../plugin/templates):

- [Expectation contract](../plugin/templates/expectation-contract.md)
- [Requirement with scenarios](../plugin/templates/requirement.md)
- [Slice](../plugin/templates/slice.md)
- [Scope change](../plugin/templates/scope-change.md)
- [Audience profile](../plugin/templates/audience-profile.md)
- [Empathy review](../plugin/templates/empathy-review.md)
- [Critical flow](../plugin/templates/critical-flow.md)
- [Component floors](../plugin/templates/component-floors.md)
- [Anti-pattern catalog](../plugin/templates/anti-patterns.md)
