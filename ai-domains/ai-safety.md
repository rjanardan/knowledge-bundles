---
type: Domain
title: AI safety
description: The interdisciplinary field concerned with preventing accidents, misuse and other harmful consequences from AI systems, and the domain the four frontier labs in this bundle are all recorded as operating in.
resource: https://en.wikipedia.org/wiki/AI_safety
tags:
  - ai-safety
  - alignment
  - existential-risk
  - governance
aliases:
  - AI safety
  - AI alignment (as a sub-field)
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-15T10:29:00Z
stale_after: 2027-09-15T00:00:00Z
relations:
  - { type: related-to, target: /ai-domains/agi.md }
  - { type: related-to, target: /ai-domains/foundation-models.md }
  - { type: related-to, target: /ai-domains/interpretability.md }
  - { type: related-to, target: /ai-domains/agentic-ai.md }
sources:
  - id: wiki-aisafety
    resource: https://en.wikipedia.org/wiki/AI_safety
    title: "AI safety"
    author: "wiki:en"
  - id: wiki-agi
    resource: https://en.wikipedia.org/wiki/Artificial_general_intelligence
    title: "Artificial general intelligence"
    author: "wiki:en"
---

# AI safety

## Definition

AI safety is an interdisciplinary field focused on preventing accidents, misuse or other harmful consequences arising from AI systems. It encompasses AI alignment (ensuring systems behave as intended), monitoring systems for risks, and enhancing robustness, and is particularly concerned with the existential risks posed by advanced AI models. Beyond technical research it involves norms and policy, including advocacy for regulation at different levels of government.[^wiki-aisafety]

## Who is recorded as operating here

This is the domain that already had four `operates-in` edges into it before this file was written — Anthropic, Google DeepMind, OpenAI and SSI all point here. That is the single most concentrated corner of the corpus, and it is why this file was the highest-inbound pending domain: the bundle already claimed all four labs operate here, and the file now makes that claim legible and cited rather than a dangling target.

The relationship to `/ai-domains/agi.md` is the load-bearing one: AI safety is where the existential-risk debate about AGI lands as a technical and governance programme.

## The empirical structure of the debate

The sources give a concrete, surveyable picture of how seriously experts take the risk, and this file records the numbers rather than the slogans:

| Signal | Value | Source |
| --- | --- | --- |
| Expert median on "extremely bad" (e.g. human extinction) outcome | 5% probability | [^wiki-aisafety] |
| NLP community, 2022 survey | 37% agreed or weakly agreed a catastrophe at least as bad as nuclear war is plausible | [^wiki-aisafety] |
| Open letter on AI societal impacts | signed by 8,000+ incl. LeCun, Legg, Bengio, Russell | [^wiki-aisafety] |

The counter-position is recorded too: Andrew Ng's 2015 comparison of AGI concern to "worrying about overpopulation on Mars when we have not even set foot on the planet yet", against Stuart Russell's urging to "anticipate human ingenuity rather than underestimate it".[^wiki-aisafety]

## The governance record

The field produced a concrete governance timeline, which this file records as the domain's institutional footprint: the 2016 White House/CMU workshop, the 2017 Asilomar principles (including the race-avoidance norm), the 2023 UK AI Safety Summit and the US/UK AI Safety Institutes, the April 2024 US–UK partnership, and the first International AI Safety Report (2025), chaired by Yoshua Bengio and commissioned by 30 nations and the UN.[^wiki-aisafety]

## Why the frontier labs are here

The companies recorded as operating here are the frontier labs. The connection to the rest of the corpus is structural: `foundation-models` is the capability, `agentic-ai` is the deployment, and `ai-safety` is the risk domain all four labs explicitly claim. A consumer reading "which domains do these companies share" now gets a four-node `ai-safety` cluster as the answer.

## Disputed and unverified

1. **Severity disagreement is intrinsic.** The 5%-median and the 37%-catastrophe figures come from surveys with different populations and dates; they are recorded as survey results, not as settled probabilities.[^wiki-aisafety]
2. **Whether safety measures are keeping pace with capability** is contested — researchers have expressed concern that they are not; the sources record the concern rather than resolve it.[^wiki-aisafety]
3. **The AGI existential-risk framing** is one of the two poles recorded in `/ai-domains/agi.md`; this file inherits that unresolved debate rather than settling it.

[^wiki-aisafety]: Wikipedia, "AI safety", https://en.wikipedia.org/wiki/AI_safety
[^wiki-agi]: Wikipedia, "Artificial general intelligence", https://en.wikipedia.org/wiki/Artificial_general_intelligence