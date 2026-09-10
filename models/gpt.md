---
type: Model
title: GPT
description: OpenAI's generative pre-trained transformer model family, from GPT-3's 175 billion parameters to the router-based GPT-5 system and the GPT-6 Astra release of September 2026.
resource: https://platform.openai.com/docs/models
tags:
  - llm
  - frontier-models
  - model-family
  - reasoning-models
  - open-weights
aliases:
  - GPT
  - GPT series
  - GPT-6 Astra
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-10T20:05:08Z
stale_after: 2026-12-10T00:00:00Z
relations:
  - { type: developed-by, target: /companies/openai.md, since: 2018-06 }
  - { type: related-to, target: /models/claude.md }
  - { type: related-to, target: /models/gemini.md }
  - { type: related-to, target: /ai-domains/foundation-models.md }
sources:
  - id: wiki-gpt5
    resource: https://en.wikipedia.org/wiki/GPT-5
    title: Wikipedia, "GPT-5"
    author: wiki:en
  - id: wiki-openai
    resource: https://en.wikipedia.org/wiki/OpenAI
    title: Wikipedia, "OpenAI"
    author: wiki:en
  - id: openai-docs
    resource: https://platform.openai.com/docs/models
    title: OpenAI, API documentation and model index
    author: org:openai
  - id: openai-news
    resource: https://openai.com/news/
    title: OpenAI, news index
    author: org:openai
  - id: gpt3
    resource: https://arxiv.org/abs/2005.14165
    title: Brown et al., "Language Models are Few-Shot Learners"
    author: human:brown-et-al
---

# GPT

## What it is

GPT is OpenAI's family of generative pre-trained transformer models and the model line behind ChatGPT. Its published starting point in this bundle's sources is GPT-3, an autoregressive language model with 175 billion parameters - ten times more than any previous non-sparse model - presented as reaching competitive task-agnostic few-shot performance without task-specific fine-tuning.[^gpt3]

## Release lineage

| Model | Released | Note | Source |
| --- | --- | --- | --- |
| GPT-3 | 2020 | 175 billion parameters; few-shot performance from scale | [^gpt3] |
| GPT-4 | 2023-03-14 | Released as an API with a waitlist and as a ChatGPT Plus feature | [^wiki-openai] |
| GPT-4o | not established here | Referenced in the source in comparisons against GPT-5; no release date was read in this batch | [^wiki-gpt5] |
| GPT-4.5 | 2025-02 | The model developed internally as Orion and intended as GPT-5 was released under this name instead, after the effort failed to produce a better model | [^wiki-gpt5] |
| GPT-OSS | 2025-08-05 | Two open-weight models with reasoning capability, released two days before GPT-5 | [^wiki-gpt5] |
| GPT-5 | 2025-08-07 | Unveiled at a livestream event | [^wiki-gpt5] |
| GPT-5.2 | 2025-12-11 | Announced shortly after Google's Gemini 3 release | [^wiki-openai] |
| GPT-5.6 family | 2026 | Terra, Sol, Luna and Cyber appear in the vendor's current model documentation | [^openai-docs] |
| GPT-6 Astra | 2026-09-09 | Announced as "the next generation in intelligence for work" | [^openai-news] |

## How GPT-5 changed the shape of the product

GPT-5 is described as a system rather than a single network: a fast high-throughput model, a deeper reasoning model, and a real-time router that selects between them based on conversation type, complexity, tool needs and explicit user instruction. Smaller variants of the thinking model exist (including a nano version), and the API exposes adjustable reasoning effort at low, medium, high or minimal, plus adjustable verbosity.[^wiki-gpt5]

The router is also the most criticised part of the design. Users reported inconsistent routing, and comparisons with GPT-4o described the older model as more detailed and personable while GPT-5 was more direct and concise.[^wiki-gpt5]

## Current line

The vendor's documentation lists the GPT-5.6 family as Terra, Sol, Luna and Cyber alongside GPT-6 Astra, with the quickstart using Astra, and describes GPT-5.6 Sol as having been used in quantum computing experiments.[^openai-docs] [^openai-news] This file treats the vendor's own model index as authoritative for what is currently served and treats secondary sources as authoritative for history.

## Not disclosed

Parameter counts, mixture-of-experts use, pretraining corpus composition and training compute are not published for any current generation, and this batch found no source that states them. The 175-billion-parameter figure above is citable only because it comes from the GPT-3 paper, which predates the current policy of not disclosing.

## Disputed and unverified

1. **Version naming does not track internal development.** The model intended as GPT-5 was released as GPT-4.5 when it failed to clear the internal bar, which means public version numbers are marketing decisions as much as technical ones.[^wiki-gpt5]
2. **The GPT-5.6 sub-names** (Terra, Sol, Luna, Cyber) are established here from the vendor's own documentation rather than from an announcement page, and the bundle does not yet carry a citation for each variant's release date.
3. **Benchmark comparisons between generations** are not recorded in this file, because the sources read state comparisons qualitatively rather than with numbers.
4. **The router's selection policy is not published**, so routing behaviour cannot be reproduced or audited from outside.[^wiki-gpt5]

[^wiki-gpt5]: Wikipedia, "GPT-5", https://en.wikipedia.org/wiki/GPT-5
[^wiki-openai]: Wikipedia, "OpenAI", https://en.wikipedia.org/wiki/OpenAI
[^openai-docs]: OpenAI, API documentation and model index, https://platform.openai.com/docs/models
[^openai-news]: OpenAI, news index, https://openai.com/news/
[^gpt3]: Brown et al., "Language Models are Few-Shot Learners", https://arxiv.org/abs/2005.14165
