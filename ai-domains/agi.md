---
type: Domain
title: AGI
description: Artificial general intelligence - a hypothetical system that matches or surpasses human capability across virtually all cognitive tasks, distinct from narrow AI; the stated goal of the frontier labs in this bundle.
resource: https://en.wikipedia.org/wiki/Artificial_general_intelligence
tags:
  - agi
  - frontier-goal
  - long-horizon
  - existential-risk
aliases:
  - Artificial general intelligence
  - Strong AI
  - Human-level AI
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-15T10:28:00Z
stale_after: 2027-09-15T00:00:00Z
relations:
  - { type: related-to, target: /ai-domains/foundation-models.md }
  - { type: related-to, target: /ai-domains/ai-safety.md }
  - { type: related-to, target: /ai-domains/agentic-ai.md }
  - { type: related-to, target: /ai-domains/llms.md }
sources:
  - id: wiki-agi
    resource: https://en.wikipedia.org/wiki/Artificial_general_intelligence
    title: "Artificial general intelligence"
    author: "wiki:en"
---

# AGI

## Definition and boundary

AGI is a hypothetical form of AI that matches or surpasses human capability across virtually all cognitive tasks, in contrast to artificial narrow intelligence (ANI), whose competence is confined to well-defined tasks. An AGI system would generalise knowledge, transfer skills between domains and solve novel problems without task-specific reprogramming.[^wiki-agi] Creating AGI is a stated goal of OpenAI, Google, SpaceXAI and Meta.[^wiki-agi]

The term has a precise lineage: "artificial general intelligence" was used in 1997 by Mark Gubrud; a mathematical formalism (AIXI) followed in 2000 from Marcus Hutter; and the acronym was popularised by Shane Legg and Ben Goertzel around 2002.[^wiki-agi]

## Why it matters to this bundle

AGI is the stated destination of the frontier labs this corpus covers, and it is the conceptual anchor for two other domains here: `foundation-models` (the scaling path to it) and `ai-safety` (the risk it concentrates). The DeepMind classification framework (2023) gives five performance levels — emerging, competent, expert, virtuoso, superhuman — and a "competent" AGI outperforms 50% of skilled adults on a task.[^wiki-agi]

## Tests and their contested status

| Test | What it claims to show | Note | Source |
| --- | --- | --- | --- |
| Turing test | Machine can be taken for human | A 2025 pre-registered three-party study by Jones and Bergen judged GPT-4.5 human in 73% of five-minute text conversations, surpassing the 67% rate of real confederates | [^wiki-agi] |
| Ikea test | Physical assembly from raw parts | MIT's 2013 IkeaBot assembled an IKEA Lack table in ten minutes with no human intervention | [^wiki-agi] |
| Coffee test | Operate in an ordinary home | Proposed by Steve Wozniak; a machine must enter a home and make coffee | [^wiki-agi] |

Each test is contested: passing a Turing-test-like protocol is not accepted as evidence of the internal state the term "general" implies, and the sources treat the 2014 Eugene Goostman claim with open scepticism.[^wiki-agi]

## The existential-risk debate

Contention over whether AGI is an existential risk is the load-bearing tension of this domain. Some AI experts and industry figures state that mitigating the risk of extinction posed by AGI should be a global priority; others argue AGI is too remote a stage for the risk to be present. The bundle records both sides and does not adjudicate them — this is exactly the kind of disagreement it files under "recorded, not resolved."[^wiki-agi]

## Who is recorded as operating here

The companies already in this bundle that the sources place in this domain are the ones that also operate in `foundation-models` and `agentic-ai`: OpenAI (whose founding charter names AGI as its mission), Google DeepMind, and (by the `related-to` edge) the labs whose stated goal is AGI. No company in this bundle has an explicit `operates-in: agi` edge yet, because none of the sources read states "AGI" as the company's formal operating domain — the charter-level goal is recorded here and in the company files, not promoted to an edge.

## Disputed and unverified

1. **Whether AGI is a realisable goal or a rhetorical one.** The sources record both the research programmes pursuing it (72 active AGI projects across 37 countries as of a 2020 survey) and the criticism that the term is used to bundle ambitions rather than a defined target.[^wiki-agi]
2. **Test validity.** No test in this file is accepted by the research community as definitive evidence of general intelligence; each is recorded with its status.
3. **The boundary with "narrow" frontier models.** Modern large language models demonstrate computational creativity, automated reasoning and decision support across domains, which blurs the ANI/AGI line without resolving it.[^wiki-agi]

[^wiki-agi]: Wikipedia, "Artificial general intelligence", https://en.wikipedia.org/wiki/Artificial_general_intelligence