---
type: Log
title: leading-ai-companies bundle history
---

# Bundle history

## 2026-09-11 - review batch 3: the OpenAI founding cohort, LeCun, and a timeline directory

**Addition.** Twelve `Person` concepts: [Ilya Sutskever](/founders/ilya-sutskever.md), [Greg Brockman](/founders/greg-brockman.md), [Andrej Karpathy](/founders/andrej-karpathy.md), [John Schulman](/founders/john-schulman.md), [Durk Kingma](/founders/durk-kingma.md), [Trevor Blackwell](/founders/trevor-blackwell.md), [Vicki Cheung](/founders/vicki-cheung.md), [Pamela Vagata](/founders/pamela-vagata.md), [Wojciech Zaremba](/founders/wojciech-zaremba.md), [Elon Musk](/founders/elon-musk.md), [Mira Murati](/founders/mira-murati.md) and [Yann LeCun](/founders/yann-lecun.md). Plus a new `timeline/` directory holding [the chronology](/timeline/ai-ecosystem.md), which carries `related-to` edges to all 25 concepts it covers.

**What the first-party source settled.** The founding announcement at openai.com names the group precisely: Ilya Sutskever as research director, Greg Brockman as chief technology officer, and "other founding members ... Trevor Blackwell, Vicki Cheung, Andrej Karpathy, Durk Kingma, John Schulman, Pamela Vagata, and Wojciech Zaremba", with Sam Altman and Elon Musk as co-chairs and $1B pledged by the founding funders. That settles the eleven-name list from the primary document rather than from an encyclopaedia, and it closes seven pending targets the OpenAI concept had carried since batch 2.

**Two corrections of a common claim, recorded in-file rather than as a remark here.**

* **Mira Murati is not an OpenAI founder.** She joined in 2018 as vice president of applied AI and partnerships, two and a half years after the founding; her file says so at the top and carries `previously-at`, never `founded`, toward the OpenAI concept.
* **Yann LeCun has no OpenAI connection at all.** His file sits in `founders/` because he founded Advanced Machine Intelligence Labs in December 2025, not because of any OpenAI history.

**New directory, and the schema change it forced.** `timeline/` is the first directory in this bundle whose concepts are derived rather than primary, so conventions gained a layout row, a short "Timeline files" section, and a maintenance rule: a batch that adds a dated fact updates the timeline and its chart in the same commit, with the chart regenerated rather than appended to. `type: Timeline` is now known to both tools - the checker maps the directory and accepts the type, and the index generator lists it.

**Refusals and gaps, kept rather than smoothed over.** No current artificial-intelligence role is established for Trevor Blackwell, and his file says so plainly rather than implying he left the field. Vicki Cheung and Pamela Vagata have no encyclopaedia articles, so those files rest on a personal site, a 2020 conference biography, a firm page and self-reported profiles, and no dates are asserted for Cheung's sequence of roles. Wojciech Zaremba's OpenAI Foundation role comes from a trade report and his own profile, not from a first-party page. Wikipedia is the sole source for the Nvidia investment in Safe Superintelligence and for the AMI Labs round. The 2026-08-05 role change at Google DeepMind is quoted from the first-party post, which is the only source used for it, so the name of the successor is still not asserted anywhere in this bundle.

**Open decision, unchanged.** The succession gap in [Google DeepMind](/companies/google-deepmind.md) - `CEO 2010-2026` with the successor unnamed - is still waiting on a choice, and this batch deliberately did not resolve it. The timeline records the announcement without saying who took over.


## 2026-09-11 - media

**Addition.** An `images/` directory now holds four binaries, each cited from the concept that uses it.

| File | Cited by | Source | Licence |
| --- | --- | --- | --- |
| `images/anthropic-logo.svg` | [Anthropic](/companies/anthropic.md) | [Commons](https://commons.wikimedia.org/wiki/File:Anthropic_logo.svg) | public domain |
| `images/replit-logo.svg` | [Replit](/companies/replit.md) | [Commons](https://commons.wikimedia.org/wiki/File:New_Replit_Logo.svg) | public domain |
| `images/dario-amodei.jpg` | [Dario Amodei](/founders/dario-amodei.md) | [Commons](https://commons.wikimedia.org/wiki/File:Dario_Amodei_at_TechCrunch_Disrupt_2023_01_(cropped).jpg) | CC BY 2.0, credit TechCrunch |
| `images/amjad-masad.jpg` | [Amjad Masad](/founders/amjad-masad.md) | [Commons](https://commons.wikimedia.org/wiki/File:Amjad_Masad_with_Reid_Hoffman_(52531028724).jpg) | CC BY 2.0, credit Village Global |

**Conventions this fixes.**

* Frontmatter gains `image:`, holding a bundle-relative absolute path (`/images/x.svg`) - the same form the concept links use.
* The body embeds the file with ordinary markdown, which needs a path relative to the file's own directory (`../images/x.svg`). The two forms are deliberate: tools read the frontmatter, GitHub and Obsidian render the body.
* An asset is cited twice, by the same rule as a claim: a `sources[]` entry with a footnote from the caption, and a `[^id]:` definition line at the foot of the body. `licence`, `licence_url`, `file`, `sha256` and `retrieved` are extension keys. OKF §5.1 forbids storing a *credibility* score; a licence is a fact, so it is stored.
* The shipped files are derivatives and their captions say so. Portraits are resampled to a 900 px long edge; the Amjad Masad photograph is cropped from a two-person frame, which CC BY permits with the change noted. No artwork was altered - the SVGs differ from upstream only in their `width`/`height` display attributes, normalised so that a 32 px mark and a 1024 px wordmark render at comparable weight.
* `images/` holds no concepts, so it gets no `index.md` and is listed as a non-concept directory in [index.md](/index.md).

**Limits, stated rather than smoothed over.** Commons holds six files depicting Amjad Masad, all frames from a single Village Global event in 2022; none is a frontal solo portrait, so the shipped image is cropped from the largest of them. The Replit wordmark on Commons carries a share-alike licence, so the bundle uses the public-domain mark instead. The Anthropic wordmark is near-black on transparency and will read poorly against a dark background; it was left at its brand colour rather than recoloured for a theme.

**Method note.** Each image was inspected rather than trusted: both SVGs were checked for embedded scripting, rasterised and looked at, and the photographs were confirmed against their Commons metadata, dimensions included, so that the file credited is the file shipped.

## 2026-09-10 - review batch 1

**Initialization.** Created the bundle root with `okf_version: "0.2"`, this log, and two subdirectories, `companies/` and `founders/`.

**Creation.** Four concepts written:

* [Anthropic](/companies/anthropic.md) and [Replit](/companies/replit.md) - `type: Company`
* [Dario Amodei](/founders/dario-amodei.md) and [Amjad Masad](/founders/amjad-masad.md) - `type: Person`

The pair was chosen so the sample exercises three of the brief's four entry points at once: a frontier lab (step 1), a 2016-founded company that broke out after the November 2022 ChatGPT launch (step 2), and a Y Combinator company (step 3). It also produces a genuine edge running in both directions - Replit is an Anthropic customer, and Anthropic's Claude Code competes with Replit's own agent.

**Source bar applied.** Every load-bearing claim carries a footnote whose label is a `sources[].id` in the same file. Source authors use the actor convention with two extensions of the observed `<kind>:<id>` pattern: `org:<slug>` for institutional authors (a company, a press outlet, an analyst tracker) and `wiki:<lang>` for community-edited reference works. The two are deliberately distinguishable, because a figure that exists only in a wiki infobox and a figure on a company's own announcement page should not read as equally solid. No credibility score is stored: OKF §5.1 requires credibility to be inferred from signals, so the namespace is the signal.

**Schema decisions taken, for review.** These are cheapest to change now and most expensive after sixty files.

| Decision | Choice |
| --- | --- |
| Typed edges | `relations:` frontmatter, one entry per edge, `{ type, target, ... }` |
| Link form | bundle-relative absolute paths (`/companies/openai.md`), per spec §6.1 |
| Edge vocabulary | `founded-by`, `invested-by`, `operates-in`, `applies-to`, `contributes-to`, `ships`, `competes-with`, `partners-with`, `customer-of`, `uses`, `previously-at`, `educated-at`, `employs` |
| Aliases | `aliases:` on every entity; the dedupe key for graph resolution |
| Corporate money | a company-to-company `invested-by` edge; only firms get an `investors/` concept |
| Staleness | `stale_after` differs by fact type - company funding 90 days, founder affiliations 365 |
| Trust | `generated` present; `verified` deliberately absent until you sign off a batch (spec §5.3) |

**Not done in this batch, by design.** No computed claims, so no `computations/`. No subdirectory `index.md` files - with two concepts each they would be padding; they arrive with iteration 2. `conventions.md` is not written yet either: the vocabulary above is better reviewed as prose in this log first, then frozen into a concept once you accept it.

**Pending concepts.** Links in this batch point at concepts that do not exist yet, which OKF §6.1 treats as not-yet-written knowledge rather than as an error. The set below is the checklist for iteration 2.

* Domains: `/ai-domains/foundation-models.md`, `/ai-domains/agentic-ai.md`, `/ai-domains/ai-safety.md`, `/ai-domains/interpretability.md`
* Use cases: `/ai-use-cases/ai-sdlc.md`, `/ai-use-cases/enterprise-knowledge.md`, `/ai-use-cases/computer-use.md`, `/ai-use-cases/scientific-research.md`, `/ai-use-cases/no-code-app-building.md`
* Technologies: `/technologies/mcp.md`, `/technologies/agent-skills.md`, `/technologies/jsrepl.md`
* Models: `/models/claude.md`
* Companies referenced but not written: `openai`, `google`, `google-deepmind`, `amazon`, `microsoft`, `meta`, `palantir`, `spacex`, `samsung`, `micron`, `sk-hynix`, `anysphere`, `github`, `lovable`, `databricks`, `accenture`, `okta`, `baidu`, `facebook`, `codecademy`, `udacity`
* Founders referenced but not written: `daniela-amodei`, `jack-clark`, `jared-kaplan`, `chris-olah`, `ben-mann`, `sam-mccandlish`, `tom-brown`, `faris-masad`, `haya-odeh`
* Investors referenced but not written: `altimeter-capital`, `dragoneer`, `greenoaks`, `sequoia-capital`, `coatue`, `capital-group`, `d1-capital-partners`, `georgian`, `a16z`, `prysm-capital`, `g-squared`, `y-combinator`, `okta-ventures`, `craft-ventures`
* Institutions referenced but not written: `princeton-university`, `stanford-university`, `caltech`, `princess-sumaya-university-for-technology`

**Method note.** `web_extract` stopped working partway through this batch - the keyless extractor began returning HTTP 403 on its own API. Sources after that point were read in a browser instead. Two citations in this batch are press articles whose URL resolves but whose body was not read (marked `headline-only` in the source `title`), and every such case is stated in the file rather than smoothed over.

---

## 2026-09-11 - batch 2: intersection nodes, breadth, tooling

Approved as A, B and C together. Twelve concepts added, the conventions frozen, tooling added, and version control started.

**A - the intersection nodes.** Chosen from data rather than taste: the five paths that both of batch 1's companies pointed at, so that the brief's first downstream query stops returning an empty set.

* `/ai-domains/foundation-models.md`, `/ai-domains/agentic-ai.md`, `/ai-use-cases/ai-sdlc.md`, `/technologies/mcp.md`, `/models/claude.md`

After this batch, the overlap between Anthropic and Replit is a computable set rather than an aspiration.

**B - breadth, following the brief's step 1.** Added `/companies/openai.md`, `/companies/google.md`, `/companies/google-deepmind.md`, `/models/gpt.md`, `/models/gemini.md`, `/founders/sam-altman.md`, `/founders/demis-hassabis.md`. Google is filed as one concept covering Alphabet with the merge stated in the file, because the pending-target list referenced `google` and no `alphabet` node existed. Google DeepMind is separate because the parent sells cloud and silicon while the lab builds the models, and because several edges only make sense against one or the other.

**C - tooling and conventions.**

* `conventions.md` freezes the layout, frontmatter keys, edge vocabulary, the mirror rule, attribution, staleness windows, the image rule and the never-write list. Changing it requires a log entry.
* `_tools/okf-check.py` replaces the throwaway `/tmp` checker with a real linter: frontmatter parse, type-versus-directory match, footnote reference and definition pairing, unused `sources[]` ids, dangling relation targets, duplicate edges, image resolution, and a scan for secrets and connection strings.
* `_tools/build-index.py` generates `index.md` in every populated directory and the root index, including the traversal recipes. Both index levels carry no frontmatter except `okf_version` at the root, per spec §8.
* Version control started in `~/github/knowledge-bundles`. Batch 1 and its media pass are one commit because the media edits are interleaved in the same files; batch 2 is the second commit. No remote is configured and nothing was pushed.

**Schema additions this batch, for review.**

| Addition | Reason |
| --- | --- |
| `owns` / `subsidiary-of` | Google and Google DeepMind are legally distinct and both needed concepts |
| `invested-in` as the mirror of `invested-by` | Google's file needed to state an investment it made, not one it received |
| `developed-by` as the mirror of `ships` | A model file should name its developer where a reader looks for it |
| `related-to` | Concept-to-concept association; the only edge a domain file normally carries |
| `co-founded-with`, `created` | Already in use in batch 1 but missing from the vocabulary |

**One fact, one edge.** Edges are recorded on the file that owns the evidence. Mirrors exist only for `invested-by`/`invested-in`, `ships`/`developed-by` and `owns`/`subsidiary-of`, and a consumer counting a relationship must treat a mirror pair as one edge. `customer-of` is deliberately not mirrored.

**Findings worth carrying forward.**

1. OpenAI's 2026 round is internally inconsistent in the source: Wikipedia's lead dates the $852B close to March 2026 and its body to April 2026. Both are recorded in the file.
2. Google's consolidated financials are missing. Alphabet's investor relations page was confirmed reachable but its contents were not parsed, so the file carries market-position statements and no revenue or headcount figure. The largest gap in the batch.
3. Two independent RCTs disagree on AI-assisted developer productivity: GitHub Copilot measured 55.8% faster, METR measured 19% slower for experienced maintainers. Both are recorded and the conflict is not resolved.
4. First-party sources were required for current model lines, and they changed the picture: OpenAI's documentation currently serves the GPT-5.6 family (Terra, Sol, Luna, Cyber) and GPT-6 Astra; Anthropic's serves Fable 5.1, Opus 5, Sonnet 5 and Haiku 4.5; DeepMind's serves Gemini 3.8 Flash, Omni 1.1 Flash, Robotics 2, Lyria 3.5 and Gemma 4. Wikipedia lags all three.
5. Hassabis's successor as Google DeepMind chief executive is not named in any source read, so the file says so rather than guessing.

**Defects caught and fixed in this batch.** The linter found three source titles whose values contained a colon and broke YAML parsing, one `sources[]` entry cited in prose but never declared, and the linter's own bug of iterating a scalar `image` value character by character. All fixed; the run is clean at 17 concepts and 192 edges.

**Pending concepts, regenerated.** 88 distinct targets, 115 dangling edges. The top of the menu by inbound degree, which is how the next increment should be chosen:

| Inbound | Target |
| --- | --- |
| 6 | `/companies/microsoft.md` |
| 4 | `/companies/amazon.md` |
| 3 | `/ai-domains/ai-safety.md` |
| 3 | `/investors/coatue.md` |
| 2 | `/technologies/agent-skills.md`, `/ai-use-cases/no-code-app-building.md`, `/ai-use-cases/enterprise-knowledge.md`, `/ai-use-cases/computer-use.md`, `/ai-use-cases/scientific-research.md`, `/founders/faris-masad.md`, `/founders/haya-odeh.md`, `/founders/daniela-amodei.md`, `/institutions/stanford-university.md`, `/companies/isomorphic-labs.md`, `/investors/y-combinator.md`, `/investors/altimeter-capital.md` |

New dangling nodes this batch introduced: the ten remaining OpenAI founders, Shane Legg and Mustafa Suleyman, the companies Loopt, Hydrazine Capital, Reddit, Worldcoin, Helion Energy, Instacart, Isomorphic Labs, Bullfrog Productions, Lionhead Studios, Elixir Studios, plus `/technologies/tpu.md`, `/technologies/alphafold.md` and three institution paths. Whole directories still empty: `investors/`, `institutions/`, `people/`, `concepts/`.

**Method note.** The web search tool began returning HTTP 403 during this batch, so research was routed through direct HTTP with a browser user agent, the Wikipedia API for extracts, and the arXiv abstract pages for paper claims. Every citation URL used here was status-checked with its title compared against the intended source before writing: 29 of 30 resolved, and the one dated MCP specification URL that failed was replaced with the current revision path, which resolves. `web_extract` remains unusable in this session.

**Still not done, by design.** No computed claims, so no `computations/`. `verified` remains absent on all 17 concepts until you sign off a batch (spec §5.3). The image convention is recorded in `conventions.md` rather than in this log, which supersedes the earlier note that it would live here.
