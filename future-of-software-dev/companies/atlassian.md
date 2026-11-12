---
type: Company
title: Atlassian
description: Collaboration and work-tracking vendor founded in 2002, whose Jira sits at the planning end of the software lifecycle and whose 2025 developer-experience survey reports AI gains alongside rising organisational friction.
resource: https://www.atlassian.com
tags:
  - work-tracking
  - agile-tooling
  - developer-experience
  - ai-agents
  - australia
aliases:
  - Atlassian Corporation
  - Atlassian Corporation Plc
founded: 2002
hq: Sydney, Australia
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-11T00:00:00Z
stale_after: 2026-12-10T00:00:00Z
relations:
  - { type: founded-by, target: /people/mike-cannon-brookes.md, since: 2002 }
  - { type: founded-by, target: /people/scott-farquhar.md, since: 2002 }
  - { type: produced, target: /technologies/rovo.md, note: "AI agent layer across Confluence, Jira and connected third-party apps" }
sources:
  - id: atl-about
    resource: "https://www.atlassian.com/company"
    title: "About Us | Atlassian"
    author: "org:atlassian"
  - id: atl-devex
    resource: "https://www.atlassian.com/teams/software-development/state-of-developer-experience-2025"
    title: "State of Developer Experience Report 2025"
    author: "org:atlassian"
    note: "(survey of 3,500 developers and managers with Wakefield Research)"
  - id: atl-rovo
    resource: "https://www.atlassian.com/blog/rovo/rovo-ai-agents-at-work"
    title: "Rovo at Work: AI that moves work forward"
    author: "org:atlassian (Gunjan Sood)"
    note: "2026-02-25"
  - id: rally-ipo
    resource: "https://www.prnewswire.com/news-releases/rally-software-announces-pricing-of-initial-public-offering-202671891.html"
    title: "Rally Software Announces Pricing of Initial Public Offering"
    author: "org:rally-software"
    note: "2013-04-12"
---

# Atlassian

## Snapshot

Atlassian was founded in 2002 by Mike Cannon-Brookes and Scott Farquhar, then "two college friends".[^atl-about] Its own About page reports 300,000+ customers, 12,000+ staff, a presence in 14 countries and 5,700+ apps in its Marketplace.[^atl-about] For this bundle the company matters for a structural reason: it occupies the planning and tracking end of the lifecycle — the phase where work is described and assigned rather than written — and by 2026 it was selling agents into exactly that phase.[^atl-rovo]

## Founding and lineage

Founded 2002 by Mike Cannon-Brookes and Scott Farquhar, per Atlassian's own account of its history.[^atl-about] The date is year-granular in the source and is recorded that way rather than widened to a day the source does not give.

Rally, covered separately in this bundle, is the near-contemporary equivalent in the same market: founded in the same period, sold agile tracking to enterprises, floated in 2013 and was acquired in 2015.[^rally-ipo] The two companies are the clearest illustration in this corpus of how the pre-AI tooling generation ended up — one independent and expanding its surface, the other absorbed into a hardware-and-infrastructure conglomerate.

## What the sources show

**A survey with an unflattering find.** Atlassian's State of Developer Experience report for 2025 was produced with Wakefield Research from a survey of 3,500 developers and managers.[^atl-devex] Its reported pattern is that more development teams perceive they are gaining more time from AI while also reporting *greater* organisational inefficiencies than before, with a widening disconnect between leadership expectations and developers' own experience.[^atl-devex] The finding is a perception study, not a productivity measurement, and is recorded with that limit attached.

**A product surface moving onto the agent layer.** In February 2026 Atlassian described Rovo agents performing work across its stack: skills for repeating workflows, an agent that takes a Jira spec to a merge-ready pull request, a studio for building custom agents without code, and connections to third-party tools such as Amplitude, Canva and Figma over the Model Context Protocol.[^atl-rovo] The MCP adoption is the load-bearing detail: a tracking vendor wiring its agents into other vendors' tools through a shared protocol is the same pattern recorded elsewhere in this corpus, and it is how the planning phase stops being a place work is described and becomes a place work is dispatched.

## What it says about the SDLC

Atlassian's position is the counterweight to the coding-agent story. If the 2020s shift is agents moving from suggesting lines to completing tasks, then the phase where a task is specified, assigned, tracked and reported becomes the phase where the agent receives its instructions — and Jira is where a large share of enterprise software work is specified.[^atl-rovo] The company's own framing points there: the agent is sold as taking a Jira spec to a merge-ready PR, which spans the planning phase and the implementation phase in one step.[^atl-rovo]

The survey's finding is the interesting complication, because it points the other way from the product narrative. A vendor whose product is sold to reduce organisational friction reports that AI adoption coincides with more of it, and identifies the gap as being between leadership expectation and developer experience rather than between tool and no tool.[^atl-devex] That is a claim about how organisations absorb the tools, and it is recorded here as a survey result rather than promoted to a finding.

## Evidence it has produced

This concept currently presents the developer-experience survey as a source with its method and sample attached — 3,500 developers and managers, fielded with Wakefield Research, reported in 2025.[^atl-devex] It is a candidate for an `evidence/` concept under `method: survey` once that shard is built out. It is recorded here first because a survey about perception belongs with the company that commissioned it, where a reader can see who paid for it.

## Relations

Two `founded-by` edges point at `/people/mike-cannon-brookes.md` and `/people/scott-farquhar.md`, neither of which exists yet; `founded-by` has no mirror by convention, so no reciprocal edge is required. `produced` points at `/technologies/rovo.md`, likewise pending, and that concept will carry the `produced-by` mirror. No `contradicts` edge is recorded against the survey, because no source in this batch measures the same quantity in the opposite direction; a perception gap and a task-time measurement are not comparable.

## Commercials

Not established in this batch. The About page gives customer and staff counts but no revenue or pricing figure was retrieved.[^atl-about]

## What is not established

* **The vintage of the About page.** The retrieved page says Atlassian is "now 20 years in", which is consistent with a 2022 passage of copy rather than a 2026 one, while the same page carries staff and customer counts that read as current.[^atl-about] The page's own consistency is therefore in doubt for the prose and not for the figures, and this file does not use it for anything dated.
* **Whether Rovo Dev's spec-to-PR claim has been measured.** It is a product claim on the vendor's blog, with no sample and no interval, and it is recorded as a claim.[^atl-rovo]
* **Atlassian's legal form and listing status**, which no retrieved source states.
* **Any independent replication of the developer-experience finding.**

## Disputed and unverified

Nothing in this batch disputes the survey, and the survey disputes no other concept here. Its honest status is that it measures what respondents said about their own efficiency while AI adoption rose, which is a different quantity from the task-time measurements recorded in `evidence/` — and the two are not placed in conflict because they do not measure the same thing.

[^atl-about]: org:atlassian, "About Us | Atlassian", https://www.atlassian.com/company
[^atl-devex]: org:atlassian, "State of Developer Experience Report 2025" (survey of 3,500 developers and managers with Wakefield Research), https://www.atlassian.com/teams/software-development/state-of-developer-experience-2025
[^atl-rovo]: org:atlassian (Gunjan Sood), "Rovo at Work: AI that moves work forward", 2026-02-25, https://www.atlassian.com/blog/rovo/rovo-ai-agents-at-work
[^rally-ipo]: org:rally-software, "Rally Software Announces Pricing of Initial Public Offering", 2013-04-12, https://www.prnewswire.com/news-releases/rally-software-announces-pricing-of-initial-public-offering-202671891.html
