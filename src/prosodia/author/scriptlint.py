"""Deterministic comprehension checks on a finished transcript.

The editor is now told to count forward references, enumerated lists and ideas per passage.
An LLM cannot do that reliably — the first episode made fifteen cross-episode references in
thirty-four minutes and no editorial round reported the number. This module counts them, the
way `planlint` counts what a plan asserts, and for the same reason: the checks a model is
worst at are the ones that are exactly mechanical.

Everything here is about the listener the persona is written for: travelling, one voice, no
picture, no way to re-read or look anything up, losing twenty seconds of attention several
times an episode.
"""

from __future__ import annotations

import itertools
import re
import statistics
from dataclasses import dataclass
from pathlib import Path

ERROR, WARN, NOTE = "error", "warn", "note"

_WORDS_PER_MINUTE = 130
_EPISODE_REF = re.compile(
    r"(?i)\b(?:episode|episodes)\s+(one|two|three|four|five|six|seven|eight|nine|ten|eleven|"
    r"twelve|thirteen|\d+)\b"
)
_VAGUE_DEFER = re.compile(
    r"(?i)\b(?:a )?(?:later|the next|a future|a coming) (?:episode|series)\b|"
    r"\bcome back to (?:this|that)\b|\bwe(?:'ll| will) return to\b"
)
_DEIXIS = re.compile(
    r"(?i)\bas you can see\b|\bas shown\b|\bat the top\b|\bin the (?:diagram|table|figure)\b|"
    r"\bthe (?:left|right)-hand\b|\bbelow,|\babove,"
)
_RECAP = re.compile(
    r"(?i)\bso far\b|\bwhere we are\b|\bwhat we have\b|\bto recap\b|\bwe now have\b|"
    r"\btwo things\b|\bthree things\b|\bwe have established\b"
)
_SENTENCE = re.compile(r"[^.!?]+[.!?]")
# Spoken quotation marks: the phrases a narrator uses to open or close a quotation aloud.
_AUDIBLE_BRACKET = re.compile(
    r"(?i)(?:\b\w+'s (?:own )?words\b|\b(?:his|her|its|their) (?:own )?words\b"
    r"|\b(?:says|said|reads|puts it|goes like this|runs like this|reads as follows)\b"
    r"|\bend of (?:the )?(?:quote|quotation|definition)\b"
    r"|\b(?:quotation|quote|verbatim)\b|\bword for word\b|\bI am quoting\b)"
)
# A beat the writer marked `{tone: quoting}` IS bracketed, by construction — the renderer
# delivers it in the statute's voice and the script says so around it. Directives are
# stripped before the text is examined, so this is read off the raw transcript.
_QUOTING_BEAT = re.compile(r"(?m)^##[^\n]*\{[^}]*tone:\s*quoting[^}]*\}[^\n]*$")
# Places a listener is given a moment: an authored silence, a beat boundary (which the
# renderer realises as real silence), or a question put to them.
_BREATH = re.compile(r"(?m)\{pause[^}]*\}|^##|\?")
# A relative clause punctuated as a sentence — "Which leaves the load-bearing word." It is
# idiomatic once or twice in speech and a tic beyond that. A GENERIC repeated-opener count was
# tried first and was pure noise: it flagged sixteen sentences opening "And" and five opening
# "But" in a script whose persona requires "but" to carry every turn. Spoken register opens
# with conjunctions; what is worth flagging is the construction, not the frequency.
_FRAGMENT = re.compile(r"(?m)(?:^|(?<=[.!?]\s))(Which|Who|Whose|Whereas)\s")
# "It is not X. It is Y." — the correction-by-contrast shape the series bans. Episode 7
# shipped twelve of them through a round-one pass, because the ban is on a SHAPE and the
# watchlist only ever held literal phrases.
_NOT_X_Y = re.compile(
    r"(?m)(?:(?:is|are|was|were|s)\s+not\b[^.!?]{0,70}[.!?]\s+(?:It|That|They|These|This)\s+(?:is|are|was|were)\b"
    r"|(?:^|(?<=[.!?]\s))Not\s+[a-z][^.!?]{0,40}[.!?])"
)
def _enumerations(body: str) -> list[str]:
    """Sentences that read a LIST aloud: four or more short parallel items.

    The first version matched any sentence with three commas and an "and", which is most
    prose — "Three years later, in volume 113 of the Harvard Law Review, Lawrence Lessig
    answered him, and..." was reported as an enumeration. What distinguishes a list is that
    the segments are short and parallel, not that commas are present.
    """
    out = []
    for sent in _SENTENCE.findall(body):
        parts = [p.strip() for p in re.split(r",|;", sent) if p.strip()]
        if len(parts) < 4:
            continue
        short = [p for p in parts if len(re.findall(r"[A-Za-z']+", p)) <= 5]
        # a run of at least four short segments, consecutive, is a list being read out
        best = run = 0
        for p in parts:
            run = run + 1 if p in short else 0
            best = max(best, run)
        # A real list coordinates its final item. Without this, "The tribunal called it
        # remarkable, which, from a tribunal member, means absurd." reads as four short
        # segments and was reported as a list read aloud.
        if best >= 4 and re.search(r",\s+(?:and|or)\s", sent):
            out.append(re.sub(r"\s+", " ", sent).strip())
    return out


@dataclass
class Finding:
    level: str
    code: str
    message: str

    def render(self) -> str:
        return f"  [{self.level:<5}] {self.code:<20} {self.message}"


def spoken_body(transcript: str) -> str:
    """The words that reach the ear: no front-matter, no beat titles, no directives."""
    body = transcript.split("---", 2)[-1] if transcript.lstrip().startswith("---") else transcript
    body = re.sub(r"(?m)^##[^\n]*$", "", body)   # beat titles are not spoken (SPEC §4)
    body = re.sub(r"\{[^{}]*\}", "", body)
    return re.sub(r"[*_`]", "", body)


def _num(word: str) -> int | None:
    names = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
             "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13}
    return int(word) if word.isdigit() else names.get(word.lower())


def _quoting_beats(raw: str) -> str:
    """The text of every beat delivered in the instrument's own voice."""
    out, marks = [], list(_QUOTING_BEAT.finditer(raw))
    for m in marks:
        nxt = re.search(r"(?m)^##", raw[m.end():])
        out.append(raw[m.end(): m.end() + (nxt.start() if nxt else len(raw))])
    return "\n".join(out)


def _unbracketed_quotations(body: str, docket: str, quoting: str = "") -> list[str]:
    """Runs of the instrument's exact words the script speaks without marking as a quotation.

    Twelve words, calibrated rather than guessed. At ten, a script's own recap trips it — the
    series earns statutory phrases as the NAMES of concepts ("placed on the market or put into
    service") and then uses them constantly, which is correct and must not be flagged. At
    sixteen, a genuine near-quotation of Art. 2(6) slips through. Twelve separates the two on
    the three episodes written so far.

    The persona requires quoted text to be audibly bracketed, because the listener cannot see
    quotation marks. One editorial round caught a provision spoken near-verbatim without them;
    nothing mechanical was watching for it.
    """
    # Only the operative text counts. Matching the whole docket meant any phrase a compiler
    # happened to write in a note could trigger — episode 3's own recap ("So far we have the
    # gate — what counts as an AI system at all...") was reported as quoting the instrument,
    # because those words appear in a teaching note. The verbatim provisions live in fenced
    # blocks; fall back to the whole docket only when there are none.
    fenced = re.findall(r"```text\n(.*?)```", docket, re.S)
    source = "\n".join(fenced) if fenced else docket
    dn = re.sub(r"[^a-z0-9 ]", " ", source.lower())
    dn = re.sub(r"\s+", " ", dn)
    hits = []
    sents = _SENTENCE.findall(body)
    for i, sent in enumerate(sents):
        if '"' in sent or "\u201c" in sent:
            continue
        # The persona requires quotations to be bracketed AUDIBLY, not typographically — the
        # listener cannot hear a quotation mark. "His sentence, and these are his words: ..."
        # is correctly bracketed and was being reported as unmarked, which penalised the
        # script for doing the right thing for the medium.
        near = " ".join(sents[max(0, i - 1):i + 2])
        if _AUDIBLE_BRACKET.search(near):
            continue
        if quoting and sent.strip()[:60] in quoting:
            continue
        words = re.findall(r"[A-Za-z']+", sent)
        for i in range(max(0, len(words) - 11)):
            window = " ".join(w.lower() for w in words[i:i + 12])
            if window in dn:
                hits.append(sent.strip()[:110])
                break
    return hits


def lint_script(transcript: str, *, episode: int | None = None,
                target_minutes: int | None = None,
                banned: list[str] | None = None,
                docket: str = "") -> list[Finding]:
    body = spoken_body(transcript)
    # Keep the match POSITIONS, not just the tokens: slicing the head and tail out of a
    # re-joined token list silently drops every digit, so "Episode 7" became "Episode" and
    # neither the early-pointer check nor the bibliography check could see what it was for.
    tokens = list(re.finditer(r"[A-Za-z']+", body))
    words = [m.group(0) for m in tokens]
    minutes = len(words) / _WORDS_PER_MINUTE
    out: list[Finding] = [
        Finding(NOTE, "length", f"{len(words)} spoken words, about {minutes:.0f} min"
                + (f" against a {target_minutes} min brief" if target_minutes else ""))
    ]

    # --- forward references: a pointer to something unheard is a debt ---
    fwd, back = [], []
    for m in _EPISODE_REF.finditer(body):
        n = _num(m.group(1))
        if n is None or (episode is not None and n == episode):
            continue
        (fwd if episode is None or n > episode else back).append(n)
    vague = _VAGUE_DEFER.findall(body)
    total_fwd = len(fwd) + len(vague)
    if total_fwd > 3:
        out.append(Finding(ERROR, "forward-refs",
                           f"{total_fwd} forward references ({len(fwd)} numbered "
                           f"{sorted(set(fwd))}, {len(vague)} unnumbered) — budget is 3. Each "
                           "asks a travelling listener to hold a pointer to something unheard"))
    elif total_fwd:
        out.append(Finding(NOTE, "forward-refs", f"{total_fwd} forward references (budget 3)"))
    if back:
        out.append(Finding(NOTE, "back-refs",
                           f"{len(back)} references to earlier episodes {sorted(set(back))} — "
                           "these cost the listener nothing and are not budgeted"))

    # the first five minutes must be free of them
    cut = int(5 * _WORDS_PER_MINUTE)
    head = body[: tokens[cut].end()] if len(tokens) > cut else body
    early = len(_EPISODE_REF.findall(head)) + len(_VAGUE_DEFER.findall(head))
    if early:
        out.append(Finding(ERROR, "early-forward-ref",
                           f"{early} episode reference(s) in the first five minutes"))

    # --- enumeration: no list read aloud ---
    runs = _enumerations(body)
    if runs:
        sample = re.sub(r"\s+", " ", runs[0]).strip()[:90]
        out.append(Finding(WARN, "enumeration",
                           f"{len(runs)} sentence(s) run four or more comma-separated items: "
                           f'e.g. "{sample}..."'))

    # --- can a listener who lapsed rejoin? ---
    recaps = _RECAP.findall(body)
    if len(recaps) < 2:
        out.append(Finding(WARN, "no-recap",
                           f"{len(recaps)} mid-episode orientation marker(s) — someone who lost "
                           "twenty seconds has no way back in"))

    # --- a spoken bibliography is dead air where attention is lowest ---
    tail = body[tokens[-220].start():] if len(tokens) > 220 else body
    if re.search(r"(?i)\bsources?\b", tail) and len(re.findall(r"(?i)\(\d{4}\)|\b\d{4}\b", tail)) >= 3:
        out.append(Finding(ERROR, "spoken-sources",
                           "the closing minutes read like a source list — sources belong in "
                           "`prosodia references`, not in the audio"))

    # --- ear-only hygiene ---
    for m in _DEIXIS.finditer(body):
        out.append(Finding(ERROR, "spatial-deixis", f'"{m.group(0)}" — the listener has no picture'))
    for phrase in banned or []:
        n = len(re.findall(rf"(?i)\b{re.escape(phrase)}\b", body))
        if n:
            out.append(Finding(WARN, "banned-phrase", f'"{phrase}" x{n} (series watchlist)'))

    # --- attention: how long the listener goes with no pause and no question ---
    #
    # Beat titles and directives are stripped from `body`, so this measures the RAW script:
    # an editorial round found a 730-word stretch — five and a half minutes — with neither a
    # silence nor a retrieval question in it, which is where a travelling listener is lost.
    raw = transcript.split("---", 2)[-1] if transcript.lstrip().startswith("---") else transcript
    marks = [0] + [m.start() for m in _BREATH.finditer(raw)] + [len(raw)]
    worst, where = 0, 0
    for a, b in itertools.pairwise(marks):
        n = len(re.findall(r"[A-Za-z']+", raw[a:b]))
        if n > worst:
            worst, where = n, a
    if worst > 450:
        out.append(Finding(WARN, "no-breath",
                           f"{worst} words (~{worst / _WORDS_PER_MINUTE:.1f} min) with no pause, "
                           f"beat break or question: \"...{re.sub(chr(10), ' ', raw[where:where + 70]).strip()}...\""))

    # --- a construction used often enough to become a tic ---
    frags = [m.group(1) for m in _FRAGMENT.finditer(body)]
    if len(frags) >= 3:
        out.append(Finding(WARN, "fragment-tic",
                           f"{len(frags)} sentences are relative clauses punctuated as sentences "
                           f'("{frags[0]} ...") — idiomatic twice, a tic beyond'))

    if docket:
        for sent in _unbracketed_quotations(body, docket, _quoting_beats(raw)):
            out.append(Finding(WARN, "unbracketed-quote",
                               f'speaks twelve or more of the instrument\'s exact words without '
                               f'marking them as a quotation: "{sent}..."'))

    shapes = _NOT_X_Y.findall(body)
    if len(shapes) >= 4:
        out.append(Finding(WARN, "not-x-y",
                           f"{len(shapes)} uses of the 'it is not X, it is Y' correction shape — "
                           "the series bans it; two is a move, twelve is the narrator's only gear"))

    # --- rhythm ---
    lens = [len(re.findall(r"[A-Za-z']+", s)) for s in _SENTENCE.findall(body)]
    lens = [n for n in lens if n]
    if lens:
        med = statistics.median(lens)
        short = sum(1 for n in lens if n <= 8) / len(lens)
        out.append(Finding(NOTE, "rhythm",
                           f"median sentence {med:.0f} words, {short:.0%} at 8 or fewer "
                           "(persona: about 12, a third short)"))
        if med > 17:
            out.append(Finding(WARN, "rhythm", f"median {med:.0f} words is written register"))
    return out


def lint_episode_file(path: Path, *, episode: int | None = None,
                      target_minutes: int | None = None,
                      banned: list[str] | None = None, docket: str = "") -> list[Finding]:
    return lint_script(path.read_text(encoding="utf-8"), episode=episode,
                       target_minutes=target_minutes, banned=banned, docket=docket)
