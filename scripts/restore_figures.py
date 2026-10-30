#!/usr/bin/env python3
"""Insert the licensed replacements for figure omissions in the Saylor HTML."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "images" / "restored" / "manifest.json"


def figure_block(figure):
    """Render one numbered figure or unnumbered photo group with its credits."""
    first, *others = figure["assets"]
    body = f'**{figure["title"]}.** {figure["caption"]}'
    for asset in others:
        body += f'\n\n![{asset["alt"]}](../images/restored/{asset["file"]})'
    credits = [
        f'[{asset["title"]} — {asset["credit"]}]({asset["source"]}), '
        f'[{asset["license"]}]({asset["license_url"]})'
        for asset in figure["assets"]
    ]
    body += "\n\nCredits: " + "; ".join(credits) + ". Images resized for the web."
    if any("White background added" in asset.get("changes", "") for asset in figure["assets"]):
        body += " White background added for legibility."
    numbering = (
        f':enumerator: {figure["number"]}'
        if figure.get("number") else ":enumerated: false"
    )
    return (
        f'```{{figure}} ../images/restored/{first["file"]}\n'
        f':label: {figure["label"]}\n{numbering}\n:alt: {first["alt"]}\n'
        f':align: center\n:width: {figure.get("width", "70%")}\n\n{body}\n```'
    )


def existing_block(text, label):
    """Find the generated directive, excluding standalone legacy targets."""
    match = re.search(rf"(?m)^:label: {re.escape(label)}$", text)
    if not match:
        return None
    start = text.rfind("```{figure}", 0, match.start())
    end = text.find("\n```", match.end())
    if start < 0 or end < 0:
        raise ValueError(f"Incomplete figure directive: {label}")
    return start, end + 4


def insertion_position(text, anchor, unique=True):
    """Place images after the containing paragraph or enclosing callout.

    Keeping new figure fences outside the existing callouts avoids closing an
    outer three-backtick fence and keeps the original exercises intact.
    """
    count = text.count(anchor)
    if not count or (unique and count != 1):
        raise ValueError(f"Invalid insertion anchor ({count} matches): {anchor}")
    position = text.index(anchor)
    stack = []
    for match in re.finditer(r"(?m)^(`{3,})([^\n]*)$", text[:position]):
        fence, rest = match.groups()
        if not rest.strip():
            if stack and len(fence) >= stack[-1]:
                stack.pop()
        elif not stack or len(fence) > stack[-1]:
            stack.append(len(fence))
    if stack:
        for match in re.finditer(r"(?m)^(`{3,})[ \t]*$", text[position:]):
            if len(match[1]) >= stack[0]:
                return position + match.end()
        raise ValueError(f"Unclosed callout around {anchor}")
    end = text.find("\n\n", position)
    return len(text.rstrip()) if end < 0 else end


def update_periodic_names():
    """Keep the adjacent source data table consistent with the new diagram.

    Atomic masses remain the source edition's values; the text explicitly
    identifies them as such and points to CIAAW for current atomic weights.
    """
    page = ROOT / "chapters/ap-periodic-table.md"
    text = page.read_text(encoding="utf-8")
    names = {
        113: ("nihonium", "Nh"), 114: ("flerovium", "Fl"),
        115: ("moscovium", "Mc"), 116: ("livermorium", "Lv"),
        117: ("tennessine", "Ts"), 118: ("oganesson", "Og"),
    }
    rows = {}
    for match in re.finditer(r"(?m)^\| ([^\n]+) \|$", text):
        cells = [cell.strip() for cell in match[1].split("|")]
        if len(cells) == 5 and cells[2].isdigit():
            number = int(cells[2])
            if number in names:
                name, symbol = names[number]
                cells[:2] = [name + r"\*", symbol]
            rows[number] = cells
    rows.setdefault(117, [r"tennessine\*", "Ts", "117", "", ""])
    if len(rows) != 118:
        raise ValueError(f"Expected all 118 elements in the appendix; found {len(rows)}")
    start = text.index("| actinium")
    end = text.index("\n\n", start)
    body = "\n".join(
        "| " + " | ".join(cell or " " for cell in cells) + " |"
        for cells in sorted(rows.values(), key=lambda row: row[0])
    )
    text = text[:start] + body + text[end:]
    old = "represent the number of decimal places recognized by the International Union of Pure and Applied Chemistry, the worldwide body that develops standards for chemistry."
    new = (
        "are retained from the source edition, with element names and symbols updated "
        "to their modern forms. For current standard atomic weights, consult the "
        "[Commission on Isotopic Abundances and Atomic Weights](https://ciaaw.org/atomic-weights.htm)."
    )
    text = text.replace(old, new)
    page.write_text(text, encoding="utf-8")


def restore_figures():
    figures = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for figure in figures:
        page = ROOT / figure["page"]
        text = page.read_text(encoding="utf-8")
        label = figure["label"]
        citation = f'Figure {figure.get("number")} "{figure["title"]}"'
        block = existing_block(text, label)
        if block:
            start, end = block
            text = text[:start].rstrip() + "\n\n" + figure_block(figure) + "\n\n" + text[end:].lstrip("\n")
        else:
            # A partial legacy figure can have a target, image, and caption
            # inside a callout. Remove that fragment before adding its complete
            # replacement after the callout.
            if figure.get("remove_legacy"):
                pattern = figure["remove_legacy"]
                text, count = re.subn(pattern, "", text, flags=re.MULTILINE)
                if count != 1:
                    raise ValueError(f"Expected one legacy figure to replace: {label}")
            if figure.get("after_label"):
                previous = existing_block(text, figure["after_label"])
                if not previous:
                    raise ValueError(f"Missing preceding figure: {figure['after_label']}")
                paragraph_end = previous[1]
            else:
                anchor = figure.get("anchor", citation)
                paragraph_end = insertion_position(text, anchor, unique="anchor" in figure)
            text = text[:paragraph_end].rstrip() + "\n\n" + figure_block(figure) + "\n\n" + text[paragraph_end:].lstrip("\n")
        for old, new in figure.get("text_replacements", {}).items():
            text = text.replace(old, new)
        page.write_text(re.sub(r"\n{3,}", "\n\n", text), encoding="utf-8")
        if figure.get("number"):
            reference = f"{{ref}}`{citation} <{label}>`"
            for other in (ROOT / "chapters").glob("*.md"):
                original = other.read_text(encoding="utf-8")
                # Match plain source citations without nesting existing refs.
                updated = re.sub(r"(?<!\{ref\}`)" + re.escape(citation) + r"(?! <)", reference, original)
                if updated != original:
                    other.write_text(updated, encoding="utf-8")

    update_periodic_names()
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
    print(f"Prepared {restore_figures()} licensed figure groups.")
