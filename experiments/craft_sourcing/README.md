# craft_sourcing — acquire and measure a teacher's corpus

Tooling for the process in [`docs/reference/craft-sourcing.md`](../../docs/reference/craft-sourcing.md):
turn a candidate persona-soul into a **traceable corpus plus numbers**, so the craft dossier
that follows is grounded in the person's own words rather than in their reputation.

Standalone by design — stdlib Python plus external binaries, no imports from `prosodia`,
nothing added to the torch-free authoring install. Same rule that keeps the prosody harness
out of the MIT package.

```
craft_sourcing/
  fetch.py            # manifest -> corpus/<slug>/ + manifest.json (sha256, words, duration)
  profile.py          # corpus/<slug>/ -> out/<slug>-profile.json + a printed summary
  transcribe.py       # audio -> punctuated text, when a source has no human captions
  sources/<slug>.json # what to fetch, and the one job the source is hired for
  corpus/             # raw third-party text — GITIGNORED, never committed
  out/                # derived profiles — GITIGNORED, regenerable
```

## Usage

```bash
# 1. acquire (subtitles only for video; never the video itself)
python experiments/craft_sourcing/fetch.py experiments/craft_sourcing/sources/fisher.json

# 2. measure — prose shape, delivery proxies, and mined verbatim habits
python experiments/craft_sourcing/profile.py fisher --kind manual   # punctuated: prose stats
python experiments/craft_sourcing/profile.py fisher --kind auto     # word-timed: pause stats
```

```bash
# 3. transcribe, only when captions are auto-only (needs the RENDER venv for faster-whisper)
.venv-render/bin/python experiments/craft_sourcing/transcribe.py harford --ids VIDEOID1,VIDEOID2
```

**Requires:** `curl`; `yt-dlp` for YouTube items (`pip install yt-dlp` in a throwaway venv is
fine — pass `--ytdlp /path/to/yt-dlp`); `pdftotext` (poppler) for PDF items.

## Manifest gotcha

`totals.words` sums **every** track type, so a lecture held as captions *and* as a local
transcription is counted twice. Quote `totals.words_by_kind` instead. Records are keyed on
`(slug, kind)` for the same reason — keying on slug alone silently drops a transcription of an
item that already exists as captions, leaving files on disk the provenance record cannot see.

## What the numbers are and aren't

Delivery metric names match [`prosody-profiling.md`](../../docs/reference/prosody-profiling.md)
so a source profile can act as the tuning target for a persona's `voice_profiles.yaml`. They
are **caption-derived proxies** — good for comparing sources measured the same way, not
calibrated against that harness's VAD numbers. Caveats, biases and the unpunctuated-captions
trap are documented in the process doc; read them before quoting a figure.

Pitch, energy and register need audio and are simply absent. Leave them empty.

## Acquisition status

| source | hired for | status |
|---|---|---|
| `fisher` | architecture | **pass 5 of 6** — 40 segments ≈17 h, 141k caption words, + his pedagogy paper and 2020 exam (both read), syllabus, maps → [`fisher-craft.md`](../../docs/reference/fisher-craft.md) |
| `harford` | cases | **complete, pass 3 of 3** → [`harford-craft.md`](../../docs/reference/harford-craft.md); 7 episodes, 263 min, transcribed locally. no official transcripts exist (confirmed: neither the Cautionary Tales feed nor the BBC feed carries `podcast:transcript` tags, and YouTube offers auto-captions only at 0.17 marks/100 words). Solved by transcribing the audio locally with `transcribe.py`: **8.04 marks/100 words**, proper nouns correct |
| `hildebrandt` | gaze | **complete, pass 3 of 3** — open-access book, 113k words of her prose, + master-course syllabus → [`hildebrandt-craft.md`](../../docs/reference/hildebrandt-craft.md). Content source; written corpus, so no delivery metrics |
| `sapolsky` | device: levels | **complete, pass 3 of 3** — 25 lectures, 36.7 h, 355k words → [`sapolsky-craft.md`](../../docs/reference/sapolsky-craft.md). Auto-captions only, so four method lectures (50,151 words) were re-transcribed locally with `transcribe.py` to get valid prose metrics |
| ~~`oneill`~~ | — | **dropped from the roster** (never started); BBC answers `curl` if revived |
| ~~`ian-shapiro`~~ | — | **dropped from the roster** (never started); Open Yale needs the browser headers now in `fetch.py` |

**Bot-blocking is a fetch-mechanics problem, not a licence problem.** `fetch.py` now sends a
realistic browser header set, which is what turned PubPub from 403 into 200. Retry any host that
previously refused before concluding a corpus is unavailable.
