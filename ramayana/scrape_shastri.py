#!/usr/bin/env python3
"""Scrape the full Shastri translation of the Valmiki Ramayana from wisdomlib.org
into a single clean text file. Resumable: skips chapters already saved."""
import re, os, sys, time, html, json, urllib.request

BASE = "https://www.wisdomlib.org/hinduism/book/the-ramayana-of-valmiki"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"}
OUTDIR = "/Users/janardan/github/knowledge-bundles/ramayana/shastri_parts"
os.makedirs(OUTDIR, exist_ok=True)

BOOK_INDEXES = [
    ("Book 1 - Bala-kanda", "doc423850"),
    ("Book 2 - Ayodhya-kanda", "doc423947"),
    ("Book 3 - Aranya-kanda", "doc424097"),
    ("Book 4 - Kishkindha-kanda", "doc424173"),
    ("Book 5 - Sundara-kanda", "doc424559"),
    ("Book 6 - Yuddha-kanda", "doc424628"),
    ("Book 7 - Uttara-kanda", "doc424761"),
]

def fetch(url, retries=3):
    req = urllib.request.Request(url, headers=UA)
    for i in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:
            if i == retries - 1:
                raise
            time.sleep(3 * (i + 1))

def chapter_links(book_page_html):
    """Return ordered list of (doc_id, title) from a book index page."""
    out = []
    for m in re.finditer(r'href="[^"]*/the-ramayana-of-valmiki/d/(doc\d+)\.html"[^>]*>\s*(Chapter \d+[^<]*)', book_page_html):
        doc, title = m.group(1), m.group(2).strip()
        # skip nav links (Previous/Next) — they won't match "Chapter N" pattern anyway
        if doc not in [d for d, _ in out]:
            out.append((doc, title))
    return out

def extract_content(html_text):
    start = html_text.find('id="scontent"')
    if start < 0:
        return None
    # skip past the opening tag itself
    tag_end = html_text.find('>', start)
    chunk = html_text[tag_end + 1:tag_end + 200000]
    for marker in ['chapter-dates', 'id="stickymain"', 'id="stickyoverlay"', '<div class="row no-gutters', 'class="footer', 'Related articles', 'Buy now']:
        i = chunk.find(marker)
        if i > 0:
            # if the marker is an attribute inside a tag, cut at the start of that tag
            lt = chunk.rfind('<', 0, i)
            if lt >= 0 and i - lt < 120:
                i = lt
            chunk = chunk[:i]
    chunk = re.sub(r'<script.*?</script>', '', chunk, flags=re.S)
    chunk = re.sub(r'<br\s*/?>', '\n', chunk)
    chunk = re.sub(r'</p>', '\n\n', chunk)
    chunk = re.sub(r'<[^>]+>', '', chunk)
    chunk = html.unescape(chunk)
    chunk = re.sub(r'[ \t]+\n', '\n', chunk)
    chunk = re.sub(r'\n{3,}', '\n\n', chunk)
    return chunk.strip()

def main():
    index_cache = os.path.join(OUTDIR, "_index.json")
    if os.path.exists(index_cache):
        plan = json.load(open(index_cache))
    else:
        plan = []
        for book_name, doc in BOOK_INDEXES:
            page = fetch(f"{BASE}/d/{doc}.html")
            links = chapter_links(page)
            print(f"{book_name}: {len(links)} chapters ({links[0][0]}..{links[-1][0]})", flush=True)
            plan.append({"book": book_name, "chapters": links})
        json.dump(plan, open(index_cache, "w"))
        time.sleep(1)

    for entry in plan:
        book_name = entry["book"]
        slug = re.sub(r'[^A-Za-z0-9]+', '_', book_name).strip('_')
        outpath = os.path.join(OUTDIR, f"{slug}.txt")
        done = set()
        if os.path.exists(outpath):
            done = set(re.findall(r'^@@(\d+)@@$', open(outpath).read(), re.M))
        parts = []
        fetched = 0
        for doc, title in entry["chapters"]:
            if doc in done:
                continue
            page = fetch(f"{BASE}/d/{doc}.html")
            body = extract_content(page)
            if body is None:
                print(f"  WARN: no content for {doc} ({title})", flush=True)
                continue
            parts.append(f"@@{doc}@@\n{title}\n{'='*len(title)}\n\n{body}\n")
            fetched += 1
            time.sleep(0.35)
            if fetched % 25 == 0:
                print(f"  {book_name}: {fetched} fetched so far", flush=True)
        if parts:
            with open(outpath, "a") as f:
                f.write("\n".join(parts))
            print(f"DONE {book_name}: appended {fetched} chapters -> {outpath}", flush=True)
    print("ALL BOOKS COMPLETE", flush=True)

if __name__ == "__main__":
    main()
