---
type: Study
title: The METR open-source developer productivity trial
description: Randomised controlled trial in which experienced open-source developers took 19% longer with AI tools across 246 tasks in their own mature repositories, and a 2026 follow-up that found the trial design itself had stopped producing a usable signal.
resource: https://arxiv.org/abs/2507.09089
tags:
  - rct
  - productivity
  - agentic-coding
  - selection-effects
  - measurement-validity
method: rct
n: 16
population: "16 developers with moderate AI experience in mature projects where they averaged 5 years of prior experience; 246 tasks, each randomised to AI-allowed or AI-disallowed"
effect: "+19% task time (slower with AI)"
effect_ci: "+2% to +39%"
measured_at: "2025-02 to 2025-06"
pre_registered: true
aliases:
  - METR slowdown study
  - Measuring the Impact of Early-2025 AI
  - The METR RCT
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-11T00:00:00Z
stale_after: 2027-09-11T00:00:00Z
relations:
  - { type: contradicted-by, target: /evidence/copilot-task-completion-rct.md, note: "opposite sign on a comparable question; the difference is the setting, one greenfield task versus 246 tasks in familiar repositories" }
  - { type: contradicts, target: /companies/github.md, note: "the vendor's headline speed-up is contradicted by an independent trial on tasks in mature repositories" }
  - { type: related-to, target: /evidence/algorithmic-scoring-overstates-usability.md }
  - { type: related-to, target: /evidence/swe-bench-merge-audit.md }
sources:
  - id: metr-rct
    resource: "https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/"
    title: "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity"
    author: "org:metr"
    note: "(paper at arXiv:2507.09089)"
  - id: metr-update
    resource: "https://metr.org/blog/2026-02-24-uplift-update/"
    title: "We are Changing our Developer Productivity Experiment Design"
    author: "org:metr (Joel Becker, Nate Rush, Tom Cunningham, David Rein, Khalid Mahamud)"
    note: "2026-02-24"
  - id: peng
    resource: "https://arxiv.org/abs/2302.06590"
    title: "Peng, Kalliamvakou, Cihon and Demirer, 'The Impact of AI on Developer Productivity: Evidence from GitHub Copilot', arXiv:2302.06590"
    author: "human:sida-peng"
---

# The METR open-source developer productivity trial

## Snapshot

METR ran a randomised controlled trial with 16 experienced open-source developers working in their own repositories, and found that when AI tools were allowed the tasks took 19% longer than when they were disallowed.[^metr-rct] The result's significance is less in its direction than in its setting: mature projects, developers averaging five years of prior experience in those projects, and 246 tasks randomly assigned within developer and repository.[^metr-rct] It is the strongest available counterweight to the vendor task-completion experiment, and its own authors later reported that the design had stopped producing a usable signal.[^metr-update]

## Method

A randomised controlled trial. Sixteen developers with moderate AI experience completed 246 tasks in mature projects where they averaged five years of prior experience; each task was randomly assigned to an "AI allowed" or an "AI disallowed" condition.[^metr-rct] In the AI-allowed condition developers primarily used Cursor Pro and Claude 3.5/3.7 Sonnet.[^metr-rct] Before starting each task, developers forecast that allowing AI would reduce completion time by 24%.[^metr-rct]

Randomisation within developer and within repository is what makes the result informative: it removes the selection that makes observational comparisons of AI adoption unusable, since the developers who adopt earliest are not a random sample of developers. The authors additionally collected and evaluated evidence for 20 properties of the setting that could a priori have contributed to the slowdown, including the size and quality standards of the projects and prior developer experience.[^metr-rct]

`n` here is 16 developers; the 246 tasks are the unit of analysis. Both are recorded because either alone is misleading — a reader who takes `n: 16` as the whole sample would understate the evidence, and one who takes 246 as the sample size would overstate its independence.[^metr-rct]

## Result

Tasks took 19% longer with AI tools allowed than without, with a confidence interval of +2% to +39%.[^metr-update] The developers expected a 24% reduction.[^metr-rct] The gap between the forecast and the outcome is therefore not a disagreement about magnitude but a difference in sign: the people best placed to judge were confident of a speed-up and experienced a slowdown.

The interval is wide, and its lower bound of +2% is why this concept records `effect` and `effect_ci` as strings rather than a point estimate. The trial establishes a slowdown; it cannot pin the magnitude, and a corpus that stored only "19%" would imply a precision the interval does not support.[^metr-update]

## What it does not show

* **It is not a statement about later tools.** The trial measures the February–June 2025 frontier. METR frames the result as "a snapshot of early-2025 AI capabilities in one relevant setting" and plans to repeat the method as the systems change.[^metr-rct]
* **It does not generalise beyond experienced developers in familiar repositories.** The population is deliberately experts in their own code; a task-time result there does not transfer to a newcomer, and does not transfer to greenfield work, which is the setting of the experiment it contradicts.[^peng]
* **It does not establish that the developers were worse off.** Time and value are different quantities, and slower completion of a task can coexist with a better outcome, a point the follow-up raises when it notes that developers leaned on AI's strengths and thereby changed which tasks they attempted.[^metr-update]
* **It does not measure delivered value, only recorded task time**, and the follow-up itself questions the reliability of that measurement for developers running several agents at once.[^metr-update]

## Follow-ups

The follow-up is the most important entry in this concept, because what failed is the measurement rather than the result. A second experiment began in August 2025 with 10 returning developers and 47 newly recruited ones, at $50/hour rather than the original $150/hour.[^metr-update] METR concluded the data "gives us an unreliable signal of the current productivity effect of AI tools", for three stated reasons: a significant increase in developers declining to participate because they did not wish to work without AI, which biases the estimate downward; selection effects from the lower pay rate; and unreliable time measurement for developers running multiple agents concurrently.[^metr-update] Between 30% and 50% of developers reported withholding tasks they did not want to do without AI.[^metr-update]

The raw numbers moved direction. For the subset of the original developers the estimate became a speed-up of 18%, interval -38% to +9%; among newly recruited developers it was a speed-up of 4%, interval -15% to +9%.[^metr-update] METR's own reading is that developers are "likely" more sped up in early 2026 than in early 2025, while describing its data as "only very weak evidence for the size of this increase".[^metr-update] Both intervals cross zero, which is the honest summary: after the design change the follow-up cannot distinguish the two directions.

The generalisable finding, and the reason this concept anchors the corpus, is that **the counterfactual decayed**. Once enough developers decline to work without AI, the AI-disallowed arm stops being comparable to normal work, and a randomised trial of AI's effect on developers becomes harder to run exactly when it becomes most interesting to run.[^metr-update] That is a property of the field in 2026 and not of any one tool, and it constrains what any subsequent study in this shard can claim.

## Relations

This concept carries both of the corpus's `contradicts` edges in one file. It is `contradicted-by` the vendor task-completion experiment, and it `contradicts` the company that published it, with each counterpart written as the correct mirror on the other side. `related-to` links the two benchmark-validity audits, which examine the scoring apparatus used to claim agent capability rather than task time.

## What is not established

* **The true speed-up in early 2026.** METR states its own follow-up is unreliable and biased downward, and this corpus does not substitute a better number in its place. The null result is recorded as a null result.
* **Whether the slowdown holds for less experienced developers.** The population excludes them by construction, and no source in this batch tests that group.
* **The magnitude, as distinct from the direction, of the 2025 result.** The interval spans a factor of roughly twenty between its bounds.[^metr-update]
* **Any current estimate the authors stand behind.** As of this batch there is none.[^metr-update]

[^metr-rct]: org:metr, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity" (paper at arXiv:2507.09089), https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
[^metr-update]: org:metr (Joel Becker, Nate Rush, Tom Cunningham, David Rein, Khalid Mahamud), "We are Changing our Developer Productivity Experiment Design", 2026-02-24, https://metr.org/blog/2026-02-24-uplift-update/
[^peng]: human:sida-peng, "Peng, Kalliamvakou, Cihon and Demirer, 'The Impact of AI on Developer Productivity: Evidence from GitHub Copilot', arXiv:2302.06590", https://arxiv.org/abs/2302.06590
