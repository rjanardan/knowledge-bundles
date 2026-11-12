# Ramayana texts (knowledge bundle)

Two complete English translations of the Valmiki Ramayana, as single long text files.

## Files

| File | Translation | Style | Coverage | Source |
|---|---|---|---|---|
| `griffith-ramayana.txt` | Ralph T. H. Griffith, 1870–74 | Verse (poetry) | Books I–VI in full verse; Book VII (Uttara-kanda) as prose summary | Project Gutenberg #24869 (public domain) |
| `shastri-ramayana.txt` | Hari Prasad Shastri, 1952 | Prose | All 7 books, 661 chapters, complete | wisdomlib.org (chapter-wise scrape) |

## Notes

- **Griffith** is the classic Victorian verse translation. It is complete for Books I–VI; Griffith judged the Uttara-kanda a later appendix and rendered it only as a condensed prose epitome borrowing from Gorresio and Muir. Includes the Project Gutenberg license header.
- **Shastri** is a modern readable prose rendering of all seven kandas (Bala, Ayodhya, Aranya, Kishkindha, Sundara, Yuddha, Uttara) — 527k words. This is the "detailed" full story.
- Both are in the public domain in the US (Shastri 1952; check local copyright rules if redistributing).

## Scripts (for regeneration)

- `scrape_shastri.py` — resumable chapter-by-chapter scraper; writes per-book parts to `shastri_parts/`.
- `assemble_shastri.py` — merges per-book parts into the single `shastri-ramayana.txt`.

## Structure of the Shastri file

Chapters appear as:

```
Chapter 5 - King Dasaratha's kingdom and capital
================================================
<body text>
```

Book dividers: `==== Book N - X-kanda ====`. Chapters within each book are in original order.
