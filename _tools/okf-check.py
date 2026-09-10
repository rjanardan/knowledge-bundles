#!/usr/bin/env python3
"""okf-check - conformance linter for an OKF bundle.

Run from anywhere:  python3 _tools/okf-check.py [--quiet]

Errors fail the run (exit 1). Pending relation targets are reported as
information, because OKF 6.1 treats a link to unwritten knowledge as legal.
"""
import os
import re
import sys
import collections

try:
    import yaml
except ImportError:
    sys.exit("okf-check: PyYAML is required (python3 -m pip install pyyaml)")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
REF_RE = re.compile(r"\[\^([A-Za-z0-9._-]+)\]")
DEF_RE = re.compile(r"^\[\^([A-Za-z0-9._-]+)\]:", re.M)
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")
SECRET_RE = re.compile(
    r"(sk-[A-Za-z0-9]{20,}|api[_-]?key\s*[:=]\s*[^\s\"']+|password\s*[:=]\s*[^\s\"']+|"
    r"Bearer\s+[A-Za-z0-9._-]{20,}|(?:postgres|mysql|mongodb\+srv|redis)://)", re.I)

SKIP_DIRS = {".git", ".obsidian", "images", "_tools", "node_modules"}
RESERVED = {"index.md", "log.md"}
TYPE_BY_DIR = {
    "companies": "Company", "founders": "Person", "investors": "Investor",
    "ai-domains": "Domain", "ai-use-cases": "UseCase", "technologies": "Technology",
    "models": "Model", "institutions": "Institution", "people": "Person",
    "concepts": "Concept",
}
SYMMETRIC = {"related-to", "competes-with", "partners-with"}
MIRRORS = {("invested-by", "invested-in"), ("ships", "developed-by"), ("owns", "subsidiary-of")}
KNOWN_TYPES = {"Company", "Person", "Investor", "Domain", "UseCase", "Technology",
               "Model", "Institution", "Concept", "Convention", "Log"}

errors, warns, info = [], [], []


def concepts():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in sorted(filenames):
            if not name.endswith(".md") or name in RESERVED:
                continue
            yield os.path.relpath(os.path.join(dirpath, name), ROOT)


def main():
    files = list(concepts())
    targets = collections.Counter()
    edges = collections.Counter()
    n_edges = 0

    for rel in files:
        path = os.path.join(ROOT, rel)
        text = open(path, encoding="utf-8").read()
        body = text
        fm = {}
        m = FM_RE.match(text)
        if not m:
            errors.append(f"{rel}: no YAML frontmatter block")
        else:
            body = text[m.end():]
            try:
                fm = yaml.safe_load(m.group(1)) or {}
            except Exception as exc:  # noqa: BLE001
                errors.append(f"{rel}: frontmatter does not parse as YAML: {exc}")
                fm = {}

        expected = TYPE_BY_DIR.get(rel.split(os.sep)[0])
        if "type" not in fm:
            errors.append(f"{rel}: frontmatter is missing the required key 'type'")
        else:
            if fm["type"] not in KNOWN_TYPES:
                warns.append(f"{rel}: unusual type {fm['type']!r}")
            if expected and fm["type"] != expected:
                warns.append(f"{rel}: type {fm['type']!r} does not match directory {expected!r}")
        for key in ("title", "description", "resource", "tags", "aliases", "status",
                    "generated", "stale_after"):
            if key not in fm:
                warns.append(f"{rel}: missing recommended key {key!r}")
        if "verified" in fm:
            warns.append(f"{rel}: 'verified' present; it is added only on sign-off (spec 5.3)")

        refs = set(REF_RE.findall(body))
        defs = set(DEF_RE.findall(body))
        for label in sorted(refs - defs):
            errors.append(f"{rel}: footnote [^{label}] has no definition line at the foot")
        for label in sorted(defs - refs):
            errors.append(f"{rel}: footnote definition [^{label}]: is never referenced")

        sources = fm.get("sources") or []
        ids = [s.get("id") for s in sources if isinstance(s, dict)]
        if not ids and sources:
            errors.append(f"{rel}: sources entries are not mappings with an 'id'")
        for sid in ids:
            if sid not in refs:
                errors.append(f"{rel}: source {sid!r} is declared but never cited")
        for label in sorted(refs - set(ids)):
            warns.append(f"{rel}: footnote [^{label}] has no sources[] entry with that id")
        for i, s in enumerate(sources):
            if isinstance(s, dict) and not s.get("resource"):
                warns.append(f"{rel}: sources[{i}] has no 'resource'")

        for i, r in enumerate(fm.get("relations") or []):
            if not isinstance(r, dict):
                errors.append(f"{rel}: relations[{i}] is not a mapping")
                continue
            t, tgt = r.get("type"), r.get("target")
            if not t or not tgt:
                errors.append(f"{rel}: relations[{i}] needs both 'type' and 'target'")
                continue
            tgt = str(tgt)
            n_edges += 1
            edges[t] += 1
            if not tgt.startswith("/") or not tgt.endswith(".md"):
                errors.append(f"{rel}: relations[{i}] target {tgt!r} is not a bundle-absolute .md path")
            elif not os.path.exists(os.path.join(ROOT, tgt.lstrip("/"))):
                targets[tgt] += 1
        seen = collections.Counter((r.get("type"), str(r.get("target")))
                                   for r in fm.get("relations") or [] if isinstance(r, dict))
        for (t, tgt), n in seen.items():
            if n > 1:
                warns.append(f"{rel}: duplicate edge {t} -> {tgt} ({n} times)")

        declared = fm.get("image") or []
        if isinstance(declared, str):
            declared = [declared]
        for img in set(declared) | set(IMG_RE.findall(body)):
            if str(img).startswith(("http://", "https://", "data:")):
                continue
            if not str(img).startswith("/") and not str(img).startswith(".."):
                warns.append(f"{rel}: image {img!r} is neither bundle-absolute nor relative")
                continue
            candidate = os.path.join(ROOT, str(img).lstrip("/")) if str(img).startswith("/") \
                else os.path.normpath(os.path.join(os.path.dirname(path), str(img)))
            if not os.path.exists(candidate):
                errors.append(f"{rel}: image {img!r} does not resolve to a file")

        for hit in SECRET_RE.finditer(text):
            errors.append(f"{rel}: possible secret or connection string: {hit.group(0)[:24]!r}")

    def dump(title, items, limit=40):
        if not items:
            return
        print(f"\n{title} ({len(items)})")
        for line in items[:limit]:
            print(f"  - {line}")
        if len(items) > limit:
            print(f"  ... and {len(items) - limit} more")

    print(f"okf-check: {len(files)} concepts, {n_edges} edges, "
          f"{len(targets)} pending targets, {sum(targets.values())} pending edges")
    dump("ERRORS", errors)
    dump("WARNINGS", warns)
    if targets and "--quiet" not in sys.argv:
        print("\nPending targets by inbound degree (next increment menu)")
        for tgt, n in targets.most_common(15):
            print(f"  {n:>2}  {tgt}")
    if edges:
        print("\nEdge vocabulary in use")
        print("  " + ", ".join(f"{t}({n})" for t, n in edges.most_common()))
    if errors:
        print(f"\nChecker FAILS: {len(errors)} error(s)")
        return 1
    print("\nChecker passes clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
