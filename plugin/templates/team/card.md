# Card

```markdown
Card: <id and title>
Slice / requirement: <link>
Type: execution / diagnosis / analysis / exploration
Timebox (analysis, exploration): <hours>; delivers a spec, then becomes execution cards
Repositories and areas: <repo: area>
Complexity C: <hours or points>
Responsibility R (rubric): <1-5> · Effective R = max(R, R_repo floors) = <n>
Integration factor: <+20 % per extra repository>

Primary (A): <person> · expected time T: <h>
Secondary (B): <person>
Tertiary (C): <person>
Co-holder (if effective R is above A's ceiling): <person, rate used in planning>
Rotation card? no / yes: <who learns which repository>

Checks (share of A's expected time; evidence, not status)
| # | At | Evidence asked | Met? | Action |
| 1 | <%> | <plan and failing tests / reproduced failure / questions and sources> | | continue / reassign to B |
| 2 | <%> | <draft PR / cause shown / alternatives> | | continue / reassign |

Relay: A → B → C → LT. Never back to A.
Reassignments: <when, at which check, to whom, hours absorbed in margin>
```
