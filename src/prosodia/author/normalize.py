"""Text normalization for narration.

Converts numbers, years, ranges, and common symbols/abbreviations into spoken
form, since Chatterbox has no SSML to lean on. Pragmatic v0.1 coverage of the
cases common in historical narration (years, year ranges, section symbols,
percentages, era abbreviations); extend the tables as needed. Applied to
``spoken_text`` only — the authored transcript stays readable.
"""

from __future__ import annotations

import re

_ONES = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen",
]
_TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def _two(n: int) -> str:
    if n < 20:
        return _ONES[n]
    t, o = divmod(n, 10)
    return _TENS[t] + ("-" + _ONES[o] if o else "")


def _three(n: int) -> str:
    h, r = divmod(n, 100)
    parts = []
    if h:
        parts.append(_ONES[h] + " hundred")
    if r:
        parts.append(_two(r))
    return " ".join(parts)


def int_to_words(n: int) -> str:
    if n == 0:
        return "zero"
    if n < 0:
        return "minus " + int_to_words(-n)
    parts: list[str] = []
    for value, name in [(10**9, "billion"), (10**6, "million"), (10**3, "thousand"), (1, "")]:
        if n >= value:
            q, n = divmod(n, value)
            parts.append(_three(q) + (" " + name if name else ""))
    return " ".join(p for p in parts if p)


def year_to_words(y: int) -> str:
    # Two-pair reading ("ten sixty-six", "nineteen forty-five") covers historical
    # narration from the year 1000 onward; this is the documented era coverage.
    if 1000 <= y <= 1999:
        hi, lo = divmod(y, 100)
        if lo == 0:
            # 1000 reads as "one thousand", not "ten hundred"; 1100+ as "<n> hundred".
            return "one thousand" if hi == 10 else _two(hi) + " hundred"
        return f"{_two(hi)} {('oh ' + _ONES[lo]) if lo < 10 else _two(lo)}"
    if 2000 <= y <= 2099:
        lo = y - 2000
        if lo == 0:
            return "two thousand"
        if lo < 10:
            return f"two thousand {_ONES[lo]}"
        return f"twenty {_two(lo)}"
    return int_to_words(y)


# Unconditional, unambiguous abbreviations (whole-word). Era markers (AD/BC/CE/
# BCE) are deliberately NOT here: they collide with ordinary English words ("CE
# marked goods", "AD tests"), so they are expanded only adjacent to a number
# (see _ERA_* below).
_ABBREV = {
    "WWII": "World War Two",
    "WWI": "World War One",
    "USSR": "U S S R",
    "EEC": "E E C",
}

# Era markers spoken letter-by-letter, only when next to a number.
_ERA = {"BCE": "B C E", "CE": "C E", "AD": "A D", "BC": "B C"}
# Number-then-marker, e.g. "200 BCE" -> "... B C E"; longest key first.
_ERA_AFTER = re.compile(r"(?<=\d)\s+(BCE|BC|CE|AD)\b")
# Marker-then-number, e.g. "AD 1066" -> "A D ...".
_ERA_BEFORE = re.compile(r"\b(BCE|BC|CE|AD)\s+(?=\d)")

_YEAR_RANGE = re.compile(r"\b(\d{3,4})\s*[–—-]\s*(\d{3,4})\b")
_SECTION = re.compile(r"§\s*(\d+)([a-zA-Z])?")
_YEAR = re.compile(r"\b(1[0-9]{3}|2[0-9]{3})\b")
# Decades like "1820s": _YEAR's trailing \b fails between the digit and the "s", so these
# would otherwise reach the engine as raw digits. Handle them explicitly, before _YEAR.
_DECADE = re.compile(r"\b(1[0-9]{3}|2[0-9]{3})s\b")
_DECIMAL = re.compile(r"\b(\d+)\.(\d+)\b")
_INT = re.compile(r"\b\d{1,3}(?:,\d{3})+\b|\b\d+\b")


def _looks_like_year(s: str) -> bool:
    return len(s) == 4 and s.isdigit() and 1000 <= int(s) <= 2999


def _num_or_year(s: str) -> str:
    return year_to_words(int(s)) if _looks_like_year(s) else int_to_words(int(s))


def _decade_to_words(year: int) -> str:
    """1820 -> 'eighteen twenties'; pluralise the trailing word of the spoken year form
    (twenty->twenties, hundred->hundreds, ten->tens)."""
    head, _, last = year_to_words(year).rpartition(" ")
    plural = last[:-1] + "ies" if last.endswith("y") else last + "s"
    return f"{head} {plural}".strip()


def _decimal_to_words(whole: str, frac: str) -> str:
    digits = " ".join(_ONES[int(d)] for d in frac)
    return f"{int_to_words(int(whole))} point {digits}"


def normalize_text(text: str) -> str:
    for k in sorted(_ABBREV, key=len, reverse=True):
        text = re.sub(rf"\b{re.escape(k)}\b", _ABBREV[k], text)
    # Era markers only in number-adjacent context (avoids corrupting "CE marked").
    text = _ERA_AFTER.sub(lambda m: " " + _ERA[m.group(1)], text)
    text = _ERA_BEFORE.sub(lambda m: _ERA[m.group(1)] + " ", text)
    # Decimals before years/ints so the dot is not treated as a separator.
    text = _DECIMAL.sub(lambda m: _decimal_to_words(m.group(1), m.group(2)), text)
    text = _YEAR_RANGE.sub(lambda m: f"{_num_or_year(m.group(1))} to {_num_or_year(m.group(2))}", text)
    text = _SECTION.sub(
        lambda m: f"section {int_to_words(int(m.group(1)))}"
        + (f" {m.group(2).lower()}" if m.group(2) else ""),
        text,
    )
    text = _DECADE.sub(lambda m: _decade_to_words(int(m.group(1))), text)
    text = _YEAR.sub(lambda m: year_to_words(int(m.group(1))), text)
    text = text.replace("%", " percent").replace("&", " and ")
    text = _INT.sub(lambda m: int_to_words(int(m.group(0).replace(",", ""))), text)
    return re.sub(r"\s+", " ", text).strip()
