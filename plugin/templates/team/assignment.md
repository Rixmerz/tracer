# Assignment procedure

For each card, at planning and at every reassignment.

```markdown
1. Type, C, R (rubric), repositories. Effective R = max(R, every R_repo floor).
2. For each person in the team, expected time:
   T = C × K_repo × f(expertise in repo) × f(speed in type)   (+ integration factor)
3. Eligible people:
   - T fits in H − margin − their other cards (for a reassignment: fits in their margin)
   - effective R ≤ min(role R_max, expertise ceiling: new R2, guided R3, else role)
   - sum of R of their active cards + R ≤ budget B
4. Mode of the sprint (Speed / Cruise / Balance): if this card is low R and the
   rotation share is not reached, prefer an eligible new or guided person in that
   repository, with an expert as secondary. Otherwise:
5. Primary = eligible person with the lowest T. Never chosen by seniority.
6. Secondary and tertiary = next lowest T in the cell, preferring people who know
   the card's repositories.
7. If nobody is eligible on R but someone fits on capacity: assign with a co-holder
   whose role and expertise cover the card; cost those hours at the co-holder's rate.
8. If nobody fits at all: split the card, move it, or replan with the PO. Never
   overload someone to fit it.
9. Checks from effective R, as shares of the primary's T.
Relay on a missed check: A → B → C → LT, never back to A.
```
