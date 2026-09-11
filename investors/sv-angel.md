---
type: Investor
title: SV Angel
description: "The San Francisco seed firm founded in 2009 by Ron Conway and David Lee, a participant in the Safe Superintelligence round and in the ElevenLabs Series A, and the firm whose growth fund is reported to hold positions in OpenAI and Anthropic."
resource: https://en.wikipedia.org/wiki/SV_Angel
tags:
  - investor
  - venture-capital
  - seed
  - ai
  - san-francisco
aliases:
  - SV Angel
  - SVA
  - SV Angel Management LLC
founded: 2009
hq: San Francisco, California, United States
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-11T12:45:00Z
stale_after: 2026-12-10T00:00:00Z
relations:
  - { type: founded-by, target: /founders/ron-conway.md, since: 2009, note: "with David Lee, who left the firm in 2015" }
  - { type: founded-by, target: /founders/david-lee.md, since: 2009, note: "managing partner until 2015" }
  - { type: invested-in, target: /companies/ssi.md, at: 2024-09-04, amount_usd: 1000000000, note: "named among five investors in the reported round" }
  - { type: invested-in, target: /companies/elevenlabs.md, round: "Series A", at: 2023-06-20, amount_usd: 19000000, role: participant, note: "listed among other participants" }
  - { type: partners-with, target: /investors/dst-global.md, since: 2011, note: "the Start fund, managed by David Lee" }
sources:
  - id: wiki-sva
    resource: https://en.wikipedia.org/wiki/SV_Angel
    title: "Wikipedia, \"SV Angel\""
    author: wiki:en
  - id: sva-team
    resource: https://svangel.com/about/team
    title: "SV Angel, \"Team\", firm site"
    author: org:sv-angel
  - id: sva-ai
    resource: https://svaai.vc/about/team
    title: "SV Angel, \"Team\", the firm's AI site"
    author: org:sv-angel
  - id: forbes-bachireddy
    resource: https://www.forbes.com/profile/ashvin-bachireddy/
    title: "Forbes, \"Ashvin Bachireddy\", Midas profile updated 27 May 2026, claim read as a search-result summary: the page body did not load for the crawler"
    author: org:forbes
  - id: tc-ssi
    resource: https://techcrunch.com/2024/09/04/ilya-sutskevers-startup-safe-super-intelligence-raises-1b/
    title: "TechCrunch, \"Ilya Sutskever's startup Safe Superintelligence raises $1B\", 4 September 2024"
    author: org:techcrunch
  - id: tc-eleven
    resource: https://techcrunch.com/2023/06/20/voice-generating-platform-elevenlabs-raises-19m-launches-detection-tool/
    title: "TechCrunch, \"Voice-generating platform ElevenLabs raises $19M, launches detection tool\", 20 June 2023"
    author: org:techcrunch
---

# SV Angel

A seed firm that has been in the same deals as the largest growth funds in this directory for two decades, and the only investor here whose portfolio page defers to a third party: svangel.com states that the full portfolio lives on Crunchbase.[^sva-team]

## Snapshot

* **Founded.** 2009 by Ron Conway and David Lee, focused on seed funding; the first fund raised 10 million dollars, after Conway had made most of his investments through Baseline Ventures.[^wiki-sva]
* **Focus.** The firm describes itself as investing in artificial intelligence, software and information technology.[^wiki-sva]
* **The AI site.** The firm runs a separate site for its AI practice, which lists its team and describes individual partners' work with AI companies.[^sva-ai]
* **Where the money comes from now.** In June 2018 the firm said it would stop raising funds from outside investors and that Conway would invest his own money, which reduces the cheque size per company.[^wiki-sva]
* **Growth fund.** A 269 million dollar first growth equity fund was reported in March 2022, a shift from the special purpose vehicles the firm had used for later-stage deals.[^wiki-sva]

## Timeline

* **2009.** SV Angel is founded by Conway and David Lee.[^wiki-sva]
* **2010-09.** David Lee attends the super-angel meeting that sparked Angelgate; Conway writes a letter criticising the group.[^wiki-sva]
* **2011-01.** The firm partners with DST Global on the Start fund, which invests in every Y Combinator startup.[^wiki-sva]
* **2012-05.** Conway states that the firm is Lee's; filings show Lee owning more than 75 per cent since March 2010.[^wiki-sva]
* **2015-05.** Lee leaves the firm.[^wiki-sva]
* **2018-06.** The firm stops raising money from outside investors.[^wiki-sva]
* **2022-03.** The 269 million dollar growth fund is reported.[^wiki-sva]
* **2023-06-20.** Participates in the ElevenLabs Series A.[^tc-eleven]
* **2024-09-04.** Named among the five investors in the Safe Superintelligence round.[^tc-ssi]

## AI companies invested in

| Company | Round | Date | What the source states |
| --- | --- | --- | --- |
| [Safe Superintelligence](/companies/ssi.md) | reported 1 billion dollars | 2024-09-04 | one of five named investors, with NFDG, a16z, Sequoia and DST Global[^tc-ssi] |
| [ElevenLabs](/companies/elevenlabs.md) | Series A, 19 million dollars | 2023-06-20 | listed among the other participants, alongside Creator Ventures and Instagram co-founder Mike Krieger[^tc-eleven] |
| [OpenAI](/companies/openai.md) | growth-fund position | - | a Midas profile of the partner who leads the growth fund describes investments into AI labs including OpenAI[^forbes-bachireddy] |
| [Anthropic](/companies/anthropic.md) | growth-fund position | - | the same profile describes investments into Anthropic[^forbes-bachireddy] |

The two OpenAI and Anthropic rows are a different class of claim and are **not** encoded as edges, because this bundle never turns a single-source or disputed claim into a `relations` entry. They rest on one press profile of one partner rather than on a round announcement, and that profile was read as a search-result summary because the page body did not load.[^forbes-bachireddy] They are repeated below under disputed material rather than asserted here.

## The team

The firm's own site names Ron Conway as founder and managing partner, with Ronny Conway, Topher Conway and Ashvin Bachireddy as managing partners, the latter leading the growth fund; Mike Sho Liu and Andrea Wang as general partners; Sourav Gupta as principal; Zachary Miller as chief operating officer; and Aashai Avadhani as AI lead.[^sva-ai] The AI site's entry for Topher Conway describes him as working closely with OpenAI and Rippling, which is a relationship claim rather than an investment claim and is recorded here rather than as an edge.[^sva-ai]

## Relations

* `founded-by` to [Ron Conway](/founders/ron-conway.md) and [David Lee](/founders/david-lee.md), 2009.[^wiki-sva]
* `invested-in` to [Safe Superintelligence](/companies/ssi.md) and [ElevenLabs](/companies/elevenlabs.md).[^tc-ssi][^tc-eleven]
* No edge for the reported OpenAI and Anthropic positions, for the reason given above.[^forbes-bachireddy]
* `partners-with` to [DST Global](/investors/dst-global.md), for the Start fund of January 2011.[^wiki-sva]

## What is not established

* **Sizes and vintages of the current funds.** The encyclopaedia entry stops at the 2022 growth fund, and the firm publishes no fund sizes.[^wiki-sva]
* **Which vehicles hold the AI positions.** The evidence for OpenAI and Anthropic names the growth fund, which is a different vehicle from the seed funds; whether the seed funds also hold them is not stated.[^forbes-bachireddy]
* **Any Hugging Face position.** Often attributed to this firm in passing; no source read here states it, so it is not recorded.

## Disputed and unverified

* **Reported OpenAI and Anthropic positions.** A Forbes Midas profile of Ashvin Bachireddy, who leads the growth fund, describes a string of investments into AI labs including OpenAI and Anthropic.[^forbes-bachireddy] It is a single press source, the profile page body did not load for the crawler, and no round announcement read here names the firm. It is therefore recorded here, labelled, and left out of the graph.
* **A portfolio page that is not a portfolio page.** svangel.com points readers to Crunchbase for the full portfolio, and the page's own sector filter is rendered client-side, so nothing could be read from it directly. The observation is recorded because a reader who follows the link expecting a list will not find one.[^sva-team]

[^wiki-sva]: Wikipedia, "SV Angel", https://en.wikipedia.org/wiki/SV_Angel
[^sva-team]: SV Angel, "Team", firm site, https://svangel.com/about/team
[^sva-ai]: SV Angel, "Team", the firm's AI site, https://svaai.vc/about/team
[^forbes-bachireddy]: Forbes, "Ashvin Bachireddy", Midas profile updated 27 May 2026, read as a search-result summary, https://www.forbes.com/profile/ashvin-bachireddy/
[^tc-ssi]: TechCrunch, "Ilya Sutskever's startup Safe Superintelligence raises $1B", https://techcrunch.com/2024/09/04/ilya-sutskevers-startup-safe-super-intelligence-raises-1b/
[^tc-eleven]: TechCrunch, "Voice-generating platform ElevenLabs raises $19M, launches detection tool", 20 June 2023, https://techcrunch.com/2023/06/20/voice-generating-platform-elevenlabs-raises-19m-launches-detection-tool/
