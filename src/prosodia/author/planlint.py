"""Deterministic checks on a Planner outline, before twelve episodes are written from it.

The writer has an editor; the plan had nothing, and it sits upstream of every episode in
the series, so one bad decision in it is multiplied by the episode count. This module is
the cheap half of reviewing a plan: everything that can be settled by counting or by
string comparison against the research docket, with no model call.

It is deliberately NOT a planner/reviewer loop. The defects worth catching here are the
ones an LLM reviewer is worst at — whether 110 article numbers all resolve, whether a
quotation is verbatim, whether two thirds of a statute is covered only by a range — while
the judgement it is good at (is the difficulty curve right, is the contested material
steelmanned) wants an independent read, not another turn of the same model.

Checks that need a docket are skipped, with a note, when ``research/`` is absent, so this
runs against any project.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

from prosodia.author.planparse import (
    extract_episode_section,
    extract_series_sections,
    parse_episode_index,
)

ERROR, WARN, NOTE = "error", "warn", "note"


@dataclass
class Finding:
    level: str
    code: str
    message: str
    episode: int | None = None

    def render(self) -> str:
        where = f"ep{self.episode:02d}" if self.episode else "series"
        return f"  [{self.level:<5}] {where:<7} {self.code:<18} {self.message}"


# ---- text helpers -----------------------------------------------------------

def norm(t: str) -> str:
    """Fold to a comparable form: no accents, no markdown, no punctuation, lowercase."""
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[*_`]", "", t)
    t = re.sub(r"[^\w\s%]", " ", t)
    return re.sub(r"\s+", " ", t).strip().lower()


_CITE = re.compile(r"\b(?:Article|Articles|Art\.|Arts\.)\s*(\d+[a-z]?)")
_ANNEX = re.compile(r"\bAnnex\s+([IVXL]+)\b")
# "Art. 166(7) of the Italian Data Protection Code" is not a citation to THIS instrument.
_OTHER_INSTRUMENT = re.compile(
    r"^(?:\([\dا-ي\w]{1,4}\)\s*)*\s*of\s+(?:the\s+)?[A-Z][\w’'-]*(?:\s+[A-Z][\w’'-]*)*"
)
def quoted_spans(text: str) -> list[tuple[int, str]]:
    """(offset, span) for each quotation, paired sequentially.

    A regex of the form "([^"]+)" mispairs as soon as a short quotation appears: it happily
    matches from the CLOSING quote of one to the OPENING quote of the next, inventing a span
    that is not a quotation at all. Split and take the odd segments instead.
    """
    out, pos = [], 0
    for i, seg in enumerate(text.split('"')):
        if i % 2 == 1:
            out.append((pos + 1, seg))
        pos += len(seg) + 1
    return out
_OUTSIDE = re.compile(r"\[OUTSIDE DOCKET:")
# Markers that say the quoted words are a MISREADING being corrected, not the instrument's.
_MISREADING = re.compile(
    r"(?i)\bwrong(?: reading)?\s*[:\u2014-]|\bnot\b[^.]{0,20}\bmeaning\b|\bhears?\b[^.]{0,12}$|"
    r"\bthinks? it means\b|\bmistakes? it for\b"
)
_TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$", re.MULTILINE)
_RANGE = re.compile(r"(\d+)\s*[‐-―-]\s*(\d+)")
_LENGTH = re.compile(r"(?im)\*\*Length:?\*\*[^\n\d]{0,20}(\d{1,3})")
_VERIFY = re.compile(r"(?i)\b(verify|check .{0,30}before (?:it is|being) (?:spoken|read))\b")


_DOCKET_RANGE = re.compile(
    r"\b(?:Articles|Arts\.?)\s*(\d+)\s*(?:[\u2010-\u2015-]|to)\s*(\d+)", re.IGNORECASE
)
_DOCKET_ONE = re.compile(r"\b(?:Article|Art\.)\s*(\d+[a-z]?)", re.IGNORECASE)
_DOCKET_ANNEX = re.compile(r"\bAnnex(?:es)?\s+([IVXL]+)(?:\s*(?:[\u2010-\u2015-]|,|and)\s*([IVXL]+))*",
                           re.IGNORECASE)


def docket_provisions(docket: str) -> set[str]:
    """Every provision the docket names, with its ranges expanded.

    A docket that says "Arts. 65-68" does supply Article 67. Not expanding here would make
    this module commit the exact error it exists to catch in the plan.
    """
    covered: set[str] = set()
    for m in _DOCKET_RANGE.finditer(docket):
        lo, hi = int(m.group(1)), int(m.group(2))
        if 0 < hi - lo < 40:
            covered |= {f"article {n}" for n in range(lo, hi + 1)}
    covered |= {f"article {m.group(1).lower()}" for m in _DOCKET_ONE.finditer(docket)}
    for m in re.finditer(r"\bAnnex(?:es)?\s+([IVXL]+(?:\s*(?:,|and|[\u2010-\u2015-])\s*[IVXL]+)*)",
                         docket, re.IGNORECASE):
        for part in re.split(r"\s*(?:,|and|[\u2010-\u2015-])\s*", m.group(1)):
            if part.strip():
                covered.add(f"annex {part.strip().lower()}")
    return covered


_SUPERSEDED = re.compile(r"(?im)^[>\s*_]*SUPERSEDED\b")


def _load_docket(proj: Path) -> tuple[str, str, list[str]]:
    """Return (all docket text, the QUOTABLE subset, file names).

    A file the docket marks SUPERSEDED stays a legitimate place to learn that a provision
    exists — it is usually kept for the articles its replacement does not carry — but it is
    not a place to take words from. Episode 1's writer quoted Art. 2(1)(c) out of a file
    headed SUPERSEDED and saying in terms that nothing in it should be spoken; the editor
    caught it and this check had not, because it compared against the whole directory.
    """
    files = sorted((proj / "research").glob("*.md")) if (proj / "research").is_dir() else []
    texts = {f: f.read_text(encoding="utf-8") for f in files}
    quotable = [t for f, t in texts.items() if not _SUPERSEDED.search(t[:4000])]
    return "\n".join(texts.values()), "\n".join(quotable), [f.name for f in files]


# ---- checks -----------------------------------------------------------------

def check_structure(episodes: list[dict], sections: dict[int, str]) -> list[Finding]:
    out = []
    for e in episodes:
        s = sections.get(e["n"]) or ""
        if not s:
            out.append(Finding(ERROR, "no-section", "episode has no extractable section", e["n"]))
            continue
        required = ["Transfer questions", "Sources"]
        if e.get("type", "apparatus") == "apparatus":
            required += ["Opening instance", "The variants"]
        for field in required:
            if field.lower() not in s.lower():
                out.append(Finding(WARN, "missing-field", f"no '{field}' beat", e["n"]))
    return out


def check_citations(text: str, docket: str, sections: dict[int, str]) -> list[Finding]:
    """Every citation must resolve in the docket, or be marked OUTSIDE DOCKET."""
    covered = docket_provisions(docket)
    out, seen = [], set()
    for ep, s in sections.items():
        for m in _CITE.finditer(s):
            tail = s[m.end():m.end() + 90]
            if _OTHER_INSTRUMENT.match(tail.strip()):
                continue  # a citation to a different instrument, named right after it
            key = f"article {m.group(1).lower()}"
            if key in covered or (ep, key) in seen:
                continue
            seen.add((ep, key))
            out.append(Finding(ERROR, "cite-not-in-docket",
                               f"cites Article {m.group(1)}, which no research/ file contains", ep))
        for m in _ANNEX.finditer(s):
            key = f"annex {m.group(1).lower()}"
            if key in covered or (ep, key) in seen:
                continue
            seen.add((ep, key))
            out.append(Finding(ERROR, "cite-not-in-docket",
                               f"cites Annex {m.group(1)}, which no research/ file contains", ep))
    return out


def check_quotations(sections: dict[int, str], docket: str) -> list[Finding]:
    """A quoted span presented next to a citation must be verbatim in the docket."""
    dn = norm(docket)
    out = []
    for ep, s in sections.items():
        for start, q in quoted_spans(s):
            if len(q.split()) < 5 or "\n" in q:
                continue
            before = s[max(0, start - 250):start]
            if not (_CITE.search(before) or _ANNEX.search(before)):
                continue  # not attributed to the instrument
            if _MISREADING.search(before[-70:]):
                # The load-bearing-terms beat quotes the listener's WRONG reading next to the
                # article that defines the term — `**intended purpose** (3(12)) — wrong: "what
                # it is used for"`. That is the plan doing its job, not quoting the instrument.
                continue
            if norm(q) in dn:
                continue
            out.append(Finding(ERROR, "quote-not-verbatim",
                               f'quotes "{q[:70]}..." — not verbatim in any quotable '
                               "research/ file (a file marked SUPERSEDED does not count)", ep))
    return out


def check_coverage_map(series_md: str, episodes: list[dict]) -> list[Finding]:
    """Bare ranges, and parts listed against parts assigned."""
    out = []
    rows = _TABLE_ROW.findall(series_md)
    assigned_rows = [r for r in rows if re.search(r"\*\*Ep\s*\d+\*\*|\bEp\s*\d+\b", r)]
    for r in assigned_rows:
        part = r.split("|")[1] if r.count("|") >= 2 else r
        for m in _RANGE.finditer(part):
            lo, hi = int(m.group(1)), int(m.group(2))
            if hi - lo < 2:
                continue
            members = {str(n) for n in range(lo, hi + 1)}
            named = set(re.findall(r"\b(\d+)\b", _RANGE.sub(" ", part)))
            if not members & named:
                out.append(Finding(
                    ERROR, "bare-range",
                    f"coverage map assigns {m.group(0)} as a bare range ({hi - lo + 1} parts) — "
                    "a range silently covers provisions you never read, including ones inserted "
                    "by a later amendment",
                ))
    if not assigned_rows:
        out.append(Finding(WARN, "no-coverage-map", "found no coverage-map table with episode assignments"))
    return out


def check_applied_coverage(sections: dict[int, str], episodes: list[dict],
                           series_md: str) -> list[Finding]:
    """Provisions the episode APPLIES, against provisions it is assigned to teach.

    The failure this catches is an episode that names twenty-five obligations in one
    enumerated paragraph and then works three of them — exposition front-loaded with a case
    attached as decoration. Counting citations in the opening instance is the wrong proxy,
    because an instance is narrative and its citations land later; what separates taught from
    merely listed is whether a provision appears OUTSIDE the enumeration.
    """
    taught: dict[int, set[str]] = {}
    for row in _TABLE_ROW.findall(series_md):
        m = re.search(r"\*\*Ep\s*(\d+)\*\*", row)
        if not m:
            continue
        part = row.split("|")[1]
        expanded = _RANGE.sub(
            lambda x: " ".join(str(n) for n in range(int(x.group(1)), int(x.group(2)) + 1))
            if 0 < int(x.group(2)) - int(x.group(1)) < 40 else x.group(0), part)
        taught.setdefault(int(m.group(1)), set()).update(re.findall(r"\b(\d+)\b", expanded))
    out = []
    for e in episodes:
        if e.get("type", "apparatus") != "apparatus":
            continue
        s = sections.get(e["n"]) or ""
        n_taught = len(taught.get(e["n"], ()))
        if n_taught < 12:
            continue
        worked: set[str] = set()
        for para in re.split(r"\n\s*\n", s):
            cites = _CITE.findall(para)
            if len(cites) >= 6:
                continue  # an enumeration: listed, not worked
            worked |= set(cites)
        ratio = len(worked) / n_taught
        if ratio < 0.40:
            out.append(Finding(
                WARN, "applied-coverage",
                f"assigned ~{n_taught} provisions, works {len(worked)} of them outside an "
                f"enumeration ({ratio:.0%}: {', '.join(sorted(worked, key=int)[:8])}) — the rest "
                "arrive as assertion, with no instance to apply them to",
                e["n"]))
    return out


def check_runtime(episodes: list[dict], target: int) -> list[Finding]:
    """Report the summed runtime; flag only a LARGE divergence, in either direction.

    The series default is a soft anchor, not a cap. The first version of this check flagged
    any overshoot above 5% — which punished exactly the honesty it should reward, since a
    planner that sizes a dense episode properly and says so is doing its job. What is worth
    a look is a plan whose own figures have drifted far from the anchor: either the anchor
    is wrong for this material, or the lengths were not thought about.
    """
    stated = [e.get("target_minutes") for e in episodes if e.get("target_minutes")]
    total = sum(e.get("target_minutes") or target for e in episodes)
    budget = target * len(episodes)
    if not budget or not stated:
        return []
    drift = total / budget - 1
    if abs(drift) > 0.25:
        way = "over" if drift > 0 else "under"
        return [Finding(WARN, "runtime",
                        f"planned length sums to {total} min against {budget} "
                        f"({target} x {len(episodes)}), {abs(drift):.0%} {way} — if the episodes "
                        "are right, the series default is wrong for this material")]
    return []


def check_opening_types(sections: dict[int, str], episodes: list[dict]) -> list[Finding]:
    types: dict[str, list[int]] = {}
    for e in episodes:
        if e.get("type", "apparatus") != "apparatus":
            continue
        m = re.search(r"(?i)\*type:\s*([^*.]+)", sections.get(e["n"]) or "")
        if m:
            types.setdefault(norm(m.group(1)), []).append(e["n"])
    out = []
    for t, eps in types.items():
        if len(eps) > 1:
            out.append(Finding(WARN, "opening-repeat",
                               f"episodes {eps} declare the same opening type ('{t}')"))
    return out


def check_do_not_use(sections: dict[int, str], docket: str) -> list[Finding]:
    """Tokens the docket marks unusable, appearing in the plan anyway."""
    banned: set[str] = set()
    for para in re.split(r"\n\s*\n", docket):
        if re.search(r"(?i)\bdo not use\b|\bunverified\b|\bmust not be used\b", para):
            for t in re.findall(
                r"(?:€|EUR)\s?[\d][\d.,\s]{0,12}?(?:\s?(?:m|million|bn|billion))?\b", para
            ):
                banned.add(re.sub(r"\s+", " ", t).strip())
    out = []
    for ep, s in sections.items():
        flat = re.sub(r"[\s*_]+", " ", s)
        hit: set[str] = set()
        for tok in banned:
            amount = re.sub(r"^(?:€|EUR)\s?", "", tok)
            pat = re.escape(amount).replace(r"\ ", r"\s*")
            if amount in hit:
                continue
            if re.search(rf"(?:€|EUR)\s?{pat}", flat):
                hit.add(amount)
                out.append(Finding(WARN, "docket-veto",
                                   f"uses the figure '{tok}', which the docket flags as "
                                   "unverified or marks do-not-use", ep))
    return out


def check_budgets(sections: dict[int, str]) -> list[Finding]:
    out = []
    for ep, s in sections.items():
        n_outside = len(_OUTSIDE.findall(s))
        if n_outside > 3:
            out.append(Finding(ERROR, "outside-docket",
                               f"{n_outside} items marked OUTSIDE DOCKET — this episode is not "
                               "plannable from this docket", ep))
        n_verify = len(_VERIFY.findall(s))
        if n_verify > 1:
            out.append(Finding(WARN, "verify-budget",
                               f"{n_verify} items to verify at write time; the writer's budget is 1",
                               ep))
        if _TABLE_ROW.search(s):
            out.append(Finding(WARN, "unsayable",
                               "contains a table — one voice, no picture; plan the spoken path "
                               "through it instead", ep))
        for para in re.split(r"\n\s*\n", s):
            nums = _CITE.findall(para)
            if len(nums) >= 8:
                out.append(Finding(WARN, "unsayable",
                                   f"one paragraph names {len(nums)} provisions in sequence — "
                                   "that is a list read aloud, not a passage", ep))
                break
    return out


def check_prerequisites(sections: dict[int, str], episodes: list[dict]) -> list[Finding]:
    out = []
    known = {e["n"] for e in episodes}
    for e in episodes:
        m = re.search(r"(?i)\*\*Prerequisites:?\*\*([^\n]*)", sections.get(e["n"]) or "")
        if not m:
            continue
        refs: set[int] = set()
        for run in re.findall(r"\bEps?\.?\s*((?:\d+\s*(?:[,&]|and|[\u2010-\u2015-])?\s*)+)", m.group(1)):
            nums = [int(x) for x in re.findall(r"\d+", run)]
            if re.search(r"\d\s*[\u2010-\u2015-]\s*\d", run) and len(nums) == 2:
                refs |= set(range(min(nums), max(nums) + 1))
            else:
                refs |= set(nums)
        for n in sorted(refs):
            if n >= e["n"]:
                out.append(Finding(ERROR, "forward-prereq",
                                   f"lists Episode {n} as a prerequisite of Episode {e['n']}", e["n"]))
            elif n not in known:
                out.append(Finding(ERROR, "unknown-prereq",
                                   f"lists Episode {n}, which the plan does not define", e["n"]))
    return out


# ---- driver -----------------------------------------------------------------

def lint_plan(outline_md: str, *, docket: str = "", quotable: str | None = None,
              target_minutes: int = 30) -> list[Finding]:
    episodes = parse_episode_index(outline_md)
    if not episodes:
        return [Finding(ERROR, "no-episodes", "no episode headings found in the outline")]
    sections = {e["n"]: (extract_episode_section(outline_md, e["n"]) or "") for e in episodes}
    series_md = extract_series_sections(outline_md) or ""

    findings: list[Finding] = []
    findings += check_structure(episodes, sections)
    findings += check_prerequisites(sections, episodes)
    findings += check_coverage_map(series_md, episodes)
    findings += check_applied_coverage(sections, episodes, series_md)
    findings += check_opening_types(sections, episodes)
    findings += check_runtime(episodes, target_minutes)
    findings += check_budgets(sections)
    if docket.strip():
        findings += check_citations(outline_md, docket, sections)
        findings += check_quotations(sections, docket if quotable is None else quotable)
        findings += check_do_not_use(sections, docket)
    else:
        findings.append(Finding(NOTE, "no-docket",
                                "no research/*.md — citation, quotation and veto checks skipped"))
    order = {ERROR: 0, WARN: 1, NOTE: 2}
    return sorted(findings, key=lambda f: (order[f.level], f.episode or 0, f.code))


def lint_project(proj: Path, *, target_minutes: int | None = None) -> list[Finding]:
    outline = proj / "plan" / "outline.md"
    if not outline.is_file():
        return [Finding(ERROR, "no-plan", f"{outline} does not exist — run `prosodia plan` first")]
    docket, quotable, _ = _load_docket(proj)
    return lint_plan(outline.read_text(encoding="utf-8"), docket=docket, quotable=quotable,
                     target_minutes=target_minutes or 30)
