---
type: UseCase
title: AI in the software development lifecycle
description: Code generation, review, testing and maintenance performed or assisted by AI models; the use case with the strongest independent experimental evidence and the largest gap between forecast and measured effect.
resource: https://dora.dev/research/2025/dora-report/
tags:
  - ai-sdlc
  - coding-agents
  - developer-productivity
  - code-review
  - benchmarks
aliases:
  - AI-assisted software development
  - AI-SDLC
  - Vibe coding (colloquial)
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-10T20:05:08Z
stale_after: 2027-03-10T00:00:00Z
relations:
  - { type: related-to, target: /ai-domains/agentic-ai.md }
  - { type: related-to, target: /ai-use-cases/no-code-app-building.md }
  - { type: related-to, target: /technologies/mcp.md }
sources:
  - id: copilot-rct
    resource: https://arxiv.org/abs/2302.06590
    title: "Peng et al., 'The Impact of AI on Developer Productivity: Evidence from GitHub Copilot'"
    author: human:peng-et-al
  - id: metr-rct
    resource: https://arxiv.org/abs/2507.09089
    title: Becker et al., "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity"
    author: human:becker-et-al
  - id: swebench
    resource: https://arxiv.org/abs/2310.06770
    title: "Jimenez et al., 'SWE-bench: Can Language Models Resolve Real-World GitHub Issues?'"
    author: human:jimenez-et-al
  - id: sweagent
    resource: https://arxiv.org/abs/2405.15793
    title: "Yang et al., 'SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering'"
    author: human:yang-et-al
  - id: dora-2025
    resource: https://dora.dev/research/2025/dora-report/
    title: DORA, "State of AI-assisted Software Development" (2025)
    author: org:dora
  - id: anthropic-replit-case
    resource: https://www.anthropic.com/customers/replit
    title: "Anthropic, 'Replit: agentic software creation on Claude'"
    author: org:anthropic
  - id: wiki-claude
    resource: https://en.wikipedia.org/wiki/Claude_(language_model)
    title: Wikipedia, "Claude (language model)"
    author: wiki:en
  - id: wiki-openai
    resource: https://en.wikipedia.org/wiki/OpenAI
    title: Wikipedia, "OpenAI"
    author: wiki:en
---

# AI in the software development lifecycle

## Definition and boundary

This use case covers AI applied to producing and maintaining software: writing code, reviewing it, writing tests, diagnosing failures and doing the maintenance work that dominates a mature repository. It is deliberately separated from `/ai-use-cases/no-code-app-building.md`, where the product's user is not a developer and the artifact is a deployed application rather than a change to an existing codebase. The two overlap in tooling and are kept apart because the evidence about them is not the same.

## The measured evidence, which does not agree with itself

Two randomised controlled trials sit at the centre of this file, and a reader should hold both.

| Study | Setting | Design | Result |
| --- | --- | --- | --- |
| GitHub Copilot, 2023 | Recruited developers implementing an HTTP server in JavaScript as quickly as possible | Controlled experiment, treatment had Copilot access | The treatment group finished 55.8% faster than the control group | [^copilot-rct] |
| METR, 2025 | 16 experienced open-source developers, 246 tasks in mature projects they had averaged five years on | Randomised per task, AI allowed or disallowed | Developers forecast a 24% time reduction and believed after the study that AI had cut their time by 20%; measurement showed completion time **increased** by 19%. Economists predicted 39% shorter and ML experts 38% shorter | [^metr-rct] |

The two are not necessarily contradictory - a single greenfield task in a familiar language, and sustained work in a mature repository with established quality standards, are different populations of work - but this bundle does not adjudicate between them and records the conflict instead. METR's authors also state that experimental artefacts cannot be entirely ruled out, while reporting that the slowdown was robust across their analyses.[^metr-rct]

## Benchmark evidence

Progress in the use case is usually argued from SWE-bench, which is 2,294 problems drawn from real GitHub issues and their pull requests across 12 popular Python repositories, where a solution often requires coordinated changes across files.[^swebench] SWE-agent showed that the interface given to the model changes measured performance in the same setting, which is why agent harness design is treated as part of the result rather than as plumbing.[^sweagent]

## Organisational evidence

DORA's 2025 study of AI-assisted software development reports AI as an amplifier rather than a level: the largest returns come from the underlying sociotechnical systems rather than from tool adoption alone.[^dora-2025] The same study is the source most often cited for the claim that individual-level speedups do not automatically become delivery-level throughput, and this file records the distinction rather than the slogan.

## Products that occupy the use case

| Product | Owner | Note | Source |
| --- | --- | --- | --- |
| Claude Code | Anthropic | Research preview 2025-02, generally available 2025-05 with Claude 4; Anthropic reported a 5.5x increase in Claude Code revenue by July after enterprise adoption | [^wiki-claude] |
| Codex | OpenAI | Described by its vendor as an AI coding agent; the Codex Sites feature shipped in June 2026 with Wix, Base44, Replit, Lovable, Figma and Emergent as partners | [^wiki-openai] |
| Replit Agent | Replit | Claude is the model behind Replit Agent, and the vendor case study describes agent sessions running for six hours and longer | [^anthropic-replit-case] |

## Disputed and unverified

1. **Whether AI speeds up professional software work.** The Copilot and METR results point in opposite directions; this file deliberately holds both and marks the question open.
2. **Vendor productivity claims.** Revenue growth, session length and adoption figures in this file are company-reported and unaudited.
3. **Benchmark-to-production transfer.** No source read here establishes that a SWE-bench score predicts performance inside a customer's repository.
4. **Task-level versus delivery-level effect.** The DORA framing implies they differ; the size of the gap is not established in the sources read.

[^copilot-rct]: Peng et al., "The Impact of AI on Developer Productivity: Evidence from GitHub Copilot", https://arxiv.org/abs/2302.06590
[^metr-rct]: Becker et al., "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", https://arxiv.org/abs/2507.09089
[^swebench]: Jimenez et al., "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?", https://arxiv.org/abs/2310.06770
[^sweagent]: Yang et al., "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering", https://arxiv.org/abs/2405.15793
[^dora-2025]: DORA, "State of AI-assisted Software Development" (2025), https://dora.dev/research/2025/dora-report/
[^anthropic-replit-case]: Anthropic, "Replit: agentic software creation on Claude", https://www.anthropic.com/customers/replit
[^wiki-claude]: Wikipedia, "Claude (language model)", https://en.wikipedia.org/wiki/Claude_(language_model)
[^wiki-openai]: Wikipedia, "OpenAI", https://en.wikipedia.org/wiki/OpenAI
