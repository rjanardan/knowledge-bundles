---
type: Company
title: Rally
description: Agile work-tracking product floated on the NYSE in 2013 and absorbed through CA Technologies into Broadcom, where by 2026 it is sold as enterprise value-stream management with AI forecasting.
resource: https://www.broadcom.com/products/software/value-stream-management/rally
tags:
  - agile-tooling
  - work-tracking
  - value-stream-management
  - acquired
  - broadcom
aliases:
  - Rally Software
  - Rally Software Development Corp.
  - CA Agile Central
  - Rally
founded: null
hq: Boulder, Colorado, US
parent: Broadcom
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-11T00:00:00Z
stale_after: 2027-03-10T00:00:00Z
relations:
  - { type: subsidiary-of, target: /companies/broadcom.md, note: "via CA Technologies, which announced its acquisition of Rally in 2015; Broadcom later acquired CA" }
sources:
  - id: rally-ipo
    resource: "https://www.prnewswire.com/news-releases/rally-software-announces-pricing-of-initial-public-offering-202671891.html"
    title: "Rally Software Announces Pricing of Initial Public Offering"
    author: "org:rally-software"
    note: "2013-04-12"
  - id: rally-vsm
    resource: "https://www.broadcom.com/products/software/value-stream-management/rally"
    title: "Rally | Business Agility & Value Stream Management"
    author: "org:broadcom"
  - id: ca-close
    resource: "https://businesswire.com/news/home/20150708005716/en/CA-Technologies-Completes-Acquisition-Rally-Software"
    title: "CA Technologies Completes Acquisition of Rally Software (headline only; page returned HTTP 403 at retrieval 2026-09-11)"
    author: "org:ca-technologies"
    note: "2015-07-08"
  - id: pcw-ca
    resource: "https://pcworld.com/article/427695/ca-gets-agile-with-480-purchase-of-rally.html"
    title: "CA gets 'agile' with $480 million purchase of Rally"
    author: "org:pcworld"
---

# Rally

## Snapshot

Rally is an agile work-tracking product that was, at the time of its 2013 flotation, described as "a leading provider of cloud-based solutions for managing Agile software development", based in Boulder, Colorado.[^rally-ipo] It priced its initial public offering on 2013-04-12 at $14.00 a share for 6,000,000 shares, and began trading on the New York Stock Exchange under the symbol "RALY".[^rally-ipo] By 2026 the product is sold by Broadcom as "the foundation for business agility and digital transformation", part of a ValueOps platform alongside Clarity, ConnectALL and Insights, available on-premise or in the cloud.[^rally-vsm] It is the clearest "before" case in this corpus: a product for tracking human work, now marketed for forecasting it.

## Founding and lineage

`founded` is `null`. No retrieved source states Rally's founding year or founders, so the field is left empty rather than filled from memory, and a first-party history is a pending item for a later batch.

The ownership line is documented in outline and broken in detail. Rally was independent and publicly traded as of April 2013.[^rally-ipo] CA Technologies announced an acquisition in 2015, and the completion release is dated 2015-07-08, but that page returned HTTP 403 to this batch's retrieval, so it is declared as a headline-only source and nothing rests on its body.[^ca-close] Broadcom now markets the product.[^rally-vsm] The line therefore runs Rally to CA to Broadcom, with the CA-to-Broadcom step undated here.

## What the sources show

Three dated states of one product, which is the whole reason this concept exists:

* **2013, independent.** A cloud product for managing agile software development, floated on the NYSE at $14.00 a share.[^rally-ipo]
* **2015, acquired.** CA Technologies completed its acquisition on 2015-07-08 according to the release headline, at a price reported by press coverage as $480 million.[^ca-close][^pcw-ca] The release's body was not read, and the announcement date and closing price are not established here.
* **2026, absorbed.** Broadcom sells Rally for enterprise visibility and alignment, connecting portfolios, programs and products to business strategy, within a ValueOps platform that integrates Clarity, Rally, ConnectALL and Insights, with "AI-powered insights" that forecast outcomes and predict risks.[^rally-vsm]

## What it says about the SDLC

The product's own vocabulary carries the evidence, and it is measurable across the two dated states. In 2013 the object being managed was agile software development.[^rally-ipo] In 2026 it is portfolio, program and product aligned to strategy, within a platform whose other named components — Clarity, ConnectALL, Insights — are portfolio-finance and integration products rather than developer tools.[^rally-vsm] The individual developer has dropped out of the description entirely. That is the planning phase's centre of gravity moving from the team to the portfolio, and it happened before AI arrived rather than because of it.

The AI layer is an addition to that structure rather than a replacement of it: forecasting outcomes and predicting risks is a feature on a management layer, not an agent performing the tracked work.[^rally-vsm] The distinction is worth keeping because "AI-powered" in 2026 vendor literature describes both a code-completion tool and a dashboard, and only one of the two changes who does the task. A corpus that records the phrase without the object cannot tell them apart.

## Evidence it has produced

None. Rally's sources here are corporate, promotional and, in one case, unreachable, and the concept states that plainly instead of treating a product page as research. The absence is recorded because a reader comparing this concept to a lab's should be able to see why there is nothing to weigh.

## Relations

`subsidiary-of` points at `/companies/broadcom.md`, which does not exist yet, so the checker reports it as a pending target. The edge deliberately carries no `since` date: the CA-to-Broadcom step is undated in this batch, and supplying a date to make the edge look complete is precisely what the conventions forbid. `/companies/atlassian.md` is a near-contemporary in the same market and is cross-referenced in prose rather than by edge, because the two companies never shared an owner or a product and an edge would overstate the relationship.

## Commercials

Not established in this batch beyond the 2013 flotation price of $14.00 per share.[^rally-ipo] No current price for the Broadcom product was retrieved, and Broadcom's page is a marketing page rather than a price list.[^rally-vsm]

## What is not established

* **Founding year and founders.** `founded` is `null`.
* **The completion date of the CA acquisition.** Recorded from a headline whose page was unreachable at retrieval time.[^ca-close]
* **The acquisition price as a first-party figure.** $480 million is a press figure and is marked as secondary rather than attributed to the acquirer.[^pcw-ca]
* **When Broadcom acquired CA**, and therefore when Rally changed hands the second time.
* **Whether "CA Agile Central" was the product's interim name.** It is carried as an alias for deduplication only; no retrieved source confirms it.

## Disputed and unverified

The $480 million price appears in the coverage retrieved but in no first-party document this batch could read, so it is stated as a press figure and not as a company fact. The completion release was identified by title and date — which is how its `title` in `sources` records it — but returned HTTP 403 to retrieval, so no sentence here rests on its content, and the concept it would have supported is marked unestablished instead.[^ca-close]

[^rally-ipo]: org:rally-software, "Rally Software Announces Pricing of Initial Public Offering", 2013-04-12, https://www.prnewswire.com/news-releases/rally-software-announces-pricing-of-initial-public-offering-202671891.html
[^rally-vsm]: org:broadcom, "Rally | Business Agility & Value Stream Management", https://www.broadcom.com/products/software/value-stream-management/rally
[^ca-close]: org:ca-technologies, "CA Technologies Completes Acquisition of Rally Software (headline only; page returned HTTP 403 at retrieval 2026-09-11)", 2015-07-08, https://businesswire.com/news/home/20150708005716/en/CA-Technologies-Completes-Acquisition-Rally-Software
[^pcw-ca]: org:pcworld, "CA gets 'agile' with $480 million purchase of Rally", https://pcworld.com/article/427695/ca-gets-agile-with-480-purchase-of-rally.html
