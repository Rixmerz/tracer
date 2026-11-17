# Adaptation: teams, responsibility and relay

TRACER says how to build one MEV. This adaptation answers who builds each
piece, with how much load, and what happens when someone does not get there
in time. It keeps the ten principles and plugs into TRACER at the same two
points as every adaptation: the unit of work is the slice (here, a card of a
slice), and the moment to change the rules is the end of a slice or sprint.

## 1. The problem

- A card is late and wrong, and nobody could act early: the delay is seen
  at the deadline.
- Methods measure a card's complexity, never its responsibility. A two-hour
  change to how a charge is computed is treated as lighter than a large
  feature nobody depends on.
- People are paid partly for the responsibility of their role, yet nothing
  stops a team from loading them with responsibility their role does not
  hold.
- Fatigue is not modelled. Whoever finishes early gets more work, and
  finishing again brings more; with AI agents speeding up the output, this
  loop is faster and the wear is greater.
- Speed comes from keeping people on the repositories they know, and that
  same concentration means one absence stops the team.

## 2. Two measures per card

| Measure | Question | Scale |
| --- | --- | --- |
| **Complexity (C)** | How much work is it? | Hours or points, as the team already estimates |
| **Responsibility (R)** | How much harm if it is late or wrong? | 1 to 5, from the rubric |

**Responsibility rubric.** R is the **highest** of these factors, not their
average: one critical factor makes the card critical.

| Factor | 1 | 3 | 5 |
| --- | --- | --- | --- |
| Money or operation | None | A team's work slows | Revenue, billing or operation stops |
| People affected | Internal, few | One client segment | All clients, or vulnerable people |
| Legal or data | None | Personal data read | Personal data written, legal or regulatory duty |
| Reversibility | Undone in minutes | Undone with effort | Cannot be undone |
| Blocks others | Nobody | One team | Several teams or a release |

R is set by the outcome owner (PO) and the technical lead (LT) together,
never by whoever executes the card, so it is not inflated or deflated.

## 3. Repositories

Each repository has a profile (template: [repository profile](../../plugin/templates/team/repository-profile.md)):

- **Repository complexity (K_repo):** a multiplier on the work of any card
  that touches it: size, coupling, test coverage, documentation.
- **Repository responsibility (R_repo):** a floor for R. A trivial change in
  the payments repository is never R1. Critical zones inside a repository
  may carry their own floor.

For a card:

- **Effective R** = max(card R, R_repo of every area it touches).
- **A card over several repositories:** effective R is the highest; its
  complexity is the sum, plus an integration factor (default +20 %).

## 4. Card types

How much is known changes how the card is estimated, checked and assigned:

| Type | The card says | Uncertainty | Delivers |
| --- | --- | --- | --- |
| **Execution** | "Apply this change in X" | Low | Code and tests |
| **Diagnosis** | "This fails; find why" | Medium | The cause, shown, and its fix |
| **Analysis** | "Y must be solved; how is unknown" | High | A proposal with alternatives: the spec of the next card |
| **Exploration** | "New repository or technology" | Very high | A map of the ground and its risks |

**Analysis and exploration are timeboxed and deliver a spec, not code.**
When they end they become execution cards. This is TRACER's spike: never
estimate "investigate and build" as one card. An execution card that turns
out to need analysis is stopped at its first check and split; the time lost
is counted against how the card was written, not against the person.

## 5. People

Each person has:

| Limit | Meaning |
| --- | --- |
| **Productive capacity (H)** | Hours of real production in their fixed working day, measured, not assumed. Eight hours of work are not eight hours of development. Meetings and coordination are subtracted. |
| **Free margin (M)** | 20 to 25 % of H, never planned (section 9) |
| **Role ceiling (R_max)** | The highest R their role holds, per card |
| **Responsibility budget (B)** | The highest sum of R of their active cards at once, so nobody carries five critical cards even when each fits their role |
| **Expertise per repository** | new · guided · autonomous · reference |
| **Speed per card type** | Their own factor for execution, diagnosis, analysis, exploration |

**Expected time** of a card for a person:

```
T = C × K_repo × f(expertise in that repository) × f(speed in that card type)
```

Factors start from what the person declares, checked by the LT, and after
about five cards they are replaced by the ratio of real to estimated time of
that person's last cards in that repository and of that type. Capacity is
therefore dynamic: whoever works often on a repository becomes faster there,
and the plan notices without anyone declaring it.

**Expertise also limits responsibility.** Being senior does not make
someone able to answer for a critical repository they have never touched:

```
Effective R_max = min(role R_max, ceiling of their expertise in the repository)
```

| Expertise in the repository | May hold alone up to |
| --- | --- |
| New | R2 |
| Guided | R3 |
| Autonomous | The role's ceiling |
| Reference | The role's ceiling |

## 6. Assigning a card

A person may hold a card only if:

1. T fits in their H minus M and their other cards;
2. effective R ≤ their effective R_max;
3. their budget B is not exceeded.

Among those who may, the card goes to **the one with the lowest expected
time**: towards the fastest, never up the hierarchy. A semi-senior who is a
reference in the repository beats a senior who is new to it.

**Above the ceiling.** When a card's R is above someone's effective R_max
but its work fits their capacity, it may still be given to them with a
**co-holder** whose role and expertise cover it. The co-holder approves the
plan, reviews the pull request and spends their own budget B. In planning,
those hours are costed at the co-holder's rate, so the choice is visible as
the expensive one it is. The person is not paid for a responsibility their
role does not hold; doing it well repeatedly is evidence for a promotion.

The full procedure is in the [assignment template](../../plugin/templates/team/assignment.md).

## 7. Cells of three and the relay

Teams work in **cells of three**. Every card has three roles in its cell:

| Role | Does | At the start |
| --- | --- | --- |
| **Primary (A)** | Executes | Plan and first tests |
| **Secondary (B)** | Reviews the plan at the first check; takes the card if it is reassigned | Reads the card and the plan (15 to 30 minutes, in their margin) |
| **Tertiary (C)** | Reviews the pull request; second relay | Reads the card |

Responsibility has two layers:

- **Execution responsibility is individual and moves with the card.** At any
  moment exactly one person holds it.
- **Delivery responsibility belongs to the cell, in equal parts.** Delivery
  is measured per cell, not per person.

One layer alone fails: only individual means looking for culprits; only
shared means nobody answers. With both, someone answers today and the three
win or lose together, which is what makes B and C really know the card.

**The relay goes A → B → C, and never back to A.** If A did not reach a
check, A may be tired or pulled elsewhere; handing the card back defeats the
mechanism. If C also falls, the card goes to the LT, who redistributes it
outside the cell or replans it with the PO. B and C are chosen by the same
rule as A: the fastest eligible people, so a cell's secondary and tertiary
are chosen with the card's repositories in mind.

A team whose size is not a multiple of three forms cells of three and lends
its remaining one or two people as secondary or tertiary to the existing
cells; it never forms a cell of one.

## 8. Progress checks

A check asks for **evidence**, not for "how is it going":

| Card type | First check | Later checks |
| --- | --- | --- |
| Execution | Plan written, scenario tests created and failing | Draft pull request with the success path working |
| Diagnosis | Failure reproduced by a test | Cause shown |
| Analysis | Questions and sources listed | Alternatives with their trade-offs |
| Exploration | What was read and run | Map of risks |

When the checks fall depends on effective R, as a share of the person's
expected time T (never the base estimate, or the new person always fails
and the expert never feels it):

| Effective R | Checks |
| --- | --- |
| 1 to 2 | One, at 50 % |
| 3 | At 40 % and 70 % |
| 4 to 5 | At 25 %, 50 % and 75 % |

**A check not met reassigns the card at that moment**, to the next in the
relay, while there is still time to deliver it. The person is not
penalized; their factors are recalibrated (section 5). Template:
[check plan](../../plugin/templates/team/card.md).

## 9. The free margin

20 to 25 % of each person's H is never planned (about two hours of eight).
It is used, in this order:

1. Absorbing a reassigned card.
2. Reviewing pull requests from other teams (section 12).
3. Reading cards as secondary or tertiary.
4. Whatever is left is the person's: learning or rest.

**Finishing early never pulls new work into the margin** in the same day or
sprint. A person who finishes early repeatedly has a capacity H that is too
low; the next planning raises it. This breaks the loop of "finish, get more,
finish, get more".

**A margin consumed sprint after sprint means capacity is overestimated.**
The answer is to plan less, not to pay more.

## 10. Pay for absorbed load

Absorbing a reassigned card is load the person had not committed to, so it
is paid, within limits:

1. **Paid** per hour of reassigned card absorbed in the margin.
2. **Capped** per period (the team sets it). Without a cap, the bonus rewards
   the wear the method exists to prevent.
3. **No penalty for the person who did not arrive.** When it repeats, first
   their capacity estimate is checked (a system error), then the person.
4. **Watched for gaming:** letting cards fall so a colleague gets paid is
   seen in the reassignment rate per pair of people.

The cost of planning badly then shows in payroll, which is a useful signal
for the company. How this pay is treated (variable pay within the agreed
working day, or overtime outside it) depends on the country's labour law and
must be checked with whoever handles it.

## 11. Technical leads

An LT keeps the cells working, coordinates with POs and other LTs, and is
the last link of the relay. Their H is what is left after meetings and
coordination, and meetings also spend their budget B. They take cards of
**high R and low C**, and only while their capacity and budget are not
taken by meetings.

## 12. Work across teams

Another team that needs an integration with a product does not wait for the
product's team:

- It builds in the product's repository with **its own capacity**, and
  leaves a pull request.
- The product's cell reviews it **in its margin**: two reviewers when the
  effective R is 3 or more, one below.
- The author team answers for the behaviour of the integration; the product
  team answers for the integrity of its product. The two reviewers share the
  approval, so neither carries a wrong step alone.

## 13. Speed and balance

Keeping people on the repositories they know maximizes speed; rotating them
spreads expertise. Neither alone is good: pure speed leaves a repository in
one person's hands, and when that person is absent the speed and the
forecast are lost; pure rotation wastes the expertise the team has.

### Worst-case velocity

Two numbers are measured each sprint:

- **Nominal velocity:** what the team delivers with everyone present.
- **Worst-case velocity:** what it would deliver without its most critical
  person: remove each person in turn, recompute expected times with the
  expertise matrix, keep the lowest.

The gap between them is the **concentration risk**. A team that delivers 100
with everyone and 40 without one person is not fast; it depends on that
person. The goal is to **maximize worst-case velocity**, which values speed
and pushes towards balance at once.

### The rotation dial

The control is the **share of rotation cards**: low-R cards given on purpose
to someone new or guided in that repository, with an expert as secondary.
Their extra time is in the forecast; it is investment, not inefficiency.

| Mode | Rotation | When |
| --- | --- | --- |
| **Speed** | 5 to 10 % | The forecast is behind the committed date |
| **Cruise** | about 20 % | Normal |
| **Balance** | 30 to 40 % | Expertise is dangerously concentrated |

**Floor:** every critical repository keeps at least two autonomous or
reference people (bus factor ≥ 2), in every mode. Speed is never bought by
leaving a critical repository in one pair of hands. Rotation uses only low-R
cards; critical work stays with whoever knows it.

### Switching, with hysteresis

The company (PO and LT) sets the starting priority (speed because it is
late, or balance) and the thresholds X and Y. The mode then follows the
data, with different thresholds in each direction so it does not swing
every week:

- **To Speed:** the forecast slips more than X % past the committed date.
  **Back to Cruise:** the slip falls under X/2 %.
- **To Balance:** worst-case velocity falls under Y % of nominal, or a
  critical repository has a bus factor of 1. **Back to Cruise:** worst-case
  velocity rises above Y + 10 %.
- **Balance wins over Speed** when both apply, unless the company decides
  otherwise and records why.
- **The mode changes only at the end of a sprint or slice**, never in the
  middle.

The cycle is: speed up until the date is recovered, balance until the risk
is down, and around again. When someone is absent, the forecast falls to the
worst-case velocity, which was already known and accepted.

## 14. Metrics

| Metric | Shows |
| --- | --- |
| On-time delivery weighted by R | Missing an R5 card is not missing an R1 |
| Responsibility delivered | Sum of R shipped, per cell and per person |
| Reassignment rate, and at which check | Where plans break |
| Check pass rate by R and by card type | Whether checks are well placed |
| Margin consumed | Above about half, sprint after sprint, planning is wrong |
| Estimate accuracy per person × repository × type | Where the plan is wrong |
| Nominal and worst-case velocity, current mode and why | The speed and balance trade-off |
| Bus factor per critical repository | Who can hold it |
| Expertise map and its growth | The return on rotation |
| Analysis cards turned into clear specs | Whether analysis delivers |
| Time lost to misclassified cards | Whether cards are written well |
| Fatigue signals | Several reassignments in a row for one person, or their margin consumed several weeks running: answered with less load, never with a penalty |

## 15. Parameters

| Parameter | Default | Change it when |
| --- | --- | --- |
| Cell size | 3 | Never fewer than 3 for cards of R 3 or more |
| Free margin | 20 to 25 % of H | Teams with many integrations need more |
| Responsibility budget B | Set per role | Measured overload or underload |
| Integration factor | +20 % per extra repository | Measured |
| Check points | Section 8 | Measured pass rates |
| Rotation per mode | 5-10 / 20 / 30-40 % | The company's risk appetite |
| Thresholds X and Y | 10 % and 60 % | The company's risk appetite |
| Cap on paid absorbed load | Set by the team | Always set |

## 16. Risks

- **R inflation:** if a higher R makes a card more valuable, every card
  becomes R4. The PO and the LT calibrate the rubric, never the executor,
  and the calibration is reviewed against incidents.
- **Feeling watched:** checks are a safety net, not control. The message is
  "your card will not fall on you".
- **Gaming the pay:** see section 10.
- **Cold start:** factors are guesses until the history exists; plan the
  first sprints in Cruise with wide forecasts.

## 17. Templates

- [Card](../../plugin/templates/team/card.md): type, C, R, repositories, roles, checks
- [Responsibility rubric](../../plugin/templates/team/responsibility-rubric.md)
- [Repository profile](../../plugin/templates/team/repository-profile.md)
- [Person and expertise](../../plugin/templates/team/person.md)
- [Assignment](../../plugin/templates/team/assignment.md): the procedure step by step
- [Sprint balance report](../../plugin/templates/team/balance-report.md)
