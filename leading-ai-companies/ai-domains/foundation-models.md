---
type: Domain
title: Foundation models
description: Models trained on broad data at scale and adapted to many downstream tasks; the domain the frontier labs in this bundle compete in.
resource: https://arxiv.org/abs/2108.07258
tags:
  - foundation-models
  - pretraining
  - scaling-laws
  - transformers
  - frontier-models
  - llm
aliases:
  - Foundation model
  - Base model
  - Pretrained model
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-10T20:05:08Z
stale_after: 2027-09-10T00:00:00Z
relations:
  - { type: related-to, target: /ai-domains/agentic-ai.md }
  - { type: related-to, target: /models/claude.md }
  - { type: related-to, target: /models/gpt.md }
  - { type: related-to, target: /models/gemini.md }
sources:
  - id: fm-report
    resource: https://arxiv.org/abs/2108.07258
    title: Bommasani et al., "On the Opportunities and Risks of Foundation Models"
    author: human:bommasani-et-al
  - id: transformer
    resource: https://arxiv.org/abs/1706.03762
    title: Vaswani et al., "Attention Is All You Need"
    author: human:vaswani-et-al
  - id: kaplan
    resource: https://arxiv.org/abs/2001.08361
    title: Kaplan et al., "Scaling Laws for Neural Language Models"
    author: human:kaplan-et-al
  - id: chinchilla
    resource: https://arxiv.org/abs/2203.15556
    title: Hoffmann et al., "Training Compute-Optimal Large Language Models"
    author: human:hoffmann-et-al
  - id: gpt3
    resource: https://arxiv.org/abs/2005.14165
    title: Brown et al., "Language Models are Few-Shot Learners"
    author: human:brown-et-al
  - id: instructgpt
    resource: https://arxiv.org/abs/2203.02155
    title: Ouyang et al., "Training language models to follow instructions with human feedback"
    author: human:ouyang-et-al
  - id: wiki-gemini
    resource: https://en.wikipedia.org/wiki/Gemini_(language_model)
    title: Wikipedia, "Gemini (language model)"
    author: wiki:en
---

# Foundation models

## Definition and origin

The term was coined in the 2021 Stanford report *On the Opportunities and Risks of Foundation Models*: models "trained on broad data at scale" that are "adaptable to a wide range of downstream tasks", which the authors call foundation models "to underscore their critically central yet incomplete character".[^fm-report] The report's own examples were BERT, DALL-E and GPT-3, and it deliberately covers capability, technical principle, application and societal impact rather than a single architecture.[^fm-report]

This file treats the domain as the pretraining-and-adaptation layer. Agentic systems that plan and act sit in the sibling domain; models that report their own internal states sit in interpretability, which is referenced elsewhere in this bundle and not yet written.

## The five results the domain rests on

| Result | Year | What it established | Source |
| --- | --- | --- | --- |
| Transformer | 2017 | Attention-only sequence transduction with no recurrence or convolution; 28.4 BLEU on WMT 2014 English-to-German, more than 2 BLEU above the then-best published result including ensembles, and less time to train | [^transformer] |
| Scaling laws | 2020 | Cross-entropy loss falls as a power law in model size, dataset size and training compute, with some trends spanning more than seven orders of magnitude; width and depth matter little within a wide range, and larger models are more sample-efficient | [^kaplan] |
| Few-shot behaviour | 2020 | GPT-3, an autoregressive model with 175 billion parameters and ten times more than any previous non-sparse model, reached competitive task-agnostic few-shot performance without task-specific fine-tuning | [^gpt3] |
| Instruction following by feedback | 2022 | Scaling alone does not make a model follow a user's intent; fine-tuning on demonstrations and then on human rankings of outputs does | [^instructgpt] |
| Compute-optimal training | 2022 | Scale model size and token count together; for every doubling of parameters the training tokens should double too, which made the largest models of the day undertrained. Chinchilla reached better loss than Gopher on the same compute budget with 70 billion parameters and four times the data | [^chinchilla] |

Two of these are in tension by design. The 2020 scaling-law paper concluded that compute-optimal training means very large models on a relatively modest amount of data, stopping well before convergence; the 2022 work inverted the allocation.[^kaplan] [^chinchilla] The later result is the one the field built on, and the earlier one is still cited for the power-law relationship rather than for its allocation advice.

## What the term covers in practice

* **Pretraining at scale, then adaptation.** The distinguishing feature is not the architecture but the two-stage life of the model: broad pretraining followed by prompting, fine-tuning or preference optimisation for a task.[^fm-report]
* **Multimodality as a design goal rather than a bolt-on.** Gemini is presented by its developers as a family of multimodal models, and the successor to LaMDA and PaLM 2, announced to the public on 2023-12-06.[^wiki-gemini]
* **Boundary with adjacent domains.** Foundation models are the substrate; agentic AI is the loop built above it; interpretability is the attempt to read the substrate. The bundle records all three as separate domains so that a domain-overlap query returns the distinction rather than collapsing it.

## Who is recorded as operating here

Inbound edges to this file, counted from the concepts written so far: Anthropic, Replit, OpenAI, Google and Google DeepMind each carry an `operates-in` edge to this path. The count is a traversal over `companies/`, not an editorial ranking - see the bundle's `index.md` for the query form. Labs named in the brief but not yet written (Meta, Alibaba, DeepSeek) are absent from the count because their files do not exist, not because the edge was judged false.

## Disputed and unverified

1. **Whether scale produces capability smoothly or in jumps.** The scaling-law and Chinchilla papers describe continuous loss curves; the "emergent abilities" claim made from benchmark discontinuities is widely repeated and is not sourced in this batch. No position is taken here.
2. **The term's boundaries.** The 2021 report is the source of the word, not of an agreed membership test; whether a fine-tuned derivative or a small distilled model is a "foundation model" is unresolved in the sources read.
3. **Parameter counts for current frontier models.** OpenAI, Anthropic and Google have stopped publishing them. The figures in the table above are historical and citable only because they came from papers.

[^fm-report]: Bommasani et al., "On the Opportunities and Risks of Foundation Models", https://arxiv.org/abs/2108.07258
[^transformer]: Vaswani et al., "Attention Is All You Need", https://arxiv.org/abs/1706.03762
[^kaplan]: Kaplan et al., "Scaling Laws for Neural Language Models", https://arxiv.org/abs/2001.08361
[^chinchilla]: Hoffmann et al., "Training Compute-Optimal Large Language Models", https://arxiv.org/abs/2203.15556
[^gpt3]: Brown et al., "Language Models are Few-Shot Learners", https://arxiv.org/abs/2005.14165
[^instructgpt]: Ouyang et al., "Training language models to follow instructions with human feedback", https://arxiv.org/abs/2203.02155
[^wiki-gemini]: Wikipedia, "Gemini (language model)", https://en.wikipedia.org/wiki/Gemini_(language_model)
