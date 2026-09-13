#!/usr/bin/env python3
"""Measure a craft-source corpus: delivery numbers + prose numbers + mined verbatim habits.

Part of the craft-sourcing process (docs/reference/craft-sourcing.md). Turns "he
sounds deliberate" into `speech_rate_wpm: 143`, and turns "he uses signposting
transitions" into the actual list of his most frequent sentence openers.

Delivery metric names deliberately match docs/reference/prosody-profiling.md, so a
source's profile can serve as the *target vector* when tuning a persona's
voice_profiles.yaml against real narration.

Timings come from caption cues, not audio: cue gaps approximate pause structure well
enough to rank sources, and it needs no download beyond subtitles.

Usage:
    python profile.py fisher [--kind manual]
"""

from __future__ import annotations

import argparse
import json
import re
import statistics as st
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
CORPUS = HERE / "corpus"
OUT = HERE / "out"

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")
WORD = re.compile(r"[A-Za-z']+")
STOP_OPENER = {"the", "a", "an", "and", "but", "so", "that", "this", "it", "there"}


def sentences(text: str) -> list[str]:
    return [s.strip() for s in SENT_SPLIT.split(text) if s.strip()]



WORD_TS = re.compile(r"<(\d+):(\d+):([\d.]+)><c>\s*([^<]+)</c>")


def word_timings(vtt: Path) -> list[tuple[float, str]]:
    """Per-word (start, word) pairs from an auto-generated VTT.

    Auto-captions carry inline word timestamps; cue boundaries do NOT reflect silence
    (they scroll), so the inter-word deltas are the only way to see pause structure
    without downloading audio. Duplicates from the rolling display are collapsed.
    """
    seen: dict[tuple[float, str], None] = {}
    for m in WORD_TS.finditer(vtt.read_text(encoding="utf-8", errors="replace")):
        t = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
        w = m.group(4).strip()
        if w:
            seen.setdefault((round(t, 3), w), None)
    return sorted(seen.keys())


def pause_metrics(words: list[tuple[float, str]], punctuated: str) -> dict:
    """Pause structure from inter-word deltas, plus where the long ones fall.

    A "long pause" is a delta at least 0.6 s above the corpus-typical word interval.
    Mid-sentence classification aligns the 5 words before the gap against the
    punctuated (manual) transcript and asks whether a sentence ended there.
    """
    if len(words) < 50:
        return {}
    deltas = [(b[0] - a[0], i) for i, (a, b) in enumerate(zip(words, words[1:])) if 0 < b[0] - a[0] < 30]
    if not deltas:
        return {}
    typical = st.median(d for d, _ in deltas)
    dur = words[-1][0] - words[0][0]
    long_idx = [i for d, i in deltas if d >= typical + 0.6]
    flat = re.sub(r"\s+", " ", punctuated)
    mid = 0
    checked = 0
    for i in long_idx:
        gram = " ".join(w for _t, w in words[max(0, i - 4):i + 1])
        j = flat.lower().find(gram.lower())
        if j < 0:
            continue
        checked += 1
        tail = flat[j + len(gram):j + len(gram) + 2].strip()
        if not tail[:1] in (".", "!", "?", ""):
            mid += 1
    return {
        "speech_rate_wpm": round(len(words) / (dur / 60)),
        "word_interval_median_s": round(typical, 3),
        "long_pause_per_min": round(len(long_idx) / (dur / 60), 2),
        "long_pause_midsentence_frac": round(mid / checked, 3) if checked >= 20 else None,
        "pause_alignment_checked": checked,
        "pause_ratio": round(sum(max(0.0, d - typical) for d, _ in deltas) / dur, 3),
    }


def punctuation_density(text: str) -> float:
    """Sentence terminators per 100 words. Normal written/captioned prose is ~4-6.

    YouTube auto-captions are frequently unpunctuated, which silently invalidates every
    sentence-level statistic. Anything under 1.5 is treated as unpunctuated and its prose
    metrics are suppressed rather than reported as if meaningful.
    """
    w = len(WORD.findall(text)) or 1
    return round(100 * len(re.findall(r"[.!?]", text)) / w, 2)


def prose_metrics(text: str) -> dict:
    sents = sentences(text) or [""]
    lens = [len(s.split()) for s in sents] or [0]
    words = WORD.findall(text)
    n = len(words) or 1
    per_k = lambda pat: round(1000 * len(re.findall(pat, text, re.IGNORECASE)) / n, 2)
    dens = punctuation_density(text)
    out = {
        "words": len(words),
        "punctuation_density": dens,
        "punctuated": dens >= 1.5,
        "sentences": len(sents),
        "sent_len_mean": round(st.mean(lens), 1),
        "sent_len_median": round(st.median(lens), 1),
        "sent_len_p90": sorted(lens)[int(0.9 * (len(lens) - 1))],
        "sent_len_max": max(lens),
        "sent_len_sd": round(st.pstdev(lens), 1),
        "short_sent_frac": round(sum(1 for x in lens if x <= 8) / len(lens), 3),
        "question_rate": round(sum(1 for s in sents if s.rstrip().endswith("?")) / len(sents), 4),
        "you_per_1k": per_k(r"\byou\b|\byour\b"),
        "we_per_1k": per_k(r"\bwe\b|\bour\b|\bus\b"),
        "i_per_1k": per_k(r"\bI\b|\bmy\b"),
        "hedge_per_1k": per_k(r"\bperhaps\b|\barguably\b|\bprobably\b|\bmight\b|\bseems?\b|\bappears?\b"),
        "imperative_lead_frac": round(
            sum(1 for s in sents if re.match(r"(Note|Consider|Notice|Suppose|Imagine|Recall|Remember|Look)\b", s))
            / len(sents), 4),
    }
    if not out["punctuated"]:
        # ratios per 1k words survive; sentence-level figures do not
        for k in ("sentences", "sent_len_mean", "sent_len_median", "sent_len_p90", "sent_len_max",
                  "sent_len_sd", "short_sent_frac", "question_rate", "imperative_lead_frac"):
            out[k] = None
    return out


def timing_metrics(cues: list[tuple[float, float, str]]) -> dict:
    if len(cues) < 5:
        return {}
    dur = cues[-1][1] - cues[0][0]
    words = sum(len(c[2].split()) for c in cues)
    gaps = []
    for (a, b, ta), (c, _d, _tb) in zip(cues, cues[1:]):
        gap = c - b
        if gap > 0.05:
            gaps.append((gap, ta.rstrip()))
    long_gaps = [(g, t) for g, t in gaps if g >= 0.6]
    mid = [1 for _g, t in long_gaps if not re.search(r"[.!?]$", t)]
    return {
        "duration_min": round(dur / 60, 1),
        "speech_rate_wpm": round(words / (dur / 60)),
        "pause_ratio": round(sum(g for g, _ in gaps) / dur, 3),
        "long_pause_per_min": round(len(long_gaps) / (dur / 60), 2),
        "long_pause_midsentence_frac": round(len(mid) / len(long_gaps), 3) if long_gaps else None,
        "gap_cv": round(st.pstdev([g for g, _ in gaps]) / st.mean([g for g, _ in gaps]), 2) if gaps else None,
    }


def mine(text: str, sents: list[str]) -> dict:
    openers = Counter()
    for s in sents:
        toks = s.split()
        if len(toks) < 4:
            continue
        first = toks[0].strip('"“').lower()
        if first in STOP_OPENER:
            continue
        openers[" ".join(w.lower() for w in toks[:3])] += 1
    words = [w.lower() for w in WORD.findall(text)]
    grams = Counter(" ".join(words[i:i + 4]) for i in range(len(words) - 3))
    caps = Counter(m.group(0) for m in re.finditer(r"\b[A-Z][A-Z ]{4,40}[A-Z]\b", text))
    return {
        "top_sentence_openers": openers.most_common(25),
        "top_4grams": [(g, c) for g, c in grams.most_common(40) if c > 2],
        "capitalised_markers": caps.most_common(15),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--kind", default="manual", choices=["manual", "auto"])
    args = ap.parse_args()

    base = CORPUS / args.slug
    manifest = json.loads((base / "manifest.json").read_text(encoding="utf-8"))
    picked = [r for r in manifest["items"] if r["kind"] == f"captions/{args.kind}"]
    if not picked:
        picked = [r for r in manifest["items"] if r["kind"].startswith("captions")]
    # A written corpus (a book, papers, a syllabus) has no captions at all. Those sources are
    # usually hired for frame rather than delivery, so prose metrics apply and timing does not.
    spoken = bool(picked)
    if not picked:
        picked = [r for r in manifest["items"] if r["kind"] in ("html", "pdf")]
    if not picked:
        print(f"no profilable items in {base}", file=sys.stderr)
        return 1

    texts, per_item, all_cues = [], [], []
    for rec in picked:
        text = (base / rec["file"]).read_text(encoding="utf-8", errors="replace")
        texts.append(text)
        vtt = base / rec.get("vtt", "__none__")
        cues: list[tuple[float, float, str]] = []
        if vtt.exists():
            sys.path.insert(0, str(HERE))
            from fetch import vtt_to_text
            _t, cues = vtt_to_text(vtt)
            all_cues.append(cues)
        pm = prose_metrics(text)
        auto = base / rec.get("vtt", "__none__").replace(".en.vtt", ".en-orig.vtt")
        pmetrics = pause_metrics(word_timings(auto), text) if auto.exists() else {}
        per_item.append({"slug": rec["slug"], "group": rec.get("group", ""),
                         "title": rec.get("title", ""), **pm, **timing_metrics(cues), **pmetrics})

    # Corpus-level prose metrics must use ONLY punctuated items, or one unpunctuated
    # auto-caption track poisons every sentence statistic for the whole source.
    ok = [txt for txt, d in zip(texts, per_item) if d.get("punctuated")]
    corpus_text = "\n".join(ok) if ok else ""
    profile = {
        "slug": args.slug,
        "person": manifest["person"],
        "hired_for": manifest.get("hired_for", ""),
        "caption_kind": args.kind if spoken else None,
        "corpus_kind": "spoken" if spoken else "written",
        "items_profiled": len(picked),
        "items_punctuated": sum(1 for d in per_item if d.get("punctuated")),
        "corpus": prose_metrics(corpus_text),
        "punctuated_items": sum(1 for d in per_item if d.get("punctuated")),
        "delivery_median_across_items": {
            k: round(st.median([d[k] for d in per_item if d.get(k) is not None]), 3)
            for k in ("duration_min", "speech_rate_wpm", "pause_ratio",
                      "long_pause_per_min", "long_pause_midsentence_frac",
                      "word_interval_median_s")
            if any(d.get(k) is not None for d in per_item)
        },
        "mined": mine("\n".join(texts), sentences("\n".join(texts))),
        "lexical_all_items": {k: v for k, v in prose_metrics("\n".join(texts)).items()
                              if k.endswith("_per_1k") or k == "words"},
        "per_item": sorted(per_item, key=lambda d: d["slug"]),
    }
    OUT.mkdir(exist_ok=True)
    dst = OUT / f"{args.slug}-profile.json"
    dst.write_text(json.dumps(profile, indent=2), encoding="utf-8")

    c, d = profile["corpus"], profile["delivery_median_across_items"]
    if not spoken:
        la = profile["lexical_all_items"]
        print(f"\n{manifest['person']} — {len(picked)} written items, "
              f"{la['words']:,} words (no audio: delivery metrics n/a)")
        print(f"  sentences: mean {c['sent_len_mean']} med {c['sent_len_median']} "
              f"p90 {c['sent_len_p90']} max {c['sent_len_max']} | short(<=8w) {c['short_sent_frac']:.0%} "
              f"| punctuation {c['punctuation_density']}/100w")
        print(f"  questions {c['question_rate']:.1%} | you {la['you_per_1k']} we {la['we_per_1k']} "
              f"I {la['i_per_1k']} hedges {la['hedge_per_1k']} /1k")
        print("\n  top sentence openers: " + ", ".join(
            f"{gg!r}\u00d7{n}" for gg, n in profile["mined"]["top_sentence_openers"][:12]))
        OUT.mkdir(exist_ok=True)
        dst = OUT / f"{args.slug}-profile.json"
        dst.write_text(json.dumps(profile, indent=2), encoding="utf-8")
        print(f"\n  -> {dst}")
        return 0
    print(f"\n{manifest['person']} — {len(picked)} items "
          f"({profile['items_punctuated']} punctuated), "
          f"{profile['lexical_all_items']['words']:,} words total")
    if not profile["items_punctuated"]:
        print("  !! no punctuated items: sentence-level prose metrics suppressed")
    print(f"  wpm {d.get('speech_rate_wpm')}  |  median segment {d.get('duration_min')} min"
          f"  |  pause_ratio {d.get('pause_ratio')}  |  long_pause/min {d.get('long_pause_per_min')}"
          f"  |  mid-sentence long pauses {d.get('long_pause_midsentence_frac')}")
    if c.get("sent_len_mean") is None:
        print("  sentences: n/a (unpunctuated captions)")
    else:
        print(f"  sentences: mean {c['sent_len_mean']} med {c['sent_len_median']} p90 {c['sent_len_p90']} "
              f"max {c['sent_len_max']} sd {c['sent_len_sd']} | short(<=8w) {c['short_sent_frac']:.0%}")
    q = f"{c['question_rate']:.1%}" if c.get("question_rate") is not None else "n/a"
    la = profile["lexical_all_items"]
    print(f"  questions {q} | you {la['you_per_1k']} we {la['we_per_1k']} "
          f"I {la['i_per_1k']} hedges {la['hedge_per_1k']} /1k (all items)")
    print(f"\n  top sentence openers: {', '.join(f'{g!r}×{n}' for g, n in profile['mined']['top_sentence_openers'][:12])}")
    print(f"\n  -> {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
