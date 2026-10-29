# Introductory Chemistry

MyST Markdown edition of *Introductory Chemistry*, a one-semester open textbook. The text is David W. Ball’s version 1.0 as published in HTML by Saylor Academy.

## Source and license

The textbook content is © the upstream authors and adapters and is licensed under [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/). See [`LICENSE-CONTENT.md`](LICENSE-CONTENT.md), [`license.md`](license.md), and [`SOURCES.md`](SOURCES.md).

The Saylor HTML edition is [saylordotorg/text_introductory-chemistry](https://github.com/saylordotorg/text_introductory-chemistry), also readable at [saylordotorg.github.io/text_introductory-chemistry](https://saylordotorg.github.io/text_introductory-chemistry/index.html). Saylor Academy adapted that HTML from the version maintained by Andy Schmitz. This edition names David W. Ball as the author of the underlying text. Details and the Saylor wording about attribution are in `SOURCES.md`.

Build scripts and the web-app shell come from the QuadriviumPress MyST template and remain under the [MIT License](LICENSE).

## Build

```bash
npm ci
npm run start
npm run verify
npm run build
npm run check
```

The site is written to `_build/html`. Set `BASE_URL` when testing a project-site deployment locally:

```bash
BASE_URL=/introductoryChemistry npm run build
```

To regenerate the Markdown from a fresh clone of the Saylor repository:

```bash
npm run convert -- /path/to/text_introductory-chemistry
```

## Layout

| Path | Purpose |
| --- | --- |
| `myst.yml` | Title, license, authors, and table of contents |
| `chapters/` | One section per file, `ch-NN-sMM-slug.md` |
| `images/figures/` | Figures copied from the Saylor HTML edition |
| `license.md` | License statement from the source edition |
| `SOURCES.md` | Provenance for the text and figures |
| `scripts/html_to_myst.py` | HTML to MyST conversion |
