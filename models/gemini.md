---
type: Model
title: Gemini
description: Google DeepMind's multimodal model family, announced in December 2023 as the successor to LaMDA and PaLM 2, released in Pro, Deep Think, Flash and Flash Lite variants, with the open-weight Gemma family as its sibling.
resource: https://deepmind.google/models/
tags:
  - llm
  - frontier-models
  - multimodal
  - model-family
  - open-weights
aliases:
  - Gemini
  - Gemini 3.8 Flash
  - Nano Banana
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-10T20:05:08Z
stale_after: 2026-12-10T00:00:00Z
relations:
  - { type: developed-by, target: /companies/google-deepmind.md, since: 2023-12-06 }
  - { type: related-to, target: /models/gpt.md }
  - { type: related-to, target: /models/claude.md }
  - { type: related-to, target: /ai-domains/foundation-models.md }
sources:
  - id: wiki-gemini
    resource: https://en.wikipedia.org/wiki/Gemini_(language_model)
    title: Wikipedia, "Gemini (language model)"
    author: wiki:en
  - id: wiki-deepmind
    resource: https://en.wikipedia.org/wiki/Google_DeepMind
    title: Wikipedia, "Google DeepMind"
    author: wiki:en
  - id: dm-site
    resource: https://deepmind.google/
    title: Google DeepMind, home page and model index
    author: org:google-deepmind
---

# Gemini

## What it is

Gemini is a family of multimodal large language models developed by Google DeepMind and the successor to LaMDA and PaLM 2. It was announced on 2023-12-06 by Sundar Pichai and Demis Hassabis, comprises Gemini Pro, Gemini Deep Think, Gemini Flash and Gemini Flash Lite, powers the Gemini chatbot, and is named after the Gemini zodiac sign.[^wiki-gemini]

Gemma is its open-weight sibling: a collection of open models built with similar architectures, datasets and methods, first released on 2024-02-21 in a 7-billion-parameter variant for GPU and TPU and a 2-billion-parameter variant for CPU and on-device use, and trained on up to 6 trillion tokens. Multiple publications described the release as a response to open-source competitors and a reversal of Google's earlier proprietary-only posture.[^wiki-deepmind]

## Release lineage

| Version | Released | Note | Source |
| --- | --- | --- | --- |
| Gemini 1.0 (Ultra, Pro, Nano) | 2023-12-06 | Announced by Pichai and Hassabis at a virtual press conference | [^wiki-gemini] |
| Gemini 1.5 | 2024-02 | New architecture, mixture-of-experts approach and a one-million-token context window | [^wiki-gemini] |
| Gemini 1.5 Flash | 2024-05 | Announced at I/O, alongside a desktop build of Gemini Nano for Chrome | [^wiki-gemini] |
| Gemini 2.0 Flash | 2024-12 | Experimental release; became the default in 2025-01 | [^wiki-gemini] |
| Gemini 2.5 Pro | 2025-03 | Experimental release built around chain-of-thought reasoning; 2.5 Flash-Lite introduced the same day | [^wiki-gemini] |
| Nano Banana (Gemini 2.5 Flash Image) | 2025-08 | Image generation and editing model; Google credits it with more than 10 million new Gemini app users and more than 200 million image edits within weeks | [^wiki-gemini] |
| Nano Banana Pro (Gemini 3 Pro Image) | 2025-11-20 | Improved text rendering and world knowledge | [^wiki-gemini] |
| Gemini 3 Pro, 3 Deep Think | 2025-11-18 | Fully multimodal reasoning models, integrated with Search and AI Mode the same day | [^wiki-deepmind] |
| Gemini 3.1 Pro | 2026-02-19 | | [^wiki-gemini] |
| Nano Banana 2 (Gemini 3.1 Flash Image) | 2026-02-26 | Rolled out into the Gemini chatbot, Search AI Mode and Lens | [^wiki-gemini] |
| Gemma 4 | 2026-04-02 | Open-weight sibling, purpose-built for reasoning and agentic workflows | [^wiki-gemini] |
| Gemini 3.5 Flash | 2026-05-19 | First public release in the 3.5 family | [^wiki-gemini] |
| Gemini 3.6 Flash, 3.5 Flash-Lite | 2026-07-21 | | [^wiki-gemini] |
| Gemini 3.7 Flash | 2026-08-13 | | [^wiki-gemini] |
| Gemini 3.8 Flash, 3.8 Flash Cyber | 2026-09-02 | The current workhorse line for coding and agents, per the developer's own model index | [^wiki-gemini] [^dm-site] |

## Current line

The developer's own model index as of September 2026 leads with Gemini 3.8 Flash for coding and agents, and lists Gemini Omni 1.1 Flash, Gemini 3.5 Transcribe, Gemini Robotics 2, Lyria 3.5, Nano Banana 2 Lite, Gemma 4, Co-Scientist, Gemini for Science and AlphaGenome beside it.[^dm-site] That is a wider surface than the four-variant family described at announcement, and it is the clearest evidence in this bundle that a model family is now a product portfolio rather than a single release.

## Competitive effects

Gemini 3's release on 2025-11-18 is recorded as having prompted OpenAI to hasten the release of GPT-5.2, which shipped on 2025-12-11.[^wiki-gemini] This is the bundle's clearest documented instance of release cadence in one lab being set by another's, and it is why the `competes-with` edges between the three frontier labs are recorded as structural rather than incidental.

## Not disclosed

Parameter counts, pretraining data composition and training compute are not published for any current Gemini generation, and this batch found no source stating them. The 6-trillion-token figure for Gemma is a training-data statement about an open model and is the only quantitative training fact in this file.[^wiki-deepmind]

## Disputed and unverified

1. **The causality claim about GPT-5.2** is Wikipedia's framing of the release sequence, not a statement by either company.[^wiki-gemini]
2. **Naming churn.** The family gained a 3.1, 3.5, 3.6, 3.7 and 3.8 line inside thirteen months, and Flash variants now outnumber Pro releases. A 90-day staleness window is short for this file on purpose.
3. **Vendor-reported engagement figures.** The 10-million-user and 200-million-edit claims are Google's own and unaudited.[^wiki-gemini]
4. **The mixture-of-experts claim for Gemini 1.5** comes from a secondary source describing the release, not from a technical report read in this batch.[^wiki-gemini]

[^wiki-gemini]: Wikipedia, "Gemini (language model)", https://en.wikipedia.org/wiki/Gemini_(language_model)
[^wiki-deepmind]: Wikipedia, "Google DeepMind", https://en.wikipedia.org/wiki/Google_DeepMind
[^dm-site]: Google DeepMind, home page and model index, https://deepmind.google/
