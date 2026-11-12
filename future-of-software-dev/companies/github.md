---
type: Company
title: GitHub
description: Code-hosting platform and Microsoft subsidiary, and the single largest distributor of AI coding assistance, whose published Copilot research supplies the most-quoted productivity figures in the field.
resource: https://github.com
tags:
  - code-hosting
  - developer-platform
  - ai-coding
  - copilot
  - microsoft-subsidiary
  - us
aliases:
  - GitHub, Inc.
  - GitHub Inc
founded: null
hq: San Francisco, California, US
parent: Microsoft
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-11T00:00:00Z
stale_after: 2026-12-10T00:00:00Z
relations:
  - { type: subsidiary-of, target: /companies/microsoft.md, since: 2018-06-04, amount_usd: 7500000000, note: "announced price, not the completed figure" }
  - { type: uses, target: /technologies/copilot.md, since: 2021-06, note: "technical preview, per the 2022 research post" }
  - { type: contradicted-by, target: /evidence/os-developer-productivity-rct.md, note: "the vendor figure measures one greenfield task; the independent trial measures 246 tasks in mature repositories and finds the opposite sign" }
sources:
  - id: gh-about
    resource: "https://github.com/about"
    title: "About GitHub"
    author: "org:github"
  - id: msft-gh
    resource: "https://news.microsoft.com/2018/06/04/microsoft-to-acquire-github-for-7-5-billion/"
    title: "Microsoft to acquire GitHub for $7.5 billion"
    author: "org:microsoft"
  - id: gh-2022
    resource: "https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/"
    title: "Research: quantifying GitHub Copilot's impact on developer productivity and happiness"
    author: "org:github (Eirini Kalliamvakou)"
  - id: gh-2024
    resource: "https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-in-the-enterprise-with-accenture/"
    title: "Research: Quantifying GitHub Copilot's impact in the enterprise with Accenture"
    author: "org:github (Ya Gao, GitHub Customer Research)"
  - id: peng
    resource: "https://arxiv.org/abs/2302.06590"
    title: "Peng, Kalliamvakou, Cihon and Demirer, 'The Impact of AI on Developer Productivity: Evidence from GitHub Copilot', arXiv:2302.06590"
    author: "human:sida-peng"
  - id: octoverse
    resource: "https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/"
    title: "Octoverse: A new developer joins GitHub every second as AI leads TypeScript to #1"
    author: "org:github"
---

# GitHub

## Snapshot

GitHub hosts code for 225M+ developers, 4M+ organisations and 800M+ repositories, and reports that 90% of the Fortune 100 use it.[^gh-about] It has been a Microsoft subsidiary since 2018, when Microsoft announced it would acquire the company for $7.5 billion.[^msft-gh] Its relevance to this bundle is not code hosting but distribution: Copilot put AI code completion in front of more developers than any other single product, and the research GitHub published around it supplies the figures most often quoted on both sides of the productivity argument.

## Founding and lineage

Not established in this batch. GitHub's own About page gives current scale but no founding date, and no source retrieved here states one; the field is left `null` rather than filled from memory.

Ownership is dated: Microsoft's announcement of 2018-06-04 gives $7.5 billion as the price.[^msft-gh] That announcement is the only ownership source in this batch, and it records the deal's announcement rather than its close.

## What the sources show

Two vintages of vendor research, five years apart:

* 2022-09-07. GitHub Next published a combination of surveys and experiments, concluding that Copilot helped developers "code up to 55% faster" and that 85% of developers felt more confident in their code quality.[^gh-2022] The post is authored by a GitHub researcher and the studies are GitHub's own.
* 2024-05-13. A follow-up study with Accenture, framed for enterprise buyers rather than for the research literature, re-states the 55% figure alongside the 85% confidence figure as established results.[^gh-2024]
* The academic form of the same claim is Peng et al. (2023): a controlled experiment in which developers with Copilot completed one task — implementing an HTTP server in JavaScript — 55.8% faster than the control group.[^peng]

The Octoverse telemetry series is a different kind of artefact: platform measurements rather than an experiment. The 2025 edition reports that TypeScript overtook both Python and JavaScript in August 2025 to become the most-used language on GitHub, and attributes the shift to developers preferring typed languages that "make agent-assisted coding more reliable in production".[^octoverse] The same release dates the Copilot coding agent preview to March 2025 and reports contributions splitting between AI infrastructure projects and older, unrelated ecosystems.[^octoverse]

## What it says about the SDLC

The product direction is legible from the dated surface rather than from any prediction: a 2021 completion tool, a March 2025 coding agent, and code review in the same year.[^gh-2022][^octoverse] That is the same arc the rest of this corpus records — completion, then suggestion, then delegated task — arriving at the largest distribution point in the industry.

GitHub's framing of the TypeScript result is worth separating from the result itself. The measurement is a language ranking; the causal claim about agent-assisted coding being more reliable in typed languages is GitHub's interpretation of its own data, and no source in this batch tests it.[^octoverse]

## Evidence it has produced

* The Copilot task experiment, recorded separately so it can be weighed against independent work: [The Copilot task-completion experiment](/evidence/copilot-task-completion-rct.md).
* The Octoverse series, which is telemetry rather than an experiment and is not comparable to a trial.

## Relations

`subsidiary-of` points at `/companies/microsoft.md`, a concept that does not exist yet; under OKF §6.1 the link is legal and the checker reports it as a pending target. `uses` points at `/technologies/copilot.md`, likewise unwritten. `contradicted-by` points at the independent trial in `evidence/`, and that concept carries the `contradicts` mirror, so the disagreement is a traversable edge rather than a sentence in a footnote — which is what lets a reader reach both sides from either file.

## Commercials

Not established in this batch. No pricing, seat count or revenue figure was retrieved, and none is guessed.

## What is not established

* **Founding date and founders.** `founded` is `null` for the reason given above.
* **Whether the Accenture study is independent.** It is published on GitHub's blog by GitHub's customer research function and describes a partnership with the named customer. Nothing retrieved here states who designed the measurement, so the file does not claim either way.
* **Any replication of the 55% figure on production codebases.** The 2023 experiment's task was a single greenfield implementation, and both vendor posts repeat the figure without revisiting that setting.[^peng][^gh-2024]
* **The completion date of the Microsoft acquisition**, as distinct from its announcement.

## Disputed and unverified

The 55% figure is the single most-quoted number in this field and it originates with the vendor that sells the tool. That is a reason to weigh it, not a reason to dismiss it, and this corpus does not resolve the question by authority in either direction: the measurement stands as a measurement, its setting is recorded, and the opposing measurement from an independent trial is one edge away. The disagreement itself is carried by the `contradicts` edge and is not restated here.

[^gh-about]: org:github, "About GitHub", https://github.com/about
[^msft-gh]: org:microsoft, "Microsoft to acquire GitHub for $7.5 billion", https://news.microsoft.com/2018/06/04/microsoft-to-acquire-github-for-7-5-billion/
[^gh-2022]: org:github (Eirini Kalliamvakou), "Research: quantifying GitHub Copilot's impact on developer productivity and happiness", https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/
[^gh-2024]: org:github (Ya Gao, GitHub Customer Research), "Research: Quantifying GitHub Copilot's impact in the enterprise with Accenture", https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-in-the-enterprise-with-accenture/
[^peng]: human:sida-peng, "Peng, Kalliamvakou, Cihon and Demirer, 'The Impact of AI on Developer Productivity: Evidence from GitHub Copilot', arXiv:2302.06590", https://arxiv.org/abs/2302.06590
[^octoverse]: org:github, "Octoverse: A new developer joins GitHub every second as AI leads TypeScript to #1", https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/
