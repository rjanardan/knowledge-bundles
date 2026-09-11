---
type: Company
title: OpenAI
description: Frontier model lab behind ChatGPT and the GPT model family, founded as a nonprofit in 2015 and restructured in 2025 into a public benefit corporation controlled by the OpenAI Foundation.
resource: https://openai.com
tags:
  - frontier-lab
  - llm
  - chatgpt
  - agentic-ai
  - enterprise-ai
  - us
aliases:
  - OpenAI, Inc.
  - OpenAI LP
  - OpenAI Group PBC
  - OpenAI Foundation
founded: 2015-12
hq: San Francisco, California, US
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-10T20:05:08Z
stale_after: 2026-12-10T00:00:00Z
relations:
  - { type: founded-by, target: /founders/sam-altman.md, since: 2015-12, role: "co-founder, co-chair; CEO since 2019-03" }
  - { type: founded-by, target: /founders/elon-musk.md, since: 2015-12, role: "co-founder, co-chair; resigned 2018" }
  - { type: founded-by, target: /founders/ilya-sutskever.md, since: 2015-12 }
  - { type: founded-by, target: /founders/greg-brockman.md, since: 2015-12 }
  - { type: founded-by, target: /founders/trevor-blackwell.md, since: 2015-12 }
  - { type: founded-by, target: /founders/vicki-cheung.md, since: 2015-12 }
  - { type: founded-by, target: /founders/andrej-karpathy.md, since: 2015-12 }
  - { type: founded-by, target: /founders/durk-kingma.md, since: 2015-12 }
  - { type: founded-by, target: /founders/john-schulman.md, since: 2015-12 }
  - { type: founded-by, target: /founders/pamela-vagata.md, since: 2015-12 }
  - { type: founded-by, target: /founders/wojciech-zaremba.md, since: 2015-12 }
  - { type: operates-in, target: /ai-domains/foundation-models.md }
  - { type: operates-in, target: /ai-domains/agentic-ai.md }
  - { type: operates-in, target: /ai-domains/ai-safety.md }
  - { type: applies-to, target: /ai-use-cases/ai-sdlc.md }
  - { type: applies-to, target: /ai-use-cases/enterprise-knowledge.md }
  - { type: applies-to, target: /ai-use-cases/computer-use.md }
  - { type: applies-to, target: /ai-use-cases/scientific-research.md }
  - { type: ships, target: /models/gpt.md }
  - { type: uses, target: /technologies/mcp.md }
  - { type: competes-with, target: /companies/anthropic.md, note: "frontier models, coding agents, enterprise" }
  - { type: competes-with, target: /companies/google.md }
  - { type: competes-with, target: /companies/google-deepmind.md }
  - { type: competes-with, target: /companies/xai.md }
  - { type: partners-with, target: /companies/microsoft.md, since: 2019-03, note: "model licensing and Azure; 27% stake after the 2025 restructuring" }
  - { type: partners-with, target: /companies/nvidia.md }
  - { type: partners-with, target: /companies/amd.md }
  - { type: partners-with, target: /companies/broadcom.md }
  - { type: partners-with, target: /companies/anduril.md }
  - { type: partners-with, target: /companies/replit.md, since: 2026-06, note: "Codex Sites" }
  - { type: partners-with, target: /companies/lovable.md, since: 2026-06, note: "Codex Sites" }
  - { type: partners-with, target: /companies/figma.md, since: 2026-06, note: "Codex Sites" }
  - { type: customer-of, target: /companies/microsoft.md, note: "Azure compute; $250B committed purchase" }
  - { type: customer-of, target: /companies/oracle.md, note: "cloud compute and the Stargate joint venture" }
  - { type: customer-of, target: /companies/amazon.md }
  - { type: customer-of, target: /companies/google.md }
  - { type: customer-of, target: /companies/cerebras.md }
  - { type: invested-by, target: /investors/softbank.md, round: "2025-04 and 2026-02", role: lead }
  - { type: invested-by, target: /investors/thrive-capital.md }
  - { type: invested-by, target: /investors/coatue.md }
  - { type: invested-by, target: /investors/altimeter-capital.md }
  - { type: invested-by, target: /companies/microsoft.md, note: "over $13B cumulatively; 27% stake valued at $135B after the 2025 restructuring" }
  - { type: invested-by, target: /companies/amazon.md, round: "2026-02", amount_usd: 50000000000 }
  - { type: invested-by, target: /companies/nvidia.md, round: "2026-02", amount_usd: 30000000000 }
  - { type: invested-by, target: /investors/tpg.md, round: "DeployCo", at: 2026-05 }
  - { type: invested-by, target: /investors/sequoia-capital.md, since: 2021, note: "the firm dates its partnership with OpenAI to 2021" }
sources:
  - id: wiki-openai
    resource: https://en.wikipedia.org/wiki/OpenAI
    title: Wikipedia, "OpenAI"
    author: wiki:en
  - id: wiki-gpt5
    resource: https://en.wikipedia.org/wiki/GPT-5
    title: Wikipedia, "GPT-5"
    author: wiki:en
  - id: wiki-altman
    resource: https://en.wikipedia.org/wiki/Sam_Altman
    title: Wikipedia, "Sam Altman"
    author: wiki:en
  - id: openai-news
    resource: https://openai.com/news/
    title: OpenAI, news index
    author: org:openai
  - id: openai-docs
    resource: https://platform.openai.com/docs/models
    title: OpenAI, API documentation and model index
    author: org:openai
  - id: gpt3
    resource: https://arxiv.org/abs/2005.14165
    title: Brown et al., "Language Models are Few-Shot Learners"
    author: human:brown-et-al
  - id: instructgpt
    resource: https://arxiv.org/abs/2203.02155
    title: Ouyang et al., "Training language models to follow instructions with human feedback"
    author: human:ouyang-et-al
---

# OpenAI

## Snapshot

* Frontier model lab founded in December 2015 as the nonprofit OpenAI, Inc., restructured in 2025 into OpenAI Group PBC, 26% owned by the nonprofit OpenAI Foundation, with Microsoft holding 27% and employees and other investors the remaining 47%.[^wiki-openai]
* Builds and sells the GPT model family and ChatGPT; ChatGPT is the fifth-most-visited website globally as of September 2026, and its release in November 2022 is credited with catalysing the AI boom.[^wiki-openai]
* Closed a round in 2026 at an $852B post-money valuation on $122B of committed capital, and confirmed on 2026-06-08 that it had filed for an IPO with the SEC.[^wiki-openai]
* Sits on both sides of the compute market: it is a customer of Microsoft, Oracle, Amazon, Google and Cerebras for compute, and a partner of Nvidia, AMD and Broadcom for silicon.[^wiki-openai]

## Timeline

| Date | Event | Source |
| --- | --- | --- |
| 2015-12 | Founded as the nonprofit OpenAI, Inc. in Delaware, with eleven named founders and Musk and Altman as co-chairs | [^wiki-openai] |
| 2016-08 | Nvidia gifts the first DGX-1 supercomputer | [^wiki-openai] |
| 2019-03 | For-profit OpenAI LP created; Microsoft invests $1B and services migrate to Azure | [^wiki-openai] |
| 2022-11-30 | ChatGPT released | [^wiki-openai] |
| 2023-01-23 | Microsoft announces a further $10B at a $29B valuation | [^wiki-openai] |
| 2023-03-14 | GPT-4 released, as an API and inside ChatGPT Plus | [^wiki-openai] |
| 2023-11 | Board removes Altman; 738 of about 770 employees sign a letter threatening to leave; he is reinstated five days later with a new board | [^wiki-openai] [^wiki-altman] |
| 2024-10 | $6.6B raised at a $157B valuation | [^wiki-openai] |
| 2024-12 | Sora video model and the o1 reasoning model released | [^wiki-openai] |
| 2025-01-21 | The Stargate Project announced with Oracle, SoftBank and MGX, estimated at $500B over four years | [^wiki-openai] |
| 2025-04 | $40B raised at a $300B post-money valuation, led by SoftBank - then the highest-value private technology deal in history | [^wiki-openai] |
| 2025-07 | Annualized revenue reported at $12B, up from $3.7B in 2024 | [^wiki-openai] |
| 2025-10 | Employee share sale of up to $10B values the company at $500B, the most valuable private company in the world | [^wiki-openai] |
| 2025-10-21 | ChatGPT Atlas browser introduced | [^wiki-openai] |
| 2026-02 | $110B raised at a $730B valuation, led by Amazon ($50B), SoftBank ($30B) and Nvidia ($30B); extended to $120B in March | [^wiki-openai] |
| 2026-04 | Round closed at $122B of committed capital and an $852B post-money valuation | [^wiki-openai] |
| 2026-05 | OpenAI Deployment Company launched, with more than $4B of initial investment led by TPG | [^wiki-openai] |
| 2026-05-18 | Federal jury finds for OpenAI, Altman, Brockman and Microsoft in Musk v. Altman; Musk announces an appeal | [^wiki-openai] |
| 2026-06-08 | IPO filing confirmed with the SEC | [^wiki-openai] |
| 2026-09-09 | GPT-6 Astra announced | [^openai-news] |

## Founding and team

Wikipedia names eleven founders of the December 2015 nonprofit: Elon Musk, Sam Altman, Ilya Sutskever, Greg Brockman, Trevor Blackwell, Vicki Cheung, Andrej Karpathy, Durk Kingma, John Schulman, Pamela Vagata and Wojciech Zaremba, with Musk and Altman as co-chairs.[^wiki-openai] A total of $1B was pledged by Musk, Altman, Brockman, Reid Hoffman, Jessica Livingston, Peter Thiel, Amazon Web Services and Infosys, and the same source records that collected capital lagged the pledges substantially, citing tax filings.[^wiki-openai]

Only one of those founders, Sam Altman, has a file of his own in this batch; the other ten are recorded as not-yet-written targets, which is what makes the founder-count question answerable by traversal later rather than by re-reading this file.

Musk resigned from the board in 2018.[^wiki-openai] Altman became CEO in March 2019 after leaving Y Combinator.[^wiki-altman] The 2023 removal and reinstatement is the event that made the governance structure legible: the board cited a lack of confidence and later, through board member Helen Toner, described withheld information; the employee letter and investor pressure reversed it within five days.[^wiki-openai] [^wiki-altman]

## Research background

The techniques OpenAI is identified with are the ones its own papers put into the field's common practice.

* **Reinforcement learning from human feedback.** The 2022 InstructGPT paper is the published pipeline: fine-tune on labeler demonstrations, then on rankings of model outputs, and the result follows instructions better than a larger unmodified model. Its opening claim - that making models bigger does not inherently make them better at following intent - is the reason alignment work is a discipline rather than a scaling parameter.[^instructgpt]
* **Few-shot learning as a consequence of scale.** GPT-3, at 175 billion parameters, was presented as reaching competitive task-agnostic few-shot performance without task-specific fine-tuning, which is the result that made prompting a product surface.[^gpt3]
* **Systems over single models.** GPT-5 is described not as one network but as a system containing a fast high-throughput model, a deeper reasoning model, and a real-time router that decides which to use based on the conversation, its complexity, tool needs and explicit user instruction.[^wiki-gpt5]

## How the frontier models are built

* **Router-based composition.** The GPT-5 system's router was criticised on release for inconsistent routing between models; the same source records that the API exposes adjustable reasoning effort and verbosity, which moves the choice partly to the caller.[^wiki-gpt5]
* **Open-weight releases as a parallel track.** GPT-OSS, two open-weight reasoning-capable models, shipped on 2025-08-05, two days before GPT-5 was unveiled.[^wiki-gpt5]
* **Agent infrastructure as a first-class product.** As of September 2026 the vendor's own documentation ships an Agents API, sandboxes, multi-agent orchestration, guardrails, evals and MCP connections as documented surfaces rather than as demonstrations.[^openai-docs]
* **Not in this batch.** Parameter counts, mixture-of-experts use, pretraining corpus composition and training compute volumes are not published by the company and are not stated here. The largest hole in this file is the same one as in the Anthropic file, and it is a hole in the public record rather than in the research.

## Models and products

| Product | What it is | Source |
| --- | --- | --- |
| ChatGPT | The consumer and business product, including Deep Research, Search and the Atlas browser | [^wiki-openai] |
| API | Access to the GPT models, GPT Image and audio models | [^openai-docs] |
| Codex | AI coding agent, with a CLI and a Codex Sites publishing feature | [^wiki-openai] |
| GPT Image | Image generation and editing models | [^wiki-openai] |
| Whisper | Speech recognition | [^wiki-openai] |
| Sora | Short-form AI video, launched December 2024 and discontinued by late March 2026 | [^wiki-openai] |
| Agents API, GPT-Live-1 | Agent API and a realtime voice model, both announced 2026-09-10 | [^openai-news] |

The current API model list as published by the vendor includes the GPT-5.6 family - Terra, Sol, Luna and Cyber - and GPT-6 Astra, with the documentation's own quickstart using Astra.[^openai-docs] GPT-6 Astra was announced on 2026-09-09 as "the next generation in intelligence for work", and the vendor describes GPT-5.6 Sol as having been used on quantum computing experiments.[^openai-news] See `/models/gpt.md` for the model lineage.

## Technology stack and compute

| Layer | Detail | Source |
| --- | --- | --- |
| Primary cloud | Microsoft Azure, where OpenAI systems have run since 2019; the 2025 restructuring agreement committed OpenAI to buy $250B of Azure services and Microsoft ceded its right of first refusal over future cloud purchases | [^wiki-openai] |
| Other clouds | Amazon, Cerebras, Google and Oracle are named as compute providers | [^wiki-openai] |
| Silicon partners | Nvidia, AMD and Broadcom | [^wiki-openai] |
| Own infrastructure venture | Stargate Project with Oracle, SoftBank and MGX, announced 2025-01-21 and estimated at $500B over four years | [^wiki-openai] |
| Government work | Partnerships with the US government through Stargate, and with the Department of Defense, Los Alamos National Laboratory and Anduril | [^wiki-openai] |

Google appears here as a supplier while Gemini competes with GPT in the same accounts, and Anthropic's compute deals have the same shape in the other direction. That kind of edge is why this bundle records `customer-of` and `competes-with` as separate types rather than as one relationship field.

## Contributions to the ecosystem

* **RLHF as published practice**, without which the instruction-following layer of every commercial assistant would look different.[^instructgpt]
* **Open-weight reasoning models** through GPT-OSS.[^wiki-gpt5]
* **Support for MCP** rather than a competing protocol, documented in the vendor's own agent tooling.[^openai-docs]
* **Standardised interfaces for agents** through the Agents API and its associated tools, announced 2026-09-10.[^openai-news]

## Relations

Outbound edges are in the frontmatter `relations` block. Two structural notes are worth recording in prose because they are the most query-relevant facts in the file.

First, the commercial relationship with Microsoft is unusual enough that a single edge cannot carry it: Microsoft is simultaneously an investor of over $13B, a 27% shareholder valued at $135B, the primary cloud supplier under a $250B commitment, and a distributor of OpenAI models inside Copilot, while being a competitor in enterprise AI through its own products.[^wiki-openai]

Second, the coding-agent market places OpenAI on both sides of several relationships at once: Replit, Lovable and Figma are partners for Codex Sites and competitors in agentic software creation, and OpenAI terminated Cursor's API access in August 2026 after Cursor's acquisition by SpaceX.[^wiki-openai]

## Commercials

| Fact | Value | As of | Source |
| --- | --- | --- | --- |
| Founded | 2015-12 | - | [^wiki-openai] |
| Microsoft cumulative investment | over $13B | 2026 | [^wiki-openai] |
| October 2024 round | $6.6B raised, $157B valuation | 2024-10 | [^wiki-openai] |
| April 2025 round | $40B raised, $300B post-money | 2025-04 | [^wiki-openai] |
| Employee share sale | up to $10B, $500B valuation | 2025-10 | [^wiki-openai] |
| February 2026 round | $110B raised, $730B valuation; extended to $120B | 2026-02 | [^wiki-openai] |
| 2026 round close | $122B committed capital, $852B post-money | 2026-04 | [^wiki-openai] |
| Run-rate revenue | $12B annualized, up from $3.7B in 2024 | 2025-07 | [^wiki-openai] |
| Paid subscribers | 20 million, up from 15.5 million at the end of 2024 | 2025-04 | [^wiki-openai] |
| Business users | 5 million | 2025-07 | [^wiki-openai] |
| Advertising | about $2.5B projected for the year; $1B annualized run rate about 200 days after launch | 2026-04 and 2026-08 | [^wiki-openai] |
| Forecast | cash-flow positive by 2029; about $200B revenue by 2030, company forecast | - | [^wiki-openai] |
| Headcount | Not established in this batch; the only figure read is about 770 employees at the time of the November 2023 board crisis | 2023-11 | [^wiki-openai] |

## Disputed and unverified

1. **The 2026 round's date and size conflict inside one source.** Wikipedia's lead says the company closed a round with an $852B post-money valuation in March 2026, while its body says the closure of $122B at $852B was announced in April 2026. Both readings are recorded; this batch did not resolve which is right.[^wiki-openai]
2. **Revenue is stale.** The $12B annualized figure is from July 2025. Nothing read here gives a 2026 revenue number, and the file deliberately does not extrapolate one.[^wiki-openai]
3. **Headcount is unknown.** The company does not publish it and no estimate was retrieved, unlike Anthropic where estimates existed but conflicted.[^wiki-openai]
4. **The September 2026 mathematics claim.** Wikipedia records that OpenAI claimed to have used around 10,000 agents running an internal model to solve the Navier-Stokes existence and smoothness problem, a Millennium Prize problem. The claim is extraordinary, the source is a company statement, and no independent verification was retrieved.[^wiki-openai]
5. **Sora's discontinuation** and **the termination of Cursor's API access after its acquisition by SpaceX** are each recorded from a single source, and both are recent enough that the sources may still be settling.[^wiki-openai]
6. **Founder roles after founding** are recorded loosely in the source: Wikipedia lists Sutskever and Brockman as overseeing day-to-day work through 2017, and does not give departure dates for most of the founding group in the passages read.[^wiki-openai]

[^wiki-openai]: Wikipedia, "OpenAI", https://en.wikipedia.org/wiki/OpenAI
[^wiki-gpt5]: Wikipedia, "GPT-5", https://en.wikipedia.org/wiki/GPT-5
[^wiki-altman]: Wikipedia, "Sam Altman", https://en.wikipedia.org/wiki/Sam_Altman
[^openai-news]: OpenAI, news index, https://openai.com/news/
[^openai-docs]: OpenAI, API documentation and model index, https://platform.openai.com/docs/models
[^gpt3]: Brown et al., "Language Models are Few-Shot Learners", https://arxiv.org/abs/2005.14165
[^instructgpt]: Ouyang et al., "Training language models to follow instructions with human feedback", https://arxiv.org/abs/2203.02155
