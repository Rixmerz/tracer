# Example 6. The audience gate

The learning platform of example 2. Human resources commissions it; employees
take the courses. Names, companies and figures are anonymized.

## The case that motivated it

A real project, anonymized. Company X (a mid-sized employer) hired a team to
build an internal training platform.

```markdown
Sponsor: the HR department of Company X
Audience: employees who take the courses (never consulted before code)
What happened:
1. HR described what it needed and approved the UI/UX design.
2. The interface was built to that design.
3. Test users (employees) tried it and rejected the design.
4. The test users produced their own design, which they did like.
5. The team had to rewrite the UI/UX code: the interface was built twice.
Root cause: not poor communication with the client (HR's requirements were
understood and met), but late feedback from the end user. The only person
who validated the design was the sponsor, who is not the one who uses it.
Missing gate: an audience test before code.
```

The rest of this example replays the same project with the audience gate in
place.

## The contract names sponsor and representatives

```markdown
Sponsor: Head of HR (commissions; is also the administrators' audience)
Audience profiles:
- Learners: warehouse and office staff, mostly on phones, between shifts
- Administrators: the HR team, desktop, assign and track training
Audience representatives:
- Learners: 5 (2 warehouse, 2 office, 1 new hire) · first test 2026-03-10
- Administrators: 3 from the HR team · first test 2026-03-11
```

No field is blank, so phase 0 closes.

## Round 1: sketches, before the identity is fixed

Two variants of "My courses", shown on paper-like wireframes to the five
learners. Variant A (HR's favourite, a dashboard of charts) failed
"continue the course you started" for 3 of 5; variant B (a list with a
"Continue" button first) passed 5 of 5. HR chooses within variant B.

## Round 2: the clickable mock, before sign-off

```markdown
Audience: Learners
Round: clickable mock before sign-off
Material tested: mock v3
Date: 2026-03-24
Representatives: 2 warehouse, 2 office, 1 new hire

| # | Task | Completed | Help needed | Median time | Errors | Their words vs ours |
| - | ---- | --------- | ----------- | ----------- | ------ | ------------------- |
| 1 | Continue the safe-lifting course where you stopped | 5/5 | 0 | 0:20 | 0 | — |
| 2 | Find the mandatory courses due this month | 4/5 | 1 | 0:45 | 1 | "mandatory" vs "required" |
| 3 | Download your certificate | 5/5 | 0 | 0:30 | 0 | "diploma" vs "certificate" |

Findings:
| Finding | Seen in | Blocking? | Change |
| ------- | ------- | --------- | ------ |
| "Required" not understood; they say "mandatory" | 3/5 | no | label change in the mock |

Result: met
```

The administrators' test of their screens is also *met*. The gate opens for
both audiences and the skeleton starts.

## A blocked slice, and a waiver

Mid-MEV, HR asks for a new "Team progress" screen for line managers, an
audience nobody tested. `/tracer:slice` stops:

> Blocked: the audience gate is closed for line managers (screen "Team
> progress"). No audience test exists and no waiver is signed. Run a test of
> the mock with 3 to 5 managers, or sign the drafted waiver below.

Managers are on leave for two weeks. HR signs the waiver:

```markdown
## W2 · 2026-04-15 · waiver
Step waived: audience test
Covers: line managers · "Team progress"
Why it cannot be done now: managers unavailable until 2026-04-29
Risk accepted: the screen may need to be rebuilt after managers try it
Instead: walkthrough with 2 HR members who were line managers
Pilot: slice 14 releases "Team progress" to 3 managers before everyone
Expires when: managers are back; test run on 2026-04-30
Signed by: Head of HR · 2026-04-15
```

The slice proceeds. On 2026-04-30 the test runs; one finding enters as a
spec change through `/tracer:scope`.

## What it avoided

- The sponsor's taste standing in for the learners' (round 1: HR's favourite
  variant failed the learners' main task).
- A redesign after code: both rounds cost hours, on sketches and on the mock.
- Silent skipping: the only way past the gate was a signed, dated waiver with
  its risk, its proxies and its expiry.

Handbook: section 8.4 (representatives), 9.7 (audience tests and the gate),
13 (Definition of Ready), 20 (edge cases).
