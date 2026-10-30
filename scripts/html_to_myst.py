#!/usr/bin/env python3
"""Convert the Saylor Academy Introductory Chemistry HTML tree to MyST.

Source repository:
https://github.com/saylordotorg/text_introductory-chemistry

Usage:
    python3 scripts/html_to_myst.py /path/to/text_introductory-chemistry
"""

from __future__ import annotations

import json
import os
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

from bs4 import BeautifulSoup, NavigableString, Tag

from restore_figures import MANIFEST, restore_figures
from update_references import update_references

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "chapters"
FIGURES = ROOT / "images" / "figures"

# Commands end with {} so a following letter is not swallowed (\Delta H, not \DeltaH).
COMMANDS = {
    "×": r"\times{}",
    "·": r"\cdot{}",
    "⋅": r"\cdot{}",
    "−": "-",
    "–": "-",
    "—": "---",
    "→": r"\rightarrow{}",
    "←": r"\leftarrow{}",
    "↔": r"\leftrightarrow{}",
    "⇔": r"\Leftrightarrow{}",
    "⇌": r"\rightleftharpoons{}",
    "⇋": r"\rightleftharpoons{}",
    "⇄": r"\rightleftarrows{}",
    "±": r"\pm{}",
    "≈": r"\approx{}",
    "≠": r"\neq{}",
    "≤": r"\leq{}",
    "≥": r"\geq{}",
    "∞": r"\infty{}",
    "÷": r"\div{}",
    "≡": r"\equiv{}",
    "∝": r"\propto{}",
    "°": r"^{\circ}",
    "′": "'",
    "″": "''",
    "%": r"\%",
    "α": r"\alpha{}",
    "β": r"\beta{}",
    "γ": r"\gamma{}",
    "δ": r"\delta{}",
    "ε": r"\epsilon{}",
    "θ": r"\theta{}",
    "λ": r"\lambda{}",
    "μ": r"\mu{}",
    "ν": r"\nu{}",
    "π": r"\pi{}",
    "ρ": r"\rho{}",
    "σ": r"\sigma{}",
    "φ": r"\phi{}",
    "χ": r"\chi{}",
    "ω": r"\omega{}",
    "Δ": r"\Delta{}",
    "Π": r"\Pi{}",
    "Σ": r"\Sigma{}",
    "Ω": r"\Omega{}",
    "ℓ": r"\ell{}",
    "∑": r"\sum{}",
    "↑": r"\uparrow{}",
    "↓": r"\downarrow{}",
    "↖": r"\nwarrow{}",
    "↗": r"\nearrow{}",
}


def classes(el) -> set[str]:
    if not isinstance(el, Tag):
        return set()
    return set(el.get("class") or [])


def elements(el: Tag) -> list[Tag]:
    return [child for child in el.children if isinstance(child, Tag)]


def render_rich_text(raw: str) -> str:
    """Split prose inside math into \\text and real TeX commands."""
    parts: list[str] = []
    buf: list[str] = []

    def flush() -> None:
        text = "".join(buf)
        buf.clear()
        if text:
            parts.append(r"\text{" + text_escape(text) + "}")

    index = 0
    symbols = sorted(COMMANDS, key=len, reverse=True)
    while index < len(raw):
        symbol = next((item for item in symbols if raw.startswith(item, index)), "")
        if symbol:
            flush()
            parts.append(COMMANDS[symbol])
            index += len(symbol)
            continue
        buf.append(raw[index])
        index += 1
    flush()
    return "".join(parts)


def text_escape(value: str) -> str:
    repl = {
        "\\": r"\textbackslash{}",
        "{": r"\{",
        "}": r"\}",
        "$": r"\$",
        "%": r"\%",
        "&": r"\&",
        "_": r"\_",
        "#": r"\#",
        "^": r"\textasciicircum{}",
        "~": r"\textasciitilde{}",
    }
    return "".join(repl.get(ch, ch) for ch in value)


def md_escape(value: str) -> str:
    value = value.replace("\\", "\\\\")
    value = value.replace("$", r"\$")
    value = value.replace("`", r"\`")
    value = value.replace("*", r"\*")
    value = value.replace("_", r"\_")
    value = value.replace("<", "&lt;")
    return value


def clean_text(value: str) -> str:
    value = value.replace("\xa0", " ").replace("\u2009", " ").replace("\u200a", " ")
    value = value.replace("\r", "")
    return value


def yml_str(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'


def slug_id(eid: str) -> str:
    if eid.startswith("ball-"):
        eid = eid[len("ball-") :]
    eid = re.sub(r"[^A-Za-z0-9]+", ":", eid).strip(":")
    return eid


def assign_label(labels: dict[str, str], eid: str, kind: str) -> None:
    if not eid or eid in labels:
        return
    labels[eid] = f"{kind}:{slug_id(eid)}"


class Ctx:
    def __init__(self, source: Path, labels: dict[str, str], file_map: dict[str, str]):
        self.source = source
        self.labels = labels
        self.file_map = file_map
        self.out_file = CHAPTERS / "page.md"
        self.page_title = ""
        self.saw_title = False
        self.primary_id = ""
        self.in_directive = False
        self.force_inline = False
        self.footnotes: list[tuple[str, str]] = []
        self.copied: set[str] = set()
        self.exercise_count = 0


def math_node(el) -> str:
    if isinstance(el, NavigableString):
        text = str(el)
        if not text.strip():
            return ""
        return r"\text{" + text_escape(clean_text(text)) + "}"
    if not isinstance(el, Tag):
        return ""
    name = el.name or ""
    if name in ("annotation", "annotation-xml"):
        return ""
    if name == "semantics":
        for child in el.children:
            if isinstance(child, Tag) and child.name not in ("annotation", "annotation-xml"):
                return math_node(child)
        return ""
    if name in ("math", "mrow", "mstyle", "mpadded", "merror"):
        return "".join(math_node(child) for child in el.children)
    if name == "mtext":
        raw = clean_text("".join(el.strings))
        if raw.strip() == "" and raw:
            return r"\,"
        return render_rich_text(raw)
    if name == "mn":
        raw = clean_text(el.get_text()).replace("−", "-").replace("–", "-")
        return raw.replace(",", "{,}")
    if name == "mi":
        raw = clean_text(el.get_text()).strip()
        if raw in COMMANDS:
            return COMMANDS[raw]
        if len(raw) == 1 and raw.isalpha():
            return raw
        return render_rich_text(raw)
    if name == "mo":
        raw = clean_text(el.get_text())
        if raw in COMMANDS:
            return COMMANDS[raw]
        if raw.strip() == "":
            return r"\,"
        if raw in "{}%&_#":
            return "\\" + raw
        if len(raw) == 1 and raw.isascii():
            return raw
        return render_rich_text(raw)
    if name == "mspace":
        return r"\,"
    if name == "mfrac":
        kids = elements(el)
        num = math_node(kids[0]) if kids else ""
        den = math_node(kids[1]) if len(kids) > 1 else ""
        return r"\frac{" + num + "}{" + den + "}"
    if name == "msqrt":
        return r"\sqrt{" + "".join(math_node(child) for child in el.children) + "}"
    if name == "msup":
        kids = elements(el)
        base = math_node(kids[0]) if kids else ""
        exp = math_node(kids[1]) if len(kids) > 1 else ""
        return "{" + base + "}^{" + exp + "}"
    if name == "msub":
        kids = elements(el)
        base = math_node(kids[0]) if kids else ""
        sub = math_node(kids[1]) if len(kids) > 1 else ""
        return "{" + base + "}_{" + sub + "}"
    if name == "msubsup":
        kids = elements(el)
        base = math_node(kids[0]) if kids else ""
        sub = math_node(kids[1]) if len(kids) > 1 else ""
        exp = math_node(kids[2]) if len(kids) > 2 else ""
        return "{" + base + "}_{" + sub + "}^{" + exp + "}"
    if name == "menclose":
        # The source draws a cancellation stroke. KaTeX treats the combining
        # stroke as an accent and does not load \\cancel, so the unit is kept
        # and the surrounding sentence still says that it cancels.
        return "".join(math_node(child) for child in el.children)
    if name == "munder":
        kids = elements(el)
        base = math_node(kids[0]) if kids else ""
        under = math_node(kids[1]) if len(kids) > 1 else ""
        return r"\underset{" + under + "}{" + base + "}"
    if name == "mover":
        kids = elements(el)
        base_el = kids[0] if kids else None
        over = math_node(kids[1]) if len(kids) > 1 else ""
        base_raw = clean_text(base_el.get_text()) if base_el is not None else ""
        if base_raw in ("→", "⟶"):
            return r"\xrightarrow{" + over + "}"
        if base_raw == "←":
            return r"\xleftarrow{" + over + "}"
        if base_raw in ("⇌", "⇋", "⇄"):
            return r"\overset{" + over + r"}{\rightleftharpoons}"
        return r"\overset{" + over + "}{" + (math_node(base_el) if base_el else "") + "}"
    if name == "mmultiscripts":
        return render_multiscripts(el)
    if name == "mtable":
        return render_mtable(el)
    if name in ("mtr", "mtd", "mlabeledtr"):
        return "".join(math_node(child) for child in el.children)
    if name in ("mprescripts", "none", "maligngroup", "malignmark"):
        return ""
    return "".join(math_node(child) for child in el.children)


def plain_math(el: Tag) -> str | None:
    structural = {
        "mfrac",
        "msub",
        "msup",
        "msubsup",
        "munder",
        "mover",
        "mtable",
        "mmultiscripts",
        "msqrt",
        "menclose",
    }
    parts: list[str] = []
    for child in el.children:
        if isinstance(child, NavigableString):
            parts.append(str(child))
            continue
        if not isinstance(child, Tag):
            continue
        if child.name in structural:
            return None
        inner = plain_math(child)
        if inner is None:
            return None
        parts.append(inner)
    return clean_text("".join(parts))


def render_multiscripts(el: Tag) -> str:
    kids = elements(el)
    if not kids:
        return ""
    base, rest = kids[0], kids[1:]
    post: list[tuple[Tag | None, Tag | None]] = []
    pre: list[tuple[Tag | None, Tag | None]] = []
    bucket = post
    index = 0
    while index < len(rest):
        if rest[index].name == "mprescripts":
            bucket = pre
            index += 1
            continue
        sub = rest[index]
        sup = rest[index + 1] if index + 1 < len(rest) else None
        index += 2
        bucket.append((sub, sup))

    def piece(node: Tag | None) -> str:
        if node is None or node.name == "none":
            return ""
        return math_node(node)

    tex = ""
    if pre:
        tex += "{" + "".join("_{" + piece(sub) + "}^{" + piece(sup) + "}" for sub, sup in pre) + "}"
    tex += math_node(base)
    for sub, sup in post:
        tex += "_{" + piece(sub) + "}^{" + piece(sup) + "}"
    return tex


def render_mtable(el: Tag) -> str:
    rows = []
    for tr in el.find_all("mtr", recursive=False):
        cells = ["".join(math_node(child) for child in td.children) for td in tr.find_all("mtd", recursive=False)]
        rows.append(" & ".join(cells))
    if not rows:
        return "".join(math_node(child) for child in el.children)
    return "\\begin{aligned}\n" + " \\\\\n".join(rows) + "\n\\end{aligned}"


def display_math(el: Tag) -> bool:
    if not isinstance(el, Tag):
        return False
    if el.name == "math":
        return el.get("display") == "block"
    if "informalequation" in classes(el) and "block" in classes(el):
        return True
    math = el.find("math")
    return bool(math is not None and math.get("display") == "block")


def script_body(node: Tag) -> str:
    """Turn a superscript or subscript into TeX, keeping the sign on the script."""
    text = clean_text(node.get_text()).strip().replace("−", "-").replace("–", "-").replace("—", "-")
    if re.fullmatch(r"[+\-]?\d+(?:\.\d+)?(?:/\d+)?|\d+[+\-]|[+\-]", text):
        return text
    return mathphrase_tex(node)


def mathphrase_tex(node) -> str:
    """Render a mathphrase, including its sup and sub tags.

    get_text() drops those tags, which turned 10^4 into 104 and 10^-7 into 10 minus 7.
    """
    chunks: list[str] = []
    children = node.children if isinstance(node, Tag) else [node]
    for child in children:
        chunks.append(phrase_piece(child))
    return "".join(chunks)


def phrase_piece(node) -> str:
    if isinstance(node, NavigableString):
        raw = clean_text(str(node))
        return render_rich_text(raw) if raw else ""
    if not isinstance(node, Tag):
        return ""
    kind = classes(node)
    if node.name == "sup" or "superscript" in kind:
        body = script_body(node)
        return "^{" + body + "}" if body else ""
    if node.name == "sub" or "subscript" in kind:
        body = script_body(node)
        return "_{" + body + "}" if body else ""
    if node.name in ("em", "i") or "emphasis" in kind:
        raw = clean_text(node.get_text()).strip()
        if re.fullmatch(r"[A-Za-z]", raw):
            return raw
        if re.fullmatch(r"[A-Za-z]+", raw):
            return r"\mathit{" + raw + "}"
        return r"\text{" + text_escape(raw) + "}" if raw else ""
    if node.name == "br":
        return r"\\"
    return mathphrase_tex(node)


def render_math(el: Tag, ctx: Ctx, force_display: bool = False) -> str:
    math = el if el.name == "math" else el.find("math")
    if math is None:
        phrase = el.find(class_="mathphrase")
        if phrase is not None:
            tex = mathphrase_tex(phrase).strip()
        else:
            return ""
    else:
        tex = math_node(math).strip()
    if not tex:
        return ""
    display = force_display or display_math(el) or (math is not None and math.get("display") == "block")
    if display and not ctx.force_inline:
        return f"\n\n$$\n{tex}\n$$\n\n"
    return f"${tex}$"


def is_block(el) -> bool:
    if not isinstance(el, Tag):
        return False
    if el.name in ("p", "div", "ol", "ul", "table", "h1", "h2", "h3", "h4", "blockquote", "pre"):
        return True
    if "informalequation" in classes(el) and "block" in classes(el):
        return True
    return False


def normalize_image(dest: Path) -> None:
    """KaTeX's image step rejects CMYK JPEGs and warns on files over about 1 MB."""
    if dest.suffix.lower() not in {".jpg", ".jpeg"}:
        return
    try:
        from PIL import Image
    except ImportError:
        return
    with Image.open(dest) as image:
        if image.mode != "CMYK" and dest.stat().st_size <= 1_000_000:
            return
        rgb = image.convert("RGB")
        if max(rgb.size) > 2200:
            rgb.thumbnail((2200, 2200))
        rgb.save(dest, "JPEG", quality=82, optimize=True)


def copy_image(ctx: Ctx, src: str) -> str:
    src_path = (ctx.source / unquote(src)).resolve()
    name = src_path.name
    FIGURES.mkdir(parents=True, exist_ok=True)
    dest = FIGURES / name
    if name not in ctx.copied:
        if not src_path.exists():
            raise FileNotFoundError(src_path)
        shutil.copy2(src_path, dest)
        normalize_image(dest)
        if name == "86495288d4baa241709baaed0454b93a.jpg":
            correct_electronegativity_figure(dest)
        if name == "e1287901f5021ca67a87677efadabcf6.jpg":
            correct_ionization_energy_figure(dest)
        ctx.copied.add(name)
    rel = os.path.relpath(dest, ctx.out_file.parent)
    return Path(rel).as_posix()


def flatten(text: str) -> str:
    text = clean_text(text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r" +", " ", text)
    text = re.sub(r" +\n", "\n", text)
    text = re.sub(r"\n ", "\n", text)
    return text.strip()


def fence(name: str, body: str, title: str = "", options: list[str] | None = None) -> str:
    head = f"```{{{name}}}" if not title else f"```{{{name}}} {title}"
    lines = [head]
    for option in options or []:
        lines.append(option)
    lines.append("")
    lines.append(body.strip())
    lines.append("```")
    return "\n".join(lines)


def target_line(ctx: Ctx, eid: str | None) -> str:
    if not eid or eid == ctx.primary_id:
        return ""
    label = ctx.labels.get(eid)
    if not label:
        return ""
    return f"({label})=\n\n"


def render_inline(el, ctx: Ctx) -> str:
    if isinstance(el, NavigableString):
        text = clean_text(str(el))
        if text.strip() == "":
            return " " if text else ""
        return md_escape(re.sub(r"\s+", " ", text))
    if not isinstance(el, Tag):
        return ""
    if el.name in ("script", "style"):
        return ""
    if el.name == "br":
        return "\n"
    if el.name == "math" or "informalequation" in classes(el) or "inlineequation" in classes(el):
        return render_math(el, ctx)
    if el.name == "img":
        return render_image(el, ctx, caption="")
    if "margin_term" in classes(el):
        term = el.find(class_="glossterm")
        defin = el.find(class_="glossdef")
        term_text = render_children_inline(term, ctx) if term else render_children_inline(el, ctx)
        if defin is not None:
            definition = render_children_inline(defin, ctx)
            return f"**{term_text.strip()}** (*{definition.strip()}*)"
        return f"**{term_text.strip()}**"
    if "footnote" in classes(el):
        return render_footnote(el, ctx)
    if el.name == "a":
        return render_link(el, ctx)
    if el.name == "sub":
        inner = render_children_inline(el, ctx).strip()
        return f"<sub>{inner}</sub>" if inner else ""
    if el.name == "sup":
        inner = render_children_inline(el, ctx).strip()
        return f"<sup>{inner}</sup>" if inner else ""
    inner = render_children_inline(el, ctx)
    kind = classes(el)
    if el.name in ("strong", "b") or "bold" in kind or "bolditalic" in kind:
        if "bolditalic" in kind or (el.name == "em" and "bold" in kind):
            return f"***{inner.strip()}***" if inner.strip() else ""
        return f"**{inner.strip()}**" if inner.strip() else ""
    if el.name in ("em", "i") or "emphasis" in kind:
        if "bolditalic" in kind:
            return f"***{inner.strip()}***" if inner.strip() else ""
        return f"*{inner.strip()}*" if inner.strip() else ""
    return inner


def render_children_inline(el, ctx: Ctx) -> str:
    if el is None:
        return ""
    return "".join(render_inline(child, ctx) for child in el.children)


def render_footnote(el: Tag, ctx: Ctx) -> str:
    key = re.sub(r"[^A-Za-z0-9-]", "", el.get("id") or f"fn{len(ctx.footnotes) + 1}")
    body = flatten(render_blocks(el, ctx))
    ctx.footnotes.append((key, body))
    return f"[^{key}]"


def render_link(el: Tag, ctx: Ctx) -> str:
    href = el.get("href") or ""
    text = flatten(render_children_inline(el, ctx)) or href
    parsed = urlparse(href)
    if parsed.scheme in ("http", "https", "mailto"):
        return f"[{text}]({href})"
    fragment = parsed.fragment
    if fragment and fragment in ctx.labels:
        label = ctx.labels[fragment]
        safe = text.replace("`", "'")
        if safe and "<" not in safe:
            return "{ref}`" + safe + " <" + label + ">`"
        return "{ref}`" + label + "`"
    path = unquote(parsed.path)
    if path in ctx.file_map:
        target = ctx.file_map[path]
        rel = Path(os.path.relpath(ROOT / target, ctx.out_file.parent)).as_posix()
        if fragment:
            return f"[{text}]({rel}#{fragment})"
        return f"[{text}]({rel})"
    if href.startswith("#") and href[1:] in ctx.labels:
        return "{ref}`" + text.replace("`", "'") + " <" + ctx.labels[href[1:]] + ">`"
    if text:
        return text
    return ""


def render_image(el: Tag, ctx: Ctx, caption: str) -> str:
    src = el.get("src")
    if not src:
        return ""
    path = copy_image(ctx, src)
    alt = clean_text(el.get("alt") or caption or ctx.page_title or "Illustration")
    alt = re.sub(r"<[^>]+>", "", alt)
    alt = re.sub(r"\s+", " ", alt).strip().replace('"', "'")
    return f'![{alt}]({path})'


def render_figure(el: Tag, ctx: Ctx) -> str:
    title_el = el.find("p", class_="title", recursive=False)
    title = ""
    if title_el is not None:
        title = clean_text(title_el.get_text(" ", strip=True))
        title = re.sub(r"^(Figure|Table)\s+[\d.]+\s*", "", title).strip(" \"")
    caption_parts = []
    for para in el.find_all("p", class_="para", recursive=False):
        caption_parts.append(flatten(render_blocks(para, ctx)))
    caption = " ".join(part for part in caption_parts if part)
    if title and caption:
        full_caption = f"{title}. {caption}"
    else:
        full_caption = title or caption or ctx.page_title or "Illustration"
    full_caption = re.sub(r"\s+", " ", full_caption).strip()
    alt = re.sub(r"<[^>]+>", "", full_caption).replace('"', "'")
    images = el.find_all("img")
    if not images:
        return target_line(ctx, el.get("id")) + flatten(render_blocks(el, ctx))
    label = ctx.labels.get(el.get("id") or "")
    chunks = []
    if label and not ctx.in_directive:
        options = [f":label: {label}", f':alt: "{alt}"', ":align: center"]
        if "small" in classes(el):
            options.append(":width: 45%")
        elif "large" in classes(el):
            options.append(":width: 85%")
        body = full_caption
        # One directive per image. Extra images follow as plain figures.
        first = copy_image(ctx, images[0].get("src"))
        chunks.append(f"```{{figure}} {first}\n" + "\n".join(options) + f"\n\n{body}\n```")
        for image in images[1:]:
            path = copy_image(ctx, image.get("src"))
            chunks.append(f'![{full_caption.replace("]", "")}]({path})')
        return "\n\n".join(chunks)
    lines = [target_line(ctx, el.get("id")).strip()]
    for image in images:
        path = copy_image(ctx, image.get("src"))
        lines.append(f"![{alt.replace(']', '')}]({path})")
    if full_caption:
        lines.append("")
        lines.append(f"*{flatten(full_caption)}*")
    return "\n\n".join(line for line in lines if line is not None)


def cell_text(cell: Tag, ctx: Ctx) -> str:
    previous = ctx.force_inline
    ctx.force_inline = True
    try:
        text = render_blocks(cell, ctx)
    finally:
        ctx.force_inline = previous
    text = flatten(text).replace("\n", " ")
    text = text.replace("|", r"\|")
    return text.strip() or " "


def render_table(el: Tag, ctx: Ctx) -> str:
    table = el if el.name == "table" else el.find("table")
    label = ctx.labels.get(el.get("id") or "")
    title = ""
    title_el = el.find("p", class_="title", recursive=False) if el.name != "table" else None
    if title_el is not None:
        title = clean_text(title_el.get_text(" ", strip=True))
        title = re.sub(r"^Table\s+[\d.]+\s*", "", title).strip(" \"")
    if table is None:
        return ""
    grid: dict[tuple[int, int], str] = {}
    occupied: set[tuple[int, int]] = set()
    header_rows = 0
    rows = table.find_all("tr")
    for row_index, row in enumerate(rows):
        if row.find_parent("tfoot"):
            continue
        column = 0
        is_header = row.find_parent("thead") is not None or (
            row.find(["td", "th"]) is not None and all(cell.name == "th" for cell in row.find_all(["td", "th"], recursive=False))
        )
        if is_header:
            header_rows = max(header_rows, row_index + 1)
        for cell in row.find_all(["td", "th"], recursive=False):
            while (row_index, column) in occupied:
                column += 1
            rowspan = int(cell.get("rowspan") or 1)
            colspan = int(cell.get("colspan") or 1)
            value = cell_text(cell, ctx)
            for i in range(rowspan):
                for j in range(colspan):
                    occupied.add((row_index + i, column + j))
                    grid[(row_index + i, column + j)] = value if i == 0 and j == 0 else " "
            column += colspan
    body_rows = [row for row in rows if not row.find_parent("tfoot")]
    if not body_rows:
        return ""
    width = max((column for _, column in occupied), default=0) + 1
    matrix = []
    for row_index in range(len(body_rows)):
        matrix.append([grid.get((row_index, column), " ") for column in range(width)])
    if header_rows == 0:
        header_rows = 1
    lines = []
    for row_index, row in enumerate(matrix):
        lines.append("| " + " | ".join(row) + " |")
        if row_index == header_rows - 1:
            lines.append("| " + " | ".join("---" for _ in row) + " |")
    markdown = "\n".join(lines)
    notes = []
    tfoot = table.find("tfoot")
    if tfoot is not None:
        note = flatten(render_blocks(tfoot, ctx))
        if note:
            notes.append(note)
    if ctx.in_directive or not label:
        prefix = target_line(ctx, el.get("id"))
        titled = f"**{title}**\n\n{markdown}" if title else markdown
        extra = "\n\n".join(notes)
        return prefix + titled + (("\n\n" + extra) if extra else "")
    caption = title or "Table"
    body = markdown if not notes else markdown + "\n\n" + "\n\n".join(notes)
    return fence("table", body, caption, [f":label: {label}"])


def list_marker(el: Tag, index: int) -> str:
    kind = (el.get("numeration") or "").lower()
    if kind == "loweralpha":
        return f"{chr(ord('a') + index - 1)}. "
    if kind == "upperalpha":
        return f"{chr(ord('A') + index - 1)}. "
    if kind == "lowerroman":
        return f"{to_roman(index).lower()}. "
    return f"{index}. "


def to_roman(number: int) -> str:
    values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    result = []
    for value, glyph in values:
        while number >= value:
            result.append(glyph)
            number -= value
    return "".join(result)


def render_list(el: Tag, ctx: Ctx) -> str:
    ordered = el.name == "ol"
    items = []
    for index, item in enumerate(el.find_all("li", recursive=False), start=1):
        marker = list_marker(el, index) if ordered else "- "
        body = render_blocks(item, ctx).strip()
        if not body:
            continue
        pad = " " * len(marker)
        lines = body.split("\n")
        rendered = marker + lines[0]
        for line in lines[1:]:
            rendered += "\n" + (pad + line if line else "")
        items.append(rendered)
    return "\n".join(items)


def render_heading(el: Tag, ctx: Ctx) -> str:
    text = flatten(render_children_inline(el, ctx))
    if not ctx.saw_title and el.name in ("h1", "h2", "h3"):
        ctx.saw_title = True
        ctx.page_title = clean_text(el.get_text(" ", strip=True))
        return ""
    level = {"h1": "##", "h2": "##", "h3": "###", "h4": "####"}.get(el.name, "###")
    return target_line(ctx, el.get("id")) + f"{level} {text}"


def marker_name(el) -> str | None:
    if not isinstance(el, Tag) or el.name != "p" or "simpara" not in classes(el):
        return None
    text = el.get_text(" ", strip=True).lower()
    if text in {"solution", "test yourself", "answer", "answers"}:
        return text
    return None


def consume_nodes(nodes: list, ctx: Ctx) -> str:
    wrapper = BeautifulSoup("<div></div>", "lxml").div
    for node in nodes:
        wrapper.append(node if isinstance(node, NavigableString) else node.extract() if False else node)
    # Nodes are still attached to the original tree. Render them in place.
    parts = [render_node(node, ctx) for node in nodes]
    return "\n\n".join(part.strip() for part in parts if part and part.strip())


def render_example(el: Tag, ctx: Ctx) -> str:
    title_el = el.find("h3", recursive=False)
    title = title_el.get_text(" ", strip=True) if title_el else "Example"
    buckets: list[dict] = [{"kind": "problem", "title": title, "nodes": []}]
    for child in el.children:
        if child is title_el:
            continue
        marker = marker_name(child)
        if marker == "solution":
            buckets.append({"kind": "solution", "title": "", "nodes": []})
            continue
        if marker == "test yourself":
            buckets.append({"kind": "problem", "title": "Test Yourself", "nodes": []})
            continue
        if marker in {"answer", "answers"}:
            buckets.append({"kind": "solution", "title": "", "nodes": []})
            continue
        buckets[-1]["nodes"].append(child)
    base = el.get("id") or f"{ctx.out_file.stem}-{ctx.exercise_count}"
    chunks = []
    problem_label = ""
    part = 0
    previous = ctx.in_directive
    ctx.in_directive = True
    try:
        for bucket in buckets:
            body = consume_nodes(bucket["nodes"], ctx).strip()
            if bucket["kind"] == "problem":
                if not body and not bucket["title"]:
                    continue
                part += 1
                ctx.exercise_count += 1
                suffix = "" if part == 1 else f"-ty{part}"
                problem_label = "ex:" + re.sub(r"[^A-Za-z0-9]+", "-", base + suffix).strip("-")
                lead = f"**{bucket['title']}**\n\n{body}" if bucket["title"] else body
                chunks.append(fence("exercise", lead.strip(), options=[f":label: {problem_label}"]))
            elif body and problem_label:
                solution_label = "sol:" + problem_label[len("ex:") :]
                chunks.append(
                    fence(
                        "solution",
                        body,
                        title=problem_label,
                        options=[f":label: {solution_label}", ":class: dropdown"],
                    )
                )
    finally:
        ctx.in_directive = previous
    return "\n\n".join(chunks)


def render_qanda(el: Tag, ctx: Ctx) -> str:
    title = ""
    title_el = el.find("h3", recursive=False)
    if title_el is not None:
        title = title_el.get_text(" ", strip=True)
    if title.lower() == "answers" or (el.get("id") or "").endswith("_ans"):
        return ""
    qid = el.get("id") or ""
    answers = []
    if qid:
        found = el.find_parent("html")
        answer_set = found.find(id=qid + "_ans") if found else None
        if answer_set is not None:
            answers = answer_set.find_all("li", class_="qandaentry")
    questions = []
    for item in el.find_all("li", class_="qandaentry"):
        parent = item.find_parent(class_="qandaset")
        if parent is el:
            questions.append(item)
    chunks = []
    if title:
        chunks.append(f"## {title}")
    previous = ctx.in_directive
    ctx.in_directive = True
    try:
        for index, question in enumerate(questions, start=1):
            question_body = question.find("div", class_="question") or question
            body = render_blocks(question_body, ctx).strip()
            if not body:
                continue
            q_label = "ex:" + re.sub(r"[^A-Za-z0-9]+", "-", (question.get("id") or f"{qid}-{index}")).strip("-")
            chunks.append(fence("exercise", f"**Exercise {index}.**\n\n{body}", options=[f":label: {q_label}"]))
            if index - 1 < len(answers):
                answer_body = render_blocks(answers[index - 1], ctx).strip()
                if answer_body:
                    chunks.append(
                        fence(
                            "solution",
                            answer_body,
                            title=q_label,
                            options=[
                                ":label: sol:" + q_label[len("ex:") :],
                                ":class: dropdown",
                            ],
                        )
                    )
    finally:
        ctx.in_directive = previous
    return "\n\n".join(chunks)


def render_admonition(el: Tag, ctx: Ctx, kind: str, default_title: str) -> str:
    title_el = el.find(["h2", "h3"], recursive=False)
    title = title_el.get_text(" ", strip=True) if title_el else default_title
    nodes = [child for child in el.children if child is not title_el]
    previous = ctx.in_directive
    ctx.in_directive = True
    try:
        body = consume_nodes(nodes, ctx).strip()
    finally:
        ctx.in_directive = previous
    if ctx.in_directive:
        return f"**{title}**\n\n{body}"
    low = title.lower()
    if low.startswith("chemistry is everywhere") or low.startswith("food and drink"):
        kind = "tip"
    elif low.startswith("opening"):
        kind = "note"
    return target_line(ctx, el.get("id")) + fence(kind, body, title)


def structural_block(node) -> bool:
    if not isinstance(node, Tag):
        return False
    if node.name in ("p", "div", "ol", "ul", "table", "h1", "h2", "h3", "h4", "blockquote", "pre", "img"):
        return True
    kind = classes(node)
    if kind & {
        "learning_objectives",
        "key_takeaways",
        "callout",
        "exercises",
        "qandaset",
        "figure",
        "informalfigure",
        "table",
        "informaltable",
        "section",
        "chapter",
        "appendix",
        "license",
    }:
        return True
    if "informalequation" in kind and display_math(node):
        return True
    return bool(node.name == "math" and node.get("display") == "block")


def render_blocks(el: Tag, ctx: Ctx) -> str:
    parts: list[str] = []
    buf: list[str] = []

    def flush() -> None:
        if not buf:
            return
        text = "".join(buf)
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r" *\n *", "\n", text).strip()
        if text:
            parts.append(text)
        buf.clear()

    for child in el.children:
        if structural_block(child):
            flush()
            rendered = render_node(child, ctx).strip()
            if rendered:
                parts.append(rendered)
        else:
            buf.append(render_inline(child, ctx))
    flush()
    return "\n\n".join(parts)


def render_node(node, ctx: Ctx) -> str:
    if isinstance(node, NavigableString):
        text = clean_text(str(node))
        if text.strip() == "":
            return ""
        return md_escape(re.sub(r"\s+", " ", text)).strip()
    if not isinstance(node, Tag):
        return ""
    if node.name in ("script", "style"):
        return ""
    kind = classes(node)
    if "learning_objectives" in kind:
        return render_admonition(node, ctx, "note", "Learning Objectives")
    if "key_takeaways" in kind:
        return render_admonition(node, ctx, "important", "Key Takeaways")
    if "callout" in kind:
        return render_admonition(node, ctx, "note", "Note")
    if "exercises" in kind:
        return render_example(node, ctx)
    if "qandaset" in kind:
        return render_qanda(node, ctx)
    if "figure" in kind or "informalfigure" in kind:
        return render_figure(node, ctx)
    if node.name == "table" or "table" in kind or "informaltable" in kind:
        return render_table(node, ctx)
    if "informalequation" in kind or node.name == "math":
        return render_math(node, ctx, force_display="block" in kind or (node.name == "math" and node.get("display") == "block"))
    if node.name in ("h1", "h2", "h3", "h4"):
        return render_heading(node, ctx)
    if node.name in ("ol", "ul"):
        return render_list(node, ctx)
    if node.name == "p":
        return render_paragraph(node, ctx)
    if node.name == "img":
        return render_image(node, ctx, caption=ctx.page_title)
    if node.name == "br":
        return ""
    if "section" in kind or "chapter" in kind or "appendix" in kind or "license" in kind or node.name == "div":
        return target_line(ctx, node.get("id")) + render_blocks(node, ctx)
    return render_inline(node, ctx)


def render_paragraph(el: Tag, ctx: Ctx) -> str:
    parts: list[str] = []
    buf: list[str] = []

    def flush() -> None:
        if not buf:
            return
        text = "".join(buf)
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r" *\n *", "\n", text).strip()
        if text:
            parts.append(text)
        buf.clear()

    for child in el.children:
        if isinstance(child, Tag) and (
            display_math(child) or child.name in ("div", "ol", "ul", "table") or "figure" in classes(child)
        ):
            flush()
            rendered = render_node(child, ctx).strip()
            if rendered:
                parts.append(rendered)
        else:
            buf.append(render_inline(child, ctx))
    flush()
    return target_line(ctx, el.get("id")) + "\n\n".join(parts)


def correct_ionization_energy_figure(dest: Path) -> None:
    """Figure 8.20 labels Be, Mg, and Ca with atomic radii (111, 160, 197 pm).

    Those cells are ionization energies in kJ/mol: 899, 738, and 590.
    Runs on the freshly copied source image.
    """
    from PIL import Image, ImageDraw, ImageFont

    image = Image.open(dest).convert("RGB")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
    background = (178, 210, 235)
    jobs = [
        ((348, 372, 418, 400), "899", (381, 386)),
        ((348, 606, 418, 632), "738", (381, 619)),
        ((348, 890, 418, 918), "590", (381, 904)),
    ]
    for box, text, center in jobs:
        draw.rectangle(box, fill=background)
        draw.text(center, text, font=font, fill=(0, 0, 0), anchor="mm")
    image.save(dest, "JPEG", quality=90, optimize=True)


def correct_electronegativity_figure(dest: Path) -> None:
    """Figure 9.2 gives boron as 1.5 and sulfur as 3.5. Pauling values here are 2.0 and 2.5.

    The 2.0 is copied from the arsenic cell in the same figure, and sulfur's 3 is
    replaced with that same 2. Runs on the freshly copied source image.
    """
    from PIL import Image

    image = Image.open(dest).convert("RGB")
    pixels = image.load()
    # Copy glyphs before any pixels are overwritten.
    arsenic = image.crop((1565, 618, 1622, 651))
    two = image.crop((1565, 618, 1585, 651))
    # Boron "1.5" sits at the bottom of its cell. Clear it, then center "2.0".
    for y in range(318, 363):
        for x in range(1328, 1396):
            pixels[x, y] = (255, 255, 255)
    image.paste(arsenic, (1334, 325))
    # Sulfur's first digit is 3. Clear it and paste the 2, keeping ".5".
    for y in range(468, 508):
        for x in range(1682, 1710):
            pixels[x, y] = (255, 255, 255)
    image.paste(two, (1686, 473))
    image.save(dest, "JPEG", quality=90, optimize=True)


def apply_content_corrections(text: str) -> str:
    """Corrections to the Saylor HTML that the conversion would otherwise preserve."""
    replacements = {
        # Preserve copyedits already present in this edition when regenerating.
        "heterogeneous mixtures or homogenous mixtures": "heterogeneous mixtures or homogeneous mixtures",
        "Amadeo Avogadro": "Amedeo Avogadro",
        "one starts with moles of one substance and convert to moles": "one starts with moles of one substance and converts to moles",
        "needed to bread a covalent bond": "needed to break a covalent bond",
        "The behavior of a liquid in narrow surfaces": "The behavior of a liquid in narrow tubes",
        "the maximum amount of solute is dissolved in a given amount of solute": "the maximum amount of solute is dissolved in a given amount of solvent",
        "A unstable solution": "An unstable solution",
        "plants indispensible": "plants indispensable",
        r"e^{-0.693}^{t}^{\text{/(1,600 y)}}": r"e^{-0.693t/(1{,}600\text{ y})}",
        "the number of neurons": "the number of neutrons",
        "a given number half-lives": "a given number of half-lives",
        "The change is mass is determined": "The change in mass is determined",
        "The smallest nucleus that exhibits spontaneous fission is lead-208. (Fission is the radioactive process used in nuclear power plants and one type of nuclear bomb.)":
        "Lead-208 is stable and does not fission spontaneously; measurable spontaneous fission occurs in much heavier nuclei, such as isotopes of uranium. (The fission used in nuclear power plants and in one type of nuclear bomb is induced by a neutron, rather than spontaneous.)",
        "What if the elapsed time is not an exact number of half-lives? We can still calculate the amount of material we have left, but the equation is more complicated. The equation is":
        "The amount remaining can also be calculated from the elapsed time directly, without first converting that time into a number of half-lives. The equation is",
        "Although this is a more complicated formula, the length of time *t* need not be an exact multiple of half-lives.":
        "This is the same relationship as the expression above, with *n* = *t* / *t*<sub>1/2</sub>. The elapsed time does not have to be an exact multiple of the half-life.",
        "| 0–0.4 | slightly polar covalent |\n| 0.4–1.9 | definitely polar covalent |\n| >1.9 | likely ionic |":
        "| >0–0.4 | slightly polar covalent |\n| >0.4–1.9 | definitely polar covalent |\n| >1.9 | likely ionic |\n\nA difference of 0.4 is slightly polar covalent. The cutoff at 1.9 is only a guide: a bond between a metal and a nonmetal is ionic even when the difference is smaller. Sodium and iodine differ by 1.6 on this scale, and sodium iodide is an ionic compound.",
        r"\text{)(0.08205)(298)}^{-2}": r"\text{)[(0.08205)(298)]}^{-2}",
        "In the spontaneous fission of lead-208, the following reaction occurs:":
        "Lead-208 does not spontaneously fission. Use this hypothetical equation to practice the mass-energy calculation:",
        "In the spontaneous fission of radium-226, the following reaction occurs:":
        "Radium-226 decays by alpha emission, not by the split below. Use the equation to practice the mass-energy calculation:",
        "positive if you move the decimal point to the right and negative if you move the decimal point to the left":
        "positive if you move the decimal point to the left and negative if you move the decimal point to the right",
        "One Fahrenheit degree is nine-fifths the size of a Celsius degree.":
        "One Fahrenheit degree is five-ninths the size of a Celsius degree.",
        "about one in a million": "about one in 6,400",
        """```{solution} ex:ball-ch04-s01-qs01-qd01-qa13
:label: sol:ball-ch04-s01-qs01-qd01-qa13
:class: dropdown

N<sub>2</sub>(g) + 3H<sub>2</sub>(g) → 2NH<sub>3</sub>(g)
```""":
        """```{solution} ex:ball-ch04-s01-qs01-qd01-qa13
:label: sol:ball-ch04-s01-qs01-qd01-qa13
:class: dropdown

N<sub>2</sub>(g) + 2H<sub>2</sub>(g) → N<sub>2</sub>H<sub>4</sub>(g)
```""",
        "Compounds of SO<sub>4</sub><sup>2</sup>": "Compounds of SO<sub>4</sub><sup>2−</sup>",
        "HI(aq) + KOH(aq) → KCl(aq) + H<sub>2</sub>O(ℓ)":
        "HI(aq) + KOH(aq) → KI(aq) + H<sub>2</sub>O(ℓ)",
        r"{\text{4H}}_{\text{3}}{\text{PO}}_{\text{4}}": r"{\text{4H}}_{\text{3}}{\text{PO}}_{\text{3}}",
        """```{solution} ex:ball-ch05-s07-qs01-qd01-qa01
:label: sol:ball-ch05-s07-qs01-qd01-qa01
:class: dropdown

1.2044 × 10<sup>24</sup> molecules
```""":
        """```{solution} ex:ball-ch05-s07-qs01-qd01-qa01
:label: sol:ball-ch05-s07-qs01-qd01-qa01
:class: dropdown

3.011 × 10<sup>23</sup> molecules
```""",
        r"\text{(0}\text{.00332 mmHg)": r"\text{(0}\text{.00120 mmHg)",
        r"\frac{\text{(0}\text{.00332)(435)}": r"\frac{\text{(0}\text{.00120)(435)}",
        r"$T\text{ = 1,404 K}$": r"$T\text{ = 507 K}$",
        "at 0.26 atm and −26°C": "at 0.33 atm and −26°C",
        r"\text{2C(s) + O}_{2}\text{(g) }\rightarrow{}\text{ 2CO}_{2}\text{(g)     }\Delta{}H\text{ = }-\text{393.5 kJ}":
        r"\text{C(s) + O}_{2}\text{(g) }\rightarrow{}\text{ CO}_{2}\text{(g)     }\Delta{}H\text{ = }-\text{393.5 kJ}",
        "4.69 L": "2.85 L",
        "Na<sub>2</sub>SO<sub>4</sub>(s) | −331.64": "Na<sub>2</sub>SO<sub>4</sub>(s) | −1,387.1",
        "PH<sub>3</sub>(g) | 22.89": "PH<sub>3</sub>(g) | 5.4",
        "NaCl(s) | −385.9": "NaCl(s) | −411.2",
        "1.99 × 10<sup>−22</sup> J": "1.99 × 10<sup>−25</sup> J",
        "233 K (−60°C)": "213 K (−60°C)",
        "| Bromine (59.5°C) | 15.4 |": "| Bromine (59.5°C) | 30.0 |",
        "The Δ*H*<sub>vap</sub> of Br<sub>2</sub> is 15.4 kJ/mol.":
        "The Δ*H*<sub>vap</sub> of Br<sub>2</sub> is 30.0 kJ/mol.",
        r"\frac{15.4\text{ kJ}}{\text{ mol}}=6.43\text{ kJ}":
        r"\frac{30.0\text{ kJ}}{\text{ mol}}=12.5\text{ kJ}",
        "Δ*H* = −6.43 kJ.": "Δ*H* = −12.5 kJ.",
        "10.7 kJ": "20.8 kJ",
        "The normal vapor pressure, then, is the temperature":
        "The normal boiling point, then, is the temperature",
        "Atmospheric pressure varies significantly with altitude.":
        "Atmospheric pressure varies significantly with altitude. At the summit of Mount Everest the pressure is about 250 torr, so water boils near 70°C.",
        "at 500 torr, which is the approximate atmospheric pressure at the top of Mount Everest.":
        "at 500 torr.",
        "while others, such as diamond, are very hard":
        "while some solids, such as diamond, are very hard",
        """```{solution} ex:ball-ch10-s04-qs01-qd01-qa15
:label: sol:ball-ch10-s04-qs01-qd01-qa15
:class: dropdown

a. molecular solid
b. molecular solid
c. ionic crystal
```""":
        """```{solution} ex:ball-ch10-s04-qs01-qd01-qa15
:label: sol:ball-ch10-s04-qs01-qd01-qa15
:class: dropdown

a. molecular solid
b. covalent network solid
c. ionic crystal
```""",
        "about 1.4 × 10<sup>14</sup> g of gold": "about 1.4 × 10<sup>11</sup> g of gold",
        "NaCl can dissolve up to 31.6 g per 100 g": "NaCl can dissolve up to 36.1 g per 100 g",
        "C<sub>6</sub>H<sub>12</sub>C<sub>6</sub>": "C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>",
        "−7.5°C": "−11.2°C",
        "only about 6 in 10<sup>8</sup> H<sub>2</sub>O molecules":
        "only about 2 in 10<sup>9</sup> H<sub>2</sub>O molecules",
        r"\frac{{(6.22)}^{2}}{(1.88)(13.7)}=1.502112129":
        r"\frac{{(6.62)}^{2}}{(1.88)(13.7)}=1.702",
        r"$\text{[H}_{2}\text{] = 1.15 M}$": r"$\text{[H}_{2}\text{] = 1.19 M}$",
        r"{\text{CoCl}}_{\text{2}}": r"{\text{COCl}}_{\text{2}}",
        r"${\text{MgOH}}_{\text{2}}": r"${\text{Mg(OH)}}_{\text{2}}",
        "| Ba<sup>2+</sup> + 2e<sup>−</sup> → Ba | −1.57 |\n| Al<sup>3+</sup>+ 3e<sup>−</sup> → Al | −1.66 |\n| Mg<sup>2+</sup> + 2e<sup>−</sup> → Mg | −2.37 |\n| Na<sup>+</sup> + e<sup>−</sup> → Na | −2.714 |\n| Li<sup>+</sup> + e<sup>−</sup> → Li | −3.045 |":
        "| Al<sup>3+</sup>+ 3e<sup>−</sup> → Al | −1.66 |\n| Mg<sup>2+</sup> + 2e<sup>−</sup> → Mg | −2.37 |\n| Na<sup>+</sup> + e<sup>−</sup> → Na | −2.714 |\n| Ba<sup>2+</sup> + 2e<sup>−</sup> → Ba | −2.91 |\n| Li<sup>+</sup> + e<sup>−</sup> → Li | −3.045 |",
        r"\text{ + SO}_{4}^{2-}\text{ }\rightarrow{}\text{ 2PbSO}_{4}":
        r"\text{ + 2SO}_{4}^{2-}\text{ }\rightarrow{}\text{ 2PbSO}_{4}",
        "a tiny amount (∼0.0002 g) of the radioactive element americium":
        "a tiny amount (∼2.6 × 10<sup>−7</sup> g) of the radioactive element americium",
        "The half-live of americium-241 is 432 y. If 0.0002 g of americium-241":
        "The half-life of americium-241 is 432 y. If 2.6 × 10<sup>−7</sup> g of americium-241",
        "0.000170 g; 0.0000402 g": "2.2 × 10<sup>−7</sup> g; 5.2 × 10<sup>−8</sup> g",
        "equal to 0.01 J/g of tissue": "equal to 0.01 J/kg of tissue",
        "1 g of tissue absorbing 0.01 J": "1 kg of tissue absorbing 0.01 J",
        r"\text{1 rad = 0.01 J/g}": r"\text{1 rad = 0.01 J/kg}",
        "by only 0.002°C. This may not seem like a lot, but it is enough energy to break about 1 × 10<sup>21</sup> molecular C–C bonds":
        "by only about 2 × 10<sup>−6</sup>°C. This may not seem like a lot, but it is enough energy to break about 1 × 10<sup>18</sup> molecular C–C bonds",
        "0.01 J of energy per gram of tissue": "0.01 J of energy per kilogram of tissue",
        "If the half-life of radon is 1,500 y": "If the half-life of radon is 3.823 d",
        "6.0 × 10<sup>3</sup> y": "15.29 d",
        "or about 4.5 × 10<sup>9</sup> y. Many analyses": "or about 7.0 × 10<sup>8</sup> y. Many analyses",
        "(The half-life of carbon-14 is 5,370 y.)": "(The half-life of carbon-14 is 5,730 y.)",
        "per mole of reactant is only one-tenth of the amount given off by the fission of 1 mol of uranium-235. On a mass (per gram) basis, however, hydrogen fusion gives off 10 times more energy than fission does. In addition, the product of fission is helium gas, not a wide range of isotopes (some of which are also radioactive) produced by fission.":
        "per mole of this reaction is about one-sixth of the amount given off by the fission of 1 mol of uranium-235. On a mass (per gram) basis, however, hydrogen fusion gives off 10 times more energy than fission does. The product of fusion is helium gas. Fission produces a wide range of isotopes, some of which are also radioactive.",
        "about 0.25 mg of americium-241": "about 2.6 × 10<sup>−7</sup> g of americium-241",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def convert_page(html_path: Path, out_path: Path, ctx: Ctx) -> str:
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "lxml")
    content = soup.select_one("#book-content")
    if content is None:
        raise RuntimeError(f"No book content in {html_path.name}")
    ctx.out_file = out_path
    ctx.saw_title = False
    ctx.page_title = ""
    ctx.footnotes = []
    ctx.in_directive = False
    primary = content.find("div")
    ctx.primary_id = primary.get("id") if primary and primary.get("id") else ""
    body = render_blocks(content, ctx).strip()
    title = ctx.page_title or html_path.stem
    label = ctx.labels.get(ctx.primary_id, "")
    header = [f"---", f"title: {yml_str(title)}", f"---", ""]
    if label:
        header.append(f"({label})=")
        header.append("")
    header.append(f"# {title}")
    header.append("")
    footer = ""
    if ctx.footnotes:
        lines = []
        for key, note in ctx.footnotes:
            lines.append(f"[^{key}]: {note}")
        footer = "\n\n" + "\n\n".join(lines)
    text = "\n".join(header) + "\n" + body + footer + "\n"
    text = re.sub(r"\n{3,}", "\n\n", text)
    return apply_content_corrections(text)


def is_section(name: str) -> bool:
    return bool(re.match(r"s\d+-\d+-", name)) or name.startswith("s21-") or name.startswith("s00-")


def collect(source: Path):
    index = BeautifulSoup((source / "index.html").read_text(encoding="utf-8"), "lxml")
    toc = []
    referenced: set[str] = set()
    for html in source.glob("*.html"):
        if not is_section(html.name) and html.name != "index.html":
            continue
        if html.name == "index.html":
            continue
        soup = BeautifulSoup(html.read_text(encoding="utf-8"), "lxml")
        for anchor in soup.find_all("a", href=True):
            fragment = urlparse(anchor["href"]).fragment
            if fragment:
                referenced.add(fragment)
    labels: dict[str, str] = {}
    file_map: dict[str, str] = {}
    chapter_number = 0
    top = index.select_one("#toc-top-ul")
    for item in top.find_all("li", recursive=False):
        link = item.find("h3").find("a")
        title = link.get_text(" ", strip=True)
        href = link["href"]
        children = []
        sub = item.find("ul")
        if href.startswith("s00-"):
            file_map[href] = "license.md"
            toc.append({"title": title, "file": "license.md"})
            continue
        if href.startswith("s21-"):
            path = "chapters/ap-periodic-table.md"
            file_map[href] = path
            toc.append({"title": title, "file": path})
            continue
        chapter_number += 1
        if sub is None:
            toc.append({"title": title, "file": None, "children": []})
            continue
        for child in sub.find_all("li", recursive=False):
            child_link = child.find("a")
            child_href = child_link["href"]
            match = re.match(r"s\d+-(\d+)-(.+)\.html$", child_href)
            section = int(match.group(1)) if match else len(children)
            slug = match.group(2) if match else Path(child_href).stem
            path = f"chapters/ch-{chapter_number:02d}-s{section:02d}-{slug}.md"
            file_map[child_href] = path
            children.append({"title": child_link.get_text(" ", strip=True), "file": path, "html": child_href})
        file_map[href] = children[0]["file"] if children else ""
        toc.append({"title": title, "children": children})

    for html_name in list(file_map):
        html_path = source / html_name
        if not html_path.exists() or not is_section(html_name):
            continue
        soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "lxml")
        content = soup.select_one("#book-content")
        if content is None:
            continue
        for el in content.find_all(True):
            eid = el.get("id")
            if not eid:
                continue
            kind = classes(el)
            if el.name == "div" and ("chapter" in kind or "appendix" in kind) and re.fullmatch(r"ball-ch\d+", eid):
                assign_label(labels, eid, "ch")
            elif el.name == "div" and ("section" in kind or "chapter" in kind):
                assign_label(labels, eid, "sec" if not re.fullmatch(r"ball-ch\d+", eid) else "ch")
            elif "figure" in kind or "informalfigure" in kind:
                assign_label(labels, eid, "fig")
            elif "table" in kind and el.name == "div":
                assign_label(labels, eid, "tbl")
            elif eid in referenced:
                assign_label(labels, eid, "id")
    return toc, labels, file_map, referenced


def write_myst(toc) -> None:
    lines = [
        "version: 1",
        "project:",
        "  title: Introductory Chemistry",
        "  short_title: Intro Chemistry",
        "  description: A one-semester introductory chemistry textbook. MyST edition of the Saylor Academy HTML text adapted from David W. Ball.",
        "  authors:",
        "    - name: David W. Ball",
        "    - name: Saylor Academy",
        "  license: CC-BY-NC-SA-3.0",
        "  open_access: true",
        "  github: QuadriviumPress/introductoryChemistry",
        "  keywords:",
        "    - chemistry",
        "    - introductory chemistry",
        "    - open textbook",
        "  # Remote hosts often answer 403, 404, or 5xx to the CI checker even when the",
        "  # page is fine in a browser. Internal links and missing files still fail.",
        "  error_rules:",
        "    - rule: link-resolves",
        "      severity: ignore",
        "      keys:",
        '        - "{http,https}://**"',
        "    - rule: doi-link-valid",
        "      severity: ignore",
        "  toc:",
        "    - file: index.md",
    ]
    for entry in toc:
        if "children" in entry:
            lines.append(f"    - title: {yml_str(entry['title'])}")
            lines.append("      children:")
            for child in entry["children"]:
                lines.append(f"        - file: {child['file']}")
        else:
            lines.append(f"    - file: {entry['file']}")
    lines += [
        "site:",
        "  template: book-theme",
        "  title: Introductory Chemistry",
        "  options:",
        "    favicon: images/favicon.svg",
        "    logo: images/logo.svg",
        "    logo_dark: images/logo-dark.svg",
        "    logo_alt: Open book logo",
        "    logo_text: Intro Chemistry",
        "    logo_url: /",
        "    style: css/custom.css",
        "    hide_authors: false",
        "  nav:",
        "    - title: Sources & Attribution",
        "      url: https://github.com/QuadriviumPress/introductoryChemistry/blob/main/SOURCES.md",
        "",
    ]
    (ROOT / "myst.yml").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: python3 scripts/html_to_myst.py /path/to/text_introductory-chemistry")
    source = Path(sys.argv[1]).resolve()
    toc, labels, file_map, referenced = collect(source)
    missing = sorted(fragment for fragment in referenced if fragment not in labels)
    CHAPTERS.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    for stale in CHAPTERS.glob("*.md"):
        stale.unlink()
    for stale in FIGURES.iterdir():
        if stale.is_file():
            stale.unlink()
    ctx = Ctx(source, labels, file_map)
    written = 0
    for html_name, rel in sorted(file_map.items(), key=lambda item: item[1]):
        if not is_section(html_name):
            continue
        if not rel:
            continue
        out = ROOT / rel
        text = convert_page(source / html_name, out, ctx)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
        written += 1
        print(f"wrote {rel}")
    write_myst(toc)
    restored = restore_figures()
    updated = update_references(ROOT)
    restored_ids = {figure["source_id"] for figure in json.loads(MANIFEST.read_text(encoding="utf-8")) if figure.get("source_id")}
    missing = sorted(set(missing) - restored_ids)
    print(f"restored {restored} licensed replacement figures")
    print(f"applied {updated} reference updates")
    print(f"pages {written}; labels {len(labels)}; images {len(ctx.copied)}; unresolved refs {len(missing)}")
    if missing:
        print("unresolved:", ", ".join(missing[:30]))


if __name__ == "__main__":
    main()
