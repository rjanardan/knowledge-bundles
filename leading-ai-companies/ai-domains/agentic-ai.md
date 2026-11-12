---
type: Domain
title: Agentic AI
description: Systems in which a model takes actions in a loop against tools and an environment, rather than answering once; the domain where tool protocols and agent benchmarks live.
resource: https://arxiv.org/abs/2210.03629
tags:
  - agentic-ai
  - tool-use
  - agents
  - long-horizon
  - mcp
  - evaluation
aliases:
  - Agents
  - Agentic systems
  - Tool use
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-10T20:05:08Z
stale_after: 2027-09-10T00:00:00Z
relations:
  - { type: related-to, target: /technologies/mcp.md }
  - { type: related-to, target: /ai-use-cases/ai-sdlc.md }
  - { type: related-to, target: /ai-domains/foundation-models.md }
sources:
  - id: react
    resource: https://arxiv.org/abs/2210.03629
    title: "Yao et al., 'ReAct: Synergizing Reasoning and Acting in Language Models'"
    author: human:yao-et-al
  - id: toolformer
    resource: https://arxiv.org/abs/2302.04761
    title: "Schick et al., 'Toolformer: Language Models Can Teach Themselves to Use Tools'"
    author: human:schick-et-al
  - id: swebench
    resource: https://arxiv.org/abs/2310.06770
    title: "Jimenez et al., 'SWE-bench: Can Language Models Resolve Real-World GitHub Issues?'"
    author: human:jimenez-et-al
  - id: sweagent
    resource: https://arxiv.org/abs/2405.15793
    title: "Yang et al., 'SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering'"
    author: human:yang-et-al
  - id: anthropic-agents
    resource: https://www.anthropic.com/engineering/building-effective-agents
    title: Anthropic, "Building effective agents"
    author: org:anthropic
  - id: wiki-mcp
    resource: https://en.wikipedia.org/wiki/Model_Context_Protocol
    title: Wikipedia, "Model Context Protocol"
    author: wiki:en
  - id: openai-news
    resource: https://openai.com/news/
    title: OpenAI, news index
    author: org:openai
  - id: dm-site
    resource: https://deepmind.google/
    title: Google DeepMind, home page and model index
    author: org:google-deepmind
---

# Agentic AI

## Definition

Agentic AI here means a model that acts, observes the result and acts again, against tools and an environment, instead of producing a single response. The pattern that named the field is ReAct, which generates reasoning traces and task-specific actions in an interleaved way: the traces let the model track and revise a plan, and the actions let it reach knowledge bases and environments for information it does not hold.[^react] The paper's point was that reasoning and acting had been studied separately, and that interleaving them is what produces the synergy.[^react]

## How the capability is acquired

| Mechanism | What it does | Source |
| --- | --- | --- |
| Prompted interleaving | Reasoning traces and actions alternate in the context, with no training required beyond prompting | [^react] |
| Self-supervised tool learning | Toolformer teaches a model to decide which API to call, when to call it, what arguments to pass and how to use the result, from a handful of demonstrations per API | [^toolformer] |
| Interface design | SWE-agent found that the agent-computer interface changes task performance, treating the model as a new class of user with its own needs | [^sweagent] |
| Orchestration patterns | Anthropic's engineering guidance separates workflows, where the model follows fixed paths, from agents, where it directs its own process, and recommends the simplest composable pattern that works over a framework | [^anthropic-agents] |

## How the domain is evaluated

The shift that defines the current generation is from short question answering to long-horizon work in real repositories. SWE-bench is 2,294 software engineering problems drawn from real GitHub issues and their pull requests across 12 popular Python repositories, where resolving an issue frequently requires coordinated edits across functions, classes and files.[^swebench] SWE-agent extended the same setting to interfaces, and reported that the custom interface materially improved the agent's ability to create and edit code and navigate repositories.[^sweagent]

The honest limit of this section: an agent benchmark score is a measurement of task completion under a specific harness. No source read in this batch establishes that a benchmark leader performs at the same rate inside a customer's own codebase, and the file does not claim it.

## The protocol layer

Agentic systems needed a portable way to reach tools, which is the gap the Model Context Protocol was introduced to fill in November 2024.[^wiki-mcp] The domain and the protocol are now hard to describe separately: the protocol's own revision history is the clearest public record of what the domain's practitioners found underspecified, most recently the July 2026 removal of protocol-level session tracking.[^wiki-mcp] See `/technologies/mcp.md`.

## Who is recorded as operating here

Anthropic (Claude Code, Claude Cowork), Replit (Replit Agent), OpenAI (Codex, and an Agents API announced 2026-09-10) and Google DeepMind (a Gemini Flash release described by its maker as its most intelligent workhorse for coding and agents) each carry an `operates-in` edge to this path.[^openai-news] [^dm-site] Google and Google DeepMind are written separately in this bundle because the parent company sells cloud and silicon while the lab builds the models.

## Disputed and unverified

1. **Autonomy in production.** Every autonomy figure in this file comes from a vendor or a benchmark harness. The bundle holds no independent measurement of unattended agent reliability.
2. **Benchmark leakage.** Sources read here do not establish whether the public SWE-bench split is contaminated in current training corpora. Recorded as open.
3. **"Agent" as a product label.** The word is applied in the sources to terminal coding tools, browser controllers and multi-step chat workflows alike. This file does not attempt to police the term.

[^react]: Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models", https://arxiv.org/abs/2210.03629
[^toolformer]: Schick et al., "Toolformer: Language Models Can Teach Themselves to Use Tools", https://arxiv.org/abs/2302.04761
[^swebench]: Jimenez et al., "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?", https://arxiv.org/abs/2310.06770
[^sweagent]: Yang et al., "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering", https://arxiv.org/abs/2405.15793
[^anthropic-agents]: Anthropic, "Building effective agents", https://www.anthropic.com/engineering/building-effective-agents
[^wiki-mcp]: Wikipedia, "Model Context Protocol", https://en.wikipedia.org/wiki/Model_Context_Protocol
[^openai-news]: OpenAI, news index, https://openai.com/news/
[^dm-site]: Google DeepMind, home page and model index, https://deepmind.google/
