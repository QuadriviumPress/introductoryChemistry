"""Reapply reviewed reference updates after conversion and figure restoration."""

from __future__ import annotations

import json
from pathlib import Path


UPDATES = Path(__file__).with_name("reference_updates.json")


def update_references(root: Path) -> int:
    """Apply exact, file-scoped edits; reject source drift before writing pages.

    Already updated pages are accepted so this can also update an existing
    checkout. The old text and expected occurrence counts make upstream changes
    visible instead of silently skipping an editorial correction.
    """
    updates = json.loads(UPDATES.read_text(encoding="utf-8"))["updates"]
    pages = {}
    for update in updates:
        page = root / update["page"]
        if page not in pages:
            pages[page] = page.read_text(encoding="utf-8")
        text = pages[page]
        old, new, count = update["old"], update["new"], update["count"]
        if text.count(new) == count and old not in text:
            continue
        if text.count(old) != count or new in text:
            raise ValueError(f"Reference update no longer matches {update['page']}: {old[:90]!r}")
        pages[page] = text.replace(old, new)
    for page, text in pages.items():
        if page.read_text(encoding="utf-8") != text:
            page.write_text(text, encoding="utf-8")
    return len(updates)


if __name__ == "__main__":
    print(f"Applied {update_references(Path(__file__).resolve().parents[1])} reference updates.")
