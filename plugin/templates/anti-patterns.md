# Anti-pattern catalog

Things an interface must not show or do, even if no requirement forbids them.
Every slice with an interface is checked against this list. Add an entry
whenever one is found after a slice was marked done.

```markdown
| Anti-pattern | How to detect |
| Internal data on screen: UUIDs, storage keys, ids, paths, stack traces | Scan the rendered text for id and path patterns |
| Asking for what the system knows: a URL, an id, a path | Review every input against the data the system holds |
| Lists without a way in: no search, preview, sort or empty state | Check every list against the component floors |
| Icons without labels, or text without hierarchy | Visual and accessibility inspection |
| Destructive action without confirmation or undo | Walk every delete or overwrite |
| Errors that explain nothing | Trigger each failure path of the critical flows |
| The same action solved two ways | Compare against the capability map |
| Inaccessible controls: no focus, no name, low contrast, small targets | Accessibility and layout inspection |
| Jargon the audience does not know | Compare labels with the audience profile |
| Silent states: no loading, success or error feedback | Walk the critical flows on a slow connection |
| Words where a picture reads faster: text-only buttons for common actions, statuses as plain words, numbers where a chart or thumbnail would do | Walk every toolbar, row action and status as the audience; ask what they would recognize at a glance |
| State shown only by color | Check every status in grayscale |
| Interface built on data nobody provides: a field, count or flag that no API fills | Render each screen with real data from the system, not fixtures |
| Work lost by moving on: leaving a screen or switching a tab cancels an upload, a save or a draft without warning | Start every long operation and navigate away mid-way |
| New item out of sight: adding a row or item leaves it off screen, with no scroll, focus or highlight on where it was created | Add an item to a list or table longer than the screen and check it lands in view, focused |
| Raw formats for a non-technical audience: a JSON, XML or raw-data view shown to people who do not read it (human resources, sales) | Compare every tab and panel with what the audience profile says they read |
```

## Testing anti-patterns

Things a test run must not do, even when it ends green. The verifier checks
them as part of the gates.

```markdown
| Anti-pattern | How to detect |
| A red explained away: "machine load", "flaky", "it already failed" without proof | Run the same tests on the base commit and compare the failure lists |
| Done without a clean full run: committing after a partial or timed-out suite | The last full-suite result is attached to the slice and is green, or every failure is on the base list |
| Evidence of the wrong target: a screenshot of the login page, another project, an unauthenticated URL | The evidence shows the target screen, signed in as the audience, with real data |
| Fixtures that hide the contract: tests pass on fields or shapes the real API never returns | One test per critical flow runs against the real API or a recorded real response |
| Tests that leak the machine: they depend on a binary, a path or a service that only the author's machine has | Run the suite with an isolated PATH and a clean environment |
| Only the happy path: no test interrupts, repeats or cancels the operation | Each critical flow has at least one interrupted or repeated path |
| Claims from reading code: "it works" without running it where the audience uses it | Every WORKS and CORRECT line has run evidence, or is marked unverified |
| Broken test setup: a module configured twice, shared state between tests | Tests pass alone and in random order |
```
