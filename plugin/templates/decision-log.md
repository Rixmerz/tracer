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

If the live version is not the one in "Based on" when the change is published,
stop: read it, merge, and write what was merged in the entry.
