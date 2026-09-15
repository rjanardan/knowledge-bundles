---
type: UseCase
title: Computer use
description: The use case in which a model drives a graphical interface - a browser or a desktop - by perceiving the screen and generating mouse and keyboard actions, rather than through an API; the capability Claude implemented with its computer-use tool and OpenAI with Operator.
resource: https://www.anthropic.com/docs/agents/tools/computer-use
tags:
  - computer-use
  - agentic-ai
  - browser-automation
  - gui-agents
aliases:
  - Computer use models
  - GUI agents
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-15T06:32:10Z
stale_after: 2026-12-14T00:00:00Z
relations:
  - { type: related-to, target: /ai-domains/agentic-ai.md }
  - { type: related-to, target: /ai-use-cases/ai-sdlc.md }
  - { type: related-to, target: /technologies/mcp.md }
sources:
  - id: anthropic-computer-use
    resource: https://www.anthropic.com/docs/agents/tools/computer-use
    title: "Anthropic, computer use documentation"
    author: "org:anthropic"
  - id: wiki-claude
    resource: https://en.wikipedia.org/wiki/Claude_(language_model)
    title: "Claude (language model)"
    author: "wiki:en"
  - id: wiki-openai
    resource: https://en.wikipedia.org/wiki/OpenAI
    title: "OpenAI"
    author: "wiki:en"
  - id: wiki-chatgpt
    resource: https://en.wikipedia.org/wiki/ChatGPT
    title: "ChatGPT"
    author: "wiki:en"
---

# Computer use

## Definition

Computer use here means a model that drives a graphical interface — a browser or a full desktop — by interpreting a screenshot of the screen and emitting mouse and keyboard actions, instead of calling an API. It is the branch of `/ai-domains/agentic-ai.md` that trades the reliable, typed tool interface of an API for the generality of whatever a human could do with a mouse.[^anthropic-computer-use]

## Who occupies the use case

| Product | Vendor | Notes | Source |
| --- | --- | --- | --- |
| Claude computer use | Anthropic | Introduced the computer-use tool with Claude 3.5 Sonnet (upgraded, 2024-10); Anthropic describes it as driving the browser by perceiving the screen and moving the cursor | [^wiki-claude] [^anthropic-computer-use] |
| Claude in Chrome | Anthropic | Chrome extension built on computer use; pilot 2025-08, general availability August 2026, vendor-reported prompt-injection success at 11.2% after mitigations | [^wiki-claude] |
| Operator | OpenAI | Desktop/browser agent shipping under chatgpt; the flagship agentic-computer product from OpenAI | [^wiki-chatgpt] |

## Why the security profile matters

A computer-use agent is a new attack surface because the very generality that makes it useful — it will click anything a human could click — is also what an injection can exploit. Claude in Chrome is the documented case: after mitigations Anthropic reported an 11.2% prompt-injection success rate, a figure that is vendor-reported and unaudited.[^wiki-claude] This is why computer use is treated in the bundle as its own use case rather than folded into agentic AI generally: its threat model is distinct from a tool-using agent that only talks to an allow-listed API.

## Relation to the other use cases

Computer use sits at the edge of two other branches. It overlaps with `/ai-use-cases/ai-sdlc.md` where an agent edits files rather than calling a code API (Replit described its visual self-testing as faster and cheaper than a general computer-use loop),[^wiki-claude] and with `/ai-use-cases/enterprise-knowledge.md` where a browser agent reads internal web apps. The distinctive property is that the interface — the screen — is itself part of the attack surface.

## Disputed and unverified

1. **Prompt-injection figures.** The 11.2% success rate after mitigations is Anthropic's own measurement, published by the company, and not independently verified.[^wiki-claude]
2. **Practical reliability.** No independent, quantitative evaluation of computer-use agents at production scale was read for this batch; vendors' claims and the documented injection risk are recorded, not adjudicated.
3. **Boundary with API-tool agents.** A model that prefers an API when one exists is doing agentic AI, not computer use; the line is blurry in practice and consumers should not over-assign every GUI product to this file.

[^anthropic-computer-use]: Anthropic, computer use documentation, https://www.anthropic.com/docs/agents/tools/computer-use
[^wiki-claude]: Wikipedia, "Claude (language model)", https://en.wikipedia.org/wiki/Claude_(language_model)
[^wiki-openai]: Wikipedia, "OpenAI", https://en.wikipedia.org/wiki/OpenAI
[^wiki-chatgpt]: Wikipedia, "ChatGPT", https://en.wikipedia.org/wiki/ChatGPT