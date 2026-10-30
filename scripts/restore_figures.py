#!/usr/bin/env python3
"""Insert the licensed replacements for figure omissions in the Saylor HTML."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "images" / "restored" / "manifest.json"


def restore_figures():
    figures = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for figure in figures:
        page = ROOT / figure["page"]
        text = page.read_text(encoding="utf-8")
        label = figure["label"]
        citation = f'Figure {figure["number"]} "{figure["title"]}"'
        # Idempotent when invoked on the checked-in Markdown.
        if f":label: {label}\n" in text:
            continue
        if citation not in text:
            raise ValueError(f"Missing insertion citation {citation} in {page}")
        position = text.index(citation)
        paragraph_end = text.find("\n\n", position)
        if paragraph_end < 0:
            raise ValueError(f"Missing paragraph boundary in {page}")
        assets = figure["assets"]
        first = assets[0]
        body = f'**{figure["title"]}.** {figure["caption"]}'
        for asset in assets[1:]:
            body += f'\n\n![{asset["alt"]}](../images/restored/{asset["file"]})'
        credits = []
        for asset in assets:
            credits.append(
                f'[{asset["title"]} — {asset["credit"]}]({asset["source"]}), '
                f'[{asset["license"]}]({asset["license_url"]})'
            )
        body += "\n\nCredits: " + "; ".join(credits) + ". Images resized for the web."
        directive = (
            f'\n\n```{{figure}} ../images/restored/{first["file"]}\n'
            f':label: {label}\n:enumerator: {figure["number"]}\n:alt: {first["alt"]}\n'
            f':align: center\n:width: 70%\n\n{body}\n```'
        )
        text = text[:paragraph_end] + directive + text[paragraph_end:]
        # Replace prose citations, including citations on other pages below.
        page.write_text(text, encoding="utf-8")
        reference = f"{{ref}}`{citation} <{label}>`"
        for other in (ROOT / "chapters").glob("*.md"):
            original = other.read_text(encoding="utf-8")
            if citation in original:
                other.write_text(original.replace(citation, reference), encoding="utf-8")

    # Keep the source example's numbers without claiming the replacement label
    # has the original (unavailable) label's 38 Calories.
    energy = ROOT / "chapters/ch-07-s01-energy.md"
    text = energy.read_text(encoding="utf-8")
    text = text.replace(
        'The label in {ref}`Figure 7.1 "Calories on Food Labels" <fig:ch07:s01:f01>` states that the serving has 38 Cal. How many joules is this?',
        'Suppose a food label like the one in {ref}`Figure 7.1 "Calories on Food Labels" <fig:ch07:s01:f01>` states that a serving has 38 Cal. How many joules is this?',
    )
    energy.write_text(text, encoding="utf-8")
    license_page = ROOT / "license.md"
    text = license_page.read_text(encoding="utf-8")
    if "## Separately licensed replacement figures" not in text:
        text += (
            "\n## Separately licensed replacement figures\n\n"
            "Replacement images added to fill omissions in the source edition retain "
            "their individual CC BY, CC BY-SA, CC0, or public-domain terms. "
            "Each caption links to the source and license. The textbook's "
            "CC BY-NC-SA license does not replace or restrict those image licenses. "
            "Full credits and the figure audit are in "
            "[Sources and attribution](https://github.com/QuadriviumPress/introductoryChemistry/blob/main/SOURCES.md).\n"
        )
        license_page.write_text(text, encoding="utf-8")
    return len(figures)


if __name__ == "__main__":
    print(f"Restored {restore_figures()} figure omissions.")
