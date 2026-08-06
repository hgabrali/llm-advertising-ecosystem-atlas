# The LLM Advertising Ecosystem on GitHub: A Classified Repository Index

*A companion to the main [Atlas](./README.md). This index maps notable open-source repositories in the LLM / agentic advertising space, grouped into three families: **official standards & protocol projects**, **community tooling & curated lists**, and **research / academic prototypes**. It highlights the most popular and the most distinct projects in each family, rather than being exhaustive.*

> **On the data:** Star counts, languages, and last-push dates are point-in-time observations captured on **2026-08-06** via the GitHub API and move quickly. Treat them as a snapshot; verify current figures on each repository page. Inclusion here is descriptive, not an endorsement, and does not imply any affiliation.

---

## How the three families differ

| Family | What it contains | Who typically maintains it | Why it matters |
| --- | --- | --- | --- |
| **A. Official standards & protocols** | The specs, schemas, and reference SDKs that define how agents transact (AdCP, AAMP components). | Standards bodies and their founding contributors (AgenticAdvertising.org / adcontextprotocol, IAB Tech Lab). | These are the *ground truth* the rest of the ecosystem builds on; the same repositories cited in the Atlas. |
| **B. Community tooling & curated lists** | MCP servers, multi-platform ad-API connectors, agent-skill libraries, and awesome-lists. | Independent developers, small vendors, and marketing-tech shops. | Shows how practitioners are *operationalizing* the standards today across Google/Meta/TikTok/OpenAI Ads. |
| **C. Research & academic prototypes** | Auction-design experiments, quality-preserving ad insertion, multi-agent auto-bidding, and reimagined ad UX. | Academics, students, and independent researchers. | Explores the *open questions* (auction mechanics, answer quality, welfare) ahead of production. |

---

## A. Official standards & protocol projects

The authoritative, code-backed home of the protocols described in the Atlas (Sections 5.5, 7.3). Two organizations dominate: **adcontextprotocol** (AdCP) and **IAB Tech Lab** (AAMP and its components).

| Repository | ★ | Lang | License | What it is |
| --- | ---: | --- | --- | --- |
| [adcontextprotocol/adcp](https://github.com/adcontextprotocol/adcp) | 240 | TypeScript | Apache-2.0 | Docs + reference implementation for the **Ad Context Protocol** — the flagship AdCP repo. |
| [IABTechLab/agentic-audiences](https://github.com/IABTechLab/agentic-audiences) | 41 | Python | (custom) | Open standard (donated by LiveRamp) for how agents exchange user context — from prompt-based coordination to embedding-based optimization. |
| [IABTechLab/agentic-real-time-framework](https://github.com/IABTechLab/agentic-real-time-framework) | 24 | Rust | AGPL-3.0 | **ARTF** — the container-based, sub-millisecond real-time foundation (the "Agentic Foundations" pillar of AAMP). |
| [IABTechLab/seller-agent](https://github.com/IABTechLab/seller-agent) | 23 | Python | Apache-2.0 | Reference **Seller Agent SDK** for multi-buyer discovery and transaction handling. |
| [IABTechLab/buyer-agent](https://github.com/IABTechLab/buyer-agent) | 23 | Python | Apache-2.0 | Reference **Buyer Agent SDK** — the demand-side counterpart. |
| [IABTechLab/AAMP](https://github.com/IABTechLab/AAMP) | 18 | — | Apache-2.0 | Umbrella repo for the **Agentic Advertising Management Protocols** initiative. |
| [adcontextprotocol/adcp-client](https://github.com/adcontextprotocol/adcp-client) | 18 | TypeScript | Apache-2.0 | Official TypeScript client/server SDK for AdCP. |
| [IABTechLab/agentic-direct](https://github.com/IABTechLab/agentic-direct) | 8 | JavaScript | Apache-2.0 | *Agentic Direct* schema work (built on OpenDirect). |

*Most popular:* `adcontextprotocol/adcp`. *Most distinct:* `IABTechLab/agentic-audiences` (embedding-based audience exchange) and `agentic-real-time-framework` (the only Rust, latency-focused core).

---

## B. Community tooling & curated lists

Practitioner-built connectors, MCP servers, agent-skill libraries, and reference lists that operationalize agentic buying across existing ad platforms.

| Repository | ★ | Type | License | What it is |
| --- | ---: | --- | --- | --- |
| [jshorwitz/awesome-agentic-advertising](https://github.com/jshorwitz/awesome-agentic-advertising) | 33 | Awesome-list | — | Curated list of MCP servers, tools, protocols, and resources for AI-powered ad campaign management (Google/Meta/LinkedIn/Reddit/TikTok/Amazon). |
| [itallstartedwithaidea/advertising-hub](https://github.com/itallstartedwithaidea/advertising-hub) | 31 | Multi-platform hub | MIT | "One-stop shop" for ad-platform APIs, MCP servers, and AI agents across 14 platforms with PPC automation. |
| [itallstartedwithaidea/agent-skills](https://github.com/itallstartedwithaidea/agent-skills) | 31 | Agent-skill library | MIT | 73+ Google Ads management skills for Claude Code, Cursor, Codex, Gemini, etc. |
| [fseixas/chatgpt-ads-builder](https://github.com/fseixas/chatgpt-ads-builder) | 7 | Claude skill | MIT | Builds complete **ChatGPT Ads** campaigns (context-hint ad groups, char-validated copy, icon prompts). |
| [PaidSync/paidsync-mcp](https://github.com/PaidSync/paidsync-mcp) | 1 | MCP endpoint | MIT | 430+ tools across 13 ad platforms behind one MCP endpoint (create on Google/Meta/LinkedIn/OpenAI Ads). |
| [pxpilot/adcp-sandbox](https://github.com/pxpilot/adcp-sandbox) | 0 | Sandbox | — | A hands-on sandbox for experimenting with the AdCP standard. |

*Most popular:* `awesome-agentic-advertising`. *Most distinct:* `chatgpt-ads-builder` (targets the ChatGPT Ads surface specifically) and `paidsync-mcp` (single MCP endpoint fanning out to many platforms).

---

## C. Research & academic prototypes

Experimental code exploring the economic and quality questions raised in the Atlas (Sections 5.6–5.7, 9).

| Repository | ★ | Lang | What it is |
| --- | ---: | --- | --- |
| [chaovven/maab](https://github.com/chaovven/maab) | 27 | Python | Code for *"A Cooperative-Competitive Multi-Agent Framework for Auto-bidding in Online Advertising"* (WSDM 2022) — multi-agent auto-bidding. |
| [lab1806/LLM-advertising-fusion](https://github.com/lab1806/LLM-advertising-fusion) | 5 | Python | Experimental work on fusing advertising into LLM outputs. |
| [MuzhiMa/Quality-Preserving_LLM_Advertising](https://github.com/MuzhiMa/Quality-Preserving_LLM_Advertising) | 0 | Jupyter | Research code for *quality-preserving* advertising in an LLM auction — directly on the "should we advertise at all?" trade-off. |
| [DevPranjal/steroiADs](https://github.com/DevPranjal/steroiADs) | 1 | TypeScript | Prototype reimagining ads inside LLM-powered search. |

*Most popular:* `chaovven/maab` (peer-reviewed, WSDM 2022). *Most distinct:* `Quality-Preserving_LLM_Advertising` (formalizes the answer-quality-vs-monetization tension central to the Atlas).

---

## Notes & caveats

- This is a **curated snapshot**, not a ranking or a complete census; many small forks and private efforts exist.
- Star counts and metadata were read from the GitHub API on 2026-08-06 and will drift.
- Repository descriptions are quoted/paraphrased from each project's own summary; verify scope, licensing, and maintenance status before relying on any project.
- Family A repositories are the primary sources cited throughout the [main Atlas](./README.md); Families B and C are illustrative of the surrounding ecosystem.
