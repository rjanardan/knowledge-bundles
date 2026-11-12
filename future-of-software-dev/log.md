# Directory Update Log

Newest first. Dates are ISO 8601. Entries record what changed and, where a
convention was decided rather than a fact recorded, why.

## 2026-09-11

* **Initialization**: Created the bundle skeleton - `companies/`, `roles/`,
  `sdlc/`, `practices/`, `evidence/`, `forecasts/`, `people/`, `technologies/`,
  `timeline/`, `images/`, `references/captures/` and `_tools/`.
* **Creation**: Froze the schema in [conventions.md](/conventions.md) before the
  first batch rather than after it, including the evidence/forecast split, the
  per-shard section orders, the edge vocabulary with mirrors, and the rule that a
  shard key no source supports is written `null` and explained rather than
  guessed.
* **Creation**: Established the first four company concepts -
  [GitHub](/companies/github.md), [Anthropic](/companies/anthropic.md),
  [Atlassian](/companies/atlassian.md) and [Rally](/companies/rally.md) - chosen
  to span both ends of the lineage: the agile-tooling generation that began
  around 2002 and the AI-tooling generation that began around 2023.
* **Creation**: Established
  [AI developer-productivity RCTs](/evidence/ai-developer-productivity-rcts.md),
  the first `evidence/` concept, covering the 2023 vendor-controlled experiment,
  the 2025 independent randomised controlled trial and the 2026 follow-up that
  found the trial design itself had stopped working.
* **Creation**: Installed `_tools/okf-check.py` and `_tools/build-index.py`,
  extended from the tooling used in the sibling `leading-ai-companies` bundle.
  The checker was extended past specification conformance in three places, since
  this bundle's conventions state rules a spec-only checker would not notice:
  mirrored edges are verified on both sides, the frozen per-shard section order
  is checked as a subsequence, and a `Forecast` without a `falsifier` is an
  error rather than a warning.
* **Update**: Retained 23 primary retrievals under `references/captures/` as
  `.txt` artefacts, each carrying its retrieval date, SHA-256 prefix and HTTP
  status, so that every claim in this batch can be re-checked without refetching
  a page that may since have changed. Two of the 23 are JavaScript-rendered
  landing pages that yielded no usable body text and are kept only as a record
  that the fetch was attempted and returned nothing.

### Decisions taken on 2026-09-11

Recorded here because each is cheap to reverse now and expensive after the corpus
is large.

* **A new bundle, not a new shard in an existing one.** The sibling bundle
  `leading-ai-companies` treats companies as the unit of interest; this one treats
  the *work* as the unit and companies as evidence about it. Merging them would
  have forced one frontmatter shape onto two different questions.
* **`evidence/` and `forecasts/` kept apart, rather than one `claims/` shard with
  a discriminating key.** A single shard relies on every future writer
  remembering to set the key correctly, and a reader who forgets cannot see the
  difference between a measurement and a prediction. Separate directories make
  the distinction visible in a file listing, which is where it is needed.
* **First-party sources by default.** Vendor blogs, papers and official product
  pages are the primary layer; quality press is admitted only where no primary
  record exists, and a headline-only source is marked as such.
* **Retrievals kept as artefacts.** A capture costs disk and little else, and it
  is the only way to answer "did the page really say that" after the page moves.
* **No `Microsoft` concept yet.** The parent-company edge from
  [GitHub](/companies/github.md) points at `/companies/microsoft.md`, which does
  not exist. Under OKF §6.1 a link to not-yet-written knowledge is legal, and the
  checker reports it as a pending target rather than an error.
