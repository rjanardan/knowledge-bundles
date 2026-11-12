---
type: Model
title: Claude
description: The large language model family sold by Anthropic, named after Claude Shannon, trained with a written constitution, and released in capability tiers from Haiku to Opus, with Mythos and Fable added in 2026.
resource: https://docs.claude.com/en/docs/about-claude/models/overview
tags:
  - llm
  - frontier-models
  - model-family
  - constitutional-ai
  - agentic-ai
aliases:
  - Claude
  - Claude models
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-10T20:05:08Z
stale_after: 2026-12-10T00:00:00Z
relations:
  - { type: developed-by, target: /companies/anthropic.md, since: 2023-03 }
  - { type: related-to, target: /models/gpt.md }
  - { type: related-to, target: /models/gemini.md }
  - { type: related-to, target: /ai-domains/foundation-models.md }
sources:
  - id: wiki-claude
    resource: https://en.wikipedia.org/wiki/Claude_(language_model)
    title: Wikipedia, "Claude (language model)"
    author: wiki:en
  - id: claude-docs
    resource: https://docs.claude.com/en/docs/about-claude/models/overview
    title: Anthropic, "Models overview"
    author: org:anthropic
  - id: cai
    resource: https://arxiv.org/abs/2212.08073
    title: "Bai et al., 'Constitutional AI: Harmlessness from AI Feedback'"
    author: human:bai-et-al
  - id: claude-3-family
    resource: https://www.anthropic.com/news/claude-3-family
    title: Anthropic, "Introducing the next generation of Claude"
    author: org:anthropic
  - id: anthropic-replit-case
    resource: https://www.anthropic.com/customers/replit
    title: "Anthropic, 'Replit: agentic software creation on Claude'"
    author: org:anthropic
---

# Claude

## What it is

Claude is the family of large language models developed by Anthropic, released first as a chatbot in March 2023 and used since then for general assistance and AI-assisted software development.[^wiki-claude] The family is reportedly named after Claude Shannon.[^wiki-claude]

Anthropic sells it three ways: a first-party API, subscription products around the chatbot, and availability on all three major clouds through its partners. The bundle records the commercial side in `/companies/anthropic.md` and keeps this file on the model itself.

## The training method that distinguishes it

Claude is trained using a constitution - a written set of principles, not a set of human preference labels - which is the published method known as Constitutional AI.[^wiki-claude] The method has two phases. In the supervised phase the model samples from itself, generates self-critiques and revisions against the constitution, and is fine-tuned on the revised responses. In the reinforcement-learning phase the model's own evaluations of pairs of samples are used to train a preference model, which then trains the policy.[^cai] The purpose stated in the paper is to train a harmless assistant through self-improvement without human labels identifying harmful outputs, with the only human oversight being the list of principles.[^cai]

The technique was first applied to a general product model with the Claude 3 generation, announced on 2024-03-04, when Anthropic also introduced the three-size convention that still structures the family: Haiku, Sonnet and Opus.[^claude-3-family] [^wiki-claude]

## Capability tiers

| Tier | Position | Source |
| --- | --- | --- |
| Haiku | Fastest and cheapest; the current generation is Haiku 4.5 | [^claude-docs] |
| Sonnet | Described by the vendor as the best combination of speed and intelligence; the current generation is Sonnet 5 | [^claude-docs] |
| Opus | Described as the tier for complex agentic coding and enterprise work; the current generation is Opus 5 | [^claude-docs] |
| Mythos | Restricted to a trusted-access programme; Mythos 5.1 is the current revision | [^wiki-claude] [^claude-docs] |
| Fable | Highest stated capability tier for demanding reasoning and long-horizon agentic work; the current revision is Fable 5.1 | [^claude-docs] |

That the tier split is a real deployment practice rather than marketing is supported from the customer side: Replit uses Sonnet for sustained development work and Opus for architecture and multi-file refactoring.[^anthropic-replit-case]

## Release timeline

| Model | Released | Note |
| --- | --- | --- |
| Claude | 2023-03 | First release, as a chatbot | 
| Claude 2 | 2023-07 | |
| Claude 2.1 | 2023-11 | 200K context window; tool use |
| Claude 3 (Opus, Sonnet, Haiku) | 2024-03 | Tier convention introduced |
| Claude 3.5 Sonnet | 2024-06 | |
| Claude 3.5 Sonnet (upgraded) | 2024-10 | Computer use |
| Claude 3.7 Sonnet | 2025-02 | |
| Claude 4 (Opus 4, Sonnet 4) | 2025-05 | Released with Claude Code general availability |
| Claude Sonnet 4.5 | 2025-09 | |
| Claude Haiku 4.5 | 2025-10 | |
| Claude Opus 4.5 | 2025-11 | |
| Claude Opus 4.6, Sonnet 4.6 | 2026-02 | Agent teams; Claude in PowerPoint |
| Claude Opus 4.7 | 2026-04 | |
| Claude Opus 4.8 | 2026-05 | |
| Claude Fable 5, Mythos 5 | 2026-06-09 | Mythos 5 released through Project Glasswing; Fable 5 launched publicly |
| Claude Sonnet 5 | 2026-06-30 | |
| Claude Opus 5 | 2026-07-24 | 3D rendering capabilities added |
| Claude Fable 5.1, Mythos 5.1 | 2026-09-01 | Vendor states roughly 25% lower cost on typical token-billed workloads and up to about 45% lower on agentic workloads, attributed to efficiency |

Source for the table: Wikipedia's Claude article, which is a secondary source for release dates; Anthropic's own models overview was read for the current lineup, not for every historical row.[^wiki-claude] [^claude-docs]

## Controlled access and guardrails

The Mythos tier began as a restricted release. Its existence became public in March 2026 through leaked draft blog posts, and on 2026-04-07 Anthropic announced Project Glasswing, releasing Mythos Preview to 11 organisations to find and fix cybersecurity vulnerabilities.[^wiki-claude] Access was expanded on 2026-06-02 to 150 organisations in more than 15 countries.[^wiki-claude] Fable 5 shipped with additional guardrails that restrict responses in high-risk domains such as cybersecurity and biology and downgrade a request to Opus 4.8 when it is classified as high-risk, while the less restricted Mythos 5 stayed in the trusted-access programme.[^wiki-claude]

## Products built on the family

Claude Code (terminal coding agent, preview 2025-02, general availability 2025-05, web version 2025-10), Claude Cowork (a graphical tool for non-programmers, preview 2026-01), Claude in Chrome (browser control; the vendor reported prompt-injection success at 11.2% after mitigations, and general availability in August 2026), Claude Design (2026-04-17) and Claude Science (announced 2026-06-30).[^wiki-claude]

## Not disclosed

Parameter counts, whether a mixture-of-experts architecture is used, pretraining data composition and training compute are not published by Anthropic, and no source read for this batch states them. The fields are left empty rather than filled by inference, which is the bundle's standing rule where a vendor does not disclose.

## Disputed and unverified

1. **Release dates.** Every date in the timeline above comes from Wikipedia rather than from Anthropic's own release notes, which were not read row by row.[^wiki-claude]
2. **Cost claims.** The 25% and 45% reductions attributed to Fable 5.1 are vendor statements and unaudited.[^wiki-claude]
3. **Naming churn.** The family gained the Mythos and Fable tiers during 2026; older secondary sources describe a three-tier family only, and any consumer of this bundle should treat the tier list as a moving target with a 90-day staleness window.
4. **Behavioural complaints are not adjudicated here.** Social-media reports that one release regressed against its predecessor appear in the source and are recorded rather than resolved.[^wiki-claude]

[^wiki-claude]: Wikipedia, "Claude (language model)", https://en.wikipedia.org/wiki/Claude_(language_model)
[^claude-docs]: Anthropic, "Models overview", https://docs.claude.com/en/docs/about-claude/models/overview
[^cai]: Bai et al., "Constitutional AI: Harmlessness from AI Feedback", https://arxiv.org/abs/2212.08073
[^claude-3-family]: Anthropic, "Introducing the next generation of Claude", https://www.anthropic.com/news/claude-3-family
[^anthropic-replit-case]: Anthropic, "Replit: agentic software creation on Claude", https://www.anthropic.com/customers/replit
