# TRACER

**A development method for building software with AI agents.**

Agree up front on the value the product must deliver, specify all of it, then
build it in thin slices that are already part of the final product.

## Why

AI agents build for what they are asked today, not for where the product is
going. A proof of concept gets a proof-of-concept architecture, and that code
is later thrown away or duplicated. Writing the whole spec and handing it over
in one go fixes that, but brings back waterfall.

TRACER separates two horizons:

- **Design** for the complete destination, so architecture is decided once.
- **Execute** in slices of 1 to 3 days on that final architecture, each one
  tested, traced and deployed as it lands.

The destination is the **Minimum Expected Value (MEV)**: the smallest scope
that delivers an outcome the business already expects, defined by a metric, a
target and a quality floor.

Agents also produce work that *looks* finished: green tests, a rendered
screen, and still a navbar without icons or a file picker that asks a
non-technical user for a CDN path. TRACER closes that last 10%:

- **See the product from the client's side.** Specs are written in two
  rounds: a base round for what is sought, and an empathy round that reads
  every capability through an audience profile and makes explicit what its
  users take for granted.
- **Done means correct, not just working.** Every capability has critical
  flows tested end to end through the interface, with success and failure
  paths, and every criterion states what *works* and what is *correct* for
  its audience. Slices are checked against component floors and a catalog of
  UI/UX anti-patterns by a verifier who did not build them.

## The acronym

- **T**raceable: every requirement is linked to code and tests.
- **R**equirement-complete: the MEV is fully specified before building.
- **A**rchitected for the destination: no temporary architecture.
- **C**ontinuously validated: every slice passes the validation gates.
- **E**xecuted in slices: 1 to 3 days each, each one deployable.
- **R**eleased at MEV: delivery happens when the expected value is verified.

## Read next

- [The method](docs/method.md): the full handbook, from problem to templates.
- [Templates](plugin/templates/): expectation contract, audience profile,
  requirement, empathy review, critical flow, component floors, anti-pattern
  catalog, slice, scope change, design system.

## Claude Code plugin

The `plugin/` folder packages TRACER for Claude Code: a `tracer` skill that
walks the agent through the method step by step, six commands and a design
catalog server.

```
/plugin marketplace add Rixmerz/claude-plugins
/plugin install tracer@rixmerz
```

Installing it also installs [livespec](https://github.com/Rixmerz/livespec),
which keeps the chain from requirements to code and tests, and
[layout-inspector](https://github.com/Rixmerz/layout-inspector-mcp), which
measures each rendered screen against its design system. layout-inspector
needs `uv` and Playwright's Chromium (see its README). The method itself
does not require livespec; the plugin uses it as the reference toolchain.

| Command | Phase | Does |
| ------- | ----- | ---- |
| `/tracer:contract` | 0-1 | Expectation contract, audience profiles, base round, capability map, ADRs, slice plan |
| `/tracer:empathy` | 1 | Empathy round: expectations, improved and new specs, critical flows |
| `/tracer:design-system` | 1 | Chooses the documented design system the product is built on, its style and the brand overlay |
| `/tracer:slice` | 3 | One slice: ready check, test-first build, gates, track |
| `/tracer:verify` | 3 | Independent verification: critical flows, CORRECT criteria, floors, anti-patterns |
| `/tracer:scope` | 4 | Runs an idea or correction through the scope filter |

### Design catalog

The plugin runs `tracer-design-catalog`, an MCP server (Python, standard
library only) over [`plugin/catalog/`](plugin/catalog/):

- **Design systems**: documented systems by category (enterprise, dense data,
  commerce, public service, editorial, developer tools, consumer, Japanese,
  composable, platform) such as Material 3, Carbon, Fluent 2, Ant Design,
  Primer, GOV.UK, USWDS, the Japanese Digital Agency's, SmartHR, Spindle and
  freee Vibes, each with its owner, documentation, packages and licenses.
- **Styles**: visual directions by family (calm craft, dense commercial,
  editorial, rational grid, technical dark, neo-brutalist, soft 3D,
  translucent, retro digital, playful, organic, heritage), each with its
  accessibility risks and the systems that carry it.

Tools: `search_design_systems`, `get_design_system`, `search_styles`,
`get_style`, `design_system_brief`, `check_overlay`, `check_contrast`. A
product is never given an invented design system: a style or a company's
brand is an overlay of only what it changes on a documented base, checked
against it, and the render is measured against its tokens with
[layout-inspector](https://github.com/Rixmerz/layout-inspector-mcp)'s
`check_design_system`.

To add a system, add an entry to `systems.json` with its owner's
documentation and the packages and licenses its registry states, and run
`python3 -m unittest discover plugin/mcp`.

## License

[CC BY 4.0](LICENSE). Use it, adapt it, share it; credit the source.
