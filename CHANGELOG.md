# Changelog

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
