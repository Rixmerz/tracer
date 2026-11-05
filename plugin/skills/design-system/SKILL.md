---
description: Choose the documented design system a TRACER product is built on, the style it wears and the brand overlay that adapts it, from the design catalog (part of phase 1, identity)
argument-hint: "[what the product is and who uses it]"
disable-model-invocation: true
---

Choose the design system for "$ARGUMENTS". Follow the `tracer` skill's rules.
No production code is written in this command.

The product is built on a design system that already exists, is documented
by its owner and is known to work: its rules, tokens, components and
accessibility come from its documentation. Never invent a design system for
the project, and never write one from memory. A company's identity is a
brand overlay on that base, and a visual style is applied the same way.

Use the `tracer-design-catalog` tools. If they are not available, read
`${CLAUDE_PLUGIN_ROOT}/catalog/systems.json` and `styles.json` directly.

## 1. Read the context

Read `docs/tracer/contract.md` and `docs/tracer/audiences.md`: the audience,
their devices, their language (Japanese text needs a system built for it),
the density of the work (dense data or reading), the platform and the stack.
If the company already has a design system of its own, documented and in
use, that is the base: skip to step 4.

## 2. Propose base systems

Call `search_design_systems` with that context (and `platform`, `japanese`
when they apply). Present two or three with their reasons, packages and
licenses (`get_design_system`). Say any license limit plainly (some are tied
to their owner's platform). The outcome owner chooses; record why.

## 3. Propose a style, if the identity needs one

When the contract or the owner asks for a look beyond the base (calm craft,
editorial, technical dark…), call `search_styles`. A style brings traits and
risks, never components or tested values. Prefer a style whose `carriers`
include the chosen base; if not, say why the base still fits. Then produce
the two or three identity variants of phase 1 as overlays of this one base.

## 4. Write the design system file

Call `design_system_brief` with the base (and the style) and write the
result to `docs/tracer/design-system.md`, or start from
`${CLAUDE_PLUGIN_ROOT}/templates/design-system.md`. Fill the overlay table
with the chosen variant: one row per base token or rule changed, its base
value from the system's documentation, the new value and the reason. Write
every color pair the overlay sets as `#fg on #bg`.

## 5. Check the overlay

Call `check_overlay` with the base id and the table, and `check_contrast` for
any pair it cannot read. Fix every problem before it is approved: a row
without a base rule is an invented rule, a row that weakens focus, contrast,
target size, labels, motion or errors is refused, and a pair under AA is
changed. Record the choice in `identity.md` with a link to
`design-system.md`.

## 6. Hand over

Every slice reads `design-system.md` before any interface code, installs the
packages it lists, and uses the base's components and tokens; a component
the base lacks is built from its tokens and documented there as an addition.
The verifier checks each screen against the base's documentation and the
overlay.
