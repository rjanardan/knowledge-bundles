---
type: UseCase
title: Enterprise knowledge and productivity
description: Using AI on the knowledge a business already holds - internal documents, mail, slides, spreadsheets and web apps - for retrieval, summarisation and document work; the terrain where Copilot, Gemini in the Workspace, NotebookLM/Gemini Notebook and internal-knowledge search compete head to head.
resource: https://en.wikipedia.org/wiki/Microsoft_365_Copilot
tags:
  - enterprise
  - knowledge-management
  - retrieval-augmented-generation
  - copilot
  - productivity
aliases:
  - Enterprise productivity
  - Knowledge work AI
  - Copilots
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-15T06:32:30Z
stale_after: 2026-12-14T00:00:00Z
relations:
  - { type: related-to, target: /ai-use-cases/ai-sdlc.md }
  - { type: related-to, target: /ai-use-cases/scientific-research.md }
  - { type: related-to, target: /ai-domains/foundation-models.md }
sources:
  - id: wiki-m365
    resource: https://en.wikipedia.org/wiki/Microsoft_365_Copilot
    title: "Microsoft 365 Copilot"
    author: "wiki:en"
  - id: wiki-gemini
    resource: https://en.wikipedia.org/wiki/Gemini_(chatbot)
    title: "Gemini (chatbot)"
    author: "wiki:en"
  - id: wiki-notebooklm
    resource: https://en.wikipedia.org/wiki/Gemini_Notebook
    title: "Gemini Notebook (formerly NotebookLM)"
    author: "wiki:en"
  - id: wiki-perplexity
    resource: https://en.wikipedia.org/wiki/Perplexity_AI
    title: "Perplexity AI"
    author: "wiki:en"
  - id: wiki-chatgpt
    resource: https://en.wikipedia.org/wiki/ChatGPT
    title: "ChatGPT"
    author: "wiki:en"
---

# Enterprise knowledge and productivity

## Definition and boundary

This use case covers AI working on the knowledge a business already holds: internal documents, mail, slides, spreadsheets, and the web apps that run the business, for retrieval, summarisation, drafting and document work. It is distinct from `/ai-use-cases/ai-sdlc.md` (the artifact is a document or an action on knowledge, not a codebase change) and from `/ai-use-cases/scientific-research.md` (the audience is an enterprise knowledge worker, not a scientist, and the rigour bar is lower). The boundary that matters is *whose* knowledge is being grounded: this is the use case where grounding is on private, enterprise-held corpora, which is why retrieval and access control are the central capabilities.[^wiki-m365]

## The landscape

| Product | Vendor | Notes | Source |
| --- | --- | --- | --- |
| Microsoft 365 Copilot | Microsoft | Ship of the copilot analogy; Bing Chat (launched Feb 2023) was unified under Copilot branding through 2023; the M365 app arrived Jan 2025. Natively grounded in the tenant's mail, files and calendar | [^wiki-m365] |
| Gemini for Workspace | Google | Gemini/Google Workspace integration; the vendor's answer to Copilot, competing head-to-head on the same document surface | [^wiki-gemini] |
| Gemini Notebook (formerly NotebookLM) | Google | Grounded retrieval over uploaded documents; popular Audio Overviews (podcast-like summaries) and Slide Deck/Infographics outputs | [^wiki-notebooklm] |
| ChatGPT Enterprise / Team | OpenAI | Enterprise tier of ChatGPT with org separation and admin controls | [^wiki-chatgpt] |
| Perplexity Internal Knowledge Search | Perplexity | Pro/Enterprise feature to browse web and internal documents together; Enterprise Pro indexes up to 500 files | [^wiki-perplexity] |

## The competitive core

The Copilot frame is the clearest single thread in this use case. Microsoft launched Bing Chat in February 2023 explicitly to preempt Google after ChatGPT threatened the search duopoly, and by the end of 2023 had unified its various assistants under the "Copilot" brand.[^wiki-m365] Google responded with Bard, rushed out days before Microsoft's February 2023 event (after Google's own emergency meetings and its co-founders re-entering the room), and the two have competed head to head in the productivity suite ever since.[^wiki-m365] [^wiki-gemini] The bundle records that competitive thread as a single use-case because it is one *market* — knowledge work on private documents — even though the products are rivalling across two vendors.

The secondary thread is retrieval grounding. Gemini Notebook, Perplexity's Internal Knowledge Search and (more recently) ChatGPT grounded in an enterprise corpus all carry the same promise — answer from the documents you actually have, with provenance — and differ mainly on how much external web knowledge they blend in.[^wiki-notebooklm] [^wiki-perplexity] [^wiki-chatgpt]

## Evidence quality note

Almost all product claims in this file are vendor-described. The three most independently attested facts are (a) the Bing Chat launch and its roll-out dates, (b) the Prometheus model built on OpenAI's GPT line, and (c) Perplexity's March-2023-env legal and scraping controversies, which were independently reported.[^wiki-m365] [^wiki-perplexity] The rest — "99% accuracy", "10x productivity" and the like — are marketing and recorded only where they are part of a product's own description, never as an independent measure.

## Disputed and unverified

1. **Vendor productivity claims.** M365 Copilot and Gemini in Workspace both ship headline productivity numbers sourced to the vendors themselves; none are independently audited in this batch.[^wiki-m365] [^wiki-gemini]
2. **The "Copilot" brand sweep.** Whether the unification of Bing Chat, Windows Copilot and M365 Copilot into one brand represents one product or a marketing umbrella is not established in the sources read.[^wiki-m365]
3. **Prompt-injection and access-control safety at the tenant level** is a first-order concern for this use case, since the model is grounded on private data, but no standard, independent evaluation of it was read for this batch.

[^wiki-m365]: Wikipedia, "Microsoft 365 Copilot", https://en.wikipedia.org/wiki/Microsoft_365_Copilot
[^wiki-gemini]: Wikipedia, "Gemini (chatbot)", https://en.wikipedia.org/wiki/Gemini_(chatbot)
[^wiki-notebooklm]: Wikipedia, "Gemini Notebook (formerly NotebookLM)", https://en.wikipedia.org/wiki/Gemini_Notebook
[^wiki-perplexity]: Wikipedia, "Perplexity AI", https://en.wikipedia.org/wiki/Perplexity_AI
[^wiki-chatgpt]: Wikipedia, "ChatGPT", https://en.wikipedia.org/wiki/ChatGPT