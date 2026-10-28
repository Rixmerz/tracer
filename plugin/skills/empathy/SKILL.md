---
description: Run the TRACER empathy round on one capability or all of them - see it from its audience's side, classify expectations, improve and add specs, write critical flows (phase 1)
argument-hint: "[capability name; defaults to every capability in the map]"
disable-model-invocation: true
---

Run the empathy round on "$ARGUMENTS" (if empty, every capability in
`docs/tracer/capabilities.md`). Follow the `tracer` skill's rules. No
production code is written in this command.

Read first: `docs/tracer/contract.md`, `docs/tracer/audiences.md`,
`docs/tracer/floors.md`, `docs/tracer/anti-patterns.md` and the capability's
base-round specs. If there is no audience profile, stop and run the profile
step of `/tracer:contract` first.

## 1. See it from the audience's side

For each capability, and each audience that uses it, answer in
`docs/tracer/empathy/<capability>.md` (empathy review template:
`${CLAUDE_PLUGIN_ROOT}/templates/empathy-review.md`):

1. What are they trying to get done, in their words?
2. What do they know, and what do they not?
3. Where would they get stuck or frustrated?
4. What do they take for granted?
5. What has the product genre taught them to expect?
6. What would they recognize faster as a picture than as words: an icon on
   an action, a thumbnail, a chart, a status badge?
7. What information, or access to it, would they not understand? It must
   not be shown to them in that form.
8. After each action that changes something, do they land where the change
   happened, in view and focused, without the whole page reloading?

Never answer with the most common solution you know for that kind of
product. Answer from the profile: a human resources team picking training
material expects titles, thumbnails and search, not storage paths.

## 2. Classify the expectations

List every expectation found, each classified as **basic** (its absence makes
the product feel broken), **performance** (more is better) or
**differentiator** (not expected, valued). Check the capability against the
anti-pattern catalog and record each risk as a basic expectation.

Check duplication: search the capability map and livespec `search_similar`
for an existing capability that already covers this behaviour. If one does,
propose extending it instead.

## 3. Let the outcome owner decide

Present the list as a table and ask the user to accept or reject each line.
Apply the MEV rule to the accepted ones:

- Basic expectations of a capability in the cut: enter the MEV.
- Performance expectations: enter if they move the metric, otherwise the
  scope filter.
- The product as a whole: at least one deliberate differentiator.
- Everything left out: `docs/tracer/deferred.md`, with its reason.

## 4. Write the result into the specs

1. **Improve** existing requirements: new scenarios and CORRECT lines.
2. **Add** new requirements for what the base round missed.
3. Mark both as born in the empathy round.
4. **Critical flows** in `docs/tracer/flows/<capability>.md` (template:
   `${CLAUDE_PLUGIN_ROOT}/templates/critical-flow.md`):
   at least one per capability, with its success path and failure paths
   (invalid input, network or server error, no permission, empty data, plus
   domain-specific ones). Every criterion has a WORKS half and a CORRECT
   half; every CORRECT line must be checkable by someone driving the
   interface.
5. **Floors:** list the components the capability uses and their inherited
   floors.

Validate the specs (livespec `sync_openspec`, then `validate_openspec`).

End with: expectations found per level, accepted, deferred, specs improved
and added (the empathy yield), and critical flows written.
