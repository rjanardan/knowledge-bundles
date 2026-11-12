#!/usr/bin/env python3
"""Assemble the per-book parts into one long Shastri Ramayana txt, and write a README."""
import os, re, glob, time

BASE = "/Users/janardan/github/knowledge-bundles/ramayana"
PARTS = os.path.join(BASE, "shastri_parts")
FINAL = os.path.join(BASE, "shastri-ramayana.txt")

HEADER = """THE RAMAYANA OF VALMIKI
Translated into English prose by Hari Prasad Shastri (1952)
Full text of all seven kandas, scraped chapter-by-chapter from wisdomlib.org
(https://www.wisdomlib.org/hinduism/book/the-ramayana-of-valmiki)

Contents:
  Book 1 - Bala-kanda (77 chapters)
  Book 2 - Ayodhya-kanda (119 chapters)
  Book 3 - Aranya-kanda (75 chapters)
  Book 4 - Kishkindha-kanda (67 chapters)
  Book 5 - Sundara-kanda (68 chapters)
  Book 6 - Yuddha-kanda (131 chapters)
  Book 7 - Uttara-kanda (124 chapters)

================================================================================
"""

book_order = [
    "Book_1_Bala_kanda.txt",
    "Book_2_Ayodhya_kanda.txt",
    "Book_3_Aranya_kanda.txt",
    "Book_4_Kishkindha_kanda.txt",
    "Book_5_Sundara_kanda.txt",
    "Book_6_Yuddha_kanda.txt",
    "Book_7_Uttara_kanda.txt",
]

# count chapters actually scraped per book
total_chapters = 0
for fn in book_order:
    p = os.path.join(PARTS, fn)
    if os.path.exists(p):
        n = len(re.findall(r'^@@doc\d+@@$', open(p).read(), re.M))
        total_chapters += n
        print(f"{fn}: {n} chapters, {os.path.getsize(p):,} bytes")
    else:
        print(f"{fn}: MISSING")

if total_chapters < 640:
    print(f"WARNING: only {total_chapters} chapters present; expected ~661. Run scrape again.")

with open(FINAL, "w") as out:
    out.write(HEADER)
    for fn in book_order:
        p = os.path.join(PARTS, fn)
        if not os.path.exists(p):
            continue
        text = open(p).read()
        # strip @@doc@@ markers, keep chapter titles
        text = re.sub(r'^@@doc\d+@@\n', '', text, flags=re.M)
        book_title = fn.replace('.txt', '').replace('_', ' ').replace('  ', ' - ')
        book_title = re.sub(r'(Book \d) (Bala|Ayodhya|Aranya|Kishkindha|Sundara|Yuddha|Uttara) (kanda)', r'\1 - \2-\3', book_title)
        out.write(f"\n\n{'='*80}\n{book_title}\n{'='*80}\n\n")
        out.write(text)
        out.write("\n\n")

print(f"\nAssembled: {FINAL} ({os.path.getsize(FINAL):,} bytes)")
