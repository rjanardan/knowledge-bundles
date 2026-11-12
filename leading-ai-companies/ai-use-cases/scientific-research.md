---
type: UseCase
title: Scientific research
description: AI used to advance scientific discovery, analysis and knowledge synthesis - from protein-structure prediction that won a Nobel Prize to research agents that browse the literature autonomously and return citations.
resource: https://en.wikipedia.org/wiki/AlphaFold
tags:
  - scientific-research
  - deep-research
  - knowledge-synthesis
  - discovery
  - literature-search
aliases:
  - Research agents
  - Deep research
  - AI for science
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-15T06:33:00Z
stale_after: 2027-09-15T00:00:00Z
relations:
  - { type: related-to, target: /ai-use-cases/enterprise-knowledge.md }
  - { type: related-to, target: /ai-use-cases/ai-sdlc.md }
  - { type: related-to, target: /ai-domains/foundation-models.md }
sources:
  - id: wiki-alphafold
    resource: https://en.wikipedia.org/wiki/AlphaFold
    title: "AlphaFold"
    author: "wiki:en"
  - id: wiki-deepresearch
    resource: https://en.wikipedia.org/wiki/OpenAI_Deep_Research
    title: "OpenAI Deep Research"
    author: "wiki:en"
  - id: wiki-gemini-drs
    resource: https://en.wikipedia.org/wiki/Gemini_Deep_Research
    title: "Gemini Deep Research"
    author: "wiki:en"
  - id: wiki-chatgpt
    resource: https://en.wikipedia.org/wiki/ChatGPT
    title: "ChatGPT"
    author: "wiki:en"
  - id: openai-deepresearch
    resource: https://openai.com/index/introducing-deep-research/
    title: "OpenAI, Introducing Deep Research"
    author: "org:openai"
---

# Scientific research

## Boundary

This use case covers AI applied to scientific work in two senses: *discovery* — machine-generated artefacts that advance a field, of which AlphaFold's protein-structure prediction is the paradigm case — and *knowledge synthesis* — research agents that autonomously browse the literature and return cited summaries. The two are deliberately held together in one file because the downstream consumer (a scientist deciding whether to trust the output) faces the same question in both: is this a computation that can be reproduced and audited, or is it an autonomously generated text that carries its own uncertainty and may hallucinate?[^wiki-alphafold] [^openai-deepresearch]

## Discovery: AlphaFold as the paradigm

AlphaFold is the clearest measured case of AI-as-discovery in this bundle's scope. Its system for computationally predicting protein structures from amino-acid sequences made the strongest single contribution, and the protein-structure work behind it won the 2024 Nobel Prize in Chemistry.[^wiki-alphafold] The bundle records it as the anchor of this use case because the success criterion is objective (accuracy against experimentally determined structures differs from an LLM quality judgement) and because it informed Google DeepMind's later work.

## Knowledge synthesis: the research agents

The research-agent side arrived through the consumer products:

| Product | Vendor | Notes | Source |
| --- | --- | --- | --- |
| Deep Research | OpenAI | ChatGPT agent that autonomously browses the web for a user-specified topic and returns a cited report; runs on a GPT-5.2-based model since Feb 2026, originally built on a specialized o3 | [^wiki-deepresearch] [^openai-deepresearch] |
| Gemini Deep Research | Google | DeepMind/Google's counterpart, available in Gemini | [^wiki-gemini-drs] |

OpenAI's own documentation for Deep Research cautions that it "occasionally makes factual hallucinations (errors) or incorrect inferences" and "may reference rumors".[^openai-deepresearch] This is the load-bearing honesty point for the whole use case: these agents are fast, plausible and cited, but their uncertainty is exactly what a researcher must not inherit. The Guardian's Andrew Rogoyski warned that users might adopt a deep-research report verbatim without retrospective checking, even though verifying such a report can itself take many hours.[^wiki-deepresearch]

## Why a research agent is not a discovery engine

The bundle deliberately keeps the two halves distinct. A discovery tool (AlphaFold) makes an argument a specialist can check against experimental result. A synthesis agent (Deep Research) produces prose that *reads* authoritative but carries no such audit trail, and OpenAI itself says so.[^openai-deepresearch] The distinction is the most useful thing a consumer of this file can take away: one of these can be evaluated for correctness, the other only for citation discipline and uncertainty handling.

## Disputed and unverified

1. **Deep Research's reliability.** OpenAI discloses known hallucination and rumor-referencing behaviour; independent, large-scale evaluation was not read for this batch. Treat the cited-reports-on-demand as a fast literature-first-pass generator, not a verified artefact.[^wiki-deepresearch] [^openai-deepresearch]
2. **Benchmark-to-lab transfer.** No source read establishes that agents achieving high scores on research benchmarks speed up real scientific discovery in the field beyond the AlphaFold-style compute-driven case.[^wiki-alphafold] [^wiki-deepresearch]
3. **The discovery/synthesis split is a bundle's own frame**, not a term the sources use; consumers should treat it as a reading lens, not as a fact.

[^wiki-alphafold]: Wikipedia, "AlphaFold", https://en.wikipedia.org/wiki/AlphaFold
[^wiki-deepresearch]: Wikipedia, "OpenAI Deep Research", https://en.wikipedia.org/wiki/OpenAI_Deep_Research
[^wiki-gemini-drs]: Wikipedia, "Gemini Deep Research", https://en.wikipedia.org/wiki/Gemini_Deep_Research
[^wiki-chatgpt]: Wikipedia, "ChatGPT", https://en.wikipedia.org/wiki/ChatGPT
[^openai-deepresearch]: OpenAI, "Introducing Deep Research", https://openai.com/index/introducing-deep-research/