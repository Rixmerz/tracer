# Example 4. A retrospective

`/tracer:retro` on example 1, two weeks after launch. Sources: the decision
log (8 entries), the canvas version list (14 versions), the client's
screenshots. Missing: the content of intermediate versions; the author of
version `1c45`.

## Errors and rework

| # | Error | Cause | Found by | Fix | Catalog entry |
| --- | --- | --- | --- | --- | --- |
| E1 | Client claims rewritten, call to action changed **[F]** | "Less explicit" read as "rewrite" **[I]** | The client | Content restored | Client words rewritten |
| E2 | Photo frame overflowing at some widths **[F]** | Frame sized from the column, not the photo **[F]** | The client | Shadow on the image itself | Ornament that does not fit its medium |
| E3 | Orphaned fifth stage **[F]** | `auto-fit` with five items **[F]** | The client | Five fixed columns | Orphans in a grid |
| E4 | Timeline text touching its line **[F]** | `.tl>div` over `<li>` **[F]** | The client | `.tl>li` | Selectors that match nothing |
| E5 | Publish over version `1c45` **[F]** | Live version not compared **[F]** | The builder, after | Client told | Published over a version not read |

## The pattern

E2, E3 and E4 are visible on the render and invisible in the code **[F]**.
None was found before the client, because no render check ran **[F]**: the
host forbade it. The missing gate is the render check; the method's answer
is the verification request, which was not yet part of TRACER **[I]**.

## Improvements

- To this project: the verification request goes with every publish.
- To TRACER: the "Identity, not template" family, the content inventory,
  the "built, not verified" status (all in 0.11.0).
