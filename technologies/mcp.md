---
type: Technology
title: Model Context Protocol
description: Open standard introduced by Anthropic in November 2024 that connects AI assistants to tools and data through MCP hosts, clients and servers over JSON-RPC; donated to the Linux Foundation in December 2025.
resource: https://modelcontextprotocol.io/introduction
tags:
  - mcp
  - protocol
  - tool-use
  - json-rpc
  - open-standard
  - agentic-ai
aliases:
  - MCP
  - Model Context Protocol
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-10T20:05:08Z
stale_after: 2026-12-10T00:00:00Z
relations:
  - { type: developed-by, target: /companies/anthropic.md, since: 2024-11 }
  - { type: related-to, target: /technologies/agent-skills.md }
  - { type: related-to, target: /ai-domains/agentic-ai.md }
sources:
  - id: wiki-mcp
    resource: https://en.wikipedia.org/wiki/Model_Context_Protocol
    title: Wikipedia, "Model Context Protocol"
    author: wiki:en
  - id: mcp-intro
    resource: https://modelcontextprotocol.io/introduction
    title: MCP documentation, introduction
    author: org:mcp-maintainers
  - id: mcp-spec
    resource: https://modelcontextprotocol.io/specification/2026-07-28
    title: MCP specification, 2026-07-28 revision
    author: org:mcp-maintainers
  - id: mcp-versioning
    resource: https://modelcontextprotocol.io/specification/versioning
    title: MCP documentation, versioning
    author: org:mcp-maintainers
  - id: mcp-github
    resource: https://github.com/modelcontextprotocol/modelcontextprotocol
    title: MCP specification and documentation repository
    author: org:mcp-maintainers
  - id: anthropic-mcp
    resource: https://www.anthropic.com/news/model-context-protocol
    title: Anthropic, "Introducing the Model Context Protocol"
    author: org:anthropic
  - id: openai-docs
    resource: https://platform.openai.com/docs/models
    title: OpenAI, API documentation index
    author: org:openai
---

# Model Context Protocol

## What it is

MCP is an open standard, published with an open-source reference implementation, for connecting AI assistants to external tools, systems and data sources.[^wiki-mcp] Anthropic introduced it in November 2024, and its own framing of the problem is the "N by M" integration cost: without a shared protocol, every assistant needs a bespoke connector for every data source.[^wiki-mcp]

The architecture has three roles. An **MCP host** is the AI agent that needs services; for each server it wants, the host creates a dedicated **MCP client**, and the client talks to an **MCP server** that exposes tools, resources or prompts.[^wiki-mcp] Messages use JSON-RPC 2.0, and the protocol re-uses the message-flow ideas of the Language Server Protocol.[^wiki-mcp] The first release shipped with SDKs in Python, TypeScript, C# and Java.[^wiki-mcp]

## Version history

Protocol revisions are dated, following the pattern `YYYY-MM-DD`, and the version is incremented only when a change is backwards-incompatible.[^mcp-versioning] The revisions published to date are 2024-11-05, 2025-03-26, 2025-06-18, 2025-11-25 and 2026-07-28.[^mcp-intro]

The July 2026 revision is the significant one. It removed protocol-level session tracking, making MCP stateless at the protocol layer, with protocol version, client identity and capabilities carried in a `_meta` parameter on each request instead.[^wiki-mcp] Sampling was deprecated, and a mechanism for long-running operations was moved out of the base protocol into optional extensions.[^wiki-mcp] The maintainers describe it as the most substantial change since the addition of authorization, and it brings the request model closer to that of Anthropic's own Messages API.[^wiki-mcp] It is explicitly not fully backwards compatible: a server on the new revision may not interoperate with older clients without a compatibility layer.[^wiki-mcp]

## Governance

In December 2025 Anthropic donated MCP to the Agentic AI Foundation, a directed fund under the Linux Foundation co-founded by Anthropic, Block and OpenAI.[^wiki-mcp] Later the same month Anthropic published Agent Skills, a companion open standard for packaging task-specific instructions and resources that agents load on demand - the second contributed standard, and a separate concept in this bundle.[^wiki-mcp] The specification and documentation live in a public repository under the protocol's own organisation.[^mcp-github]

## Adoption

| Signal | Value | As of | Source |
| --- | --- | --- | --- |
| OpenAI adoption | Adopted March 2025 | 2025-03 | [^wiki-mcp] |
| Other major adopters | Google DeepMind and other major providers; Replit and others ship MCP support in products | 2026 | [^wiki-mcp] |
| Production servers | More than 10,000 reported deployed in production | mid-2026 | [^wiki-mcp] |
| SDK downloads | More than 97 million per month | mid-2026 | [^wiki-mcp] |
| Named customer scale | Salesforce reported 4.5 million MCP calls processed since launch | 2026 | [^wiki-mcp] |
| OpenAI's own tooling | Documents MCP connections and a self-hosted "Secure MCP Tunnel" as part of its agent tooling | 2026-09 | [^openai-docs] |

MCP also underpins a documented interoperability layer in products rather than only in developer tooling: Replit uses MCP, and Anthropic's own Claude reached its first-party tool integrations through the protocol.[^wiki-mcp]

## Disputed and unverified

1. **Adoption metrics are self-reported.** The 10,000-server and 97-million-download figures come from the maintainers and are recorded through Wikipedia in this batch; no independent measurement was retrieved.
2. **The 2026-07-28 revision is a compatibility event.** Parties running servers on earlier revisions face real migration work. The bundle records this as a risk rather than as a purely technical improvement.
3. **Client and server behaviour differences.** The protocol standardises the interface, not the tool's semantics; two MCP servers exposing the same tool name may behave differently. Not established in the sources read.

[^wiki-mcp]: Wikipedia, "Model Context Protocol", https://en.wikipedia.org/wiki/Model_Context_Protocol
[^mcp-intro]: MCP documentation, introduction, https://modelcontextprotocol.io/introduction
[^mcp-spec]: MCP specification, 2026-07-28 revision, https://modelcontextprotocol.io/specification/2026-07-28
[^mcp-versioning]: MCP documentation, versioning, https://modelcontextprotocol.io/specification/versioning
[^mcp-github]: MCP specification and documentation repository, https://github.com/modelcontextprotocol/modelcontextprotocol
[^anthropic-mcp]: Anthropic, "Introducing the Model Context Protocol", https://www.anthropic.com/news/model-context-protocol
[^openai-docs]: OpenAI, API documentation index, https://platform.openai.com/docs/models
