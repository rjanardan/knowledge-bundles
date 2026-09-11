---
type: Person
title: John Schulman
description: OpenAI co-founder, author of the policy-optimisation algorithms behind ChatGPT's training, and since 2025 chief scientist at Thinking Machines Lab by way of Anthropic.
resource: https://en.wikipedia.org/wiki/John_Schulman
tags:
  - founder
  - researcher
  - reinforcement-learning
  - openai
  - anthropic
  - us
aliases:
  - John Schulman
  - Schulman
born: 1987
nationality: US
employer: /companies/thinking-machines-lab.md
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-11T10:39:39Z
stale_after: 2027-09-11T00:00:00Z
relations:
  - { type: founded, target: /companies/openai.md, since: 2015-12, role: "co-founder" }
  - { type: previously-at, target: /companies/openai.md, from: 2015-12, to: 2024-08, role: "research lead; led the reinforcement learning team that created ChatGPT" }
  - { type: previously-at, target: /companies/anthropic.md, from: 2024-08, to: 2025-02, role: "alignment science research" }
  - { type: employs, target: /companies/thinking-machines-lab.md, since: 2025-02, role: chief scientist }
  - { type: created, target: /technologies/proximal-policy-optimization.md, from: 2017 }
  - { type: created, target: /technologies/trust-region-policy-optimization.md, from: 2015 }
  - { type: educated-at, target: /institutions/uc-berkeley.md, note: "PhD in electrical engineering and computer sciences; advisor Pieter Abbeel" }
  - { type: educated-at, target: /institutions/caltech.md, to: 2010, note: "degree in physics" }
sources:
  - id: openai-intro
    resource: https://openai.com/index/introducing-openai/
    title: 'OpenAI, "Introducing OpenAI", the December 2015 founding announcement'
    author: org:openai
  - id: ppo
    resource: https://arxiv.org/abs/1707.06347
    title: Schulman et al., "Proximal Policy Optimization Algorithms", 2017
    author: human:schulman-et-al
  - id: trpo
    resource: https://arxiv.org/abs/1502.05477
    title: Schulman, Levine, Moritz, Jordan and Abbeel, "Trust Region Policy Optimization", 2015
    author: human:schulman-et-al
  - id: wiki-schulman
    resource: https://en.wikipedia.org/wiki/John_Schulman
    title: Wikipedia, "John Schulman"
    author: wiki:en
---

# John Schulman

One of the eleven founders of OpenAI in December 2015, the author of the two policy-optimisation methods that trained ChatGPT, and chief scientist at Thinking Machines Lab since 2025.[^openai-intro] [^wiki-schulman]

## Snapshot

* Born in 1987 or 1988 in the United States.[^wiki-schulman]
* Co-founded OpenAI in December 2015, shortly before finishing his PhD.[^wiki-schulman]
* Led the reinforcement learning team at OpenAI that created ChatGPT, and has been called the architect of ChatGPT.[^wiki-schulman]
* Joined Anthropic in August 2024 and left in February 2025 for Thinking Machines Lab, where he is chief scientist.[^wiki-schulman]

## Education

* Graduated from Caltech with a degree in physics in 2010.[^wiki-schulman]
* PhD in electrical engineering and computer sciences at the University of California, Berkeley, advised by Pieter Abbeel.[^wiki-schulman]

## Career and outcomes

* Co-founded OpenAI in December 2015 with Sam Altman, Elon Musk, Ilya Sutskever, Greg Brockman, Trevor Blackwell, Vicki Cheung, Andrej Karpathy, Durk Kingma, Pamela Vagata and Wojciech Zaremba.[^wiki-schulman]
* Led the reinforcement learning team, and co-led post-training from 2022 to 2024, the period in which ChatGPT was built.[^wiki-schulman]
* Left for Anthropic in August 2024 - the first of the OpenAI founders to move to the principal competitor - then left Anthropic in February 2025 to join the startup founded by the former OpenAI chief technology officer.[^wiki-schulman]
* Received the Mark Bingham Award for Excellence in Achievement by Young Alumni from UC Berkeley in 2025.[^wiki-schulman]

## Research contributions

* Trust Region Policy Optimization, with Sergey Levine, Philipp Moritz, Michael Jordan and Pieter Abbeel, in 2015.[^trpo]
* Proximal Policy Optimization, with Filip Wolski, Prafulla Dhariwal, Alec Radford and Oleg Klimov, in 2017; PPO and TRPO are the components of ChatGPT's training loop.[^ppo] [^wiki-schulman]

## Public positions

* His published position on safety work has been that the alignment problem is best attacked from inside capability research rather than from a separate discipline, which is the pattern his career traces.[^wiki-schulman]

## Relations

The OpenAI founding edge is one of eleven on [OpenAI](/companies/openai.md). His move to Anthropic and then to Thinking Machines Lab makes him the only person in this bundle who has held research roles at both frontier labs and at the startup that recruited from both.

## Disputed and unverified

His exact birth year is recorded on Wikipedia as 1987 or 1988, which is the source's own uncertainty rather than an omission here.

[^openai-intro]: OpenAI, "Introducing OpenAI", December 2015, https://openai.com/index/introducing-openai/
[^ppo]: Schulman et al., "Proximal Policy Optimization Algorithms", arXiv:1707.06347, https://arxiv.org/abs/1707.06347
[^trpo]: Schulman, Levine, Moritz, Jordan and Abbeel, "Trust Region Policy Optimization", arXiv:1502.05477, https://arxiv.org/abs/1502.05477
[^wiki-schulman]: Wikipedia, "John Schulman", https://en.wikipedia.org/wiki/John_Schulman
