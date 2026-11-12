---
type: Company
title: Google
description: Alphabet's largest operating company and the owner of Google DeepMind, the TPU silicon line, Google Cloud and the Gemini model family; simultaneously an investor in, partner to and competitor of Anthropic.
resource: https://abc.xyz
tags:
  - frontier-lab
  - hyperscaler
  - silicon
  - cloud
  - search
  - us
aliases:
  - Google LLC
  - Google Inc.
  - Alphabet Inc.
  - Alphabet
founded: 1998-09
hq: Mountain View, California, US
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-10T20:05:08Z
stale_after: 2026-12-10T00:00:00Z
relations:
  - { type: owns, target: /companies/google-deepmind.md, since: 2014-01-26, note: "acquired as DeepMind Technologies; merged with Google Brain in 2023" }
  - { type: invested-in, target: /companies/anthropic.md, amount_usd: 500000000, at: 2023-10, note: "plus $1.5B committed, and a further $1B in 2025-03" }
  - { type: partners-with, target: /companies/anthropic.md, since: 2025-10, note: "cloud partnership giving Anthropic up to one million TPUs" }
  - { type: competes-with, target: /companies/openai.md, note: "Gemini against GPT; cloud and search distribution" }
  - { type: competes-with, target: /companies/anthropic.md, note: "Gemini against Claude; the same company is an investee and partner" }
  - { type: competes-with, target: /companies/microsoft.md, note: "cloud, productivity and enterprise AI" }
  - { type: operates-in, target: /ai-domains/foundation-models.md }
  - { type: operates-in, target: /ai-domains/llms.md, note: "Gemini is an LLM family" }
  - { type: contributes-to, target: /technologies/tpu.md, note: "the Tensor Processing Unit line, designed in-house" }
  - { type: ships, target: /models/gemini.md }
  - { type: applies-to, target: /ai-use-cases/enterprise-knowledge.md, note: "Gemini for Workspace; Gemini Notebook knowledge synthesis" }
  - { type: applies-to, target: /ai-use-cases/scientific-research.md, note: "Gemini Deep Research" }
  - { type: applies-to, target: /ai-use-cases/computer-use.md, note: "Gemini Live / Gemini in the browser" }
  - { type: applies-to, target: /ai-use-cases/ai-sdlc.md, note: "Gemini Code Assist / Gemini CLI for software engineering" }
  - { type: applies-to, target: /ai-use-cases/no-code-app-building.md, note: "Gemini as the model behind prompt-to-app surfaces" }
sources:
  - id: wiki-google
    resource: https://en.wikipedia.org/wiki/Google
    title: Wikipedia, "Google"
    author: wiki:en
  - id: wiki-alphabet
    resource: https://en.wikipedia.org/wiki/Alphabet_Inc.
    title: Wikipedia, "Alphabet Inc."
    author: wiki:en
  - id: wiki-tpu
    resource: https://en.wikipedia.org/wiki/Tensor_Processing_Unit
    title: Wikipedia, "Tensor Processing Unit"
    author: wiki:en
  - id: wiki-gemini
    resource: https://en.wikipedia.org/wiki/Gemini_(language_model)
    title: Wikipedia, "Gemini (language model)"
    author: wiki:en
  - id: wiki-anthropic
    resource: https://en.wikipedia.org/wiki/Anthropic
    title: Wikipedia, "Anthropic"
    author: wiki:en
  - id: wiki-deepmind
    resource: https://en.wikipedia.org/wiki/Google_DeepMind
    title: Wikipedia, "Google DeepMind"
    author: wiki:en
  - id: transformer
    resource: https://arxiv.org/abs/1706.03762
    title: Vaswani et al., "Attention Is All You Need"
    author: human:vaswani-et-al
  - id: dm-site
    resource: https://deepmind.google/
    title: Google DeepMind, home page and model index
    author: org:google-deepmind
  - id: wiki-openai
    resource: https://en.wikipedia.org/wiki/OpenAI
    title: Wikipedia, "OpenAI"
    author: wiki:en
---

# Google

**Scope note.** This file treats Google as the entity, with Alphabet's consolidated facts included and labelled. Google is Alphabet's largest subsidiary and the holding company for its internet interests; Alphabet was created as a holding company on 2015-10-02 out of a restructuring announced on 2015-08-11, with Sundar Pichai becoming CEO of Google and, from December 2019, of Alphabet as well.[^wiki-alphabet] Keeping the two in one concept is a deliberate merge, recorded in the bundle's `conventions.md`, because the pending-target list referenced `google` and no separate `alphabet` node existed.

## Snapshot

* Founded in 1998 by Larry Page and Sergey Brin, who together own about 14% of its listed shares; now the largest subsidiary of Alphabet.[^wiki-google]
* Alphabet is the third-largest publicly traded company in the world by market capitalisation as of July 2026, the second-largest technology company by revenue after Nvidia, and the largest technology company by profit.[^wiki-alphabet]
* Owns the full vertical stack that the rest of this bundle buys in pieces: its own accelerator line (TPU), its own frontier models (Gemini), its own cloud, and the distribution of Search, Android and Chrome.[^wiki-tpu] [^wiki-gemini]
* Is simultaneously an investor in Anthropic, a compute partner to Anthropic, and the competitor of Anthropic and OpenAI in frontier models - the densest mixed relationship in the bundle.[^wiki-anthropic]

## Timeline

| Date | Event | Source |
| --- | --- | --- |
| 1998 | Google founded by Larry Page and Sergey Brin | [^wiki-google] |
| 2015 | TPUs in internal use at Google | [^wiki-tpu] |
| 2015-08-11 | Alphabet announced as a holding company; completed 2015-10-02 | [^wiki-alphabet] |
| 2017 | The Transformer architecture published by Google researchers, the substrate of the current model generation | [^transformer] |
| 2018 | TPUs made available for third-party use through Google Cloud | [^wiki-tpu] |
| 2020-01-16 | Alphabet becomes the fourth US company to reach a $1 trillion market capitalisation | [^wiki-alphabet] |
| 2023-01-20 | About 12,000 roles cut, roughly 6% of the global workforce | [^wiki-alphabet] |
| 2023-04 | Google Brain merged into Google DeepMind | [^wiki-deepmind] |
| 2023-10 | Google invests $500M in Anthropic and commits a further $1.5B | [^wiki-anthropic] |
| 2023-12-06 | Gemini 1.0 announced by Pichai and Hassabis, in Ultra, Pro and Nano sizes | [^wiki-gemini] |
| 2024-02 | Gemini 1.5 released with a mixture-of-experts architecture and a one-million-token context window | [^wiki-gemini] |
| 2025-03 | Google agrees to invest a further $1B in Anthropic | [^wiki-anthropic] |
| 2025-04 | TPU v7, named Ironwood, unveiled at Google Cloud Next | [^wiki-tpu] |
| 2025-07 | A $200M Department of Defense AI contract goes to Google alongside Anthropic, OpenAI and xAI | [^wiki-google] |
| 2025-09 | A federal judge rules Google will not be broken up in the search antitrust case | [^wiki-google] |
| 2025-10 | Cloud partnership with Anthropic giving it access to up to one million TPUs | [^wiki-anthropic] |
| 2025-11-18 | Gemini 3 Pro and 3 Deep Think released, fully multimodal and integrated with Search and AI Mode the same day | [^wiki-gemini] |
| 2026-04-22 | Eighth-generation TPUs announced as two specialised chips, TPU 8t and TPU 8i - the first bifurcation of the line | [^wiki-tpu] |
| 2026-09-02 | Gemini 3.8 Flash and 3.8 Flash Cyber released | [^wiki-gemini] |

## The AI stack

Google is the only company in this bundle that sells every layer.

| Layer | What Google has | Source |
| --- | --- | --- |
| Silicon | TPUs, used internally since 2015 and offered to third parties through Google Cloud since 2018; Google Cloud's product revenue is described as coming primarily from TPU systems. Generations ran v4 (2021), v5e and v5p, Trillium, and Ironwood (TPU v7, April 2025), with peak performance of 4,614 TFLOP/s and configurations of 256 or 9,216 chips | [^wiki-tpu] |
| Models | Gemini (proprietary) plus Gemma (open weights for edge and GPU/TPU deployment, currently Gemma 4) | [^wiki-gemini] [^dm-site] |
| Serving and agent surfaces | Google Cloud and Vertex AI distribute the models; Gemini reached first-party products including Search's AI Mode | [^wiki-gemini] |
| Consumer distribution | Search, Android, Chrome and the Gemini app; Nano Banana is credited by Google with attracting more than 10 million new users to the Gemini app and enabling more than 200 million image edits within weeks | [^wiki-gemini] |
| Current model line | First-party pages list Gemini 3.8 Flash as the workhorse model for coding and agents, alongside Gemini Omni 1.1 Flash, Gemini 3.5 Transcribe, Gemini Robotics 2, Lyria 3.5, Nano Banana 2 Lite, Gemma 4 and Co-Scientist | [^dm-site] |

## Contributions to the ecosystem

The Transformer is the largest single contribution attributable to Google in this corpus: the architecture that the foundation-model domain is built on was published by Google researchers in 2017, with results including 28.4 BLEU on WMT 2014 English-to-German and more than 2 BLEU above the then-best published results.[^transformer] TPU is the second: an accelerator programme that began as an internal efficiency project in 2013 and became a product line sold through Google Cloud.[^wiki-tpu] Google is an adopter rather than an author of MCP, and this bundle records that distinction in the edge direction.[^wiki-anthropic]

## Relations

The structural fact worth recording in prose is the triple relationship with Anthropic. Google invested $500M in October 2023 with a further $1.5B committed and another $1B in March 2025; it signed a cloud partnership in October 2025 giving Anthropic access to up to one million TPUs and potentially more than a gigawatt of capacity by 2026; and its Gemini models compete with Claude in the same enterprise accounts.[^wiki-anthropic] A graph query asking for "companies that both invest in and compete with Anthropic" returns exactly one node, and this is it.

The second is that Google is a supplier to OpenAI, its closest competitor, for cloud compute.[^wiki-openai]

## Commercials

| Fact | Value | As of | Source |
| --- | --- | --- | --- |
| Founded | 1998 | - | [^wiki-google] |
| Founders' stake | about 14% of listed shares | 2026 | [^wiki-google] |
| Market position | third-largest publicly traded company by market capitalisation; largest technology company by profit; second-largest technology company by revenue after Nvidia | 2026-07 | [^wiki-alphabet] |
| Anthropic investment | $500M plus $1.5B committed; a further $1B in 2025-03 | 2025-03 | [^wiki-anthropic] |
| Anthropic compute deal | up to one million TPUs, potentially over 1 GW by 2026 | 2025-10 | [^wiki-anthropic] |
| DoD AI contract | $200M | 2025-07 | [^wiki-google] |
| Revenue and headcount | Not retrieved in this batch; the Alphabet article's financial detail read here is historical and too stale to quote | 2026-09-10 | not stated |

## Disputed and unverified

1. **Consolidated financials are missing.** This file has no current revenue, operating income or headcount figure. Alphabet's investor relations pages were confirmed reachable but their contents were not parsed in this batch. This is the largest gap and the first thing iteration 3 should attack.[^wiki-alphabet]
2. **The `owns` edge merges two corporate layers.** Google Inc. and Alphabet Inc. are distinct legal entities and the bundle has one concept for both. Any traversal that treats company nodes as single entities inherits that merge.
3. **TPU performance figures** are vendor claims; the Wikipedia article reports them as Google's statements, and comparable caveats apply to the industry-standard benchmarks named with them.[^wiki-tpu]
4. **The eighth-generation split into 8t and 8i** is recent enough that no independent performance analysis was retrieved.[^wiki-tpu]

[^wiki-google]: Wikipedia, "Google", https://en.wikipedia.org/wiki/Google
[^wiki-alphabet]: Wikipedia, "Alphabet Inc.", https://en.wikipedia.org/wiki/Alphabet_Inc.
[^wiki-tpu]: Wikipedia, "Tensor Processing Unit", https://en.wikipedia.org/wiki/Tensor_Processing_Unit
[^wiki-gemini]: Wikipedia, "Gemini (language model)", https://en.wikipedia.org/wiki/Gemini_(language_model)
[^wiki-anthropic]: Wikipedia, "Anthropic", https://en.wikipedia.org/wiki/Anthropic
[^wiki-deepmind]: Wikipedia, "Google DeepMind", https://en.wikipedia.org/wiki/Google_DeepMind
[^transformer]: Vaswani et al., "Attention Is All You Need", https://arxiv.org/abs/1706.03762
[^dm-site]: Google DeepMind, home page and model index, https://deepmind.google/
[^wiki-openai]: Wikipedia, "OpenAI", https://en.wikipedia.org/wiki/OpenAI
