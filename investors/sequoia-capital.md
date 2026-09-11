---
type: Investor
title: Sequoia Capital
description: "The Menlo Park venture firm founded in 1972, the first outside investor in OpenAI in 2021, a co-lead of the Anthropic Series H in 2026, and an investor in Safe Superintelligence and xAI."
resource: https://sequoiacap.com/companies/openai
tags:
  - investor
  - venture-capital
  - ai
  - menlo-park
  - frontier-models
aliases:
  - Sequoia Capital
  - Sequoia
  - Sequoia Capital Operations, LLC
founded: 1972
hq: Menlo Park, California, United States
status: draft
generated:
  by: hermes_agent/deepseek-flash
  at: NOWHERE
stale_after: STALEHERE
relations:
  - { type: founded-by, target: /founders/don-valentine.md, since: 1972 }
  - { type: invested-in, target: /companies/openai.md, since: 2021, note: "the firm dates its partnership with OpenAI to 2021 and lists Alfred Lin, James Flynn, Pat Grady and Sonya Huang on the account" }
  - { type: invested-in, target: /companies/anthropic.md, round: "Series H", at: 2026-05-28, role: lead, note: "co-lead of the 65 billion dollar round; Lauren Reeder also named on the account" }
  - { type: invested-in, target: /companies/ssi.md, since: 2024, note: "the firm dates its partnership to 2024 and lists Andrew Reed and Shaun Maguire as the partners on the account" }
  - { type: invested-in, target: /companies/xai.md, round: "Series B", at: 2024-05-26, amount_usd: 6000000000, note: "named in the company's own announcement" }
sources:
  - id: wiki-sequoia
    resource: https://en.wikipedia.org/wiki/Sequoia_Capital
    title: "Wikipedia, \"Sequoia Capital\""
    author: wiki:en
  - id: seq-openai
    resource: https://sequoiacap.com/companies/openai
    title: "Sequoia Capital, \"OpenAI\", portfolio page: founded 2015, partnered 2021"
    author: org:sequoia-capital
  - id: seq-anthropic
    resource: https://sequoiacap.com/companies/anthropic
    title: "Sequoia Capital, \"Anthropic\", portfolio page: founded 2021, partnered 2026"
    author: org:sequoia-capital
  - id: seq-ssi
    resource: https://sequoiacap.com/companies/safe-superintelligence
    title: "Sequoia Capital, \"Safe Superintelligence\", portfolio page: founded 2024, partnered 2024"
    author: org:sequoia-capital
  - id: tc-anthropic-h
    resource: https://techcrunch.com/2026/05/28/anthropic-raises-65-billion-nears-1t-valuation-ahead-of-ipo/
    title: "TechCrunch, \"Anthropic raises $65 billion, nears $1T valuation ahead of IPO\", 28 May 2026"
    author: org:techcrunch
  - id: xai-b
    resource: https://x.ai/news/series-b
    title: "xAI, \"Series B funding round\", 26 May 2024"
    author: org:xai
---

# Sequoia Capital

The oldest firm in this directory and the one with the most useful public artefact: Sequoia publishes a portfolio page for each company it backs, and that page carries two dates that matter for a graph - when the company was founded and when Sequoia partnered with it.[^seq-openai][^seq-anthropic][^seq-ssi]

## Snapshot

* **Founded.** 1972 by Don Valentine in Menlo Park, California; first fund in 1974.[^wiki-sequoia]
* **Structure.** Three regionally separate venture entities: Sequoia in the United States and Europe, Peak XV Partners in India and Southeast Asia, and formerly HongShan in China, after the 2023 break-up of the global partnership.[^wiki-sequoia]
* **Scale.** Approximately 56 billion dollars in assets under management as of January 2025.[^wiki-sequoia]
* **Leadership history.** Doug Leone and Michael Moritz took over in 1996; Moritz stepped back from daily operations in 2012; Roelof Botha has led the United States business since 2017.[^wiki-sequoia]

## Timeline

* **1972.** Sequoia is founded by Don Valentine.[^wiki-sequoia]
* **1978.** One of the first investors in Apple.[^wiki-sequoia]
* **2021.** The firm dates its partnership with OpenAI to this year.[^seq-openai]
* **2024.** Partnership with Safe Superintelligence begins, the same year the company was founded.[^seq-ssi]
* **2024-05-26.** Named in the xAI Series B.[^xai-b]
* **2026.** Partnership with Anthropic begins, dated 2026 on the firm's own page.[^seq-anthropic]
* **2026-05-28.** Co-leads the Anthropic Series H, a 65 billion dollar round at a 965 billion dollar post-money valuation.[^tc-anthropic-h]

## AI companies invested in

| Company | Round or relationship | Date | What the source states |
| --- | --- | --- | --- |
| [OpenAI](/companies/openai.md) | partnership | 2021 | the firm's page dates the partnership to 2021 and names Alfred Lin, James Flynn, Pat Grady and Sonya Huang; Sam Altman, Greg Brockman and Ilya Sutskever are listed under team[^seq-openai] |
| [Anthropic](/companies/anthropic.md) | Series H | 2026-05-28 | co-lead of the round, alongside Altimeter Capital, Dragoneer, Greenoaks, Capital Group, Coatue and D1 Capital Partners[^tc-anthropic-h] |
| [Safe Superintelligence](/companies/ssi.md) | partnership | 2024 | partnered the same year the company was founded; partners on the account are Andrew Reed and Shaun Maguire[^seq-ssi] |
| [xAI](/companies/xai.md) | Series B, 6 billion dollars | 2024-05-26 | named in the company's own announcement of the round[^xai-b] |

The coexistence of OpenAI, Anthropic and xAI on one portfolio page is the single most useful fact this file carries: three competitors for the same frontier-model market, one limited partner.[^seq-openai][^seq-anthropic][^xai-b]

## Relations

* `founded-by` to [Don Valentine](/founders/don-valentine.md), 1972.[^wiki-sequoia]
* `invested-in` to [OpenAI](/companies/openai.md), [Anthropic](/companies/anthropic.md), [Safe Superintelligence](/companies/ssi.md) and [xAI](/companies/xai.md).[^seq-openai][^xai-b]

## What is not established

* **Fund size for the current vintage.** No first-party source read here states it; the encyclopaedia figure is an assets-under-management number from January 2025, not a fund size.[^wiki-sequoia]
* **Whether Sequoia holds Cursor.** The firm's companies listing page contains no portfolio entry for Cursor or Anysphere; the only match on that page was a CSS class name, which is exactly the kind of false positive a graph should refuse.

## Disputed and unverified

* **Partnership dates as investment dates.** "Partnered 2021" on the OpenAI page and "Partnered 2026" on the Anthropic page are Sequoia's own framing of when the relationship began, and they are recorded as such rather than converted into round dates.[^seq-openai][^seq-anthropic]

[^wiki-sequoia]: Wikipedia, "Sequoia Capital", https://en.wikipedia.org/wiki/Sequoia_Capital
[^seq-openai]: Sequoia Capital, "OpenAI", portfolio page: founded 2015, partnered 2021, https://sequoiacap.com/companies/openai
[^seq-anthropic]: Sequoia Capital, "Anthropic", portfolio page: founded 2021, partnered 2026, https://sequoiacap.com/companies/anthropic
[^seq-ssi]: Sequoia Capital, "Safe Superintelligence", portfolio page: founded 2024, partnered 2024, https://sequoiacap.com/companies/safe-superintelligence
[^tc-anthropic-h]: TechCrunch, "Anthropic raises $65 billion, nears $1T valuation ahead of IPO", 28 May 2026, https://techcrunch.com/2026/05/28/anthropic-raises-65-billion-nears-1t-valuation-ahead-of-ipo/
[^xai-b]: xAI, "Series B funding round", https://x.ai/news/series-b
