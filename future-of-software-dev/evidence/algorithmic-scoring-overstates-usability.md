---
type: Study
title: Algorithmic scoring overstates agent usability
description: METR audit finding that on 18 real tasks early-2025 agents produced functionally correct code that was often not usable as-is, so automatic benchmark scoring overestimates real-world agent performance.
resource: https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/
tags:
  - benchmark-audit
  - evaluation-validity
  - swe-bench
  - code-quality
method: benchmark-audit
n: 18
population: "18 real tasks from two large open-source repositories"
effect: "functionally correct code that could not be used as-is, from test coverage, formatting, linting or general code quality"
effect_ci: null
measured_at: "2025-08-13"
pre_registered: null
aliases:
  - Algorithmic vs Holistic Evaluation
  - METR benchmark audit
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-11T00:00:00Z
stale_after: 2027-09-11T00:00:00Z
relations:
  - { type: related-to, target: /evidence/os-developer-productivity-rct.md }
  - { type: related-to, target: /evidence/copilot-task-completion-rct.md }
  - { type: related-to, target: /evidence/swe-bench-merge-audit.md }
sources:
  - id: metr-holistic
    resource: "https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/"
    title: "Research Update: Algorithmic vs. Holistic Evaluation"
    author: "org:metr (David Rein)"
    note: "2025-08-13"
  - id: metr-merge
    resource: "https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/"
    title: "Many SWE-bench-Passing PRs Would Not Be Merged into Main"
    author: "org:metr (Parker Whitfill, Cheryl Wu, Joel Becker, Nate Rush)"
    note: "2026-03-10"
---

# Algorithmic scoring overstates agent usability

## Snapshot

On 18 real tasks drawn from two large open-source repositories, early-2025 AI agents often produced code that was functionally correct — it passed the tests — but could not be used as it stood, because of gaps in test coverage, formatting and linting, or general code quality.[^metr-holistic] METR's conclusion is aimed at the measurement apparatus rather than at the agents: automatic scoring of the kind many benchmarks use "may overestimate AI agent real-world performance".[^metr-holistic] The specific mechanism is that SWE-bench Verified scores an agent by whether it passes test cases written by the original human authors of the pull request, which is a narrow definition of done.[^metr-holistic]

## Method

A benchmark audit rather than a trial. METR took 18 real tasks from two large open-source repositories and examined what agents produced against what the repositories would accept, concentrating on properties that automated scoring does not test.[^metr-holistic] The unit of analysis is the task, and the comparison is between two scoring regimes over the same outputs: the algorithmic score (do the reference tests pass) and a holistic judgement (is this usable in the repository).[^metr-holistic]

`method` is recorded as `benchmark-audit` rather than `rct` because nothing was randomised; the finding is about the validity of an instrument, and its evidentiary status is correspondingly different from the trials in this shard.

## Result

The direction of the finding is that automated scores are an upper bound on usefulness rather than an estimate of it. Functionally correct code that a repository would not accept means the benchmark counts a success where a maintainer would not.[^metr-holistic]

METR's framing is explicit that this is about the instrument, not the capability: the audit examined whether benchmark scores predict real performance, and concluded that a naive reading of them may overestimate it.[^metr-holistic] The finding is also the first statement in this corpus of a pattern the later merge audit measures directly, which is why the two concepts are linked.

## What it does not show

* **It does not show the agents could not have produced usable code.** The audit measures what was produced under the conditions the benchmark sets, not what the systems are capable of. A later audit in this shard makes the same caveat explicit, noting that agents are not given the chance to iterate on feedback the way a human developer would.[^metr-merge]
* **It does not quantify the overestimate.** The direction is established; the magnitude is not, and `effect_ci` is `null` rather than filled with a number the source does not give.
* **It does not generalise from 18 tasks to the benchmark as a whole.** Eighteen tasks from two repositories is a sample of convenience, and the concept records `n: 18` precisely so that a reader does not read it as a systematic review.

## Follow-ups

The merge audit of March 2026 is the direct follow-up: where this audit argues that passing tests is not the same as being usable, that one measures the merge gate on a larger set and finds roughly half of test-passing pull requests would not be merged.[^metr-merge]

## Relations

Three `related-to` edges connect this audit to both trials and to the merge audit. Nothing `contradicts` anything here: an audit of an instrument does not conflict with a measurement made using a different instrument, and the mere fact that one finding is unflattering to benchmark scores and another is flattering to a coding tool does not make them conflicting claims about the same quantity. Recording this distinction is part of the point — `contradicts` is reserved for opposite signs on a comparable question.

## What is not established

* **Whether the pattern holds beyond these two repositories.** `n: 18` is a convenience sample.
* **How large the gap is between algorithmic score and holistic usability**, which the source states in direction only.
* **Whether the pattern has changed since early 2025.** The audit examines agents of that period and no source in this batch repeats it.

[^metr-holistic]: org:metr (David Rein), "Research Update: Algorithmic vs. Holistic Evaluation", 2025-08-13, https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/
[^metr-merge]: org:metr (Parker Whitfill, Cheryl Wu, Joel Becker, Nate Rush), "Many SWE-bench-Passing PRs Would Not Be Merged into Main", 2026-03-10, https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/
