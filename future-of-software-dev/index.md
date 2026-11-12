---
okf_version: "0.2"
---

# The future of software development

A knowledge bundle in Google's Open Knowledge Format v0.2. It is a graph first: 9 concepts carrying 21 typed edges, with `_tools/okf-check.py` for conformance and `_tools/build-index.py` for these listings.

Roles, lifecycle phases and the tooling that changed them, kept in two epistemics: measured findings under `evidence/`, attributed predictions under `forecasts/`.

Entries are listed here for browsing; the machine-readable layer is the `relations` frontmatter block in each concept. Conventions are frozen in [conventions.md](conventions.md).

# Bundle-level concepts

Concepts that live at the bundle root rather than inside a directory:

* [conventions](conventions.md)

# Companies

* [Anthropic](companies/anthropic.md) - AI developer and safety lab, maker of Claude and Claude Code, and the only vendor in this batch publishing a longitudinal study of how AI changed work inside its own engineering organisation.
* [Atlassian](companies/atlassian.md) - Collaboration and work-tracking vendor founded in 2002, whose Jira sits at the planning end of the software lifecycle and whose 2025 developer-experience survey reports AI gains alongside rising organisational friction.
* [GitHub](companies/github.md) - Code-hosting platform and Microsoft subsidiary, and the single largest distributor of AI coding assistance, whose published Copilot research supplies the most-quoted productivity figures in the field.
* [Rally](companies/rally.md) - Agile work-tracking product floated on the NYSE in 2013 and absorbed through CA Technologies into Broadcom, where by 2026 it is sold as enterprise value-stream management with AI forecasting.

# Evidence

* [Algorithmic scoring overstates agent usability](evidence/algorithmic-scoring-overstates-usability.md) - METR audit finding that on 18 real tasks early-2025 agents produced functionally correct code that was often not usable as-is, so automatic benchmark scoring overestimates real-world agent performance.
* [The Copilot task-completion experiment](evidence/copilot-task-completion-rct.md) - Controlled experiment in which developers given GitHub Copilot completed a single greenfield HTTP-server task 55.8% faster, and the academic form of the vendor figure that rounds to 55%.
* [The METR open-source developer productivity trial](evidence/os-developer-productivity-rct.md) - Randomised controlled trial in which experienced open-source developers took 19% longer with AI tools across 246 tasks in their own mature repositories, and a 2026 follow-up that found the trial design itself had stopped producing a usable signal.
* [Many SWE-bench-passing PRs would not be merged](evidence/swe-bench-merge-audit.md) - METR audit finding that roughly half of test-passing SWE-bench Verified pull requests written by agents would not be merged into main by repository maintainers.

# Directories declared but not yet populated

Named before they exist so that a link from a populated concept resolves to a declared target. Under OKF §6.1, a link to a not-yet-written concept is not an error.

* `roles/` - Roles - Job functions in software delivery, each with a past, present and future axis.
* `sdlc/` - SDLC phases - Lifecycle phases in order, and what each one has lost to automation.
* `practices/` - Practices - Methodologies that span several phases.
* `forecasts/` - Forecasts - Attributed predictions, each with a written falsifier.
* `technologies/` - Technologies - Tools, protocols and standards.
* `people/` - People - Practitioners, researchers and executives.
* `timeline/` - Timeline - Derived chronological views over the concepts in this bundle.

# Non-concept directories

* `images/` - media cited by concepts. Every asset carries a licence, a credit, a hash and a footnote definition line in the concept that uses it, so an asset is traceable by the same rule as a claim.
* `references/captures/` - raw retrieval dumps, stored as `.txt` so the conformance checker does not read them as concepts. Each carries its retrieval date, a SHA-256 prefix and the HTTP status at fetch time.
* `_tools/` - the conformance linter and this index generator.

# How to query the graph

These are traversals over the `relations` blocks rather than searches. They map onto the four uses this bundle was built for, which are also its acceptance test:

* **For a paper - what is actually measured.** Read `evidence/` alone. Every concept there carries a `method`, an `n` and an `effect_ci`, and nothing there is an estimate about the future.
* **For a book - how a phase changed, in order.** Walk `sdlc/` by its `order` key, then follow `changed-by` to the technologies that moved it and `practised-by` on `practices/` for the methodology layer.
* **For a post - one dated, sourced shift.** Any `## Snapshot` in `roles/` names the change and its date; the supporting measurement is one hop away under `evidence/`.
* **For an interview - what a company claims, and who disagrees.** Follow `claims` from `forecasts/` to its target and `contradicts` between studies. Counting `contradicts` edges is a direct read of where the field has not settled.

Two further traversals are worth naming because they are the ones a graph buys over a folder of notes:

* **Ownership lineage.** `owns` and `subsidiary-of` trace a tool from an independent vendor to its present owner, which is how a 2002 agile tracker becomes a 2026 value-stream product.
* **Source hygiene.** `sources[].author` uses an actor namespace, so a reader can count how many of a concept's sources are first-party. A concept resting only on `org:` sources is a vendor's account of itself.

Generated by `_tools/build-index.py` on 2026-09-11.
