---
type: Domain
title: LLMs
description: Large language models - transformer-based neural networks trained on vast text corpora to generate, summarise, translate and analyse language; the substrate of the frontier models in this bundle.
resource: https://en.wikipedia.org/wiki/Large_language_model
tags:
  - llm
  - foundation-models
  - transformer
  - natural-language-processing
aliases:
  - Large language models
  - LLM
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-15T10:28:30Z
stale_after: 2027-09-15T00:00:00Z
relations:
  - { type: related-to, target: /ai-domains/foundation-models.md }
  - { type: related-to, target: /ai-domains/agentic-ai.md }
  - { type: related-to, target: /ai-domains/agi.md }
  - { type: related-to, target: /models/gpt.md }
  - { type: related-to, target: /models/claude.md }
  - { type: related-to, target: /models/gemini.md }
sources:
  - id: wiki-llm
    resource: https://en.wikipedia.org/wiki/Large_language_model
    title: "Large language model"
    author: "wiki:en"
---

# LLMs

## Definition

A large language model is an AI model — typically a neural network — trained on a vast amount of text for natural-language-processing tasks, especially language generation. LLMs generate, summarise, translate and analyse text in many contexts, and are the basis for modern chatbots such as ChatGPT, Claude, Gemini, Grok and DeepSeek.[^wiki-llm] They are typically based on the transformer architecture; generative pre-trained transformers (GPTs) are the type pre-trained to predict the next word and then fine-tuned to follow instructions and behave as assistants.[^wiki-llm]

## Why a separate domain

This file keeps `llms` distinct from the sibling `foundation-models` domain for one reason that a consumer of the corpus needs: **foundation models are the broader claim, LLMs are the concrete, measurable substrate.** Every frontier model in this bundle (Claude, GPT, Gemini) is an LLM, and the models files in `/models/` record the releases. The domain-level facts that matter here — architecture, tokenization, evaluation, open-weights — belong in this file; the commercial and capability claims belong in the model and company files.

## Architecture and preprocessing

LLMs rest on the transformer architecture introduced by Google at the 2017 NeurIPS conference ("Attention Is All You Need"), which improved on 2014 sequence-to-sequence technology.[^wiki-llm] Preprocessing is dominated by tokenization: text is converted to numbers via byte-pair encoding (BPE) or WordPiece, with special tokens for control (e.g. `[MASK]` in BERT, `Ġ` for whitespace in RoBERTa and GPT), and the compressed token stream is fed to the model.[^wiki-llm]

## The open-weights branch

The domain has a distinct open-weights line, which matters to this corpus because several bundle companies sit on it. Since 2022 open-source models have spread, led by BLOOM and LLaMA (both with field-of-use restrictions); Mistral AI's Mistral 7B and Mixtral 8x7B use the permissive Apache licence; and in January 2025 DeepSeek released R1, a 671-billion-parameter open-weight model performing comparably to OpenAI o1 at a much lower price per token.[^wiki-llm]

## Who is recorded as operating here

Every company in this bundle that ships a frontier model operates in this domain by construction — OpenAI (GPT), Anthropic (Claude), Google (Gemini), and Google DeepMind (Gemini). Replit and SSI are model *consumers*, not producers, on the evidence read, so they are not recorded as operating here; the distinction mirrors the one the `models/` directory makes between a `ships` edge and a `uses` edge.

## Evaluation

Benchmark evaluations of LLMs attempt to measure model reasoning, factual accuracy, alignment and safety; biased or inaccurate training data can make output less reliable.[^wiki-llm] This file records the benchmark landscape at the level of what is measured, and leaves specific benchmark scores to the model files in `/models/`, which carry the per-release numbers.

## Disputed and unverified

1. **"Large" is a moving target.** What counted as a large model in 2001 (a 300-million-word smoothed n-gram) is not comparable to a 2026 frontier model; the term is relative to the compute and data of its era.[^wiki-llm]
2. **The open-weights restriction set is heterogeneous.** BLOOM and LLaMA carry field-of-use restrictions while Mistral and DeepSeek are Apache-licensed; a consumer should not treat "open weights" as a single legal category.
3. **Whether LLMs are a path to AGI or a distinct paradigm** is contested (see `/ai-domains/agi.md`); the sources record both readings.

[^wiki-llm]: Wikipedia, "Large language model", https://en.wikipedia.org/wiki/Large_language_model