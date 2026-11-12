---
type: Domain
title: Neuro-symbolic AI
description: The sub-field combining neural networks with symbolic AI - knowledge representation and automated reasoning - to add reliability, data efficiency and trust to deep learning; called the third wave of AI and a candidate alternative path to AGI.
resource: https://en.wikipedia.org/wiki/Neuro-symbolic_AI
tags:
  - neuro-symbolic
  - hybrid-ai
  - reasoning
  - third-wave-ai
aliases:
  - Neuro-symbolic AI
  - Hybrid neural-symbolic AI
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-15T10:30:00Z
stale_after: 2027-09-15T00:00:00Z
relations:
  - { type: related-to, target: /ai-domains/agi.md }
  - { type: related-to, target: /ai-domains/foundation-models.md }
  - { type: related-to, target: /ai-domains/llms.md }
sources:
  - id: wiki-neurosym
    resource: https://en.wikipedia.org/wiki/Neuro-symbolic_AI
    title: "Neuro-symbolic AI"
    author: "wiki:en"
---

# Neuro-symbolic AI

## Definition

Neuro-symbolic AI combines neural networks with symbolic AI approaches — knowledge representation and automated reasoning — to create AI that is more robust, reliable and trustworthy than pure deep learning. The combination lets statistical patterns be joined with explicitly defined rules and knowledge, giving systems a better ability to represent, reason and generalise.[^wiki-neurosym]

It is often called the **third wave of AI**: the first wave (roughly 1980s–2000s) was logic-based symbolic AI, the second (2015 onward) was connectionist deep learning, and the third combines the two. Proponents argue it leverages the strengths of both while mitigating their weaknesses — deep learning supplies efficient learning from data, and symbol manipulation supplies reliable reasoning.[^wiki-neurosym]

## Why it is in this corpus

Neuro-symbolic AI is present here for two reasons that a consumer of the bundle will actually hit.

**The hallucination response.** The field gained wider industrial adoption and public visibility in 2025 specifically to address hallucination in LLMs — for example Amazon applied it in its Vulcan warehouse robots and Rufus AI shopping assistant to enhance accuracy and decision-making.[^wiki-neurosym] That makes it the technical counter-move to the LLM failure modes recorded in `/ai-domains/llms.md` and `/models/`.

**The alternative path to AGI.** Neuro-symbolic AI is claimed to offer an alternative route to AGI via the "neuro-symbolic cycle", where a neural network is trained continually while being checked for reasoning capability — the opposite of the scaling-up of deep learning that drives LLM energy use.[^wiki-neurosym] That is the edge to `/ai-domains/agi.md`: it is one of the two competing technical narratives about how general intelligence is reached.

## Approaches

There is no single dominant architecture; the field is defined by its taxonomies. Henry Kautz's taxonomy is the most cited, and this file records the four most relevant:

| Architecture | Meaning | Example |
| --- | --- | --- |
| Symbolic Neuro symbolic | Neural NLP where words/tokens are the input and output | BERT, GPT-3 |
| Symbolic[Neuro] | Symbolic technique invokes a neural one | AlphaGo (Monte Carlo tree search + neural evaluation) |
| Neural \| Symbolic | Neural interprets perception into symbols reasoned about symbolically | Neural-Concept Learner; Google DeepMind's AlphaProof Nexus |
| Neuro: Symbolic → Neuro | Symbolic reasoning generates/labels data for a neural model | A neural model trained for symbolic computation |

The System 1–System 2 borrowing from cognitive science is the intellectual frame: deep learning handles the fast, automatic kind of cognition, symbolic AI the deliberate, reasoning kind, and both are argued to be needed for robust AI.[^wiki-neurosym]

## Who is recorded as operating here

No company in this bundle carries an `operates-in: neuro-symbolic` edge, and this file does not invent one. The domain is written because the user asked for it and because it is the explicit technical alternative to the scaling path the frontier labs take — but on the evidence read, none of the bundle's companies are recorded as operating here as their formal domain. Google DeepMind's AlphaProof Nexus appears in the taxonomy above as an example of one architecture, and is referenced rather than promoted to an edge.

## Disputed and unverified

1. **Whether neuro-symbolic is a real convergence or a naming trend.** The sources record the industrial adoption (Amazon) and the AGI claim, but no source read establishes that any single neuro-symbolic architecture has beaten a frontier deep-learning model on a decisive benchmark; the field's promise is argued rather than measured.[^wiki-neurosym]
2. **The "third wave" framing is contested.** Whether 2015–present is accurately described as one connectionist wave, and whether the hybrid is a new wave or an old idea (hybrid models were proposed as early as the 1990s), are both open in the sources.[^wiki-neurosym]
3. **The AGI route is a claim, not a result.** The neuro-symbolic-cycle path to AGI is presented by its proponents; it competes with the scaling narrative and is not established.[^wiki-neurosym]

[^wiki-neurosym]: Wikipedia, "Neuro-symbolic AI", https://en.wikipedia.org/wiki/Neuro-symbolic_AI