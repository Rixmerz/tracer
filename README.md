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

## The acronym

- **T**raceable: every requirement is linked to code and tests.
- **R**equirement-complete: the MEV is fully specified before building.
- **A**rchitected for the destination: no temporary architecture.
- **C**ontinuously validated: every slice passes the validation gates.
- **E**xecuted in slices: 1 to 3 days each, each one deployable.
- **R**eleased at MEV: delivery happens when the expected value is verified.

## Read next

- [The method](docs/method.md): the full handbook, from problem to templates.
- [Templates](templates/): expectation contract, requirement, slice, scope
  change.

## License

[CC BY 4.0](LICENSE). Use it, adapt it, share it; credit the source.
