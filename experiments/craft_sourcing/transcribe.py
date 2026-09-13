#!/usr/bin/env python3
"""Transcribe a source's audio properly, when auto-captions are not good enough.

Part of the craft-sourcing process (docs/reference/craft-sourcing.md). YouTube
auto-captions arrive unpunctuated (measured as low as 0.04-0.17 sentence terminators per
100 words), which invalidates every sentence-level prose metric and mangles proper nouns.
Where a source has no human captions, this produces punctuated, reasonably accurate text
instead — and it reuses the `faster-whisper` the project already ships for the render-side
STT quality gate, so it adds no new dependency to anything.

Runs with the RENDER venv, which is where faster-whisper lives:
    .venv-render/bin/python experiments/craft_sourcing/transcribe.py harford \
        --ids ZCQvCcLRNc4,Ad78IMHTfEw --ytdlp /path/to/yt-dlp

CPU-bound and slow (roughly 2-5x realtime for `small`); intended for a handful of
representative items, not a whole corpus.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
CORPUS = HERE / "corpus"


def slugify(s: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")[:56]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", help="source slug, e.g. harford")
    ap.add_argument("--ids", required=True, help="comma-separated YouTube ids")
    ap.add_argument("--ytdlp", default="yt-dlp")
    ap.add_argument("--model", default="small", help="faster-whisper model (default: small)")
    ap.add_argument("--person", default="", help="person name, for a new manifest")
    ap.add_argument("--hired-for", default="", dest="hired_for")
    args = ap.parse_args()

    from faster_whisper import WhisperModel

    dest = CORPUS / args.slug
    audio_dir = dest / "_audio"
    audio_dir.mkdir(parents=True, exist_ok=True)

    print(f"loading model {args.model} (cpu, int8)…", flush=True)
    model = WhisperModel(args.model, device="cpu", compute_type="int8")

    records = []
    for vid in [v.strip() for v in args.ids.split(",") if v.strip()]:
        # title first, so the file is named usefully
        meta = subprocess.run([args.ytdlp, "--print", "%(title)s|%(duration)s",
                               f"https://www.youtube.com/watch?v={vid}"],
                              capture_output=True, text=True, check=False)
        line = [ln for ln in meta.stdout.strip().split("\n") if "|" in ln]
        title, dur = (line[-1].rsplit("|", 1) if line else (vid, "0"))
        # Show titles are usually "Episode Name | Show Name": keep the episode, drop the show,
        # so the slug stays short and stable enough to match an existing transcript.
        title = title.split("|")[0].strip()
        slug = f"{slugify(title)}"
        txt_existing = dest / f"{slug}.whisper.txt"
        if txt_existing.exists():
            print(f"  = already transcribed: {slug}", flush=True)
            continue
        wav = audio_dir / f"{slug}.wav"

        if not wav.exists():
            print(f"  ↓ audio: {title[:60]}", flush=True)
            r = subprocess.run([args.ytdlp, "-f", "bestaudio", "-x", "--audio-format", "wav",
                                "--postprocessor-args", "-ar 16000 -ac 1",
                                "-o", str(audio_dir / f"{slug}.%(ext)s"),
                                f"https://www.youtube.com/watch?v={vid}"],
                               capture_output=True, text=True, check=False)
            if not wav.exists():
                print(f"  !! audio download failed for {vid}\n{r.stderr[-400:]}", file=sys.stderr)
                continue

        print(f"  ▸ transcribing {slug} …", flush=True)
        segments, info = model.transcribe(str(wav), language="en", beam_size=1,
                                          vad_filter=True, condition_on_previous_text=False)
        parts = [s.text.strip() for s in segments]
        text = re.sub(r"\s+", " ", " ".join(parts)).strip()
        txt = dest / f"{slug}.whisper.txt"
        txt.write_text(text, encoding="utf-8")
        words = len(text.split())
        dens = round(100 * len(re.findall(r"[.!?]", text)) / max(words, 1), 2)
        records.append({
            "slug": slug, "title": title, "group": "transcribed audio",
            "kind": "captions/whisper", "source": f"youtube:{vid}",
            "file": txt.name, "sha256": hashlib.sha256(txt.read_bytes()).hexdigest()[:16],
            "words": words, "duration_s": float(dur or 0) or round(info.duration, 1),
            "punctuation_density": dens, "model": args.model,
        })
        print(f"    {words:,} words, punctuation {dens}/100w -> {txt.name}", flush=True)
        wav.unlink(missing_ok=True)  # audio is bulky and re-obtainable; keep only the text

    mpath = dest / "manifest.json"
    man = json.loads(mpath.read_text(encoding="utf-8")) if mpath.exists() else {
        "slug": args.slug, "person": args.person or args.slug,
        "hired_for": args.hired_for, "acquired": date.today().isoformat(),
        "permission_note": "Audio transcribed locally for private style analysis; not redistributed.",
        "items": [],
    }
    # Dedupe on (slug, kind), never slug alone: the same lecture legitimately exists as
    # captions AND as a local transcription, and keying on slug silently drops the second —
    # which leaves files on disk that the provenance record cannot see.
    have = {(r["slug"], r["kind"]) for r in man["items"]}
    man["items"] += [r for r in records if (r["slug"], r["kind"]) not in have]
    by_kind: dict[str, int] = {}
    for r in man["items"]:
        by_kind[r["kind"]] = by_kind.get(r["kind"], 0) + (r.get("words") or 0)
    man["totals"] = {"items": len(man["items"]),
                     # `words` sums every track type, so an item transcribed twice counts twice;
                     # `words_by_kind` is the figure to quote.
                     "words": sum(by_kind.values()),
                     "words_by_kind": by_kind,
                     "audio_minutes": round(sum(r.get("duration_s") or 0 for r in man["items"]) / 60, 1)}
    mpath.write_text(json.dumps(man, indent=2), encoding="utf-8")
    print(f"\n{args.slug}: {man['totals']['items']} items, {man['totals']['words']:,} words")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
