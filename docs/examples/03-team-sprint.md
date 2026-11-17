# Example 3. A team sprint

One cell of three plans a sprint under the [teams adaptation](../adaptations/teams.md).
The numbers below are the real output of the plugin's `team_assign` and
`team_balance` for these inputs.

## People

Each has a 30-hour sprint of production with a 20 % free margin, so 24
hours can be planned.

| Person | Role ceiling | billing | portal | search |
| --- | --- | --- | --- | --- |
| Ana | R5 | reference | autonomous | new |
| Ben | R4 | new | reference | guided |
| Caro | R3 | new | guided | autonomous |

## Repositories

| Repository | K | R floor | Critical |
| --- | --- | --- | --- |
| billing | 1.5 | 4 | yes |
| portal | 1.0 | 2 | no |
| search | 1.2 | 2 | yes |

## Cards

| Card | Type | C | Card R | Repositories | Effective R |
| --- | --- | --- | --- | --- | --- |
| B-1 Fix rounding in invoice totals | execution | 3 | 5 | billing | 5 |
| P-2 Profile page | execution | 10 | 1 | portal | 2 |
| S-3 Search by title | execution | 8 | 2 | search | 2 |
| P-4 Export button | execution | 4 | 1 | portal + billing | 4 |
| S-5 Typo tolerance | analysis (timeboxed) | 4 | 2 | search | 2 |

B-1 is small and critical: the rubric's money factor is 5. P-4 looks
trivial, but touching billing raises it to R4.

## Assignment

| Card | Primary | Expected time | Relay | Checks |
| --- | --- | --- | --- | --- |
| B-1 | Ana | 3.6 h | LT (relay gap) | 25 %, 50 %, 75 % |
| P-4 | Ana | 5.3 h | LT (relay gap) | 25 %, 50 %, 75 % |
| P-2 | Caro (rotation) | 14.0 h | Ben → Ana → LT | 50 % |
| S-3 | Caro | 9.6 h | Ben → Ana → LT | 50 % |
| S-5 | Ben | 6.7 h | Caro → Ana → LT | 50 % |

Load: Ana 8.9 h, Ben 6.7 h, Caro 23.6 h, all within 24 h.

Read it:

- **The fastest eligible person, not the most senior.** Only Ana may hold
  billing work above R2; new people in billing are capped at R2.
- **P-2 is a rotation card.** Ben would do it in 8 h; Caro, guided in
  portal, takes 14 h with Ben as secondary. The extra 6 hours are planned:
  they buy a second person for portal.
- **The relay gap on B-1 and P-4** is the tool saying nobody else may hold
  billing: if Ana is ill, the cards go straight to the LT.

## Balance

```markdown
Sprint: 14 · Mode: Balance · Because: bus factor under 2 in billing and search
Nominal velocity: 29 · Worst-case velocity: 25 (without Ana) → 86 % of nominal
Forecast vs committed date: 5 % late (under X = 10 %)
Rotation share next sprint: 35 %
```

The worst case looks fine (86 %), yet the mode is Balance: billing and
search each have one person who can hold them. Next sprint, low-R billing
cards go to Ben with Ana as secondary, and search cards to Ben with Caro as
secondary, until both repositories have two.

## A missed check

S-3's check at 50 % of Caro's 9.6 h asks for a draft pull request with the
success path working. Caro had a sick day and has only the failing tests.
The card goes to Ben at once, the next in its relay. Guided in search, Ben
would need 13.4 h for the whole card; the half that remains takes him about
6.7 h, which fits in the 17 planned hours he has not used, so it is not paid
as absorbed load. Had it only fitted in his margin, those hours would be paid
within the team's cap. The card never goes back to Caro, and her factors are
recalibrated, not penalized.
