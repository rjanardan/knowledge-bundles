---
type: Company
title: Google DeepMind
description: Alphabet's AI research laboratory, founded in London in 2010 as DeepMind Technologies and merged with Google Brain in 2023; the developer of the Gemini and Gemma model families and of AlphaGo and AlphaFold.
resource: https://deepmind.google
tags:
  - frontier-lab
  - research-lab
  - reinforcement-learning
  - science-ai
  - robotics
  - uk
aliases:
  - DeepMind
  - DeepMind Technologies
  - Google DeepMind
founded: 2010-11
hq: London, United Kingdom
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-10T20:05:08Z
stale_after: 2026-12-10T00:00:00Z
relations:
  - { type: subsidiary-of, target: /companies/google.md, since: 2014-01-26 }
  - { type: founded-by, target: /founders/demis-hassabis.md, since: 2010-11, role: "co-founder; chairman; CEO 2010-2026" }
  - { type: founded-by, target: /founders/shane-legg.md, since: 2010-11 }
  - { type: founded-by, target: /founders/mustafa-suleyman.md, since: 2010-11, note: "left in December 2019 for a policy role at Google" }
  - { type: operates-in, target: /ai-domains/foundation-models.md }
  - { type: operates-in, target: /ai-domains/agentic-ai.md }
  - { type: operates-in, target: /ai-domains/ai-safety.md }
  - { type: operates-in, target: /ai-domains/llms.md, note: "Gemini is an LLM family" }
  - { type: ships, target: /models/gemini.md }
  - { type: uses, target: /technologies/tpu.md }
  - { type: contributes-to, target: /technologies/alphafold.md, note: "protein structure prediction; Nobel Prize in Chemistry 2024" }
  - { type: applies-to, target: /ai-use-cases/scientific-research.md, note: "AlphaFold design work; research agents leaning on DeepMind" }
  - { type: applies-to, target: /ai-use-cases/enterprise-knowledge.md, note: "Gemini on DeepMind foundation; grounding in Workspace" }
  - { type: competes-with, target: /companies/openai.md }
  - { type: competes-with, target: /companies/anthropic.md }
sources:
  - id: wiki-deepmind
    resource: https://en.wikipedia.org/wiki/Google_DeepMind
    title: Wikipedia, "Google DeepMind"
    author: wiki:en
  - id: wiki-hassabis
    resource: https://en.wikipedia.org/wiki/Demis_Hassabis
    title: Wikipedia, "Demis Hassabis"
    author: wiki:en
  - id: wiki-gemini
    resource: https://en.wikipedia.org/wiki/Gemini_(language_model)
    title: Wikipedia, "Gemini (language model)"
    author: wiki:en
  - id: wiki-tpu
    resource: https://en.wikipedia.org/wiki/Tensor_Processing_Unit
    title: Wikipedia, "Tensor Processing Unit"
    author: wiki:en
  - id: dm-site
    resource: https://deepmind.google/
    title: Google DeepMind, home page and model index
    author: org:google-deepmind
---

# Google DeepMind

## Snapshot

* Founded in the United Kingdom in November 2010 by Demis Hassabis, Shane Legg and Mustafa Suleyman; acquired by Google on 2014-01-26 for a price reported between $400M and $650M, and merged with Google Brain in April 2023 to become Google DeepMind.[^wiki-deepmind]
* A subsidiary of Alphabet headquartered in London, and the developer of both the proprietary Gemini family and the open-weight Gemma family, plus the generative models Imagen, Veo and Lyria.[^wiki-deepmind]
* Its research record is measured in named systems rather than publications alone: AlphaGo, AlphaZero, MuZero, AlphaFold, AlphaEvolve, AlphaDev and AlphaTensor.[^wiki-deepmind]
* Distributed research reach: over 200 million predicted protein structures, representing virtually all known proteins, released on the AlphaFold database by July 2022.[^wiki-deepmind]

## Timeline

| Date | Event | Source |
| --- | --- | --- |
| 2010-11 | Founded as DeepMind Technologies by Hassabis, Legg and Suleyman; Hassabis and Legg met as postdocs at the Gatsby Computational Neuroscience Unit at UCL | [^wiki-deepmind] |
| 2013 | Deep learning agent learns to play Atari games from pixels, without altering the game code | [^wiki-deepmind] |
| 2014-01-26 | Google confirms the acquisition; the company is courted by Facebook and others before that | [^wiki-deepmind] |
| 2016 | AlphaGo beats Lee Sedol over five games | [^wiki-deepmind] |
| 2017-10 | A dedicated AI ethics research team is launched, with Nick Bostrom as an adviser | [^wiki-deepmind] |
| 2019-12 | Co-founder Suleyman leaves for a policy role at Google's parent | [^wiki-deepmind] |
| 2020 | AlphaFold reaches state-of-the-art protein folding results | [^wiki-deepmind] |
| 2022-07 | Over 200 million predicted protein structures announced for release | [^wiki-deepmind] |
| 2023-04 | Merged with Google Brain to form Google DeepMind | [^wiki-deepmind] |
| 2024-02-21 | Gemma released as an open-weight family in 7B and 2B sizes | [^wiki-deepmind] |
| 2024-05 | I/O announcement of Trillium, the sixth-generation TPU | [^wiki-tpu] |
| 2024-10 | AlphaChip's chip-layout work is described as used in every TPU iteration since 2020 | [^wiki-deepmind] |
| 2025-09 | Gemini Robotics 1.5 released | [^wiki-deepmind] |
| 2025-11-18 | Gemini 3 Pro released as a fully multimodal reasoning model, integrated with Search the same day | [^wiki-deepmind] |
| 2026-04 | Gemini Robotics ER-1.6 launched | [^wiki-deepmind] |
| 2026-09 | Gemini 3.8 Flash and 3.8 Flash Cyber released | [^dm-site] |

## Research record

| System | Contribution | Source |
| --- | --- | --- |
| AlphaGo | Beat the Go world champion Lee Sedol in 2016, later the subject of a documentary | [^wiki-deepmind] |
| AlphaZero | Reached top-level play in Go, chess and shogi from self-play after a few days of training, and needed three days to beat its predecessor's level | [^wiki-deepmind] |
| MuZero | Applied to video compression under a fixed bit budget, among other real-world problems | [^wiki-deepmind] |
| AlphaFold | Protein structure prediction; the 2024 Nobel Prize in Chemistry went jointly to Hassabis and John M. Jumper for it | [^wiki-deepmind] [^wiki-hassabis] |
| AlphaEvolve, AlphaDev, AlphaTensor | Algorithm and matrix-multiplication discovery | [^wiki-deepmind] |
| AlphaChip | Chip floorplanning that cut layout time from weeks to hours; the company says the designs were used in every TPU iteration since 2020, and independent researchers have said the public benchmarks are insufficient to confirm the claim | [^wiki-deepmind] |
| Weather nowcasting | Severe weather forecasting speed and accuracy demonstrations | [^wiki-deepmind] |

## Model families and current line

Gemini is proprietary and Gemma is open-weight; both are developed here, not in a separate product organisation, which is why the bundle points `ships` from this file rather than from the Google file.[^wiki-deepmind] Gemma's first release shipped on 2024-02-21 in a 7-billion-parameter variant optimised for GPU and TPU and a 2-billion-parameter variant for CPU and on-device use, trained on up to 6 trillion tokens using similar architectures, datasets and methods to the Gemini models.[^wiki-deepmind]

The first-party model index as of September 2026 lists Gemini 3.8 Flash as the workhorse model for coding and agents, with Gemini Omni 1.1 Flash, Gemini 3.5 Transcribe, Gemini Robotics 2, Lyria 3.5, Nano Banana 2 Lite, Gemma 4, Co-Scientist, Gemini for Science and AlphaGenome alongside it.[^dm-site]

## Leadership

Hassabis is chairman and co-founder of Google DeepMind, chief scientist of Alphabet from 2026, chief executive and co-founder of Isomorphic Labs, and a UK Government AI Adviser; he served as DeepMind's CEO from 2010 until 2026.[^wiki-hassabis] The sources read for this batch do not name his successor as chief executive, and the file does not guess. Co-founder Suleyman left in December 2019.[^wiki-deepmind]

## Investors before acquisition

Early backing came from Horizons Ventures and Founders Fund, with angels including Scott Banister, Peter Thiel and Elon Musk; Jaan Tallinn was an early investor and adviser. The company was courted by Facebook, Musk and Google before the 2014 acquisition.[^wiki-deepmind] These are historical edges: none of these parties holds a stake in Google DeepMind today, and the bundle records them only as acquisition history.

## Disputed and unverified

1. **The acquisition price is a range, not a number.** Wikipedia reports it as "reportedly ranging between $400 million and $650 million", which is what this file states and no more.[^wiki-deepmind]
2. **AlphaChip's claim to every TPU since 2020** is a company statement contradicted in part by researchers who say the public benchmarks do not prove the claimed superiority. Both are recorded.[^wiki-deepmind]
3. **The current chief executive is not established** in the sources read.[^wiki-hassabis]
4. **Headcount and compute** are not published and no estimate was retrieved, matching the pattern across this bundle's lab files.

[^wiki-deepmind]: Wikipedia, "Google DeepMind", https://en.wikipedia.org/wiki/Google_DeepMind
[^wiki-hassabis]: Wikipedia, "Demis Hassabis", https://en.wikipedia.org/wiki/Demis_Hassabis
[^wiki-gemini]: Wikipedia, "Gemini (language model)", https://en.wikipedia.org/wiki/Gemini_(language_model)
[^wiki-tpu]: Wikipedia, "Tensor Processing Unit", https://en.wikipedia.org/wiki/Tensor_Processing_Unit
[^dm-site]: Google DeepMind, home page and model index, https://deepmind.google/
