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
  catalog, slice, scope change.

## Claude Code plugin

The `plugin/` folder packages TRACER for Claude Code: a `tracer` skill that
walks the agent through the method step by step, and five commands.

```
/plugin marketplace add Rixmerz/claude-plugins
/plugin install tracer@rixmerz
```

Installing it also installs [livespec](https://github.com/Rixmerz/livespec),
which keeps the chain from requirements to code and tests. The method itself
does not require livespec; the plugin uses it as the reference toolchain.

| Command | Phase | Does |
| ------- | ----- | ---- |
| `/tracer:contract` | 0-1 | Expectation contract, audience profiles, base round, capability map, ADRs, slice plan |
| `/tracer:empathy` | 1 | Empathy round: expectations, improved and new specs, critical flows |
| `/tracer:slice` | 3 | One slice: ready check, test-first build, gates, track |
| `/tracer:verify` | 3 | Independent verification: critical flows, CORRECT criteria, floors, anti-patterns |
| `/tracer:scope` | 4 | Runs an idea or correction through the scope filter |

## License

[CC BY 4.0](LICENSE). Use it, adapt it, share it; credit the source.
