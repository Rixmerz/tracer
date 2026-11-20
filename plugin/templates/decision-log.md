# Decision log

One entry per iteration that changes what the person sees: each slice,
publish, artifact version or commit. Kept in `docs/tracer/decisions.md`,
newest last. Five lines are enough; the point is that the history keeps its
reasons.

```markdown
## D<n> · <date and time> · <version id or commit>
Trigger: <what asked for it: a request, a screenshot, a finding, in the person's words>
Change: <what changed, in one or two lines>
Dropped: <the alternative considered and not taken>
Reason: <the criterion that decided it: audience, requirement, metric>
Based on: <the version or commit read before the change> · Verified: yes / no (<how>)
```

## Waiver

A waiver is an explicit authorization to go on without a step the method
requires (an audience test, a contract field). An agent may draft it; only
the outcome owner signs it. Without a signature, the step stays blocking.

```markdown
## W<n> · <date> · waiver
Step waived: <audience test | contract field: ...>
Covers: <audience and screens, or field>
Why it cannot be done now:
Risk accepted: <what may have to be redone, in the outcome owner's words>
Instead: <proxies used, e.g. 3 new employees in a similar role>
Pilot: <the slice that puts it in front of real users first>
Expires when: <the condition that ends it, e.g. representatives available>
Signed by: <outcome owner> · <date>
```

If the live version is not the one in "Based on" when the change is published,
stop: read it, merge, and write what was merged in the entry.
