"""Build a written reference for a series, from what the episodes actually say.

A list of works read aloud is unusable to someone on a train — they cannot write it down and
will not remember it — so the scripts carry no sources beat. The sourcing still has to exist
somewhere a person can check, and this is where: one Markdown document per series, assembled
after the episodes are written, from three inputs that are each authoritative for a different
thing.

  the TRANSCRIPTS   what was actually said: every provision cited, every proper noun spoken
  the PLAN          what each episode was built on: its `**Sources:**` beat, the planner's own list
  the DOCKET        the verified citations themselves, in research/*.md

Anything the plan lists that the docket cannot support is reported rather than quietly dropped:
a reference document that hides its gaps is worse than none.
"""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path

from prosodia.author.planparse import extract_episode_section, parse_episode_index

_CITE = re.compile(r"\b(?:Article|Articles|Art\.|Arts\.)\s*(\d+[a-z]?)(\([^)]{1,10}\))?")
_ANNEX = re.compile(r"\bAnnex(?:es)?\s+([IVXL]+)\b")
_SOURCES_START = re.compile(r"(?im)^[ \t]*\*\*Sources\b")
def _looks_like_a_title(t: str) -> bool:
    """Is this italic span a WORK, or just an italicised journal name?

    Journals are italicised in a citation too — *Tex. L. Rev.*, *U. Chi. Legal F.*, *JASIST* —
    and the docket is not expected to repeat their abbreviated forms, so checking them
    produces noise rather than findings.
    """
    tokens = t.split()
    if len(tokens) < 3:
        return False
    return sum(1 for w in tokens if w.endswith(".") and len(w) <= 6) < 2


def _sources_beat(section: str) -> str | None:
    """The episode's `**Sources**` beat, label stripped, to the next blank line.

    Parsed rather than matched: the label appears as `**Sources:**` in some episodes and as
    `**Sources** (all in research/…):` in others, and a single regex spanning both kept
    running past the label to a colon later in the prose and returning only the tail.
    """
    m = _SOURCES_START.search(section)
    if not m:
        return None
    chunk = re.split(r"\n[ \t]*\n", section[m.start():], 1)[0]
    chunk = re.sub(r"^[ \t]*\*\*Sources\b[^*]*\*\*", "", chunk, count=1)  # the label
    chunk = re.sub(r"^\s*\([^)]*\)", "", chunk, count=1)                    # a parenthetical
    return re.sub(r"\s+", " ", chunk.lstrip(" :\t")).strip() or None
_LEXICON = re.compile(r"(?is)##\s+Names for the lexicon\s*\n(.*)")


def _norm(t: str) -> str:
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", t)).strip().lower()


def _spoken(transcript: str) -> str:
    """The body of a transcript, without front-matter, directives or beat titles."""
    body = transcript.split("---", 2)[-1]
    body = re.sub(r"(?m)^##[^\n]*$", "", body)          # beat titles are not spoken
    return re.sub(r"\{[^{}]*\}", "", body)


def _provisions(text: str) -> list[str]:
    """Provisions in first-mention order, with their sub-paragraphs collected."""
    out: dict[str, set[str]] = {}
    order: list[str] = []
    for m in _CITE.finditer(text):
        key = f"Article {m.group(1)}"
        if key not in out:
            out[key], _ = set(), order.append(key)
        if m.group(2):
            out[key].add(m.group(2))
    for m in _ANNEX.finditer(text):
        key = f"Annex {m.group(1)}"
        if key not in out:
            out[key], _ = set(), order.append(key)
    return [k + (" " + ", ".join(sorted(out[k])) if out[k] else "") for k in order]


def _names_spoken(transcript_body: str, lexicon_names: list[str]) -> list[str]:
    """Which of the plan's proper nouns this episode actually says.

    Matched on word boundaries: a plain substring test put "CEN" inside "licence" and
    "recent", and "Annex" inside "Annexes", so the first run reported three institutions
    that appear nowhere in the script.
    """
    spoken = _norm(transcript_body)
    out = []
    for n in lexicon_names:
        key = _norm(re.sub(r"\s*\(.*?\)", "", n))
        if key and re.search(rf"\b{re.escape(key)}\b", spoken):
            out.append(n)
    return out


def build_references(proj: Path) -> tuple[str, list[str]]:
    """Return (markdown, warnings)."""
    warnings: list[str] = []
    outline_path = proj / "plan" / "outline.md"
    if not outline_path.is_file():
        return "", [f"{outline_path} does not exist"]
    outline = outline_path.read_text(encoding="utf-8")
    episodes = parse_episode_index(outline)

    lex = _LEXICON.search(outline)
    lexicon_names = (
        [ln[2:].strip() for ln in lex.group(1).splitlines() if ln.startswith("- ")] if lex else []
    )

    research = sorted((proj / "research").glob("*.md")) if (proj / "research").is_dir() else []
    docket = "\n".join(f.read_text(encoding="utf-8") for f in research)
    docket_n = _norm(docket)

    series = (proj / "series.yaml").read_text(encoding="utf-8") if (proj / "series.yaml").is_file() else ""
    title = (re.search(r'(?m)^series:\s*"?([^"\n]+)"?', series) or [None, proj.name])[1].strip()

    lines = [
        f"# {title} — sources and references",
        "",
        "Assembled from the episode transcripts, the series plan and the research docket. **The",
        "episodes carry no spoken source list**: a bibliography read aloud is unusable to someone",
        "who is travelling, so the sourcing lives here instead. Regenerate with",
        "`prosodia references --project <dir>`.",
        "",
        "Provisions are listed in the order each episode first names them. Where an item the plan",
        "relies on could not be found in `research/`, it is marked so rather than omitted.",
        "",
    ]

    all_provisions: dict[str, list[int]] = {}
    for e in episodes:
        n = e["n"]
        tdir = proj / "episodes" / e["slug"]
        tfile = tdir / "transcript.md"
        section = extract_episode_section(outline, n) or ""
        lines.append(f"## Episode {n} — {e['title']}")
        lines.append("")
        if not tfile.is_file():
            lines += ["*Not yet written.*", ""]
            warnings.append(f"episode {n}: no transcript at {tfile}")
            continue
        body = _spoken(tfile.read_text(encoding="utf-8"))

        provs = _provisions(body)
        for p in provs:
            all_provisions.setdefault(p.split(" (")[0], []).append(n)
        if provs:
            lines += ["**Provisions cited in the episode**", "", "- " + "\n- ".join(provs), ""]

        names = _names_spoken(body, lexicon_names)
        if names:
            lines += ["**People, bodies and instruments named aloud**", "",
                      ", ".join(names) + ".", ""]

        beat = _sources_beat(section)
        if beat:
            lines += ["**What the episode was built on** *(from the plan)*", "", beat, ""]
            for work in re.findall(r"\*([^*]{6,90})\*", beat):
                if _looks_like_a_title(work.strip()) and _norm(work) not in docket_n:
                    warnings.append(
                        f"episode {n}: the plan cites '{work.strip()}' but no research/ file "
                        "mentions it"
                    )
        else:
            warnings.append(f"episode {n}: the plan states no Sources beat")

    lines += ["---", "", "## Where each provision is taught or cited", ""]
    def _key(p):
        m = re.search(r"(\d+)", p)
        return (0 if p.startswith("Article") else 1, int(m.group(1)) if m else 0)
    for p in sorted(all_provisions, key=_key):
        eps = sorted(set(all_provisions[p]))
        lines.append(f"- **{p}** — episode{'s' if len(eps) > 1 else ''} "
                     + ", ".join(str(x) for x in eps))
    lines += ["", "---", "", "## The docket these episodes were checked against", ""]
    for f in research:
        first = next((ln for ln in f.read_text(encoding="utf-8").splitlines() if ln.startswith("# ")), "")
        lines.append(f"- `research/{f.name}` — {first.lstrip('# ').strip()}")
    if not research:
        lines.append("*No `research/` directory — nothing was checked against a docket.*")
    lines.append("")
    return "\n".join(lines), warnings
