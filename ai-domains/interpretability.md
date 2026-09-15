---
type: Domain
title: Interpretability
description: Understanding the internal workings of AI models - the concrete structures, algorithms and circuits inside neural networks; a research domain Anthropic operates in and the counterpart to the black-box treatment of most frontier models.
resource: https://en.wikipedia.org/wiki/Mechanistic_interpretability
tags:
  - interpretability
  - mechanistic-interpretability
  - alignment
  - explainability
aliases:
  - Mechanistic interpretability
  - Model interpretability
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-15T10:29:30Z
stale_after: 2027-09-15T00:00:00Z
relations:
  - { type: related-to, target: /ai-domains/ai-safety.md }
  - { type: related-to, target: /ai-domains/foundation-models.md }
  - { type: related-to, target: /companies/anthropic.md }
sources:
  - id: wiki-mechinterp
    resource: https://en.wikipedia.org/wiki/Mechanistic_interpretability
    title: "Mechanistic interpretability"
    author: "wiki:en"
---

# Interpretability

## Definition and boundary

Interpretability is the research domain concerned with understanding what an AI model is actually doing internally, as opposed to treating it as a black box that produces outputs. The sub-field most relevant to this corpus is **mechanistic interpretability**, the effort to understand the internal workings of neural networks by analysing their concrete structures, algorithms and circuits — a reverse-engineering approach to a model, in contrast to the gradient-based saliency-map methods that dominated earlier work.[^wiki-mechinterp]

The term was coined by Chris Olah, co-founder of Anthropic, to describe his circuit-analysis work.[^wiki-mechinterp] That origin is why this domain is tied to Anthropic specifically: the bundle already carries an `operates-in: interpretability` edge from Anthropic, and the domain's founding concept came from an Anthropic co-founder.

## Key methods

| Method | What it does | Source |
| --- | --- | --- |
| Sparse autoencoders (SAEs) | Disentangle network activations into sparse representations whose learned dimensions often map to human-understandable concepts; applied to LLM interpretability by Anthropic | [^wiki-mechinterp] |
| Features and circuits | A circuit is a causal chain of feature activations; mapping which circuits lead to which consequences, and activating/inhibiting them, analyses how a model reaches a result | [^wiki-mechinterp] |
| Linear representation hypothesis | High-level concepts are represented as linear directions in activation space; empirically supported by word embeddings and LLMs, though not universally | [^wiki-mechinterp] |

## Why it is a safety-adjacent domain

Mechanistic interpretability is used in the AI-safety context to understand and verify the behaviour of complex systems and to attempt to identify risks such as misalignment.[^wiki-mechinterp] That is the edge to `/ai-domains/ai-safety.md`: interpretability is one of the technical routes by which the frontier labs try to make "is this model behaving as intended" a checkable question rather than a leap of faith.

## Who is recorded as operating here

Anthropic is the one company in this bundle with an `operates-in: interpretability` edge, consistent with Olah's co-founding of the field and Anthropic's public interpretability programme. The other frontier labs reference safety but are not recorded as operating in interpretability on the evidence read; the domain is deliberately held as an Anthropic-anchored node rather than inflated into a shared claim.

## Disputed and unverified

1. **Whether interpretability yields safety, or only explanation.** The sources record the intended link to misalignment detection, but no source read establishes that interpretability has yet prevented a concrete frontier-model failure; the connection is a research goal, not a measured result.[^wiki-mechinterp]
2. **The linear representation hypothesis is not universal.** The sources note it does not hold up in all cases.[^wiki-mechinterp]
3. **The general term vs the mechanistic sub-field.** A consumer searching "interpretability" may mean the loose every-model field; this file scopes itself to the mechanistic, Anthropic-originated reading that the bundle's edge actually references.

[^wiki-mechinterp]: Wikipedia, "Mechanistic interpretability", https://en.wikipedia.org/wiki/Mechanistic_interpretability