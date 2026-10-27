---
description: Run a new idea, correction or architecture change through the TRACER scope filter (phase 4)
argument-hint: "[the proposed change in one sentence]"
disable-model-invocation: true
---

Run this proposed change through the TRACER scope filter: "$ARGUMENTS".
Follow the `tracer` skill's rules. No code changes in this command.

1. **Classify it:** new idea, correction (a scenario was wrong or a constraint
   appeared) or architecture change.
2. **Write it as a spec change:** which requirements it adds, modifies or
   removes (an OpenSpec change by default).
3. **Test it against the metric** in `docs/tracer/contract.md`: does it move
   the MEV's outcome? Say why in one sentence.
4. **Size it** in slices.
5. **Propose the decision:**

| Case | Decision |
| ---- | -------- |
| Correction | Enters directly as a spec change; update the forecast and record it in the track |
| Moves the metric, small | Enters the MEV; update the slice plan and forecast |
| Moves the metric, large | Enters only by swapping out a *Should* of similar size, or by accepting a new forecast |
| Does not move the metric | Goes to `docs/tracer/backlog.md` |
| Changes an architecture decision | New ADR first, then livespec impact analysis on built slices before accepting |

The outcome owner decides, not the agent: present the proposal using the scope
change template
`${CLAUDE_PLUGIN_ROOT}/templates/scope-change.md` and
apply it only after the user agrees.
