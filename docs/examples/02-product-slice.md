# Example 2. A slice in a product

A learning platform; human resources teams upload training videos. The
capability is "Find training material". Full mode, with livespec and
layout-inspector available.

## Requirement (base round, improved in the empathy round)

```markdown
### Requirement: HR finds a training video by its title
The system SHALL let an administrator find a video by any word of its title.

Capability: Find training material
Audience: HR administrator
Round: empathy
Expectation level: basic

#### Scenario: search by a word of the title
- WHEN the administrator types "onboarding" in the search box
- THEN every video whose title contains "onboarding" is listed, across all pages
- WORKS: GET /videos?q=onboarding returns 200 with the matches from the whole catalog
- CORRECT: each result shows its title and a thumbnail, never a storage path or an id;
  the count says how many were found; the first result can be reached with the keyboard
```

## Critical flow

```markdown
Flow: "I need the onboarding video for Monday"
Audience: HR administrator · Starts at: library, signed in as HR, 240 real videos
Steps: 1. type "onboarding"  2. open the first result  3. go back

Success path
- WORKS: query over the full catalog; 3 matches
- CORRECT: "3 videos" shown; thumbnails and titles; back returns to the same query and scroll

Failure paths
| Failure | WORKS | CORRECT |
| No match | 200, empty | "No videos called 'onbaording'. Check the spelling or browse by topic" with a link |
| Server error | 503 | "Search is not working right now"; the query stays in the box; Retry |
| No permission | 403 for a learner | A learner never sees the admin library link |
```

## Gates, with evidence

| Gate | Evidence |
| --- | --- |
| Scenario tests | 6 new tests, green |
| Critical flows | `/tracer:verify` run by a second agent at 390 and 1440 px, as HR, on 240 real videos |
| Regression | Full suite on the head; 2 reds, both on the base list of commit `a1b2c3` |
| Spec integrity | `audit_coverage`: 0 untraced symbols |
| Impact | `git_diff_impact`: search service and library page only |
| UI and anti-patterns | `check_design_system`: 0 off-token values; rendered text has no ids |
| Static quality | Within limits |
| Quality floor | p95 search 180 ms under the 300 ms floor |
| Human review | Approved by the outcome owner |

## An escaped expectation

A week later, HR reports that sorting by date put "9 Mar" after "10 Mar".
The slice is reopened as rework, the spec gains a CORRECT line ("dates sort
by date, not as text") and the catalog already holds the entry ("Search and
sort that mislead"); a test for it joins the suite. Escaped expectations: 1.
