---
type: Study
title: Many SWE-bench-passing PRs would not be merged
description: METR audit finding that roughly half of test-passing SWE-bench Verified pull requests written by agents would not be merged into main by repository maintainers.
resource: https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/
tags:
  - benchmark-audit
  - swe-bench
  - evaluation-validity
  - merge-gate
method: benchmark-audit
n: null
population: "SWE-bench Verified pull requests written by agents of mid-2024 to mid and late 2025"
effect: "roughly half of test-passing PRs would not be merged into main by maintainers"
effect_ci: null
measured_at: "2026-03-10"
pre_registered: null
aliases:
  - SWE-bench merge audit
  - METR merge audit
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-11T00:00:00Z
stale_after: 2027-09-11T00:00:00Z
relations:
  - { type: related-to, target: /evidence/algorithmic-scoring-overstates-usability.md }
  - { type: related-to, target: /evidence/os-developer-productivity-rct.md }
  - { type: related-to, target: /evidence/copilot-task-completion-rct.md }
sources:
  - id: metr-merge
    resource: "https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/"
    title: "Many SWE-bench-Passing PRs Would Not Be Merged into Main"
    author: "org:metr (Parker Whitfill, Cheryl Wu, Joel Becker, Nate Rush)"
    note: "2026-03-10"
  - id: metr-holistic
    resource: "https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/"
    title: "Research Update: Algorithmic vs. Holistic Evaluation"
    author: "org:metr (David Rein)"
    note: "2025-08-13"
  - id: metr-rct
    resource: "https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/"
    title: "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity"
    author: "org:metr"
    note: "(paper at arXiv:2507.09089)"
---

# Many SWE-bench-passing PRs would not be merged

## Snapshot

METR found that roughly half of the SWE-bench Verified pull requests written by agents between mid-2024 and mid or late 2025 that passed the benchmark's tests would not be merged into main by the repositories' maintainers, even after adjusting for noise in maintainer merge decisions.[^metr-merge] The maintainer's merge gate and the benchmark's test gate therefore disagree about half the time on the same artefacts. METR is careful about what this means: because agents are not given the chance to iterate on their solution in response to feedback the way a human developer would, the authors "do not claim that this represents a fundamental capability limitation".[^metr-merge]

## Method

A benchmark audit with human judgement as the second instrument. The comparison is between two gates applied to the same set of agent-written pull requests: whether the benchmark's tests pass, and whether a repository maintainer would merge the change into main.[^metr-merge] The second judgement is treated as noisy and the result is reported as adjusted for that noise, which is the methodologically important detail — a merge decision is a human verdict, not a measurement, and the audit says so.

`n` is left `null`: the summary retrieved does not state how many pull requests were examined, and the count is not reconstructed from the phrase "roughly half". `effect_ci` is likewise `null`, since the abstract reports a share rather than an interval.

## Result

The two gates disagree on roughly half of the test-passing pull requests.[^metr-merge] Read as a statement about measurement, the finding is that a benchmark score is an upper bound on mergeability, and that a naive reading of the score overestimates how useful agents are without more evidence about what happens after the tests pass.[^metr-merge]

Read as a statement about agents, the finding is weaker than it first appears, and the source says so itself. The agents under audit had no feedback loop: a human developer responds to review comments and revises, and the audited agents did not. The audit therefore measures the mergeability of unrevised agent output, which is a real quantity and a narrower one than it is often quoted as.[^metr-merge]

## What it does not show

* **It does not show that agents cannot produce mergeable code.** The stated limitation is the absence of a revision loop, so the result speaks to first-pass output rather than to the capability.[^metr-merge]
* **It does not measure the effect on human effort.** A pull request that is not merged still may have saved or cost reviewer time, and no source here measures that. This is the same gap the trial in this shard leaves open when it measures task time rather than delivered value.[^metr-rct]
* **It does not establish a trend.** The population spans mid-2024 to late 2025, and the source reports a single figure rather than a trajectory across that period.
* **It does not say which half, or why.** No retrieved source breaks the failures down by repository, task type or model, so nothing here attributes the disagreement to a cause.

## Follow-ups

This is the later of the two audits in the shard and follows the 2025 finding that algorithmic scoring overstates usability.[^metr-holistic] No independent replication, and no equivalent audit of the benchmarks that have replaced SWE-bench Verified, was found in this batch.

## Relations

Three `related-to` edges connect this audit to the earlier audit and to both trials. The most useful traversal is to the trial that measured task time in mature repositories:[^metr-rct] the two findings are complementary rather than conflicting, since one measures how long a task took and the other whether the resulting change would have survived review, and a reader assembling an argument about AI's effect on delivery needs both and should not merge them into one claim.

## What is not established

* **The number of pull requests examined**, left `null` rather than inferred.
* **A confidence interval or spread around the roughly half figure.**
* **How much of the gap a revision loop would close**, which would require giving agents the feedback a human developer gets, and which no source in this batch reports having tried.
* **Whether maintainer disagreement is itself a reliable instrument.** The audit adjusts for noise in maintainer decisions; the size of that adjustment is not stated in the summary retrieved.

[^metr-merge]: org:metr (Parker Whitfill, Cheryl Wu, Joel Becker, Nate Rush), "Many SWE-bench-Passing PRs Would Not Be Merged into Main", 2026-03-10, https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/
[^metr-holistic]: org:metr (David Rein), "Research Update: Algorithmic vs. Holistic Evaluation", 2025-08-13, https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/
[^metr-rct]: org:metr, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity" (paper at arXiv:2507.09089), https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
