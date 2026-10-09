# eurlex — consolidated EU acts as quotable text

`consolidate.py` fetches the **consolidated** HTML of an EU act from EUR-Lex and renders it as
text that keeps the citation structure: article number and title, paragraph numbers, point
letters and their nesting, and the consolidation markers (`M1`, `M2` = as amended by the
first/second amending act, `B` = original wording).

```bash
python consolidate.py 02024R1689-20260727 aiact.txt   # fetch (cached) + convert
python consolidate.py cache/02024R1689-20260727.html aiact.txt
```

A consolidated CELEX is `0` + the act's CELEX + `-YYYYMMDD`, the date being the version's date of
application. **A 404 means no consolidated version applies at that date**, so probing dates is how
you discover which amendments exist and when they bit — that is how Regulation (EU) 2026/1744 was
confirmed as the AI Act's only amendment to date.

## The completeness guard is the point

The renderer emits only the block classes it knows, and EUR-Lex uses several that carry operative
text. An unhandled class drops binding law with no error at all. Real examples caught while
building this, each of which would have been read aloud as fact:

- `p.list` holds the **continuation sentence of a point** — dropping it deleted the Annex III 1(a)
  carve-out for biometric verification, inverting the point's meaning.
- Prose can sit as a **bare text node ahead of a nested list** — dropping it deleted the whole of
  Article 26(5), the deployer's monitoring duty.
- Exponents are a `span.superscript`, not a `<sup>` — flattening it rendered the Article 51(2)
  threshold as "1025" instead of **10^25**, wrong by twenty-three orders of magnitude.

So after rendering, every article's and annex's word count is compared against the raw text under
the same node, and any loss is reported. **Do not quote from output that reported a loss.**

## Provenance

The served HTML carries a per-request analytics id, so its hash is not stable — hash the
**extracted text** instead. Two independent fetches of the AI Act produced byte-identical text.

A consolidated text **omits the recitals** and is, in EUR-Lex's own words, a documentation tool
with no legal effect; the authentic text is the OJ. Take recitals from the original act.

## EUR-Lex now blocks scripted fetches (since 2026-10)

`eur-lex.europa.eu` answers non-browser clients with an **AWS WAF JavaScript challenge** (HTTP 202, ~2 KB),
so `fetch()` can no longer download new acts. **Cached acts still convert.** Two working routes, both
verified 2026-10-09:

- **CELLAR content negotiation** — the Publications Office repository serves the same documents:

  ```bash
  curl -L -H "Accept: application/xhtml+xml" -H "Accept-Language: eng" \
       -o cache/32024R0900.html http://publications.europa.eu/resource/celex/32024R0900
  python consolidate.py cache/32024R0900.html out.md --select "Article 18"
  ```

  The converter reads CELLAR's XHTML unchanged, completeness guard included. **Caveat:** for some works
  (the Charter, `12016P` / `12012P`) CELLAR's XHTML holds only the table of contents.
- **Court of Justice press releases** download directly from `curia.europa.eu/site/upload/docs/…/cpYYNNNen.pdf`
  — official summaries, not judgments.

Also refusing scripted requests: **HUDOC** and `echr.coe.int` (HTTP 403). The Convention's text is available
from the Council of Europe Treaty Office (`rm.coe.int/1680063765`). **FRA's Charter pages** work but put a
client behind a challenge after a burst of ~30 requests — fetch them slowly.
