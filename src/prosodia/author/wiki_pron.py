"""Pull pronunciations (IPA + Wikipedia respelling) for a list of names.

Author-side (stdlib only, no torch/GPU). Batch-queries the MediaWiki API for the
plaintext lead of each article and parses the pronunciation parenthetical, e.g.

    Thucydides ( /θjuːˈsɪdɪˌdiːz/ thew-SID-ih-deez ) was an Athenian ...
                 ^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^
                 ipa              respell

The pronunciation lives in the lead's ``{{respell|...}}`` and ``{{IPAc-en|...}}``
templates (the plaintext ``extract`` API strips them), so we fetch the lead WIKITEXT and
reconstruct them: ``{{respell|thew|SID|ih|deez}}`` -> ``thew-SID-ih-deez`` (a ``_`` arg is
a word-space, ``,_`` a variant separator). This feeds the lexicon agent AUTHORITATIVE
pronunciations so it doesn't guess. Wikipedia's respelling is its own convention (hyphens +
ALL-CAPS stress) — exactly the format Chatterbox mis-reads — so it must still be converted
to a natural run-on spelling; see ``roles/RESPELL_GUIDELINES.md``.

Usage:
    python -m prosodia.author.wiki_pron Thucydides Nietzsche "Ibn Khaldun"
    python -m prosodia.author.wiki_pron --names-file names.txt --out prons.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass

API = "https://en.wikipedia.org/w/api.php"
_UA = "prosodia-lexicon/0.1 (https://github.com/ZubeyirOflaz/prosodia)"
_BATCH = 20  # titles per revisions request

_RESPELL_TMPL = re.compile(r"\{\{\s*respell\s*\|([^{}]*)\}\}", re.I)
_IPACEN_TMPL = re.compile(r"\{\{\s*IPAc-en\s*\|([^{}]*)\}\}", re.I)


@dataclass
class Pron:
    name: str
    title: str | None = None
    ipa: str | None = None
    respell: str | None = None
    url: str | None = None
    found: bool = False
    note: str = ""


def _respell_from_args(argstr: str) -> str:
    """Reconstruct the respelling from ``{{respell}}`` args. Each arg is a syllable joined
    by '-'; a ``_`` arg is a word-space; ``,`` / ``,_`` a variant separator (', ')."""
    parts: list[str] = []
    pending = ""  # separator before the next syllable ('' -> default hyphen)
    for a in (x.strip() for x in argstr.split("|")):
        if a == "":
            continue
        if a == "_":
            pending = " "
        elif a in (",", ",_"):
            pending = ", "
        else:
            if parts:
                parts.append(pending or "-")
            parts.append(a)
            pending = ""
    s = "".join(parts)
    # Tidy artifacts from empty/odd template args: collapse repeated hyphens and strip
    # hyphens left dangling next to spaces/commas or at the ends.
    s = re.sub(r"-{2,}", "-", s)
    s = re.sub(r"\s*-\s+", " ", s)          # "os- ass" / "os -ass" -> "os ass"
    s = re.sub(r"-?\s*,\s*-?", ", ", s)     # ", " variant boundary, hyphens dropped
    return s.strip(" -")


def _ipa_from_args(argstr: str) -> str:
    """Best-effort English IPA from ``{{IPAc-en}}`` args (symbols concatenated; ``_`` ->
    space). Secondary — Chatterbox can't consume IPA; the respelling is the prize."""
    body = "".join(" " if a.strip() == "_" else a.strip() for a in argstr.split("|"))
    return f"/{body}/" if body else ""


def parse_wikitext(content: str) -> tuple[str | None, str | None]:
    """Return (ipa, respell) from a lead's wikitext — the FIRST respell/IPAc-en template
    (that's the subject's own pronunciation)."""
    rm = _RESPELL_TMPL.search(content)
    respell = _respell_from_args(rm.group(1)) if rm else None
    im = _IPACEN_TMPL.search(content)
    ipa = _ipa_from_args(im.group(1)) if im else None
    return (ipa or None), (respell or None)


def _resolve_chain(name: str, normalized: dict[str, str], redirects: dict[str, str]) -> str:
    """Follow normalization then redirect hops to the final article title."""
    title = normalized.get(name, name)
    seen = {title}
    while title in redirects and redirects[title] not in seen:
        title = redirects[title]
        seen.add(title)
    return title


def _api_wikitext(titles: list[str]) -> tuple[dict[str, str], dict[str, str], dict[str, str]]:
    """Return (lead-wikitext-by-title, normalized-map, redirects-map) for one batch."""
    params = {
        "action": "query", "prop": "revisions",
        "rvprop": "content", "rvslots": "main",
        "redirects": 1, "format": "json", "formatversion": 2,
        "titles": "|".join(titles),
    }
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": _UA})
    with urllib.request.urlopen(req, timeout=45) as r:  # noqa: S310 - fixed https host
        data = json.load(r)
    q = data.get("query", {})
    pages: dict[str, str] = {}
    for p in q.get("pages", []):
        if p.get("missing"):
            pages[p["title"]] = "\x00missing"
            continue
        revs = p.get("revisions") or []
        content = revs[0]["slots"]["main"]["content"] if revs else ""
        pages[p["title"]] = content
    normalized = {n["from"]: n["to"] for n in q.get("normalized", [])}
    redirects = {rd["from"]: rd["to"] for rd in q.get("redirects", [])}
    return pages, normalized, redirects


def fetch_pronunciations(names: list[str], *, opener=None) -> list[Pron]:
    """Fetch IPA + Wikipedia respelling for each name. ``opener`` overrides the batch
    fetcher (a ``titles -> (wikitext_by_title, normalized, redirects)`` callable) for tests."""
    fetch = opener or _api_wikitext
    out: list[Pron] = []
    for i in range(0, len(names), _BATCH):
        batch = names[i:i + _BATCH]
        try:
            pages, normalized, redirects = fetch(batch)
        except Exception as exc:  # noqa: BLE001 - one batch failing shouldn't lose the rest
            for name in batch:
                out.append(Pron(name=name, note=f"fetch error: {exc}"))
            continue
        for name in batch:
            title = _resolve_chain(name, normalized, redirects)
            content = pages.get(title)
            if content is None or content == "\x00missing":
                out.append(Pron(name=name, title=title, note="no Wikipedia article"))
                continue
            ipa, respell = parse_wikitext(content)
            url = "https://en.wikipedia.org/wiki/" + urllib.parse.quote(title.replace(" ", "_"))
            note = "" if (ipa or respell) else "article found but no pronunciation in lead"
            out.append(Pron(
                name=name, title=title, ipa=ipa, respell=respell, url=url,
                found=bool(ipa or respell), note=note,
            ))
    return out


def _cli(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="prosodia-wiki-pron",
        description="Fetch IPA + Wikipedia respelling for names (feeds the lexicon agent).",
    )
    p.add_argument("names", nargs="*", help="names to look up")
    p.add_argument("--names-file", help="read names from a file, one per line")
    p.add_argument("--out", help="write JSON here (default: stdout)")
    p.add_argument("--format", choices=("json", "tsv"), default="json")
    args = p.parse_args(argv)
    # IPA is non-ASCII; the Windows console defaults to cp1252 and would crash on it.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
        except Exception:  # noqa: BLE001 - older/odd streams: best-effort
            pass

    names = list(args.names)
    if args.names_file:
        names += [ln.strip() for ln in open(args.names_file, encoding="utf-8") if ln.strip()]
    # de-dup, preserve order
    names = list(dict.fromkeys(names))
    if not names:
        p.error("no names given (positional args or --names-file)")

    prons = fetch_pronunciations(names)
    if args.format == "tsv":
        lines = ["name\ttitle\tipa\trespell\tfound\turl\tnote"]
        for x in prons:
            lines.append("\t".join(str(v or "") for v in
                          (x.name, x.title, x.ipa, x.respell, x.found, x.url, x.note)))
        text = "\n".join(lines) + "\n"
    else:
        text = json.dumps([asdict(x) for x in prons], ensure_ascii=False, indent=2) + "\n"

    if args.out:
        open(args.out, "w", encoding="utf-8").write(text)
        found = sum(1 for x in prons if x.found)
        print(f"wrote {args.out} — {found}/{len(prons)} with a pronunciation", file=sys.stderr)
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
