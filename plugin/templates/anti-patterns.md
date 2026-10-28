# Anti-pattern catalog

Things an interface must not show or do, even if no requirement forbids them.
Every slice with an interface is checked against this catalog.

The entries are grouped by the principle they break. Check each screen
against the principles, not only against the entries: a case that breaks a
principle is an anti-pattern even when no entry names it yet. Whenever one is
found after a slice was marked done, add it under the principle it breaks; if
no principle fits, add a new family with its principle.

```markdown
## 1. Attention and place

Principle: after every action the person sees its result where it happened,
and nothing moves them away from where they were working.

| Anti-pattern | How to detect |
| --- | --- |
| Changes out of sight: after an action changes something (add, edit, move, delete, save), the view does not bring the person to where the change happened, or reloads the whole page instead of updating in place | Run every action that changes data on a screen longer than the viewport; check the change lands in view and focused, with no full reload |
| Lost place: coming back from a detail, a dialog, a save or the back button resets the scroll position, filters, sorting, page, selected tab or expanded rows | Set filters, scroll, open an item and come back by every route: back button, close, save, cancel |
| Focus dropped: closing a dialog or menu, deleting an item or finishing a step leaves keyboard focus on the page body instead of the trigger or the next logical element | Do each of these with the keyboard only and see where focus lands |
| Feedback far from its cause: the result or error of an action appears where the person is not looking (a corner message for a field error, an error at the top of a long form, a problem on another tab) | For each action, check its feedback appears next to what caused it, or the view moves to it |
| Content that jumps: the layout shifts while loading or updating, so content moves under the pointer or the reading position | Load each screen on a slow connection and interact during the load; measure layout shift |
| Silent reordering: an item jumps to another position after an edit or a refresh, with nothing to show where it went | Edit the field a list is sorted by and check the item can still be found and is pointed to |
| Side effects out of sight: an action also changes other things (totals, other rows, other screens) and nothing shows what else changed | List each action's side effects and check every one is visible or announced |
| Updates over the person's work: a background refresh or someone else's change replaces what the person is reading or editing, without notice | Edit a record while it changes from another session |

## 2. The audience's language

Principle: every piece of information, and every way to reach it, is in a
type and form the audience understands; the system's own model stays inside
the system.

| Anti-pattern | How to detect |
| --- | --- |
| Information the audience cannot read: showing information, or giving access to it, in a type or form the audience does not understand (raw data, technical formats, internal codes) | Compare every piece of information and every way to reach it with what the audience profile says they read |
| Internal data on screen: UUIDs, storage keys, ids, paths, stack traces | Scan the rendered text for id and path patterns |
| Codes instead of names: enum values, status codes, abbreviations or internal codes shown without the name the audience uses | Scan the rendered text for upper-case codes and abbreviations; compare them with the audience's words |
| Jargon the audience does not know | Compare labels with the audience profile |
| Formats of the machine: dates, times, numbers, currency, units and sizes in a raw or foreign format (ISO dates, UTC times, bytes, the wrong decimal separator, amounts without currency) | Compare every formatted value with the audience's locale and habits |
| Precision nobody uses: more digits, decimals or time detail than the person's decision needs | Ask, for each number, what the audience decides with it |
| Empty that says nothing: missing values shown as null, undefined, NaN, 0, [object Object] or a bare blank | Render every screen with incomplete records |
| Mixed languages: parts of the interface in a language other than the rest (system values, library defaults, untranslated errors, dates) | Scan the rendered text in every state, including dialogs and validation messages |
| Screens shaped like the database: navigation and screens follow tables, entities or endpoints instead of the tasks the audience does | Map each audience task to the screens it crosses; a task spread over several entity screens is a warning |
| Everything at the same weight: every field, value and action shown at once with the same prominence | Ask what the audience looks at first on each screen and check it stands out |

## 3. Effort

Principle: the person provides only what only they know, once, in the form
that is easiest for them.

| Anti-pattern | How to detect |
| --- | --- |
| Asking for what the system knows: a URL, an id, a path | Review every input against the data the system holds |
| Asking twice: data the person already gave, in this flow or an earlier one, is asked again | Walk each flow, list every input and mark the ones the system already holds |
| Typing what could be picked: free text for a value from a known set (a client, a code, a place) | Review every text input against the lists the system holds |
| Rigid formats: rejecting input the system could normalize (spaces, dots, case, separators, pasted text) | Enter each field the ways the audience writes it |
| Hidden rules: requirements revealed only after they are broken (password rules, file limits, required fields) | Read every form before submitting; every rule must be visible before it can be broken |
| Validation at the wrong time: errors before the person finishes typing, or only after a long form is submitted | Fill each form field by field and watch when errors appear |
| Frequent action buried: the action the audience does most needs menus, mode switches or extra steps | Count the steps of the audience's most frequent tasks |
| One by one where they work in batches: no bulk action when the audience handles many items at a time | Compare the audience's volumes with the actions available |
| Missing or wrong defaults: no default where one value is the usual one, or a default the audience almost always changes | Check each default against real data |
| Choices the audience cannot make: the person must pick among technical variants (platform, version, format, build) that the system could detect or that a single universal option would cover | List every choice the person makes; for each, ask whether the audience can answer it without help and whether the system could decide it |

## 4. Feedback and state

Principle: every action shows that it started, how it is going and how it
ended, and every object shows the state it is in.

| Anti-pattern | How to detect |
| --- | --- |
| Silent states: no loading, success or error feedback | Walk the critical flows on a slow connection |
| Progress that does not progress: an indicator that does not reflect real progress (stuck at 0 %, jumping from 0 to 100, spinning forever) | Run each long operation on a slow connection and with a large input; compare the indicator with what is happening |
| Success before it happened: success shown before the system confirms it, or an optimistic change not undone when it fails | Make the server fail after each action and check what the screen says |
| Ambiguous state: the person cannot tell whether something is a draft, saved, sent, validated or published | For each object, tell its state from the screen alone, as the audience |
| Unsaved without a sign: changes not saved yet look the same as saved ones | Edit without saving, look at the screen, then try to leave |
| Double submission: an action stays available while it runs, so a second click repeats it | Double-click every action that writes and check for duplicates |
| Disabled without a reason: an unavailable action gives no hint of what is missing | Hover and focus every disabled control |
| Errors that explain nothing | Trigger each failure path of the critical flows |
| Errors in the system's words: codes, exception names, HTTP statuses or validation-library output reach the person | Trigger each failure path and read the message as the audience |

## 5. Safety and recovery

Principle: mistakes are cheap. Whatever loses or changes something can be
prevented, previewed or undone, and work is never lost by accident.

| Anti-pattern | How to detect |
| --- | --- |
| Destructive action without confirmation or undo | Walk every delete or overwrite |
| Work lost by moving on: leaving a screen or switching a tab cancels an upload, a save or a draft without warning | Start every long operation and navigate away mid-way |
| Work lost by time: a session expires mid-task and the work in progress is lost | Let the session expire in the middle of each long form and each upload |
| Work lost on error: a failed submit clears what the person entered | Make each submit fail and check every input is still there |
| Consequences hidden: an action that affects many items or other people does not say how many or which before it runs | Read what each bulk or shared action shows before it is confirmed |
| Danger next to routine: destructive actions placed or styled like frequent ones | Inspect every toolbar and row; destructive actions are set apart and marked |
| Confirmation by habit: everything asks for confirmation, or dialogs say "OK" and "Cancel" instead of naming the action, so people confirm without reading | Read every dialog; only risky actions ask, and their buttons name the action |
| No way back: a step, a submission or a status change cannot be corrected when correcting it is normal for the audience | Try to fix a mistake after each step of each flow |

## 6. Orientation and navigation

Principle: every screen says where the person is and what they can do next,
and lets them leave and come back.

| Anti-pattern | How to detect |
| --- | --- |
| Lists without a way in: no search, preview, sort or empty state | Check every list against the component floors |
| Dead ends: a screen or state with no next step (after a success, after an error, an empty list) | Reach every end state and look for the next action |
| Where am I: no title, active section or path shows the current place | Open each screen from a direct link and say where you are |
| State not in the address: the address does not reflect the view, so it cannot be reloaded, shared or reached again with back and forward | Reload and share each view; use back and forward |
| Hidden features: something can only be reached by knowing an address or a gesture | Map every capability to a visible way in |
| Stacked layers: dialogs over dialogs, or drawers over dialogs | Walk the flows and count the open layers |
| Leaving without asking: links open new tabs or windows, or move the person to another product, without saying so | Follow every link and external action |

## 7. Consistency and identity

Principle: the same thing is named, looks and works the same everywhere, and
the product looks like one product built from its design system.

| Anti-pattern | How to detect |
| --- | --- |
| The same action solved two ways | Compare against the capability map |
| Words that drift: one word with two meanings, or two words for one meaning, across screens | Build the glossary from the rendered text and look for duplicates |
| Off-system look: colors, type, spacing or components that do not come from the product's design system or identity | Compare the rendered styles with the design system's tokens and scan the code for raw values |
| Moving controls: the primary action, save or close sits in a different place on each screen | Compare the position of common actions across screens |
| One component, several behaviours: the same component validates, sorts or saves differently on two screens | Compare each repeated component's behaviour across screens |

## 8. Access

Principle: everyone in the audience profile can perceive and operate every
part of the interface, on their devices and in their context.

| Anti-pattern | How to detect |
| --- | --- |
| Inaccessible controls: no focus, no name, low contrast, small targets | Accessibility and layout inspection |
| State shown only by color | Check every status in grayscale |
| Motion without control: animations that cannot be reduced, or that run on their own | Turn on reduced motion and check every animation |
| Time limits the person cannot extend: timeouts, auto-advancing content, expiring forms | Do each task slowly |
| The audience's device left out: the interface breaks, scrolls sideways or shrinks its targets on the devices and sizes the profile names | Run every critical flow at each device size of the profile |
| Text in images: information only inside an image, with no text alternative | Scan for images that carry text or data |

## 9. Recognition

Principle: people recognize at a glance instead of reading or remembering.

| Anti-pattern | How to detect |
| --- | --- |
| Words where a picture reads faster: text-only buttons for common actions, statuses as plain words, numbers where a chart or thumbnail would do | Walk every toolbar, row action and status as the audience; ask what they would recognize at a glance |
| Icons without labels, or text without hierarchy | Visual and accessibility inspection |
| Recall instead of recognition: a step needs a value, a code or something from a previous screen that the person must remember | Walk each flow without taking notes |
| Lookalike items: items that differ only in a detail the person must read to tell them apart | Look at lists of real data and pick the right item at a glance |
| Truncated with no way to the whole: values cut off with no way to see them in full | Render the longest real values |

## 10. Trust and honesty

Principle: what the screen says is true, current and traceable, and what a
machine produced is told apart from what a person confirmed.

| Anti-pattern | How to detect |
| --- | --- |
| Interface built on data nobody provides: a field, count or flag that no API fills | Render each screen with real data from the system, not fixtures |
| Numbers that do not add up: totals, counts or badges that do not match what they summarize (hidden filters, pages, rounding) | Recompute every total and count from the visible items and from the full data |
| Stale shown as current: cached or old data with no sign of its age | Change the data elsewhere and look at the screen; look for when it was last updated |
| Machine output as fact: automated or AI-generated content presented as confirmed, with no mark of what the machine filled and what a person validated | Find every machine-filled value and check it stays marked until a person confirms it |
| Unknown origin: items with no record of who or what created or last changed them, so the person cannot tell their own from what someone or something else added | Pick items created by different people and by automations; check each one says who or what made it and when |
| Leftover demo data: placeholder text, sample records or test users in a real environment | Scan the rendered text and data of the target environment |
| Search and sort that mislead: search only over the loaded page, numbers or dates sorted as text | Search for an item on another page; sort values like 9 and 10, and dates across months |
| Pressure and tricks: pre-selected choices, hidden ways out, shaming wording, false urgency | Read every choice and every way to cancel as the audience |

## 11. Permissions and visibility

Principle: each person sees what they need and may use, and nothing else.

| Anti-pattern | How to detect |
| --- | --- |
| Offering what will be refused: actions shown to people who may not use them, refused only after the work is done | Walk each flow as each role |
| Seeing what is not theirs: data of other people, clients or teams shown to someone who should not see it | Sign in as each audience and compare what they see with what they may see |
| Tools for another audience: administration, debugging, export or configuration tools shown to an audience that does not need them | Compare every control with the audience profile |
| Hidden is not forbidden: an action hidden in the interface still works through its address or the API | Call each hidden action directly as a role that may not use it |

## 12. Perceived speed

Principle: the person keeps working while the system works, and waits only
for what they asked for.

| Anti-pattern | How to detect |
| --- | --- |
| Blocking for a local action: a whole-screen loader for an action that affects one element | Run each action and note what becomes unusable while it runs |
| All before anything: nothing is shown until everything has loaded | Load each screen on a slow connection |
| Trapped while waiting: a long operation cannot be left, cancelled or picked up later | Start each long operation and try to do something else |

## 13. Composition and space

Principle: the screen gives space in proportion to the work: what the person
reads or compares gets the most room, what they check once gets the least,
and nothing important is squeezed, cut or pushed out of view by the layout.

| Anti-pattern | How to detect |
| --- | --- |
| Space against the task: the element the person works on (the source to read, the form to fill, the table to edit) gets a narrow share of the screen while secondary content takes as much or more | Name the main task of the screen and measure the share of the viewport its element gets at common widths |
| Columns by count, not by need: the screen is split into equal or fixed columns regardless of their content, so one is crammed while another sits mostly empty | Load the screen with real data, with little and with a lot, and measure each region's used and empty space |
| Reserved space for nothing: a region keeps its room when it has little or nothing to show (an empty list, a short notice) | Load cases where each region is empty or short and check its space goes to the rest |
| Side by side too narrow: things meant to be compared (an original and its extraction, before and after) sit next to each other only when each is too narrow to read, or they are not side by side at all | Compare them at common widths; check each is readable at its own size without zooming or horizontal scroll |
| Embedded viewer too small: a document, map or preview is shown in a box so small the person must zoom, scroll inside it or open it elsewhere to read it | Open real documents in the viewer at common widths and try to read a line without zooming |
| Wide content in a narrow box: a table, code or form with many fields is placed in a region narrower than it needs, so it scrolls sideways, wraps columns into nonsense or cuts values | Fill the widest content with real values and check nothing scrolls sideways or is cut |
| Nested scroll traps: several regions scroll on their own inside a scrolling page, so the wheel or swipe moves the wrong one and the person loses where things are | Scroll with wheel, touch and keyboard over each region and note which one moves |
| Fixed proportions only: regions cannot be resized, collapsed or swapped when the task needs more room for one of them | Try to give more room to each region; check the main one can take the screen when needed |
| Actions far from their content: the actions for a region (save, add, confirm) sit in another region or at the far edge of the screen, out of sight while the person works | Do the main task and check each needed action is visible from where it happens |
| No hierarchy: every region has the same weight, padding and type size, so nothing tells the eye where to start | Look at the screen for five seconds and say what the main task is; ask someone from the audience |
```

## Testing anti-patterns

Things a test run must not do, even when it ends green. The verifier checks
them as part of the gates.

Principle: a green run is evidence only when it ran in full, as the audience,
under the conditions the audience lives in; a red is pre-existing only when it
also fails on the base commit.

```markdown
| Anti-pattern | How to detect |
| --- | --- |
| A red explained away: "machine load", "flaky", "it already failed" without proof | Run the same tests on the base commit and compare the failure lists |
| Done without a clean full run: committing after a partial or timed-out suite | The last full-suite result is attached to the slice and is green, or every failure is on the base list |
| Evidence of the wrong target: a screenshot of the login page, another project, an unauthenticated URL | The evidence shows the target screen, signed in as the audience, with real data |
| Fixtures that hide the contract: tests pass on fields or shapes the real API never returns | One test per critical flow runs against the real API or a recorded real response |
| Tests that leak the machine: they depend on a binary, a path or a service that only the author's machine has | Run the suite with an isolated PATH and a clean environment |
| Only the happy path: no test interrupts, repeats or cancels the operation | Each critical flow has at least one interrupted or repeated path |
| Claims from reading code: "it works" without running it where the audience uses it | Every WORKS and CORRECT line has run evidence, or is marked unverified |
| Broken test setup: a module configured twice, shared state between tests | Tests pass alone and in random order |
| Tested as the wrong person: verification signed in as an administrator or the developer's account instead of the audience's role | Every piece of evidence names the account and role it ran as; the critical flows run as each audience |
| Presence instead of meaning: tests assert that an element exists, not what the audience reads in it (its text, value or state) | Read the assertions of each critical-flow test |
| One size only: the suite runs at a single viewport while the audience uses several devices | Run the end-to-end suite at each device size of the audience profile |
| Perfect data only: tests run on empty or tidy data, never on the volumes, lengths and gaps of real data | Seed a run with the largest, longest and most incomplete real records |
| Tests bound to the clock: results depend on today's date or the time zone | Run the suite in another time zone and on a date at a month or year boundary |
| Dependencies that never fail: every external service is faked only in its success | Each external dependency has at least one failing-path test |
| Baseline from the wrong commit: failures compared against a commit other than the slice's real base, so new failures pass as old ones | The base list names the commit the slice branched from, and that commit is the branch's merge base |
| Testing another build: the run loads a cached package, an installed copy, an old jar or a stale bundle instead of the code in the slice | The run prints or asserts the path and version of what it loaded, and it is the working tree |
| Tests that collide: tests share host resources (fixed ports, emulators, files, global services) and fail when another run or process holds them | Run the suite twice at once, and once with the usual ports already taken |
| A guard skipped instead of fixed: a hook, lint or check bypassed (no-verify, skip flags, disabled rules) because it fired | Search the slice's commits and scripts for bypass flags; each one has a written reason, or the false positive is fixed in the guard |
| Checks that change the person's state: a test or verification writes to the person's index, checkout, home, processes or real services | Snapshot the git index, the working tree and running processes before and after the full run; they are identical |
| A gate run differently: the local check uses other flags, ports, filters or commands than the pipeline, or a command that does not exist, or leaves the test code itself unchecked (types, lint) | The slice's evidence shows the exact command of the pipeline, and it covers the test files |
| Trace links that do not resolve: requirement ids or spec links are written but the traceability tool cannot resolve them (length, format, derivation mismatch) | Ask the traceability tool for each requirement's code and tests; every one returns links |
```

## Delivery anti-patterns

Things a builder's report or hand-over must not do, even when the code is
right. The verifier checks them before reading the report as evidence.

Principle: what the builder reports is true, checked first-hand, complete and
already reachable by its audience; what was not done or not verified is said
so.

```markdown
| Anti-pattern | How to detect |
| --- | --- |
| Hearsay as fact: a claim about code, data or state repeated from a summary, another agent, a comment or a config, without checking the thing itself | Every claim in the report points to the file, command or screen that shows it; a claim taken from someone else is marked as theirs |
| Someone else's work as one's own: the report says "I changed" for what another worker, a previous attempt or the person did | Compare the report's authorship with the commits and task history |
| Done but not reachable: work committed but not pushed, released, versioned, listed or deployed where the audience gets it | Get the slice the way the audience does (install, update, open the environment) and find the change |
| Half the request, reported as whole: steps, criteria or findings left out with no mention | Map every item of the request and its acceptance criteria to evidence or to an explicit "not done" |
| Spec read in part: the work starts from a truncated, empty or wrong-project request instead of the full one | The slice cites the full request and its source; an empty or cut request stops the work instead of being guessed |
| Context copied, not checked: a classification, parent, owner, label or setting is copied from the previous item instead of chosen for this one | For each such field, check it against the item's own content |
| Irreversible write with unchecked fields: an action that cannot be undone with the available tools (create, publish, send, delete) runs before its fields are confirmed | List the slice's irreversible actions; each one shows its fields were checked before it ran |
| One-environment architecture: configuration, origins, secrets or names fit the local machine and ignore how the existing product is deployed in every environment | Compare each setting with the pattern the product already uses in each environment |
| Inputs the contract does not list: a tool, command or interface accepts a closed set of values but does not state it, so callers invent one | Read each contract the slice adds; every closed set of values is listed where callers read it |
| Silent end: the work stops without a result, or narrates progress that did not happen | The last message states the outcome; every "done" or "sent" in it has its evidence |
```
