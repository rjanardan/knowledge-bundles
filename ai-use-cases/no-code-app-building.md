---
type: UseCase
title: No-code application building
description: Turning natural-language prompts into deployed web applications without writing code, addressed to non-developers; the platform that opened the market is Replit, and the agentic-tooling frontier crossed into it as vendors added prompt-to-app agents.
resource: https://replit.com/about
tags:
  - vibe-coding
  - prompt-to-app
  - no-code
  - app-builder
  - agents
aliases:
  - No-code app development
  - Prompt-to-app
  - Vibe coding platforms
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-15T06:31:40Z
stale_after: 2026-12-14T00:00:00Z
relations:
  - { type: related-to, target: /ai-use-cases/ai-sdlc.md }
  - { type: related-to, target: /ai-use-cases/computer-use.md }
  - { type: related-to, target: /ai-domains/agentic-ai.md }
  - { type: related-to, target: /technologies/mcp.md }
sources:
  - id: wiki-lovable
    resource: https://en.wikipedia.org/wiki/Lovable_(company)
    title: "Lovable (company)"
    author: "wiki:en"
  - id: wiki-replit
    resource: https://en.wikipedia.org/wiki/Replit
    title: "Replit"
    author: "wiki:en"
  - id: wiki-anysphere
    resource: https://en.wikipedia.org/wiki/Anysphere
    title: "Anysphere"
    author: "wiki:en"
  - id: anthropic-replit-case
    resource: https://www.anthropic.com/customers/replit
    title: "Replit: agentic software creation on Claude"
    author: "org:anthropic"
  - id: wiki-copilot
    resource: https://en.wikipedia.org/wiki/GitHub_Copilot
    title: "GitHub Copilot"
    author: "wiki:en"
---

# No-code application building

## Boundary

This use case covers products whose user is not primarily a developer and whose output is a deployed application rather than a change to an existing codebase. It is deliberately separated from `/ai-use-cases/ai-sdlc.md`, where the user is a developer and the artifact is a change to software under version control. The two overlap in tooling — Replit and Lovable sit on a continuum with coding-assist agents — and are kept apart because the evidence and the failure modes are not the same.[^anthropic-replit-case]

## Who occupies the use case

| Product / platform | Owner | Notes | Source |
| --- | --- | --- | --- |
| Replit | Replit | YC W18; the pitch is "prompt-to-production" — generate, run and deploy from one environment. Runs on Claude; agent sessions run for six hours and longer | [^wiki-replit] [^anthropic-replit-case] |
| Lovable | Lovable (Sweden) | Launched open access December 2024; $200M Series A (Feb 2025) at $1.8B, $330M Series B (Dec 2025) at $6.6B, $400M Series C (Aug 2026) at $13.3B; 60M projects, 900M monthly visitors as of Aug 2026 | [^wiki-lovable] |
| Cursor (Anysphere) | Anysphere / SpaceXAI | AI coding agent and IDE; largely a developer tool, but shipped no-code-ish agents for web/mobile/CLI/cloud. $29.3B valuation, >$3B ARR by early 2026; acquired by SpaceXAI (closed Aug 2026) | [^wiki-anysphere] |
| GitHub Copilot | Microsoft | Heavily developer-facing; included here as the boundary case for the coding-assist continuum | [^wiki-copilot] |

## How the evidence reads

The customer base for no-code AI is largely non-developers — Georgian, the Series D lead at Replit, described the target as students, teachers, designers, small business owners and engineers.[^anthropic-replit-case] That the market now supports these valuations rests almost entirely on company-reported usage and funding numbers, which this file records as vendor-stated and unaudited: Lovable's 60M projects and 900M monthly visitors,[^wiki-lovable] Replit's "50 million users"[^anthropic-replit-case] and $9B Series D[^wiki-replit], and Cursor's $3B ARR.[^wiki-anysphere] No independent audit of any of these figures was read for this batch.

## Relation to the SDLC use case

The cleanest read of the boundary is that no-code app-building is what AI-SDLC becomes when the developer is removed from the loop. The same model tier does the work (Claude Sonnet/Opus in Replit),[^anthropic-replit-case] but the failure modes differ: no-code deployments are more exposed to misconfigured security defaults. Lovable's March 2025 incident, in which many of its generated sites had publicly exposed Supabase databases, is the documented example.[^wiki-lovable]

## Disputed and unverified

1. **Vendor-reported usage and ARR.** All the headline numbers in this file come from the companies themselves or from their funding announcements, and none were independently audited in this batch.
2. **Whether "vibe coding" scales to production.** No source read here establishes that prompt-to-app output maintains quality, security or maintainability at enterprise scale; the Supabase exposure incident is the strongest contrary evidence.
3. **The boundary is fuzzy.** Cursor is primarily a developer tool and is included in this file only as the far end of the coding-assist continuum; consumers should not read its ARR as belonging to the no-code market.

[^wiki-lovable]: Wikipedia, "Lovable (company)", https://en.wikipedia.org/wiki/Lovable_(company)
[^wiki-replit]: Wikipedia, "Replit", https://en.wikipedia.org/wiki/Replit
[^wiki-anysphere]: Wikipedia, "Anysphere", https://en.wikipedia.org/wiki/Anysphere
[^anthropic-replit-case]: Anthropic, "Replit: agentic software creation on Claude", https://www.anthropic.com/customers/replit
[^wiki-copilot]: Wikipedia, "GitHub Copilot", https://en.wikipedia.org/wiki/GitHub_Copilot