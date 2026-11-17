# Example 1. A one-page professional site

A trial lawyer with forty years of practice wants a website. The brief is a
text document; the agent works in a hosted design canvas with no repository
and no render checks allowed. TRACER runs in light mode (handbook §22,
institutional-site profile; §22 environments without the plugin).

## Contract (phase 0)

```markdown
MEV name: Lawyer's site, first version
Outcome owner: the lawyer
Metric: consultations requested per week by phone, messaging or form
Current value: 0 (no site; referrals only)
Target: 3 per week within 8 weeks
Quality floor: WCAG 2.2 AA; the contact action reachable in two taps on a phone; every claim on the site from the client
Audience profiles: relative of a detained person; person under investigation; company HR; referred visitor
Validation window: 8 weeks
Validated by: the lawyer
Must: identity and credentials, criminal defence by stage, labour advice for companies, contact on every screen
Should: biography timeline
Post-MEV backlog: blog, client area
```

## Client content inventory (before any design)

```markdown
Source: "CONTENT FOR WEBSITE" document, received 16 Nov
Complete? no: the biography is cut at "...preparing defence strategies and litiga"

| Id | Text (as given) | Kind | Where it goes | Requirement |
| C1 | Request a consultation | literal: call to action | Primary button | REQ-cta |
| C2 | Former Public Defender | literal: claim | Home | REQ-claims |
| C3 | Over 40 years in practice | literal: claim | Home | REQ-claims |
| C4 | 24 years specialised in criminal defence and trial litigation | literal: claim | Home | REQ-claims |
| C5 | Your defence, in the hands of the one who will stand in court. | literal: headline | Section 2 | REQ-headline |
| C6 | Nine criminal services, eight labour services | free: may be grouped | Services | REQ-services |

Questions for the client:
| Question | Why it matters | Asked on | Answer |
| How does the biography end? | The source is cut | 16 Nov | pending |
| Do you take urgent calls outside office hours? | The detained person's relative calls at night | 16 Nov | pending |
| Which cities do you cover? | People compare by location | 16 Nov | pending |
| Is the first consultation free? | It decides whether people call | 16 Nov | pending |
```

The literal lines become scenarios:

```markdown
#### Scenario: the call to action is the client's
- WHEN any screen renders, at any width
- THEN the primary button reads "Request a consultation"
- CORRECT: the person reads exactly the client's words
```

## Audiences, light mode (before the first mock)

```markdown
Audience: Relative of a detained person
Trying to get done: reach a lawyer now
Context: phone, at night, under stress, will not read
Urgency: hours; the detention hearing is soon
In five seconds they look for: a phone number they can tap
Must never see: legal jargon before the contact

Audience: Person under investigation
Trying to get done: compare lawyers and choose one
Context: phone or desktop, reads headings, checks credentials
In five seconds they look for: who she is and whether she does criminal defence

Audience: Company HR
Trying to get done: labour advice for the company
Context: desktop, office hours, rational
In five seconds they look for: a path meant for companies

Audience: Referred visitor
Trying to get done: confirm the recommendation
In five seconds they look for: a face and a track record
```

## Empathy round (before the mock)

| Expectation | Level | Decision |
| --- | --- | --- |
| A tap-to-call bar always visible on phones | basic | in MEV |
| Criminal services ordered by what the person is living ("There has been a detention") | basic | in MEV |
| A separate path for companies | basic | in MEV |
| Credentials as a headline, not as a stat counter | performance | in MEV |
| The "detention" stage marked and with its own call button | differentiator | in MEV |
| Night-time availability stated | basic | **question to the client**, not text |

## Identity (design system and variants)

`search_styles("institutional site for a law firm, trial lawyer")` returns
**editorial**. Three overlays are produced as variants; the client chooses
"Case file": paper, ink and a sealing-wax red, because the site reads like
a legal file. `identity.md` traces each choice:

| Choice | From the client's world |
| --- | --- |
| Paper `#F4EFE6`, ink `#1E1B18` | A case file |
| One accent, sealing wax `#7A1F1F` | A notary's seal: urgency without alarm |
| One motion: the name settles, an ink line draws under it | A signature |

`check_contrast("#7A1F1F", "#F4EFE6")` → 8.97:1, AA. `check_genericity` on
the first draft found 6 eyebrow labels, 14 entrance animations, a marquee
and an arrow glued to a button; each was removed or given a reason.

## A slice, built and not verified

The host forbids render checks, so the slice is **built, not verified** and
the client gets the verification request:

```markdown
Slice / version: home and criminal stages · v54fc
Status: built, not verified. Reason: the canvas allows no render check

Widths
- [ ] Phone about 390 px · [ ] Tablet about 768 px · [ ] Desktop about 1440 px
At each width: nothing scrolls sideways, no stage sits alone on its row,
the photo's red frame stays attached to the photo, text never touches the timeline line.

Critical flow: "My brother was just detained"
- [ ] Open the site on a phone → the Call / WhatsApp bar is visible without scrolling
- [ ] Tap Call → the phone dials the number

Content
- [ ] The button reads "Request a consultation"
- [ ] No sentence states a fact you did not give us
```

The client's screenshot shows the timeline text touching its vertical line.
Cause: the CSS targeted `.tl>div`, the markup used `<li>`. It is rework,
and the catalog already had the entry ("Selectors that match nothing").

## Decision log

```markdown
## D7 · 16 Nov 18:53 · v54fc
Trigger: screenshot, "a lot of dead space; think of the people first"
Change: two paths on home, credential band, five fixed stage columns, labour full width, timeline, phone bar
Dropped: fixing each section's spacing one by one
Reason: the four audience profiles; the stage grid orphaned its fifth item
Based on: v193d (live version checked, unchanged) · Verified: no (request sent)
```

## Anti-patterns avoided

Client words rewritten · Facts nobody provided · Orphans in a grid · Dead
title column · Eyebrow labels · Entrance effects everywhere · Not verified,
reported as done · Published over a version not read.
