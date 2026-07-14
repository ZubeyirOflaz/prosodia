"""Repetition / freshness linter for a series of episode transcripts.

Deterministic, pure-Python (no torch, no audio). Surfaces the phrase-repetition
that makes long-form narration feel formulaic and predictable:

  * near-duplicate EPISODE OPENINGS (the "every episode starts with 'I want to'"
    problem),
  * overuse of known STOCK PHRASES / tics, per episode and across the series,
  * phrasings SHARED across multiple episodes (n-grams), as a discovery aid for
    tics not yet on the watchlist.

It also produces the feed-forward "already used — avoid these" note that gets
injected into the Writer brief for the next episode, so a fresh writer (which has
no memory of the other episodes) can actively diverge from them.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

# Known crutch phrases (lowercased, punctuation-free). Extend as new tics surface.
STOCK_PHRASES = [
    "i want to", "i want you to", "i want you", "i need you to",
    "hold that thought", "sit with that", "sit with that for a moment",
    "sit with that number", "here is the part", "here is the thing",
    "here is what", "let that sink in", "make no mistake", "more on that later",
    "remember what happened", "think about that", "think about it",
    "picture it", "picture this", "imagine you are", "imagine being",
    "keep that in mind", "but here is the thing", "and here is the thing",
]

_WORD_RE = re.compile(r"[a-z0-9']+")


def spoken_text(md: str) -> str:
    """Return just the spoken words of a transcript, lowercased.

    Strips front-matter, HTML comments, beat headers (chapter markers, not
    spoken), ``{...}`` delivery directives, standalone ``@speaker`` tags, and
    ``*`` emphasis markers.
    """
    m = re.match(r"^\s*---\n.*?\n---\n", md, flags=re.DOTALL)
    if m:
        md = md[m.end():]
    md = re.sub(r"<!--.*?-->", " ", md, flags=re.DOTALL)
    md = re.sub(r"(?m)^\s*#{1,6}\s.*$", " ", md)   # beat headers
    md = re.sub(r"\{[^}]*\}", " ", md)             # delivery directives
    md = re.sub(r"(?m)^\s*@\w+\b", " ", md)        # @speaker tags
    md = md.replace("*", " ")
    return re.sub(r"\s+", " ", md).strip().lower()


def tokens(text: str) -> list[str]:
    return _WORD_RE.findall(text.lower())


def opening(md: str, n_words: int = 18) -> str:
    """First ``n_words`` spoken words of the episode."""
    return " ".join(tokens(spoken_text(md))[:n_words])


def phrase_count(text: str, phrase: str) -> int:
    """Count non-overlapping occurrences of a lowercased phrase in spoken text."""
    return len(re.findall(r"\b" + re.escape(phrase) + r"\b", text))


def ngrams(toks: list[str], n: int) -> Counter:
    return Counter(tuple(toks[i:i + n]) for i in range(len(toks) - n + 1))


def analyze(episodes: dict[str, str], *, ngram_sizes=(4, 5)) -> dict:
    """Analyze a mapping of ``label -> transcript_md``.

    Returns a report dict with openings, opening collisions (episodes sharing the
    same first three words), stock-phrase usage, and n-grams shared across
    episodes.
    """
    spoken = {label: spoken_text(md) for label, md in episodes.items()}
    toks = {label: tokens(s) for label, s in spoken.items()}

    openings = {label: " ".join(toks[label][:18]) for label in episodes}

    # Opening collisions: episodes whose first three spoken words are identical.
    prefix_groups: dict[tuple, list[str]] = {}
    for label in episodes:
        head = tuple(toks[label][:3])
        prefix_groups.setdefault(head, []).append(label)
    collisions = {
        " ".join(head): labs for head, labs in prefix_groups.items() if len(labs) > 1 and head
    }

    # Stock phrases: per-episode counts (only phrases that actually appear).
    stock: dict[str, dict] = {}
    for phrase in STOCK_PHRASES:
        per = {label: phrase_count(spoken[label], phrase) for label in episodes}
        total = sum(per.values())
        if total:
            stock[phrase] = {"total": total, "per": {k: v for k, v in per.items() if v}}

    # Shared n-grams: appear in >= 2 episodes (a stylistic-repetition discovery aid).
    shared: list[dict] = []
    for n in ngram_sizes:
        per_ep_sets = {label: set(ngrams(toks[label], n)) for label in episodes}
        counts = {label: ngrams(toks[label], n) for label in episodes}
        seen: Counter = Counter()
        for s in per_ep_sets.values():
            seen.update(s)
        for gram, ep_count in seen.items():
            if ep_count >= 2:
                total = sum(counts[ep][gram] for ep in episodes)
                shared.append({
                    "ngram": " ".join(gram),
                    "episodes": ep_count,
                    "total": total,
                    "in": [ep for ep in episodes if gram in per_ep_sets[ep]],
                })
    shared.sort(key=lambda d: (d["episodes"], d["total"]), reverse=True)

    return {
        "openings": openings,
        "opening_collisions": collisions,
        "stock": stock,
        "shared_ngrams": shared,
    }


def format_report(report: dict, *, max_ngrams: int = 30) -> str:
    """Human-readable report."""
    out: list[str] = []
    out.append("=== EPISODE OPENINGS (first ~18 words) ===")
    for label, text in report["openings"].items():
        out.append(f"  {label}: {text}")
    if report["opening_collisions"]:
        out.append("\n!! OPENING COLLISIONS (same first three words):")
        for head, labs in report["opening_collisions"].items():
            out.append(f"  \"{head}...\" -> {', '.join(labs)}")
    else:
        out.append("\n(no opening collisions — every episode opens differently)")

    out.append("\n=== STOCK PHRASES (tics) ===")
    if report["stock"]:
        for phrase, d in sorted(report["stock"].items(), key=lambda kv: kv[1]["total"], reverse=True):
            per = ", ".join(f"{k}:{v}" for k, v in sorted(d["per"].items()))
            out.append(f"  \"{phrase}\"  x{d['total']}  ({per})")
    else:
        out.append("  (none of the watchlist phrases appear)")

    out.append("\n=== PHRASINGS SHARED ACROSS EPISODES (discovery; filter topical ones by eye) ===")
    shown = [g for g in report["shared_ngrams"]][:max_ngrams]
    if shown:
        for g in shown:
            out.append(f"  [{g['episodes']} eps x{g['total']}] \"{g['ngram']}\"  ({', '.join(g['in'])})")
    else:
        out.append("  (no n-grams shared across episodes)")
    return "\n".join(out)


def feedforward_context(prior: dict[str, str], *, max_phrases: int = 12) -> str:
    """Build the 'already used — avoid these' note for the next Writer brief.

    ``prior`` maps label -> transcript_md for episodes ALREADY written. Returns an
    empty string if there are none.
    """
    if not prior:
        return ""
    report = analyze(prior)
    lines = [
        "--- ALREADY USED IN EARLIER EPISODES (do NOT reuse; deliberately diverge) ---",
        "Openings already used (open THIS episode a different way, with a different move):",
    ]
    for label, text in report["openings"].items():
        lines.append(f"  - {label}: \"{text}...\"")
    hot = sorted(report["stock"].items(), key=lambda kv: kv[1]["total"], reverse=True)[:max_phrases]
    if hot:
        lines.append("Phrases already leaned on (avoid, or reword freshly and use at most once):")
        for phrase, d in hot:
            lines.append(f"  - \"{phrase}\" (used {d['total']}x)")
    return "\n".join(lines)


def load_episode_transcripts(project: Path) -> dict[str, str]:
    """Load ``ep*/transcript.md`` under ``project/episodes``, keyed by episode dir name,
    sorted by trailing episode number when present."""
    epdir = Path(project) / "episodes"

    def epnum(p: Path) -> int:
        m = re.search(r"(\d+)", p.parent.name)
        return int(m.group(1)) if m else 0

    found = sorted(epdir.glob("*/transcript.md"), key=epnum)
    return {p.parent.name: p.read_text(encoding="utf-8") for p in found}
