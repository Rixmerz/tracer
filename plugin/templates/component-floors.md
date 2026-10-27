# Component floors

The minimum each kind of component provides, before audience-specific
additions. A slice that builds or changes a component inherits its floor.
Add an entry whenever an expectation escapes.

```markdown
## Every component
- Keyboard operable, visible focus, accessible name
- Contrast at WCAG 2.2 AA, touch targets at least 24×24 px
- Loading, empty, error and success states
- Labels in the audience's words

## Buttons and actions
- Common actions (add, edit, delete, download, search, close) carry a
  recognizable icon, with its text label next to it
- Icon-only buttons only for universal icons in dense rows or toolbars, each
  with a tooltip and an accessible name
- One icon, one meaning across the whole product
- Status shown with icon or shape plus text, never color alone

## Navigation bar
- Icons with text labels
- Visible active section
- Landmark and accessible names
- Collapsed version on small screens

## File list or file picker
- Real file names, never storage keys or UUIDs
- Search or filter by title
- Thumbnail or type icon, size and date
- Pick from a list; never ask for a URL or path
- Empty state with the first action
- Upload errors that name the limit before the file is lost
- An upload in progress survives switching folders or tabs, or warns before
  it is cancelled

## Table or list of records
- Search, sort and pagination once it can exceed one screen
- Readable values, never raw ids
- Row actions reachable by keyboard

## Form
- Labels on every field, required fields marked
- Inline validation next to the field, in plain words
- Input preserved after an error
- One clear primary action

## Destructive action
- Confirmation that names what will be lost, or undo
```
