# Changelog

## 0.13.0

- Examples book (`docs/examples/`): a one-page professional site in light
  mode, a product slice with its gates and an escaped expectation, a team
  sprint with the real output of `team_assign` and `team_balance`, a
  retrospective, and a scope change.
- `team_assign` ends every relay at the LT and flags a relay gap when fewer
  than two other people may hold a card.
- Every template and test is in English.

## 0.12.0

- Teams adaptation (`docs/adaptations/teams.md`): every card carries
  complexity and responsibility (a rubric, highest factor wins); repository
  profiles add a complexity multiplier and a responsibility floor; card types
  (execution, diagnosis, analysis, exploration), with analysis timeboxed into
  a spec; dynamic capacity from expertise per repository and speed per type;
  responsibility capped by role and by repository expertise, with a
  co-holder above the ceiling; cells of three with a relay A → B → C → LT
  that never returns to A; evidence-based progress checks placed by
  responsibility; a protected free margin of 20 to 25 %; capped pay for
  absorbed load; technical leads' load; cross-team pull requests reviewed in
  the margin; worst-case velocity and a speed / cruise / balance mode with
  hysteresis and a bus-factor floor; metrics, parameters and risks.
- Templates in `plugin/templates/team/`: card, responsibility rubric,
  repository profile, person, assignment procedure, balance report.
- `team_assign` and `team_balance` in the catalog server (`plugin/mcp/team.py`).
- `/tracer:team`.

## 0.11.0

From the retrospective of a one-page site built without the toolchain (#5).

- Anti-pattern catalog: a new family, **Identity, not template** (eyebrow
  labels, middle-dot metadata, decorative monospace, big number with small
  label, one word in color, numbering without a sequence, entrance effects
  everywhere, endless motion, hover on every card, arrows in buttons,
  template palette, one card style, ornaments sized apart from what they
  frame); orphans in a grid and dead title columns under composition; client
  words rewritten and facts nobody provided under trust; publishing over an
  unread version, "not verified" reported as done and history with no
  reasons under delivery; selectors that match nothing and no visual
  baseline under testing.
- `check_genericity` in the design catalog server: counts those traits in a
  page's HTML and CSS.
- The client's content is a requirement: `client-content.md` inventories it
  as literal or free, each literal line is a scenario, and the builder adds
  no fact the client did not give.
- Verification without the toolchain: a slice that cannot be checked on its
  render is "built, not verified" and hands the person a verification request
  (390, 768 and 1440 px, the critical flow, the literal content, contrast);
  `visual-rubric.md` for a separate verifier reading screenshots.
- Audience profiles and the empathy round are a gate before the first mock,
  with a light mode for small products; profiles name urgency and what the
  person looks for in five seconds.
- Decision log (`decisions.md`): one entry per slice, publish or version, with
  the version it was based on; publishing checks the live version first.
- Visual baselines per closed slice, compared by the next one.
- Handbook: the client's content (8.4.1), decisions and versions (16), an
  institutional-site profile and environments without the plugin (22), new
  edge cases.
- `/tracer:retro`: a retrospective from the decision log and the history,
  marked fact, inference or hypothesis, whose lessons feed the floors and the
  catalog.
- The editorial style fits law firms, professional services and institutional
  sites, so a brand look comes from the catalog instead of being invented.

## 0.10.2

- Every skill names itself (`name`, as the Agent Skills spec requires; six of seven had none), and
  `plugin/mcp/test_skills.py` checks each skill's frontmatter against the spec as anthropics/skills'
  validator does: allowed keys, a kebab-case name equal to its folder, a description of at most
  1024 characters with no angle brackets, YAML a strict parser reads, under 500 lines.

## 0.10.1

- layout-inspector is a dependency of the plugin: the slice and verify steps
  call its `check_design_system`, so installing tracer installs it.
- Fixed a broken sentence in `/tracer:design-system` step 5.

## 0.10.0

- Each design system in the catalog says what a brand may adjust and what
  stays fixed (`limits`); `check_overlay` refuses a row that changes a fixed
  part, and any row for a system used as published (GOV.UK, Polaris).
- The CSS token prefixes of each system (`css_tokens`), read from its own
  package files, so the render can be checked against it.
- The slice and verify steps measure each screen with layout-inspector's
  `check_design_system`: values outside the system's tokens and the
  overlay, and text contrast on the real render.

## 0.9.0

- Design catalog: documented design systems by category, with their owners,
  documentation, packages and licenses (read from the npm registry), and
  visual styles by family, each with its accessibility risks and the systems
  that carry it.
- `tracer-design-catalog`, an MCP server in the plugin (standard library
  Python): ranks systems and styles for a context, writes the starting
  `docs/tracer/design-system.md`, checks a brand overlay against its base and
  checks WCAG contrast.
- `/tracer:design-system`: the product is built on a documented design
  system; a style or a company's brand is an overlay of only what it
  changes, never an invented system. The contract, slice and verify steps
  read `design-system.md`.
- Four anti-patterns under consistency and identity: invented design system,
  overlay over the rules, a style taken for a system and a rebuilt base
  component.

## 0.8.0

- New list, delivery anti-patterns, checked by the verifier before reading a
  builder's report: hearsay as fact, someone else's work as one's own, done
  but not reachable, half the request reported as whole, spec read in part,
  context copied instead of checked, irreversible write with unchecked
  fields, one-environment architecture, inputs the contract does not list
  and silent end.
- Seven testing anti-patterns: baseline from the wrong commit, testing
  another build, tests that collide, a guard skipped instead of fixed, checks
  that change the person's state, a gate run differently and trace links
  that do not resolve.
- Two interface anti-patterns: choices the audience cannot make (effort) and
  unknown origin (trust and honesty).

## 0.7.0

- New anti-pattern family, composition and space: the screen gives space in
  proportion to the work. Ten entries: space against the task, columns by
  count instead of need, reserved space for nothing, side by side too narrow,
  embedded viewer too small, wide content in a narrow box, nested scroll
  traps, fixed proportions only, actions far from their content and no
  hierarchy.

## 0.6.0

- The anti-pattern catalog is organized by the principle each entry breaks,
  in twelve families: attention and place, the audience's language, effort,
  feedback and state, safety and recovery, orientation and navigation,
  consistency and identity, access, recognition, trust and honesty,
  permissions and visibility, and perceived speed. A screen is checked
  against each principle, not only the listed entries, and a new case is
  filed under the principle it breaks.
- 65 new interface anti-patterns (81 in all), among them lost place, focus
  dropped, feedback far from its cause, codes instead of names, formats of
  the machine, asking twice, progress that does not progress, success before
  it happened, work lost on error, dead ends, off-system look, numbers that
  do not add up, machine output as fact and hidden is not forbidden.
- Six new testing anti-patterns: tested as the wrong person, presence
  instead of meaning, one size only, perfect data only, tests bound to the
  clock and dependencies that never fail.
- The verifier checks every principle on the screen as a whole; the empathy
  round asks what would make the audience doubt what they see.

## 0.5.1

- The two anti-patterns added in 0.5.0 are generalized: changes out of sight
  (any action that changes data must bring the user to where the change
  happened, without a full page reload) and information the audience cannot
  read (no information, or access to it, in a type or form the audience does
  not understand).

## 0.5.0

- New principle: mock first, then straight to the MEV. The interface is built
  as a mock with every detail the client expects and validated by the outcome
  owner before production code; there is no proof of concept and no MVP.
  Phase 1 gains the mock step and its sign-off.
- Anti-pattern catalog: new item out of sight (adding a row does not bring
  it into view), raw formats for a non-technical audience (a JSON tab for
  human resources).
- Empathy round asks what the audience must never see and whether a new item
  lands in view.
- The rule against temporary architecture says stub, not mock, for a fake
  integration.

## 0.4.0

- Anti-pattern catalog: words where a picture reads faster, state shown only
  by color, interfaces built on data nobody provides, work lost by moving on.
- New testing anti-patterns list: reds explained away, done without a clean
  full run, evidence of the wrong target, fixtures that hide the contract,
  tests that leak the machine, happy path only, claims from reading code,
  broken test setup.
- Component floors: buttons and actions (icon plus label, one meaning per
  icon, no color-only state); uploads survive navigation.
- Definition of Ready: confirmed target and a running test environment with
  base failures recorded. Definition of Done: one clean full run.
- Verifier: evidence must show the target screen, signed in, on real data;
  interruption checks.
- Empathy round: asks what the audience recognizes faster as a picture.

## 0.3.0

- Templates ship inside the plugin; empathy round, critical flows and the
  UI/UX anti-pattern catalog.
