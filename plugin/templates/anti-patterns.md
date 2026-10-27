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
```
