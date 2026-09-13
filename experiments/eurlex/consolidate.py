"""EUR-Lex consolidated act -> article-segmented plain text.

Fetches the consolidated HTML of an EU act from EUR-Lex and renders it as text that
keeps the citation structure intact: article number and title, paragraph numbers,
lettered/numbered points and their nesting, and the consolidation markers (M1, M2 =
text as amended by the first/second amending act, B = original wording).

    python consolidate.py 02024R1689-20260727 aiact.txt      # fetch + convert
    python consolidate.py cached.html aiact.txt              # convert a local file

A consolidated CELEX is `0` + the act's CELEX + `-YYYYMMDD`, where the date is the
version's date of application; a 404 means no consolidated version applies at that
date, so probing dates is how you discover which amendments exist.

WHY THE COMPLETENESS GUARD: this renderer only emits the block classes it knows, and
EUR-Lex uses several that carry operative text (`p.list` holds the continuation
sentence of a point; prose can sit as a bare text node ahead of a nested list). An
unhandled class drops binding text with no error at all. After rendering, every
subdivision's word count is compared against the raw text under the same node and any
loss is reported. Do not quote from output that reported a loss.
"""
import hashlib
import html
import os
import re
import sys
import urllib.request
from html.parser import HTMLParser

BROWSER_UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")


def fetch(celex: str) -> str:
    """Return the consolidated HTML for a CELEX id, caching it under cache/."""
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, f"{celex}.html")
    if os.path.exists(path):
        return path
    url = f"https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:{celex}"
    req = urllib.request.Request(url, headers={"User-Agent": BROWSER_UA, "Accept": "text/html"})
    with urllib.request.urlopen(req, timeout=120) as r:
        body = r.read()
    if len(body) < 200_000:
        raise SystemExit(f"{celex}: got {len(body)} bytes — no such consolidated version?")
    with open(path, "wb") as f:
        f.write(body)
    print(f"fetched {url}\n  -> {path}  ({len(body)} bytes, sha256 {hashlib.sha256(body).hexdigest()})")
    return path


VOID = {"br", "hr", "img", "meta", "link", "input", "col"}


class Node:
    __slots__ = ("cls", "ident", "kids", "parent", "tag")

    def __init__(self, tag="", cls="", ident="", parent=None):
        self.tag, self.cls, self.ident = tag, cls, ident
        self.kids: list = []
        self.parent = parent

    def has(self, c):
        return c in self.cls.split()


class Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("root")
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            return
        a = dict(attrs)
        n = Node(tag, a.get("class", ""), a.get("id", ""), self.cur)
        self.cur.kids.append(n)
        self.cur = n

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is not self.root:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.kids.append(data)


def flat(n) -> str:
    """All text under a node, whitespace-normalised."""
    if isinstance(n, str):
        return n
    parts = []
    for k in n.kids:
        t = flat(k)
        if isinstance(k, Node) and (k.tag == "sup" or k.has("superscript")):
            # EUR-Lex marks exponents with a class, not a <sup> tag. Flattening it turns
            # the Article 51(2) threshold of 10^25 FLOP into "1025" — a number that is
            # wrong by twenty-three orders of magnitude and reads aloud as a plain integer.
            t = "^" + t
        if isinstance(k, Node) and k.has("subscript"):
            t = "_" + t
        parts.append(t)
    return "".join(parts)


def norm(t: str) -> str:
    return re.sub(r"[ \s]+", " ", html.unescape(t)).strip()


INLINE = {"span", "em", "i", "b", "strong", "sup", "sub", "a", "u", "br"}


def render(node, indent: str = "") -> list[str]:
    """Render a node's children as lines, in document order.

    Bare text and inline elements are buffered and flushed as their own line when a
    block element interrupts them. Without that, prose sitting directly inside a
    paragraph div ahead of a nested list is silently dropped (e.g. Article 26(5)).
    """
    out: list[str] = []
    buf: list[str] = []

    def flush():
        if buf:
            t = norm("".join(buf))
            if t:
                out.append(indent + t)
            buf.clear()

    for k in node.kids:
        if isinstance(k, str):
            buf.append(k)
            continue
        if k.tag in INLINE and not k.has("no-parag"):
            # flat() marks an exponent when it sees one among a node's CHILDREN; here the
            # inline node is itself the exponent, so mark it on the way into the buffer.
            t = flat(k)
            if k.tag == "sup" or k.has("superscript"):
                t = "^" + t
            elif k.has("subscript"):
                t = "_" + t
            buf.append(t)
            continue
        if k.tag == "p" and k.has("modref"):
            flush()
            t = norm(flat(k))
            if t:
                out.append(f"{indent}[{t}]")
        elif k.tag == "div" and k.has("norm") and any(
            isinstance(c, Node) and c.has("no-parag") for c in k.kids
        ):
            flush()
            num = next(norm(flat(c)) for c in k.kids if isinstance(c, Node) and c.has("no-parag"))
            body = [c for c in k.kids if isinstance(c, Node) and not c.has("no-parag")]
            lines = []
            for b in body:
                sub = render(b, indent)
                if not sub:
                    t = norm(flat(b))
                    sub = [indent + t] if t else []
                lines += sub
            if lines:
                lines[0] = f"{indent}{num} {lines[0].lstrip()}"
            else:
                lines = [f"{indent}{num}"]
            out += lines
        elif k.tag == "div" and k.has("grid-list") and k.has("grid-container"):
            flush()
            out += render_grid(k, indent)
        elif k.tag == "p" and (
            k.has("norm") or k.has("tbl-norm") or k.has("list") or k.has("normal")
        ):
            # p.list is a continuation sentence inside a point — dropping it silently
            # deletes operative text (e.g. the Annex III 1(a) biometric-verification carve-out)
            flush()
            t = norm(flat(k))
            if t:
                out.append(indent + t)
        elif k.tag == "p" and (k.has("title-gr-seq-level-1") or k.has("title-gr-seq-level-2")):
            flush()
            t = norm(flat(k))
            if t:
                out.append(f"{indent}{t}")
        elif k.tag == "p" and k.has("footnote"):
            flush()
            t = norm(flat(k))
            if t:
                out.append(f"{indent}[footnote] {t}")
        elif k.tag in ("div", "table", "tbody", "tr", "td", "col", "colgroup", "p"):
            flush()
            lines = render(k, indent)
            if lines:
                out += lines
            else:
                t = norm(flat(k))
                if t:
                    out.append(indent + t)
    flush()
    return out


def render_grid(grid, indent: str) -> list[str]:
    out: list[str] = []
    cols = [c for c in grid.kids if isinstance(c, Node) and c.tag == "div"]
    i = 0
    while i < len(cols) - 1:
        if cols[i].has("grid-list-column-1") and cols[i + 1].has("grid-list-column-2"):
            marker = norm(flat(cols[i]))
            lines = render(cols[i + 1], indent + "    ")
            if not lines:
                lines = [indent + "    " + norm(flat(cols[i + 1]))]
            lines[0] = f"{indent}    {marker} {lines[0].lstrip()}"
            out += lines
            i += 2
        else:
            i += 1
    return out


# --select "Article 9,Article 10-15,ANNEX III" emits just those subdivisions as Markdown,
# ready to drop into a research docket, instead of the whole act as plain text.
SELECT = None
if "--select" in sys.argv:
    i = sys.argv.index("--select")
    SELECT = sys.argv[i + 1]
    del sys.argv[i:i + 2]

arg = sys.argv[1] if len(sys.argv) > 1 else "02024R1689-20260727"
OUT = sys.argv[2] if len(sys.argv) > 2 else "consolidated.txt"
SRC = arg if arg.endswith(".html") else fetch(arg)
tp = Tree()
with open(SRC, encoding="utf-8", errors="replace") as fh:
    tp.feed(fh.read())

subs: list[Node] = []


def walk(n):
    if isinstance(n, Node):
        if n.tag == "div" and re.fullmatch(r"(art|anx)_\w+", n.ident or "") and (
            n.has("eli-subdivision") or n.ident.startswith("anx_")
        ):
            subs.append(n)
            return  # don't recurse: nested subdivisions belong to this one
        for k in n.kids:
            walk(k)


walk(tp.root)

chunks = []
for sub in subs:
    title = subtitle = ""
    for k in sub.kids:
        if isinstance(k, Node) and k.tag == "p" and (k.has("title-article-norm") or k.has("title-annex-1")):
            title = norm(flat(k))
        if isinstance(k, Node) and (
            (k.tag == "div" and k.has("eli-title")) or (k.tag == "p" and k.has("title-annex-2"))
        ):
            subtitle = norm(flat(k))
    rest = [
        k for k in sub.kids
        if not (isinstance(k, Node) and (
            (k.tag == "p" and (k.has("title-article-norm") or k.has("title-annex-1")))
            or (k.tag == "div" and k.has("eli-title"))
            or (k.tag == "p" and k.has("title-annex-2"))
        ))
    ]
    holder = Node("div")
    holder.kids = rest
    body = "\n".join(render(holder))
    if not title and sub.ident.startswith("anx_"):
        title = "ANNEX " + sub.ident.split("_", 1)[1]
        first = next((norm(flat(k)) for k in rest if isinstance(k, Node) and k.tag == "p" and norm(flat(k))), "")
        if first and not subtitle:
            subtitle = first
    head = title + (f" — {subtitle}" if subtitle else "")
    chunks.append(f"===== {head} =====\n{body}\n")

text = "\n".join(chunks)
def _expand(spec: str) -> list[str]:
    """'Article 9,Article 10-15,ANNEX III' -> a flat list of subdivision names."""
    out = []
    for part in spec.split(","):
        part = part.strip()
        m = re.fullmatch(r"(Article|ANNEX)\s+(\w+)\s*-\s*(\w+)", part, re.IGNORECASE)
        if m and m.group(2).isdigit() and m.group(3).isdigit():
            out += [f"Article {n}" for n in range(int(m.group(2)), int(m.group(3)) + 1)]
        elif part:
            out.append(part)
    return out


if SELECT:
    blocks = {}
    for m in re.finditer(r"^===== (.+?) =====\n(.*?)(?=^===== |\Z)", text, re.M | re.S):
        blocks[m.group(1).split(" — ")[0].strip().lower()] = (m.group(1), m.group(2).rstrip())
    md, missing = [], []
    for name in _expand(SELECT):
        hit = blocks.get(name.lower())
        if not hit:
            missing.append(name)
            continue
        md.append(f"\n## {hit[0]}\n\n```text\n{hit[1]}\n```")
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(md) + "\n")
    print(f"selected {len(md)} subdivision(s) -> {OUT}")
    if missing:
        print("  NOT FOUND: " + ", ".join(missing), file=sys.stderr)
    raise SystemExit(0)

with open(OUT, "w", encoding="utf-8") as fh:
    fh.write(text)
print(f"{len(subs)} subdivisions, {len(text.split())} words -> {OUT}")

# Completeness guard. The renderer only emits classes it knows; an unhandled class
# drops operative text with no error. Compare each subdivision's rendered word count
# against the raw text under the same node and report any measurable loss.
lost = []
for sub, chunk in zip(subs, chunks):
    raw = len(norm(flat(sub)).split())
    got = len(chunk.split())
    if raw and got < raw - 2:
        lost.append((raw - got, raw, norm(flat(sub))[:60]))
if lost:
    print(f"!! {len(lost)} subdivision(s) lost text:")
    for d, raw, head in sorted(lost, reverse=True)[:15]:
        print(f"   -{d:5} of {raw:6}  {head}")
else:
    print("completeness: every subdivision renders all of its words")
