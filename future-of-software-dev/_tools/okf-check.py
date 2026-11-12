#!/usr/bin/env python3
"""okf-check - conformance linter for the future-of-software-dev OKF bundle.

Run from anywhere:  python3 _tools/okf-check.py [--quiet]

Exit 0 when the corpus is clean, 1 when there are errors. Pending relation
targets are reported as information rather than errors, because OKF 6.1 treats a
link to not-yet-written knowledge as legal.

Three checks go beyond the specification on purpose. This bundle's conventions.md
states rules that a spec-only checker would not notice, and a rule that nothing
verifies is a rule that has already been broken:

  1. Mirrored edges are checked on both sides, wherever both files exist.
  2. The frozen per-shard section order is checked as a subsequence, so a section
     may be added but not reordered or dropped.
  3. A `Forecast` without a `falsifier` is an error, because conventions.md says
     such a concept is not written at all.
"""
import collections
import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("okf-check: PyYAML is required (python3 -m pip install pyyaml)")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
REF_RE = re.compile(r"\[\^([A-Za-z0-9._-]+)\]")
DEF_RE = re.compile(r"^\[\^([A-Za-z0-9._-]+)\]:", re.M)
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")
H2_RE = re.compile(r"^##\s+(.*?)\s*$", re.M)
SECRET_RE = re.compile(
    r"(sk-[A-Za-z0-9]{20,}|api[_-]?key\s*[:=]\s*[^\s\"']+|password\s*[:=]\s*[^\s\"']+|"
    r"Bearer\s+[A-Za-z0-9._-]{20,}|(?:postgres|mysql|mongodb\+srv|redis)://)", re.I)

SKIP_DIRS = {".git", ".obsidian", "images", "_tools", "node_modules"}
RESERVED = {"index.md", "log.md"}

TYPE_BY_DIR = {
    "companies": "Company",
    "roles": "Role",
    "sdlc": "Phase",
    "practices": "Practice",
    "evidence": "Study",
    "forecasts": "Forecast",
    "people": "Person",
    "technologies": "Technology",
    "timeline": "Timeline",
}
KNOWN_TYPES = {"Company", "Role", "Phase", "Practice", "Study", "Forecast",
               "Person", "Technology", "Timeline", "Convention", "Log"}

# Edge vocabulary from conventions.md. Every non-symmetric type has a mirror.
MIRRORS = {
    "owns": "subsidiary-of", "subsidiary-of": "owns",
    "produced": "produced-by", "produced-by": "produced",
    "practises": "practised-by", "practised-by": "practises",
    "automates": "automated-by", "automated-by": "automates",
    "changes": "changed-by", "changed-by": "changes",
    "measures": "measured-by", "measured-by": "measures",
    "contradicts": "contradicted-by", "contradicted-by": "contradicts",
    "supersedes": "superseded-by", "superseded-by": "supersedes",
    "claims": "claimed-by", "claimed-by": "claims",
}
SYMMETRIC = {"related-to"}
UNMIRRORED = {"founded-by", "founded", "employs", "previously-at", "uses"}
KNOWN_EDGES = set(MIRRORS) | SYMMETRIC | UNMIRRORED

# Frozen section order per shard, from conventions.md.
SECTION_ORDER = {
    "companies": ["Snapshot", "Founding and lineage", "What the sources show",
                  "What it says about the SDLC", "Evidence it has produced", "Relations",
                  "Commercials", "What is not established", "Disputed and unverified"],
    "roles": ["Snapshot", "The role before AI", "What the sources show now",
              "What is claimed next", "What automation does not do", "Evidence",
              "Relations", "What is not established"],
    "sdlc": ["Snapshot", "Before automation", "What changed", "What AI changes now",
             "What remains human", "Evidence", "Relations", "What is not established"],
    "practices": ["Snapshot", "The problem it solved", "Era", "What it changed",
                  "Where it broke", "Evidence", "Relations", "What is not established"],
    "evidence": ["Snapshot", "Method", "Result", "What it does not show", "Follow-ups",
                 "Relations", "What is not established"],
    "forecasts": ["Snapshot", "The claim", "Who says so, and when", "Basis",
                  "What would falsify it", "Relations", "What is not established"],
}

REQUIRED_FM = ("type", "title", "description", "resource", "tags", "aliases",
               "status", "generated", "stale_after", "sources")
RECOMMENDED_FM = ("title", "description", "resource", "tags", "aliases", "status",
                  "generated", "stale_after")
SHARD_KEYS = {
    "Company": ("founded", "hq"),
    "Role": ("automation_pressure",),
    "Phase": ("order",),
    "Practice": ("era",),
    "Study": ("method", "measured_at"),
    "Forecast": ("forecaster", "at", "basis", "falsifier"),
}

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
    edge_index = {}
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

        shard = rel.split(os.sep)[0]
        expected = TYPE_BY_DIR.get(shard)
        if "type" not in fm:
            errors.append(f"{rel}: frontmatter is missing the required key 'type'")
        else:
            if fm["type"] not in KNOWN_TYPES:
                warns.append(f"{rel}: unusual type {fm['type']!r}")
            if expected and fm["type"] != expected:
                warns.append(f"{rel}: type {fm['type']!r} does not match directory {expected!r}")

        for key in RECOMMENDED_FM:
            if key not in fm:
                warns.append(f"{rel}: missing recommended key {key!r}")
        for key in SHARD_KEYS.get(fm.get("type", ""), ()):
            if key not in fm:
                warns.append(f"{rel}: {fm.get('type')} concept is missing convention key {key!r}")
        if "verified" in fm:
            warns.append(f"{rel}: 'verified' present; it is added only on sign-off (spec 5.3)")

        # A forecast with no falsifier is not written at all (conventions.md).
        if fm.get("type") == "Forecast":
            fals = fm.get("falsifier")
            if not (isinstance(fals, str) and fals.strip()):
                errors.append(f"{rel}: Forecast has no 'falsifier'; conventions.md forbids writing one")

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

        # Section order: checked as a subsequence, so additions are legal but
        # reordering and omission are not.
        want = SECTION_ORDER.get(shard)
        if want:
            got = [h for h in H2_RE.findall(body)]
            cursor, missing = 0, []
            for w in want:
                while cursor < len(got) and got[cursor] != w:
                    cursor += 1
                if cursor == len(got):
                    missing.append(w)
                else:
                    cursor += 1
            if missing:
                warns.append(f"{rel}: section order deviates from conventions.md; "
                             f"missing or out of order: "
                             + ", ".join(f"## {x}" for x in missing))

        rel_edges = []
        for i, r in enumerate(fm.get("relations") or []):
            if not isinstance(r, dict):
                errors.append(f"{rel}: relations[{i}] is not a mapping")
                continue
            t, tgt = r.get("type"), r.get("target")
            if not t or not tgt:
                errors.append(f"{rel}: relations[{i}] needs both 'type' and 'target'")
                continue
            tgt = str(tgt)
            rel_edges.append((t, tgt))
            n_edges += 1
            edges[t] += 1
            if t not in KNOWN_EDGES:
                warns.append(f"{rel}: edge type {t!r} is not in the vocabulary in conventions.md")
            if not tgt.startswith("/") or not tgt.endswith(".md"):
                errors.append(f"{rel}: relations[{i}] target {tgt!r} is not a bundle-absolute .md path")
            elif not os.path.exists(os.path.join(ROOT, tgt.lstrip("/"))):
                targets[tgt] += 1
        edge_index[rel] = rel_edges

        seen = collections.Counter(rel_edges)
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

    # Mirror verification, second pass: both files now exist in edge_index.
    for rel, rel_edges in edge_index.items():
        for etype, tgt in rel_edges:
            mir = MIRRORS.get(etype)
            if not mir:
                continue
            tgt_rel = tgt.lstrip("/")
            if not os.path.exists(os.path.join(ROOT, tgt_rel)):
                continue  # pending target, already reported
            back = edge_index.get(tgt_rel, [])
            if not any(bt == mir and str(bg).lstrip("/") == rel for bt, bg in back):
                warns.append(f"{rel}: {etype} -> {tgt} has no {mir} mirror in the target file")

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
