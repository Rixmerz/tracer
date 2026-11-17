# Verification request

When the environment cannot render or measure the interface (no
layout-inspector, no browser driver, or a host rule that forbids checking the
render), the slice is **built, not verified**. It is never reported as done.
Hand this to the person, filled in, with every publish.

```markdown
Slice / version: <id>
Status: built, not verified. Reason: <what the environment lacks or forbids>

Please check, and send a screenshot of anything that looks wrong:

Widths
- [ ] Phone, about 390 px wide
- [ ] Tablet, about 768 px wide
- [ ] Desktop, about 1440 px wide
At each width: nothing scrolls sideways, nothing overlaps, no item sits alone
on its own row, no column is mostly empty, decorations stay attached to what
they frame.

Critical flow: <the flow, as steps the person takes>
- [ ] <step> → <what they must see>

Content
- [ ] <literal client line> reads exactly as given
- [ ] No sentence states a fact you did not give us

Access
- [ ] Every button can be tapped with a thumb; text is readable without zoom
- [ ] Contrast pairs checked by tool: <pairs and ratios, from check_contrast>

What changed in this version: <decision log entry>
```

A finding from this checklist is rework of the slice, and its cause joins the
anti-pattern catalog, exactly as a verifier's finding would.
