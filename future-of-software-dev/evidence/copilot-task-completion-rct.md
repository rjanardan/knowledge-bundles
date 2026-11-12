---
type: Study
title: The Copilot task-completion experiment
description: Controlled experiment in which developers given GitHub Copilot completed a single greenfield HTTP-server task 55.8% faster, and the academic form of the vendor figure that rounds to 55%.
resource: https://arxiv.org/abs/2302.06590
tags:
  - rct
  - controlled-experiment
  - copilot
  - task-completion
  - greenfield-task
method: lab-experiment
n: null
population: "Recruited software developers; task was to implement an HTTP server in JavaScript as quickly as possible"
effect: "+55.8% task completion speed"
effect_ci: null
measured_at: "2023 (submission 2023-02-13; fieldwork date not stated in the abstract)"
pre_registered: null
aliases:
  - Peng et al. 2023
  - The Impact of AI on Developer Productivity
  - Copilot 55% study
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-11T00:00:00Z
stale_after: 2027-09-11T00:00:00Z
relations:
  - { type: contradicts, target: /evidence/os-developer-productivity-rct.md, note: "opposite sign on a comparable question; the difference is the setting, a single greenfield task versus 246 tasks in repositories the developers already knew" }
  - { type: related-to, target: /evidence/algorithmic-scoring-overstates-usability.md }
  - { type: related-to, target: /evidence/swe-bench-merge-audit.md }
sources:
  - id: peng
    resource: "https://arxiv.org/abs/2302.06590"
    title: "Peng, Kalliamvakou, Cihon and Demirer, 'The Impact of AI on Developer Productivity: Evidence from GitHub Copilot', arXiv:2302.06590"
    author: "human:sida-peng"
  - id: gh-2022
    resource: "https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/"
    title: "Research: quantifying GitHub Copilot's impact on developer productivity and happiness"
    author: "org:github (Eirini Kalliamvakou)"
  - id: gh-2024
    resource: "https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-in-the-enterprise-with-accenture/"
    title: "Research: Quantifying GitHub Copilot's impact in the enterprise with Accenture"
    author: "org:github (Ya Gao, GitHub Customer Research)"
  - id: metr-rct
    resource: "https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/"
    title: "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity"
    author: "org:metr"
---

# The Copilot task-completion experiment

## Snapshot

Peng and colleagues ran a controlled experiment in which recruited developers implemented an HTTP server in JavaScript, with a treatment group given access to GitHub Copilot and a control group without it.[^peng] The treatment group completed the task 55.8% faster.[^peng] This is the academic form of the figure that the vendor's own blog rounds to "up to 55% faster",[^gh-2022] and it is the measurement most often cited for AI coding assistance being a large net speed-up.

## Method

A controlled experiment with a treatment group and a control group, on one specified task: implement an HTTP server in JavaScript as quickly as possible.[^peng] Developers were recruited for the experiment rather than observed in their own repositories, and the task was implemented from scratch.

The abstract does not state the number of participants, and `n` is therefore `null` here rather than inferred from the count of authors, the size of the effect, or a later retelling. No confidence interval appears in the abstract either, so `effect_ci` is `null` for the same reason.[^peng]

## Result

The treatment group completed the task 55.8% faster than the control group.[^peng] The authors report heterogeneous effects and argue these "show promise for AI pair programmers to help people transition into software development careers", which is a claim about who benefits rather than about average magnitude.[^peng]

The vendor's 2022 write-up of related work reports the same finding as "up to 55% faster" alongside a second result: that 85% of developers felt more confident in their code quality.[^gh-2022] The confidence figure is a self-report and is not commensurable with the speed figure, and the two are kept distinct here for that reason. A 2024 vendor post aimed at enterprise buyers re-states both in the same sentence without revisiting the setting.[^gh-2024]

## What it does not show

Three limits matter, and a bare percentage cannot carry any of them:

* **It does not measure work in a codebase the developer already knows.** The task is greenfield. The independent trial in this shard runs the mirror experiment — mature repositories the developers had worked in for an average of five years — and finds the opposite direction.[^metr-rct]
* **It does not measure review, integration or maintenance.** The measured quantity is time to a working implementation, and no later phase of the lifecycle is observed.
* **It does not establish that the speed-up persists at scale.** One task, once, in a laboratory setting, is a measurement of that task.

The single-task design is not a flaw in the study; it is the setting the study describes, and recording it is what allows a reader to compare this result with one from a different setting instead of treating both as estimates of one quantity.

## Follow-ups

A vendor enterprise study in 2024 restated the figures for buyers.[^gh-2024] No replication on production codebases, and no re-run of this experiment with agentic tools rather than a completion tool, was found in this batch.

## Relations

`contradicts` points at the independent trial, and that concept carries the `contradicted-by` mirror, so the two measurements sit one hop apart and both are retained. `related-to` links the two benchmark-validity audits, which attack a different apparatus — how agent benchmark scores are computed and whether they predict mergeability — and are linked rather than set in conflict, because they do not measure task time.

## What is not established

* **The number of participants**, and the confidence interval: neither is stated in the abstract, and both are left `null`.
* **When the fieldwork was done**, as distinct from the 2023-02-13 submission date.
* **Who funded the study and whether it was externally reviewed.** All four authors are employed by, or affiliated with, the vendor whose product is measured, which the `author` namespace records. The sources retrieved state no funding disclosure or review status, and this concept does not assume either.

[^peng]: human:sida-peng, "Peng, Kalliamvakou, Cihon and Demirer, 'The Impact of AI on Developer Productivity: Evidence from GitHub Copilot', arXiv:2302.06590", https://arxiv.org/abs/2302.06590
[^gh-2022]: org:github (Eirini Kalliamvakou), "Research: quantifying GitHub Copilot's impact on developer productivity and happiness", https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/
[^gh-2024]: org:github (Ya Gao, GitHub Customer Research), "Research: Quantifying GitHub Copilot's impact in the enterprise with Accenture", https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-in-the-enterprise-with-accenture/
[^metr-rct]: org:metr, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
