---
type: Person
title: Durk Kingma
description: Dutch machine learning researcher and OpenAI co-founder, co-author of the Adam optimizer and the variational autoencoder, now a researcher at Anthropic in Amsterdam.
resource: https://en.wikipedia.org/wiki/Durk_Kingma
tags:
  - founder
  - researcher
  - generative-models
  - optimization
  - openai
  - anthropic
  - netherlands
aliases:
  - Durk Kingma
  - Diederik Kingma
  - Diederik P. Kingma
born: 1983
nationality: NL
employer: /companies/anthropic.md
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-11T10:39:39Z
stale_after: 2027-09-11T00:00:00Z
relations:
  - { type: founded, target: /companies/openai.md, since: 2015-12, role: co-founder }
  - { type: previously-at, target: /companies/google.md, role: "generative models, including text-to-image work" }
  - { type: employs, target: /companies/anthropic.md, role: "machine learning researcher, Amsterdam", note: "start date not established in the sources read" }
  - { type: educated-at, target: /institutions/university-of-utrecht.md, to: 2009, note: MSc }
  - { type: educated-at, target: /institutions/university-of-amsterdam.md, note: PhD }
  - { type: created, target: /technologies/adam-optimizer.md, from: 2014, role: "with Jimmy Ba" }
  - { type: created, target: /concepts/variational-autoencoder.md, from: 2013, role: "with Max Welling" }
sources:
  - id: openai-intro
    resource: https://openai.com/index/introducing-openai/
    title: 'OpenAI, "Introducing OpenAI", the December 2015 founding announcement'
    author: org:openai
  - id: adam
    resource: https://arxiv.org/abs/1412.6980
    title: 'Kingma and Ba, "Adam: A Method for Stochastic Optimization", 2014'
    author: human:kingma-and-ba
  - id: vae
    resource: https://arxiv.org/abs/1312.6114
    title: 'Kingma and Welling, "Auto-Encoding Variational Bayes", 2013'
    author: human:kingma-and-welling
  - id: wiki-kingma
    resource: https://en.wikipedia.org/wiki/Durk_Kingma
    title: Wikipedia, "Durk Kingma"
    author: wiki:en
---

# Durk Kingma

One of the eleven founders of OpenAI, and the co-author of two of the most widely reused results in modern machine learning: the Adam optimizer and the variational autoencoder.[^openai-intro] [^adam] [^vae]

## Snapshot

* Born in 1983 in the Netherlands.[^wiki-kingma]
* Named in the December 2015 founding announcement among OpenAI's founding members, described there as research engineers and scientists.[^openai-intro]
* Previously worked at Google on generative AI, specifically text-to-image models.[^wiki-kingma]
* Currently a machine learning researcher at Anthropic, in the Netherlands.[^wiki-kingma]

## Education

* MSc at Utrecht University in 2009.[^wiki-kingma]
* PhD at the University of Amsterdam.[^wiki-kingma]

## Career and outcomes

* Co-founded OpenAI in December 2015 and stayed on the research staff through its early scaling period.[^openai-intro]
* Moved to Google, working on generative models and text-to-image systems, before joining Anthropic, which makes him the second OpenAI founder in this bundle to end up at Anthropic after John Schulman.[^wiki-kingma]

## Research contributions

* Adam, with Jimmy Ba, submitted in December 2014: an adaptive per-parameter gradient method.[^adam]
* The variational autoencoder, with Max Welling, in 2013, one of the two generative-model families that preceded the diffusion and autoregressive era.[^vae]

## Relations

The founding edge into OpenAI is one of eleven recorded on [OpenAI](/companies/openai.md). Both of his published contributions are declared targets rather than files, so a query that counts them will find these edges before it finds the concepts.

## Disputed and unverified

Wikipedia is the sole source read for his current employment, and it gives no start date for the Anthropic role. His Google tenure is described there only as text-to-image generative modelling, without dates or a team.

[^openai-intro]: OpenAI, "Introducing OpenAI", December 2015, https://openai.com/index/introducing-openai/
[^adam]: Kingma and Ba, "Adam: A Method for Stochastic Optimization", arXiv:1412.6980, https://arxiv.org/abs/1412.6980
[^vae]: Kingma and Welling, "Auto-Encoding Variational Bayes", arXiv:1312.6114, https://arxiv.org/abs/1312.6114
[^wiki-kingma]: Wikipedia, "Durk Kingma", https://en.wikipedia.org/wiki/Durk_Kingma
