---
okf_version: "0.2"
---

# Leading AI companies

A knowledge bundle in Google's Open Knowledge Format v0.2. It is a graph first: 17 concepts carrying 192 typed edges, with `_tools/okf-check.py` for conformance and `_tools/build-index.py` for these listings.

Entries are listed here for browsing; the machine-readable layer is the `relations` frontmatter block in each concept. Conventions are frozen in [conventions.md](conventions.md).

# Bundle-level concepts

Concepts that live at the bundle root rather than inside a directory:

* [conventions](conventions.md)

# Companies

* [Anthropic](companies/anthropic.md) - AI safety and research company whose Claude family of frontier language models underpins coding, enterprise and agentic products.
* [Google DeepMind](companies/google-deepmind.md) - Alphabet's AI research laboratory, founded in London in 2010 as DeepMind Technologies and merged with Google Brain in 2023; the developer of the Gemini and Gemma model families and of AlphaGo and AlphaFold.
* [Google](companies/google.md) - Alphabet's largest operating company and the owner of Google DeepMind, the TPU silicon line, Google Cloud and the Gemini model family; simultaneously an investor in, partner to and competitor of Anthropic.
* [OpenAI](companies/openai.md) - Frontier model lab behind ChatGPT and the GPT model family, founded as a nonprofit in 2015 and restructured in 2025 into a public benefit corporation controlled by the OpenAI Foundation.
* [Replit](companies/replit.md) - Agentic software-creation platform that turns natural-language prompts into deployed applications; Y Combinator Winter 2018.

# Founders

* [Amjad Masad](founders/amjad-masad.md) - Co-founder and CEO of Replit; previously a software engineer at Facebook and a founding engineer at Codecademy.
* [Dario Amodei](founders/dario-amodei.md) - Co-founder and CEO of Anthropic; previously VP of Research at OpenAI, Google Brain, and Baidu's Silicon Valley AI Lab.
* [Demis Hassabis](founders/demis-hassabis.md) - Co-founder and chairman of Google DeepMind, Alphabet's chief scientist from 2026, chief executive of Isomorphic Labs and joint winner of the 2024 Nobel Prize in Chemistry; a chess prodigy turned game developer turned neuroscientist.
* [Sam Altman](founders/sam-altman.md) - Co-founder and chief executive of OpenAI, previously president of Y Combinator and co-founder of Loopt; the central figure in OpenAI's 2023 board crisis and its 2026 listing attempt.

# AI Domains

* [Agentic AI](ai-domains/agentic-ai.md) - Systems in which a model takes actions in a loop against tools and an environment, rather than answering once; the domain where tool protocols and agent benchmarks live.
* [Foundation models](ai-domains/foundation-models.md) - Models trained on broad data at scale and adapted to many downstream tasks; the domain the frontier labs in this bundle compete in.

# AI Use Cases

* [AI in the software development lifecycle](ai-use-cases/ai-sdlc.md) - Code generation, review, testing and maintenance performed or assisted by AI models; the use case with the strongest independent experimental evidence and the largest gap between forecast and measured effect.

# Technologies

* [Model Context Protocol](technologies/mcp.md) - Open standard introduced by Anthropic in November 2024 that connects AI assistants to tools and data through MCP hosts, clients and servers over JSON-RPC; donated to the Linux Foundation in December 2025.

# Models

* [Claude](models/claude.md) - The large language model family sold by Anthropic, named after Claude Shannon, trained with a written constitution, and released in capability tiers from Haiku to Opus, with Mythos and Fable added in 2026.
* [Gemini](models/gemini.md) - Google DeepMind's multimodal model family, announced in December 2023 as the successor to LaMDA and PaLM 2, released in Pro, Deep Think, Flash and Flash Lite variants, with the open-weight Gemma family as its sibling.
* [GPT](models/gpt.md) - OpenAI's generative pre-trained transformer model family, from GPT-3's 175 billion parameters to the router-based GPT-5 system and the GPT-6 Astra release of September 2026.

# Directories declared but not yet populated

Named before they exist so a link from a populated concept resolves to a declared target. Under OKF §6.1, a link to a not-yet-written concept is not an error.

* `investors/` - Investors - Venture, growth and corporate funds.
* `concepts/` - Concepts - Techniques and ideas.
* `institutions/` - Institutions - Universities and labs founders came out of.
* `people/` - People - Non-founder executives.

# Non-concept directories

* `images/` - media cited by concepts. Every asset carries a licence, a credit, a hash and a footnote definition line in the concept that uses it, so an asset is traceable by the same rule as a claim.
* `_tools/` - the conformance linter and this index generator.

# How to query the graph

The brief's downstream questions are traversals over the `relations` blocks, not searches:

* **Domain overlap.** Count `operates-in` edges pointing at a domain path; two companies overlap in the domains they both point at.
* **Founder track record.** Walk `previously-at` and `founded` from a `founders/` concept to companies, then read each company's current status.
* **Who supplies whom.** Follow `customer-of` for demand, `partners-with` for alliances and `competes-with` for rivalry; note that a pair can hold several at once, as Google and Anthropic do.
* **Institutional lineage.** Follow `educated-at` from founders into `institutions/`.

Generated by `_tools/build-index.py` on 2026-09-11.
