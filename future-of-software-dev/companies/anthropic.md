---
type: Company
title: Anthropic
description: AI developer and safety lab, maker of Claude and Claude Code, and the only vendor in this batch publishing a longitudinal study of how AI changed work inside its own engineering organisation.
resource: https://www.anthropic.com
tags:
  - frontier-lab
  - ai-coding
  - coding-agents
  - economic-research
  - us
aliases:
  - Anthropic PBC
founded: null
hq: San Francisco, California, US
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-11T00:00:00Z
stale_after: 2026-12-10T00:00:00Z
relations:
  - { type: produced, target: /technologies/claude-code.md, note: "a coding agent shipped across terminal, IDE, web and mobile surfaces" }
sources:
  - id: anth-cc
    resource: "https://www.anthropic.com/claude-code"
    title: "Claude Code"
    author: "org:anthropic"
  - id: anth-work
    resource: "https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic"
    title: "How AI is transforming work at Anthropic"
    author: "org:anthropic"
  - id: anth-index
    resource: "https://www.anthropic.com/news/the-anthropic-economic-index"
    title: "Introducing the Anthropic Economic Index"
    author: "org:anthropic"
    note: "(initial report at arXiv:2503.04761)"
---

# Anthropic

## Snapshot

Anthropic builds the Claude model family and sells a coding agent, Claude Code, that runs in a terminal, an IDE, the web and mobile, and integrates with GitHub.[^anth-cc] Two of its publications matter to this bundle for a reason that is unusual among vendors: one measures AI's effect on work using its own 132 engineers as subjects, and the other quantifies which occupations use AI by analysing real production traffic rather than asking people what they think.[^anth-work][^anth-index] Both are vendor-controlled, which the sources themselves acknowledge rather than conceal.

## Founding and lineage

Not established in this batch. No source retrieved here states Anthropic's founding date or founders, so the field is `null`. The gap is noted rather than filled, and the concept is a pending target for the batch that adds the company's own history.

## What the sources show

**On its own workforce.** In August 2025 Anthropic surveyed 132 of its engineers and researchers, conducted 53 in-depth qualitative interviews, and analysed internal Claude Code transcripts.[^anth-work] It reports engineers getting more done, becoming more "full-stack", accelerating learning and iteration, and picking up previously-neglected work. The task mix moved measurably between February and August 2025 across 200,000 internal transcripts: implementing new features rose from 14.3% of transcripts to 36.9%, and code design or planning from 1.0% to 9.9%, while average task complexity and consecutive tool calls per transcript rose and human turns fell.[^anth-work]

The paper states its own limitation directly: studying AI's impact at a company building AI "means representing a privileged position", because those engineers have early access to frontier tools, work in a stable field, and are themselves contributing to the transformation they are measuring.[^anth-work] It also cites the independent METR trial against its own findings, noting that experienced developers working with AI on familiar codebases overestimated their productivity gain.[^anth-work] A vendor citing the result that contradicts its interest is rare enough in this corpus to be worth recording as a fact about the source.

**On the labour market.** The Anthropic Economic Index, launched 2025-02-10, analyses millions of anonymised Claude.ai conversations and open-sources the dataset.[^anth-index] Its first report found that over one-third of occupations (roughly 36%) show AI use in at least a quarter of their associated tasks, while about 4% of occupations use it across three-quarters of their tasks; that use leans toward augmentation (57%) rather than automation (43%); and that use is concentrated in mid-to-high-wage occupations such as computer programmers and data scientists, and is lower at both extremes of the pay distribution.[^anth-index] The report's own headline finding is also the most relevant one here: "Today, usage is concentrated in software development and technical writing tasks."[^anth-index]

## What it says about the SDLC

The work-transformation study describes a shift in what the job is rather than only how fast it goes: engineers "shifting toward higher-level work managing AI systems", with the study explicitly raising the question of the long-term trajectory of software engineering as a profession.[^anth-work] The transcript analysis is the concrete version of that claim — new-feature implementation nearly tripling as a share of agent sessions, planning appearing where it had barely registered, and fewer human turns per session.[^anth-work]

That is a claim about task composition measured before and after, not a controlled comparison, and the concept records it as such. The Economic Index is the complementary measurement at population scale: if software development is where AI usage concentrates, then findings about developer roles are also findings about where AI has penetrated furthest, which is why a corpus on developer roles depends on this source.[^anth-index]

## Evidence it has produced

Two sources sit near the `evidence/` boundary and are deliberately kept here rather than there, for now:

* **The work-transformation study.** It has a sample, a method and a date, but no control group and a self-selected population of early-access engineers, so it measures its own organisation rather than an effect on the field.[^anth-work]
* **The Economic Index.** Vendor telemetry with an open dataset, which is a strong shape for a study, but it measures Claude.ai usage and not the labour market.[^anth-index]

Both are candidates for `evidence/` concepts once the batch that builds out that shard can give them the `method`, `n` and `effect_ci` shape the conventions require. Recording them here first, with their limitations stated, is the honest interim state rather than a promotion on the strength of the publisher's name.

## Relations

`produced` points at `/technologies/claude-code.md`, which does not exist yet; the checker reports it as a pending target and the eventual concept will carry the `produced-by` mirror.

## Commercials

Not established in this batch. No pricing or revenue figure was retrieved.

## What is not established

* **Founding date, founders and legal form.** `founded` is `null`.
* **The launch date of Claude Code**, as distinct from its 2026 product surface. The page retrieved describes current availability across terminal, IDE, web, Slack, iOS and Android,[^anth-cc] and no retrieved source dates the first release.
* **Whether the internal transcript analysis was reviewed outside Anthropic.** The study describes its method and its limitations but the sources do not record an external review, so this file does not claim one.
* **Model versions in current use.** The study names the models available at data collection;[^anth-work] that is a 2025 fact and is not extended forward here.

## Disputed and unverified

Nothing in this batch disputes Anthropic's own reporting of its internals, and no second source for those internals exists. The study's self-described privileged position is recorded above as a limitation the source states, not as a defect the corpus found. The one overlap with an independent result — that developers overestimate their own AI speed-up — is recorded in `evidence/`, and Anthropic's own citation of it is the reason the two are linked rather than the corpus adjudicating between them.

[^anth-cc]: org:anthropic, "Claude Code", https://www.anthropic.com/claude-code
[^anth-work]: org:anthropic, "How AI is transforming work at Anthropic", https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
[^anth-index]: org:anthropic, "Introducing the Anthropic Economic Index" (initial report at arXiv:2503.04761), https://www.anthropic.com/news/the-anthropic-economic-index
