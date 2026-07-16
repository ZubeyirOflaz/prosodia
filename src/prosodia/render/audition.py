"""Voice audition — hear each reference clip across the FULL delivery range.

Isolates the variation that comes from the *reference clip* by holding the written
content constant, so you can A/B candidate voices before committing to one. But a
single somber passage only reveals one corner of a voice; a clip that sounds perfect
grave-and-slow can fall apart wry-and-fast. So the audition renders a *suite* of short
passages chosen to span the tonal range (measured → warm → wry → tense → urgent →
dramatic → reverent → somber → grave) and the cadence range (brisk enumerations, long
flowing sentences, short punchy ones, a posed question with a beat, slow deliberate
lines).

Crucially, each passage is rendered with the SAME engine parameters the real pipeline
would use for that delivery — pulled from the persona's ``voice_profiles.yaml`` (the
tone table + global ``pace`` dial) and the rate multiplier — so what you hear in the
audition is what the show will actually produce, not an arbitrary fixed setting.

Runs on the GPU box (needs the render extra); it's a thin loop over the warm
ChatterboxBackend plus the existing audio helpers, and writes an ``index.html`` with
players grouped by passage for quick comparison.
"""

from __future__ import annotations

import html
from dataclasses import dataclass, field
from pathlib import Path

from prosodia.core.intents import rate_to_multiplier
from prosodia.render import audio as A

# cfg_weight clamp range — mirrors author/tone.py so the audition reproduces the
# pipeline's pacing exactly.
_CFG_MIN, _CFG_MAX = 0.15, 0.95
_FALLBACK = {"exaggeration": 0.40, "cfg_weight": 0.50, "temperature": 0.75}


@dataclass(frozen=True)
class Passage:
    """One audition line: text plus the delivery intent it should be spoken with.

    ``tone`` and ``rate`` are engine-neutral (the transcript vocabulary); they are
    resolved to real engine parameters through the persona's tone table, exactly as
    the render pipeline does — so the audition matches production.
    """

    key: str          # short slug, used in output filenames
    label: str        # human label for the section header
    text: str
    tone: str = "measured"
    rate: str = "normal"


# The default range suite. Numbers are already in spoken form (the reference clip is the
# only thing that should vary), and each passage is written to exercise BOTH a distinct
# tonal register AND a distinct cadence — so a voice is heard everywhere it will have to
# work, not just in calm narration. Tones/rates use the transcript vocabulary and are
# resolved through voice_profiles.yaml at render time.
RANGE_SUITE: tuple[Passage, ...] = (
    Passage(
        "measured", "Measured — baseline narration", tone="measured", rate="normal",
        text=(
            "Here is where the argument really starts. Not with a battle or a king, but "
            "with a question so ordinary you have probably asked it yourself, without ever "
            "noticing it had a name."
        ),
    ),
    Passage(
        "warm", "Warm — an intimate close-up", tone="warm", rate="normal",
        text=(
            "He was, by every account, a gentle man at home. He wrote to his daughter in "
            "the evenings, small jokes folded into the margins, and he signed every letter "
            "the same way, every single time."
        ),
    ),
    Passage(
        "matter-of-fact", "Matter-of-fact, fast — a brisk run of dates",
        tone="matter-of-fact", rate="fast",
        text=(
            "The dates come quickly now. Eighteen forty-eight, revolution. Eighteen "
            "seventy-one, again. Nineteen fourteen, the lights go out. Nineteen eighteen, "
            "they come back on, dimmer, and no one quite trusts them."
        ),
    ),
    Passage(
        "wry", "Wry — a dry aside", tone="wry", rate="normal",
        text=(
            "Naturally, the committee formed a subcommittee. The subcommittee, in its "
            "wisdom, commissioned a report. And the report, when it finally arrived, "
            "recommended forming a committee."
        ),
    ),
    Passage(
        "question", "Questioning — a posed choice, then a beat", tone="measured", rate="normal",
        text=(
            "So ask yourself, honestly, before you answer too fast... if you had been "
            "standing in that square, on that morning, with that crowd — are you really so "
            "sure you would have walked the other way?"
        ),
    ),
    Passage(
        "reverent", "Reverent, slow — hushed", tone="reverent", rate="slow",
        text=(
            "We do not know his name. We know only that he carried the others out, one at a "
            "time, until the roof came down — and that the people he saved could never "
            "agree, afterward, on what he looked like."
        ),
    ),
    Passage(
        "somber", "Somber, slow — the aftermath", tone="somber", rate="slow",
        text=(
            "By the spring, the fields were quiet again. The same larks, the same low wind "
            "off the water. But the men who had worked those fields were not coming back, "
            "and the village had learned to look at the horizon and expect nothing."
        ),
    ),
    Passage(
        "grave", "Grave, very slow — the heaviest register", tone="grave", rate="very-slow",
        text=(
            "Understand what was decided in that room. Not a policy. Not a border. The fate "
            "of millions of people who would never learn the names of the men deciding it, "
            "and who were given no say at all."
        ),
    ),
    Passage(
        "tense", "Tense — a rising build in short sentences", tone="tense", rate="normal",
        text=(
            "The messenger did not knock. He came straight through the door, still holding "
            "the reins. Something in his face stopped every conversation in the hall. And "
            "then he said the one word no one there wanted to hear."
        ),
    ),
    Passage(
        "urgent", "Urgent, fast — pressing, no time", tone="urgent", rate="fast",
        text=(
            "Move — now — there is no time to gather anything, leave it, all of it. The "
            "bridge goes up at dawn, and if you are on the wrong side of the river when it "
            "does, no one is coming back for you."
        ),
    ),
    Passage(
        "dramatic", "Dramatic — the climax, full dynamics", tone="dramatic", rate="normal",
        text=(
            "This was the moment. Everything — every alliance, every betrayal, every quiet "
            "promise made in the dark for twenty years — all of it came down to what one "
            "frightened man would choose to do in the next ten seconds."
        ),
    ),
    Passage(
        "cadence", "Cadence stress — one long sentence, then short ones",
        tone="measured", rate="normal",
        text=(
            "It began, as these things so often do, not with a decision but with a thousand "
            "small refusals to decide — a letter left unanswered, a warning politely filed "
            "away, a rumor everyone repeated and no one checked — until the day the choice "
            "was finally forced, and there was only one left to make. Then it moved fast. "
            "Faster than anyone expected. Faster than anyone could stop. And the only "
            "question left was who would be blamed for not seeing it coming."
        ),
    ),
)

# Back-compat: some callers/tests import DEFAULT_TEXT. It is the baseline passage.
DEFAULT_TEXT = RANGE_SUITE[0].text


def discover_clips(voices) -> list[Path]:
    """Resolve ``voices`` (a dir of ``*.wav``, or a list of files/dirs) to clip paths."""
    items = [voices] if isinstance(voices, (str, Path)) else list(voices)
    clips: list[Path] = []
    for v in items:
        p = Path(v)
        if p.is_dir():
            clips += sorted(p.glob("*.wav"))
        elif p.exists():
            clips.append(p)
    seen: set[Path] = set()
    out: list[Path] = []
    for c in clips:  # de-dupe, preserve order
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out


@dataclass
class _Section:
    """One passage's worth of rendered takes, ready for the HTML page."""

    label: str
    tone: str
    rate: str
    params: str          # human-readable resolved engine parameters
    text: str
    note: str = ""       # e.g. an unknown-tone fallback warning
    players: list[tuple[str, str]] = field(default_factory=list)  # (player_label, wav_name)


def _index_html(sections: list[_Section]) -> str:
    """Build a self-contained A/B page: one section per passage, players within."""
    blocks = []
    for s in sections:
        players = "".join(
            f'<div class="take"><span>{html.escape(label)}</span>'
            f'<audio controls preload="none" src="{html.escape(wav)}"></audio></div>'
            for label, wav in s.players
        )
        note = f'<div class="note">{html.escape(s.note)}</div>' if s.note else ""
        blocks.append(
            "<section>"
            f'<h2>{html.escape(s.label)} '
            f'<span class="chip">{html.escape(s.tone)} · {html.escape(s.rate)}</span></h2>'
            f'<div class="params">{html.escape(s.params)}</div>'
            f'<div class="txt">{html.escape(s.text)}</div>'
            f"{note}{players}"
            "</section>"
        )
    return (
        "<!doctype html><meta charset='utf-8'>"
        "<meta name=viewport content='width=device-width,initial-scale=1'>"
        "<title>Prosodia voice audition</title>"
        "<style>body{font:16px/1.6 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;"
        "max-width:820px;margin:0 auto;padding:28px;background:#faf8f5;color:#1a1a1a}"
        "h1{font-size:20px;margin:0 0 4px}.lead{color:#6b6b6b;font-size:14px;margin:0 0 8px}"
        "section{border-top:1px solid #e6e3dd;padding:16px 0}"
        "h2{font-size:16px;margin:0 0 4px}.chip{display:inline-block;background:#efe7df;color:#7c4a2d;"
        "font-size:12px;font-weight:600;padding:1px 8px;border-radius:10px;vertical-align:middle}"
        ".params{font:12px/1.5 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;color:#8a7d70;"
        "margin:0 0 6px}"
        ".txt{background:#fff;border-left:3px solid #7c4a2d;padding:10px 14px;border-radius:0 8px 8px 0;"
        "margin:6px 0 10px}.note{color:#a33;font-size:13px;margin:0 0 8px}"
        ".take{display:flex;align-items:center;gap:12px;margin:6px 0}"
        ".take span{width:210px;color:#6b6b6b;font-size:13px}audio{flex:1}</style>"
        "<h1>Voice audition — the full delivery range</h1>"
        "<p class=lead>Same text per row, different reference clips. Each passage is rendered with the "
        "engine parameters the pipeline would use for that tone and rate.</p>" + "".join(blocks)
    )


def _load_profiles(profiles, voice_profiles_source, *, project=None):
    """Resolve a VoiceProfiles. ``voice_profiles_source`` may be a persona NAME
    (e.g. ``"thinkers"``) or a path to a ``voice_profiles.yaml``; an existing file
    is loaded directly, otherwise it is resolved as a persona name. With nothing
    given, use the default persona's table (or, last resort, the built-in fallback)."""
    if profiles is not None:
        return profiles
    from prosodia.author.persona import Persona
    from prosodia.author.tone import VoiceProfiles

    if voice_profiles_source:
        p = Path(voice_profiles_source)
        if p.is_file():
            return VoiceProfiles.load(p)
        # Not a file -> treat it as a persona name (project-local first, then built-in).
        persona = Persona.resolve(str(voice_profiles_source), project=project)
        return VoiceProfiles.load(persona.voice_profiles_path())
    try:
        return VoiceProfiles.load()  # default persona's tone table (shipped package data)
    except Exception:
        return VoiceProfiles(None)   # fallback params for every tone


def _resolve_params(profiles, passage, *, exaggeration, cfg_weight, temperature):
    """Compute (exaggeration, cfg_weight, temperature, rate_multiplier, ok) for a
    passage, mirroring author/tone.py: table lookup, global pace scale on cfg, clamp;
    explicit overrides win per-field. ``ok`` is False when the tone fell back."""
    p, ok = profiles.params_for_tone(passage.tone)
    exa = exaggeration if exaggeration is not None else float(
        p.get("exaggeration", _FALLBACK["exaggeration"])
    )
    tmp = temperature if temperature is not None else float(
        p.get("temperature", _FALLBACK["temperature"])
    )
    if cfg_weight is not None:
        cfg = float(cfg_weight)
    else:
        cfg = float(p.get("cfg_weight", _FALLBACK["cfg_weight"])) * profiles.pace
        cfg = max(_CFG_MIN, min(_CFG_MAX, cfg))
    try:
        mult = rate_to_multiplier(passage.rate)
    except ValueError:
        mult = 1.0
    return exa, cfg, tmp, mult, ok


def audition(
    voices,
    out_dir,
    *,
    text: str | None = None,
    tone: str = "measured",
    rate: str = "normal",
    passages: "list[Passage] | tuple[Passage, ...] | None" = None,
    backend=None,
    takes: int = 1,
    base_seed: int = 12345,
    profiles=None,
    voice_profiles_path=None,
    project=None,
    exaggeration: float | None = None,
    cfg_weight: float | None = None,
    temperature: float | None = None,
    target_lufs: float = -16.0,
) -> list[Path]:
    """Render an audition suite for each clip in ``voices`` and write ``index.html``.

    By default (no ``text``/``passages``) the full :data:`RANGE_SUITE` is rendered, so
    every clip is heard across the whole tonal and cadence range. Pass ``text`` to fall
    back to the old single-passage mode (spoken with ``tone``/``rate``), or ``passages``
    to supply a custom suite.

    Each passage is spoken with the engine parameters the pipeline would use for its
    ``tone``/``rate`` (from ``voice_profiles_path`` / the default persona table), unless
    an explicit ``exaggeration``/``cfg_weight``/``temperature`` is given, which overrides
    that field for every passage. ``voice_profiles_path`` may be a persona NAME or a path
    to a ``voice_profiles.yaml``. ``takes`` extra renders per cell reveal seed-to-seed
    variance; seeds are matched across clips so the clip stays the only variable per cell.
    Returns the written .wav paths.
    """
    clips = discover_clips(voices)
    if not clips:
        raise ValueError("no reference .wav clips found in the given path(s)")

    if passages is not None:
        suite: tuple[Passage, ...] = tuple(passages)
    elif text is not None:
        suite = (Passage("custom", "Custom text", text, tone=tone, rate=rate),)
    else:
        suite = RANGE_SUITE

    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    profiles = _load_profiles(profiles, voice_profiles_path, project=project)

    if backend is None:
        from prosodia.render.backends.chatterbox_backend import ChatterboxBackend

        backend = ChatterboxBackend()
    backend.load()
    sr = backend.sample_rate

    n_takes = max(1, takes)
    written: list[Path] = []
    sections: list[_Section] = []
    for pi, passage in enumerate(suite):
        exa, cfg, tmp, mult, ok = _resolve_params(
            profiles, passage,
            exaggeration=exaggeration, cfg_weight=cfg_weight, temperature=temperature,
        )
        section = _Section(
            label=passage.label,
            tone=passage.tone,
            rate=passage.rate,
            params=(
                f"exaggeration {exa:.2f}  ·  cfg_weight {cfg:.2f}  ·  "
                f"rate x{mult:.2f}  ·  temperature {tmp:.2f}"
            ),
            text=passage.text,
            note=(
                f"tone '{passage.tone}' not in the tone table -> fell back to "
                f"'{profiles.default_tone}'"
                if not ok else ""
            ),
        )
        for ti in range(n_takes):
            seed = base_seed + pi * 100 + ti  # matched across clips for a given cell
            for ci, clip in enumerate(clips):
                wav = backend.generate(
                    passage.text, exaggeration=exa, cfg_weight=cfg, temperature=tmp,
                    rate_multiplier=mult, seed=seed, audio_prompt_path=str(clip),
                )
                wav = A.trim_silence(wav, sr)
                name = f"{pi:02d}_{passage.key}__{ci:02d}_{clip.stem}__seed{seed}.wav"
                raw = out_dir / f"_raw_{name}"
                A.write_wav(raw, wav, sr)
                final = out_dir / name
                if not A.loudness_normalize(raw, final, target_lufs, sr=sr):
                    A.write_wav(final, A.peak_normalize(wav), sr)
                raw.unlink(missing_ok=True)
                written.append(final)
                label = clip.stem if n_takes == 1 else f"{clip.stem} · seed {seed}"
                section.players.append((label, name))
        sections.append(section)

    (out_dir / "index.html").write_text(_index_html(sections), encoding="utf-8")
    return written
