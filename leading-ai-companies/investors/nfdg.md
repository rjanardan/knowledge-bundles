---
type: Investor
title: NFDG
description: "The AI-focused investment partnership of Nat Friedman and Daniel Gross, founded in 2023, one of five named investors in the reported 1B dollar round in Safe Superintelligence, and the operator of the Andromeda Cluster supercomputer for its portfolio."
resource: https://techcrunch.com/2024/09/04/ilya-sutskevers-startup-safe-super-intelligence-raises-1b/
tags:
  - investor
  - venture-capital
  - ai
  - seed
  - supercomputer
aliases:
  - NFDG
  - Nat Friedman and Daniel Gross
founded: 2023
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: 2026-09-11T12:45:00Z
stale_after: 2026-12-10T00:00:00Z
relations:
  - { type: founded-by, target: /founders/nat-friedman.md, since: 2023, role: "co-founder of the partnership" }
  - { type: founded-by, target: /founders/daniel-gross.md, since: 2023, role: "co-founder of the partnership" }
  - { type: invested-in, target: /companies/ssi.md, at: 2024-09-04, amount_usd: 1000000000, note: "one of five named investors in the reported round" }
  - { type: related-to, target: /companies/meta.md, at: 2025-07-03, note: "Meta offered to buy a minority stake in the funds after hiring both principals" }
sources:
  - id: tc-ssi
    resource: https://techcrunch.com/2024/09/04/ilya-sutskevers-startup-safe-super-intelligence-raises-1b/
    title: "TechCrunch, \"Ilya Sutskever's startup Safe Superintelligence raises $1B\", 4 September 2024"
    author: org:techcrunch
  - id: wiki-gross
    resource: https://en.wikipedia.org/wiki/Daniel_Gross_(businessman)
    title: "Wikipedia, \"Daniel Gross (businessman)\""
    author: wiki:en
  - id: wiki-nat
    resource: https://en.wikipedia.org/wiki/Nat_Friedman
    title: "Wikipedia, \"Nat Friedman\""
    author: wiki:en
  - id: seedlist-nfdg
    resource: https://seedlist.com/firms/nfdg.html
    title: "Seedlist, \"NFDG\", analyst tracker, secondary"
    author: org:seedlist
  - id: dcd-nfdg
    resource: https://www.datacenterdynamics.com/en/news/meta-in-talks-to-partially-acquire-vc-fund-nfdg-hire-nat-friedman-and-daniel-gross-for-ai-shakeup/
    title: "Data Center Dynamics, \"Meta in talks to partially acquire VC fund NFDG, hire Nat Friedman and Daniel Gross for AI shakeup\", 21 June 2025"
    author: org:datacenterdynamics
  - id: wsj-nfdg
    resource: https://www.wsj.com/articles/meta-offers-to-buy-stake-in-venture-funds-started-by-ai-hires-nat-friedman-and-daniel-gross-cc72ad49
    title: "The Wall Street Journal, \"Meta Offers to Buy Stake in Venture Funds Started by AI Hires Nat Friedman and Daniel Gross\", 3 July 2025, read as a headline only: the article body returned a paywall"
    author: org:wsj
  - id: wiki-ssi
    resource: https://en.wikipedia.org/wiki/Safe_Superintelligence
    title: "Wikipedia, \"Safe Superintelligence\""
    author: wiki:en
  - id: el-blog
    resource: https://elevenlabs.io/blog/elevenlabs-launches-new-generative-voice-ai-products-and-announces-19m-series-a-round-led-by-nat-friedman-daniel-gross-and-andreessen-horowitz
    title: "ElevenLabs, \"ElevenLabs Announces $19m Series A Round Led by Nat Friedman, Daniel Gross, and Andreessen Horowitz\", 20 June 2023"
    author: org:elevenlabs

---

# NFDG

The investment partnership of Nat Friedman and Daniel Gross, described by TechCrunch as "an investment partnership run by Nat Friedman and SSI CEO Daniel Gross" when it joined the September 2024 round in Safe Superintelligence.[^tc-ssi] It is the least conventional concept in this directory: a two-person vehicle that also runs its own GPU cluster for the companies it backs.

## Snapshot

* **What it is.** A venture partnership, not a diversified fund manager.[^tc-ssi] Founded in 2023 with 1.1 billion dollars of committed capital for its debut fund, according to the analyst tracker Seedlist, which also states that the name is formed from the founders' initials.[^seedlist-nfdg]
* **Infrastructure it operates.** The Andromeda Cluster, a supercomputer the partnership deployed for use by its portfolio companies.[^dcd-nfdg] Wikipedia's article on Gross gives the scale as 2,512 H100 GPUs, deployed in 2023.[^wiki-gross]
* **Programme it runs.** AI Grant, started in 2021 with Friedman, which gives 250,000 dollars to AI-native companies.[^wiki-gross]
* **Where the principals now work.** Both left for Meta in mid-2025; see the timeline below.[^dcd-nfdg][^wiki-nat]

## Timeline

* **2021.** Friedman and Gross begin investing in AI together and start AI Grant.[^wiki-gross]
* **2023.** The partnership is founded, with 1.1 billion dollars of committed capital for the debut fund.[^seedlist-nfdg] The Andromeda Cluster is deployed.[^wiki-gross]
* **2024-09-04.** NFDG is named among five investors in the reported 1 billion dollar round in Safe Superintelligence.[^tc-ssi]
* **2025-06-21.** Trade reporting has Meta in talks to partially acquire the fund and hire both principals.[^dcd-nfdg]
* **2025-07-03.** The Wall Street Journal reports Meta offering to buy a minority stake in the funds, giving limited partners a chance to exit early.[^wsj-nfdg]

## Founding and partners

**Nat Friedman** (born 6 August 1977) is an American technology executive and investor, currently head of product at Meta Superintelligence Labs.[^wiki-nat] He co-founded Ximian in 1999, founded Xamarin in 2011, and was chief executive of GitHub from October 2018 until 2021. He is a board member of the Arc Institute and an advisor to Midjourney.[^wiki-nat]

**Daniel Gross** (born 1991 in Jerusalem) is an Israeli-American businessman who co-founded Cue, led artificial intelligence efforts at Apple, and was a partner at Y Combinator from 2017.[^wiki-gross] He created Pioneer in 2018, co-founded Safe Superintelligence in June 2024, and left it in July 2025 to join Meta Superintelligence Labs.[^wiki-gross][^wiki-ssi]

Where the two sit now is the reason this file carries a `related-to` edge to the Meta concept rather than an `employs` edge: the fund and the Meta roles coexist, and the sources describe the second without saying the first has ended.[^dcd-nfdg][^wiki-nat]

## AI companies invested in

| Company | Round | Date | What the source states |
| --- | --- | --- | --- |
| [Safe Superintelligence](/companies/ssi.md) | reported 1 billion dollars, 5 billion dollar valuation | 2024-09-04 | NFDG named as one of the five investors, alongside a16z, Sequoia, DST Global and SV Angel[^tc-ssi] |

That row is the whole of the fund-level portfolio this bundle can currently source. The partnership publishes no portfolio page, and its own domain did not resolve on the date of writing (see below).

Beyond the fund, the principals invest personally, and the distinction matters for anyone counting edges:

* Gross is described as a notable technology investor in Uber, Instacart, Figma, GitHub, Airtable, Rippling, CoreWeave, Character.ai and Perplexity AI.[^wiki-gross]
* Those are personal positions, not fund positions, and no source read here attributes them to NFDG. They are therefore written down and deliberately **not** encoded as `invested-in` edges.

## Relations

* `founded-by` to [Nat Friedman](/founders/nat-friedman.md) and [Daniel Gross](/founders/daniel-gross.md), since 2023.[^seedlist-nfdg]
* `invested-in` to [Safe Superintelligence](/companies/ssi.md), at the reported round of 4 September 2024.[^tc-ssi]
* `related-to` to [Meta](/companies/meta.md), for the 2025 stake offer.[^wsj-nfdg]

## What is not established

* **Fund size after the debut.** Seedlist gives 1.1 billion dollars of committed capital and no later figure was found.[^seedlist-nfdg]
* **Whether the ElevenLabs Series A was a fund investment.** The 19 million dollar round of 20 June 2023 was co-led by "Nat Friedman, Daniel Gross and Andreessen Horowitz", and the firm's own announcement names the two men rather than NFDG.[^el-blog] Since the sources do not say whose money it was, no edge is recorded, on the same principle that keeps unverified architecture out of the model files.
* **Current status of the fund.** No source read states whether the partnership is investing in new companies after the Meta transaction.[^wsj-nfdg]

## Disputed and unverified

* **Meta's stake purchase.** Reported by the Journal as an offer to buy a minority stake in the funds.[^wsj-nfdg] Only the headline was readable: the article body returned HTTP 401. A secondary trade account describes the fund as "acquired by Meta", which is a stronger claim than the headline supports and is therefore recorded here rather than as an edge.[^dcd-nfdg]
* **A first-hand observation, not a sourced claim.** On 2026-09-11 the domain nfdg.com did not resolve from the machine used to build this bundle - the apex returned NOERROR with no address and `www` returned NXDOMAIN - while aigrant.com, the programme the principals run, resolved normally. Recorded because a reader following the fund's name will otherwise look for a site that is not serving.

[^tc-ssi]: TechCrunch, "Ilya Sutskever's startup Safe Superintelligence raises $1B", https://techcrunch.com/2024/09/04/ilya-sutskevers-startup-safe-super-intelligence-raises-1b/
[^wiki-gross]: Wikipedia, "Daniel Gross (businessman)", https://en.wikipedia.org/wiki/Daniel_Gross_(businessman)
[^wiki-nat]: Wikipedia, "Nat Friedman", https://en.wikipedia.org/wiki/Nat_Friedman
[^seedlist-nfdg]: Seedlist, "NFDG", analyst tracker, secondary, https://seedlist.com/firms/nfdg.html
[^dcd-nfdg]: Data Center Dynamics, "Meta in talks to partially acquire VC fund NFDG, hire Nat Friedman and Daniel Gross for AI shakeup", 21 June 2025, https://www.datacenterdynamics.com/en/news/meta-in-talks-to-partially-acquire-vc-fund-nfdg-hire-nat-friedman-and-daniel-gross-for-ai-shakeup/
[^wsj-nfdg]: The Wall Street Journal, "Meta Offers to Buy Stake in Venture Funds Started by AI Hires Nat Friedman and Daniel Gross", https://www.wsj.com/articles/meta-offers-to-buy-stake-in-venture-funds-started-by-ai-hires-nat-friedman-and-daniel-gross-cc72ad49
[^wiki-ssi]: Wikipedia, "Safe Superintelligence", https://en.wikipedia.org/wiki/Safe_Superintelligence
[^el-blog]: ElevenLabs, "ElevenLabs Launches New Generative Voice AI Products and Announces $19m Series A Round Led by Nat Friedman, Daniel Gross, and Andreessen Horowitz", https://elevenlabs.io/blog/elevenlabs-launches-new-generative-voice-ai-products-and-announces-19m-series-a-round-led-by-nat-friedman-daniel-gross-and-andreessen-horowitz
