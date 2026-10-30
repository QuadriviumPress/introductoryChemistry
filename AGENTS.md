# AGENTS.md

## Standard

This book follows the [QuadriviumPress MyST baseline](https://github.com/QuadriviumPress/bindery/blob/main/doc/myst-baseline.md) and the [presentation skill](https://github.com/QuadriviumPress/bindery/blob/main/skills/quadrivium-myst-presentation/SKILL.md).

## Commands

```bash
npm run start
npm run build
npm run verify
npm run check
npm run convert -- /path/to/text_introductory-chemistry
```

`npm run check` is the production-equivalent verification and HTML build.

`npm run convert` rebuilds `chapters/`, `license.md`, `myst.yml`, and `images/figures/` from a checkout of [saylordotorg/text_introductory-chemistry](https://github.com/saylordotorg/text_introductory-chemistry). It is not part of `check`.

## Intentional differences

- One Markdown file per source section, `chapters/ch-NN-sMM-slug.md`, because the chapters are too long to review as single files.
- `convert` runs `python3 scripts/html_to_myst.py`. It uses Pillow, when installed, to turn CMYK JPEGs into RGB and to shrink figures over 1 MB so the HTML build can encode them.
- `verify` checks MyST metadata, that every TOC page exists, that local images exist, and that cross-references and solution targets resolve.
- Openly licensed replacements for 22 upstream figure omissions live in `images/restored/`, with credits, licenses, alt text, and SHA-256 hashes in `manifest.json`. `verify` checks these records and their figure blocks. `convert` runs `scripts/restore_figures.py` after conversion to preserve the replacements and their license notice.

## Presentation gap

Worked examples and end-of-section problems use `{exercise}` with `{solution}` dropdowns. The source’s own “Example N” and “Exercise N” labels stay in the problem text, because later sentences cite those numbers. Even-numbered answers were not in the student HTML. Display math is `$$` rather than numbered `{math}` blocks; the source does not cross-reference equation numbers. Cancellation strokes on units are not drawn; KaTeX rejects the combining strike used for them, and the sentence above each factor still says the unit cancels. Margin definitions from the HTML are kept in parentheses after the bold term.
