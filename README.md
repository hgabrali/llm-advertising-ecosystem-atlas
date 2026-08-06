# The LLM Advertising Ecosystem: An Atlas

*An independent research report mapping how advertising is emerging inside Large Language Models (LLMs) and AI answer engines. It distinguishes the roles of media agencies, AdTech companies, and the LLM platforms themselves, and explains the technical and economic frameworks that connect them.*

> Status: living document | Scope: strategic + technical | Audience: marketers, AdTech builders, agency strategists, researchers

> **On sources:** Claims are keyed to numbered references in [Section 11](#11-references--sources). This is a fast-moving space; many sources are dated 2025-2026. Always verify time-sensitive figures against the primary source and note the observation date.

---

## Table of Contents

1. Executive Summary
2. Why LLM Advertising Is Different
3. The Ecosystem Map: Who Does What
4. How the System Works: Mechanics
5. The Evolving Role of Media Buying Agencies
6. The Agentic Future
7. Practical Examples & Case Studies
8. Open Questions & Risks
9. Glossary
10. How to Contribute
11. References & Sources

---

## 1. Executive Summary

Advertising inside LLMs is a genuinely new channel rather than a re-skin of search. Traditional search advertising matches ads to discrete keywords; LLM advertising instead reasons over a conversation's context and the user's underlying intent, then decides whether a commercial answer is even appropriate. That single shift reshapes every layer of the value chain [11][14].

At a high level the chain runs from the brand or marketer, through planning and buying intermediaries (agencies and/or AdTech), into an ad-decisioning layer, and finally to a placement rendered inside a model's response. What is unusual is that several of these layers are being redesigned at once: new protocols are proposed for how buyers and sellers talk to each other [3][5][7], new economic models are debated (outcome-based rather than impression-based) [12], and new "agentic" software can plan and execute buys with limited human touch [18][19].

This report separates three often-conflated groups. Media agencies own strategy, brand safety, and accountability [15][16]. AdTech vendors (DSPs, SSPs, and emerging agent platforms) own the plumbing that targets, transacts, and measures [18][20][21]. LLM platforms own the surface, the user relationship, and ultimately the rules for when an ad can appear at all [9][10][13].

---

## 2. Why LLM Advertising Is Different

**From keywords to intent.** A keyword auction assumes the query itself is the intent. In a conversation, intent accumulates over multiple turns and may never be stated as a keyword at all. The system must infer that a user comparing hiking boots for a rainy trip is a commercial opportunity, and choose whether a sponsored suggestion helps or annoys [11][23].

**From pages to answers.** Classic display and search place ads beside content. An LLM often *is* the content, synthesizing a single answer. An ad can therefore appear as a distinct sponsored element, or be woven into a recommendation, which raises sharper transparency and trust questions than a labeled sidebar unit [10][24].

**From position to timing.** In search, position on a results page is the scarce good. In a conversation, *timing* is scarce: showing a product suggestion at the wrong moment breaks the assistant's usefulness. Deciding *whether and when* to advertise becomes a first-class ranking problem, not just *which* ad to show [22][25].

**Trust is the constraint, not inventory.** Because users treat an assistant as an advisor, an ad that feels like a betrayal of that advice is far costlier than a skippable banner. This pushes the ecosystem toward heavy labeling, answer independence, conservative frequency, and outcome-based pricing [9][10][24].

---

## 3. The Ecosystem Map: Who Does What

Think of four primary actor groups plus the standards bodies that let them interoperate.

### 3.1 Brands & Marketers
The demand origin. They bring budgets, objectives, creative assets, and first-party data. The open strategic question for them is build vs. buy: run campaigns in-house against platform APIs, or delegate to an agency that abstracts the complexity.

### 3.2 Media Buying Agencies
Historically the primary executors of media plans. In an LLM world their tactical execution role is partly automated, but their strategic role — audience strategy, brand safety, measurement design, cross-channel orchestration, and accountability to the CMO — arguably grows. Rather than being disintermediated, the large holding groups are repositioning as owners of the AI *operating system* a brand uses, building proprietary platforms (see Section 5) precisely to avoid becoming a thin layer on top of someone else's tech [15][16][17].

### 3.3 AdTech: DSPs, SSPs, and New Intermediaries
- **DSPs (Demand-Side Platforms)** buy inventory on behalf of advertisers. Incumbents are adapting by adding AI planning copilots and "agent" interfaces that can be instructed in natural language; for example, Yahoo's DSP has publicized agentic-AI capabilities and interoperability with partner agents [20][21].
- **SSPs (Supply-Side Platforms)** represent the sell side. Their LLM analogue is any layer that packages, prices, and exposes model "ad opportunities" to buyers; SSPs such as Magnite and PubMatic have participated in early agentic test buys [19].
- **New specialized intermediaries** build the agents themselves. Scope3, for instance, positions an "agentic media platform" where buying and selling agents act on behalf of brands and publishers [18][8]. These sit between classic DSP/SSP roles and the agentic protocols described in Section 4.

### 3.4 LLM Platforms (OpenAI, Google, and others)
The surface owners. Their posture can resemble three different archetypes: a **publisher** selling attention on its own property; a **walled garden** controlling data, targeting, and measurement end to end; or a **new platform/marketplace** exposing APIs and protocols so third parties can transact against the surface.

- **OpenAI** began testing ads in ChatGPT, emphasizing clear labeling, privacy protection, and that ads run on separate systems so advertisers cannot shape or rank ChatGPT's responses ("answer independence") [9][10]. It has also been reported to expose cost-per-click buying and a conversions pixel/API for advertisers [12][13].
- **Google** is extending its existing ads stack into AI surfaces — ads in AI Overviews and AI Mode — where an ad can appear when it matches both the query and the AI answer's content [11][14].

### 3.5 Standards Bodies
Interoperability is being worked on in the open. The **IAB Tech Lab Agentic Advertising Initiative** (umbrella: AAMP, Agentic Advertising Management Protocols) aims to embed agent protocols with existing Tech Lab standards for buying and selling [1][2][6]. Without shared standards each LLM becomes its own silo, which favors walled gardens over an open ecosystem.

---

## 4. How the System Works: Mechanics

### 4.1 Targeting & Placement
Two paradigms coexist. **Keyword-based** targeting matches a literal query to a bid. **Conversational-intent** targeting reads the accumulated dialogue — the task the user is trying to accomplish — and treats a relevant sponsored suggestion as one possible output [11][23]. A useful mental model is a "contextual hint": the model is given signals about commercial context and may surface a sponsored card only when it improves the answer.

### 4.2 Technical Architecture
Conceptually, an ad-decisioning path is inserted around the model's response generation:

```text
User turn
  -> Intent & context extraction
    -> Ad opportunity check (should we advertise at all?)
      -> Request to ad server / DSP (candidate ads + bids)
        -> Ranking (relevance x bid x trust/quality)
          -> Placement decision (whether, where, how labeled)
            -> Rendered answer with sponsored element
              -> Feedback signals (impression, click, action)
```

The novel part is the "should we advertise at all?" gate and the tight coupling between the ad server/DSP and the model's generation step, rather than a separate page-render pipeline [22][25].

### 4.3 Protocols & Interoperability
A cluster of emerging protocols aims to standardize how these components talk:
- **MCP (Model Context Protocol)** — an open standard, introduced by Anthropic in November 2024, that connects LLM applications to external data sources and tools; advertising systems can use it to expose catalogs, offers, or ad decisioning as tools [3][4].
- **AdCP (Ad Context Protocol)** — an open standard for AI agents to communicate and transact (plan, buy, sell) across the advertising ecosystem [5][7][8].
- **Agent-to-agent (A2A) communication** — patterns for a buyer's agent and a seller's agent to negotiate directly, referenced within the IAB Tech Lab agentic work [1].
- **Industry initiatives** — the IAB Tech Lab Agentic Advertising Initiative / AAMP align the above into shared specs and Ad Management APIs [1][2][6].

### 4.4 Decisioning: When and What to Show
Placement becomes a ranking problem with an extra dimension. Beyond "which ad wins the auction," the system estimates the *cost to trust and usefulness* of interrupting, and may decline to show anything. Academic work explores auction design, disclosure, ad timing, and how ad insertion affects answer quality and user welfare — including generative-auction mechanisms and optimal-stopping approaches to *when* to insert an ad [22][25][26][27].

### 4.5 Economics & Pricing
No single model has won. Candidates include:
- **CPM (cost per mille)** — pay per thousand impressions; simple but a weak fit for a low-frequency, trust-sensitive surface.
- **CPC (cost per click)** — familiar from search; OpenAI has been reported to turn on cost-per-click ads in ChatGPT, letting advertisers compare results against other channels [12].
- **CPA / cost-per-conversion or cost-per-action** — pay for outcomes; a strong conceptual fit because the assistant can often observe task completion, supported by conversion pixels/APIs [13].

The direction of travel favors outcome-based pricing, because it lets platforms show fewer, higher-quality ads while still monetizing.

### 4.6 Measurement & Optimization
The channel needs its own analogues of CTR and conversion rate. Likely metrics include sponsored-suggestion acceptance rate, assisted-conversion attribution across the conversation, downstream action completion (via conversions pixel/API) [13], and *negative* signals such as trust erosion or session abandonment after an ad. Optimization loops resemble programmatic today (bid, measure, adjust) but must weight answer quality and retention far more heavily [24].

---

## 5. The Evolving Role of Media Buying Agencies

### 5.1 Holding Groups Are Building Platforms
The large holding groups are responding by investing in proprietary AI platforms rather than only reselling third-party tech: WPP has **WPP Open** (an agentic marketing platform), Publicis has **CoreAI**, and Omnicom has **Omni** [15][16][17]. Each is positioned as an intelligence/operating layer that unifies data, planning, creative, and activation across channels. The strategic goal is to own the interface the client uses, so the agency's value is not commoditized by any single AdTech or LLM vendor.

### 5.2 Build vs. Buy for Agencies
Agencies blend both: proprietary layers for data, identity, and orchestration; third-party AdTech and LLM APIs for reach and execution. Their differentiated value proposition is increasingly *governance and accountability* — brand safety, measurement integrity, and cross-channel strategy — rather than the mechanical act of buying [16].

### 5.3 The Changing Job of the Media Buyer
The classic "trader" role shifts from tactical button-pushing toward strategy, prompt/agent supervision, quality control, and interpreting outcomes. Tools like a "planning agent" can turn a single conversational prompt into a media plan in minutes, moving human expertise up the stack: setting objectives and guardrails, auditing what agents do, and owning client trust [21].

---

## 6. The Agentic Future

### 6.1 What "AI Agents" Mean in Advertising
Here an *agent* is software that can be given a goal ("acquire customers under a target CPA in these markets") and then plan, negotiate, execute, and optimize with limited step-by-step human instruction. Agents can operate on both sides: a buyer's agent seeking outcomes, a seller's agent maximizing yield [18][8].

### 6.2 Planning, Negotiation, Execution
- **Planning:** translate business goals into audience, budget, and channel strategy [21].
- **Negotiation:** buyer and seller agents settle price and terms directly, potentially in real time.
- **Execution & optimization:** a buying agent can evaluate many inventory options simultaneously, build campaign structure, allocate budget, and adjust continuously against outcome signals [8].

### 6.3 Interoperability & Standards
For agents from different vendors to transact, they need shared rules: common ad protocols (AdCP, AAMP), agreed message formats, identity/authorization, and audit trails. Early cross-vendor test buys have already occurred — Magnite and MiQ completed one of the first AdCP test buys in December 2025, with Scope3 acting as the buyer agent [19]. Without such standards, agentic buying fragments into incompatible walled gardens [1][5].

### 6.4 Governance
Agentic buying raises new questions: who is accountable when an agent misbehaves, how brand-safety rules are enforced at machine speed, how collusion between buyer/seller agents is prevented, and how humans stay meaningfully in the loop. Expect guardrails, spend caps, and human sign-off gates to be first-class features, not afterthoughts [1][18].

---

## 7. Practical Examples & Case Studies

*Illustrative categories of what LLM advertising looks like in practice. Treat specifics as fast-moving; verify against primary sources before citing.*

- **Sponsored elements in chat assistants** — OpenAI's ChatGPT ads test displays clearly labeled sponsored content selected from conversational context, on systems separate from the chat model [9][10][12].
- **Ads in AI answer/overview surfaces** — Google places ads in AI Overviews and AI Mode when the ad matches both the query and the AI answer's content, extending existing Search ad formats [11][14].
- **Agentic media buys** — cross-vendor agent transactions using AdCP, e.g. the Magnite/MiQ/Scope3 test buy, and DSP agent interoperability such as Yahoo DSP with MiQ Sigma [19][20][21].

### 7.1 Effectiveness — What to Look For
When evaluating case studies, separate three things: (1) *engagement* (did users click/accept the suggestion?), (2) *outcomes* (did it drive conversions or actions?), and (3) *trust cost* (did satisfaction, retention, or return usage decline?). Independent analysis notes advertisers currently have fewer delivery/testing controls than in mature channels, so early results are mixed and format-dependent [23][24]. Insist on studies that report the trust/retention dimension, not just CTR.

---

## 8. Open Questions & Risks

- **Trust vs. monetization:** the core tension. Over-advertising can destroy the advisor relationship that makes assistants valuable [10][24].
- **Answer integrity:** research warns that conflicting incentives could change how an LLM interacts with users when ads are present; answer independence and labeling are mitigations [10][24].
- **Disclosure & regulation:** how must sponsored content be labeled inside a synthesized answer? Expect regulatory attention on deception and native-ad blurring.
- **Measurement legitimacy:** who verifies conversions and prevents self-marking by walled gardens?
- **Data & privacy:** conversational intent is deeply personal; targeting on it invites scrutiny [9].
- **Market structure:** does the value chain consolidate into a few walled gardens, or do open protocols (AdCP/AAMP) keep it competitive? [1][5]

---

## 9. Glossary

- **LLM** — Large Language Model; the engine behind AI answer/chat surfaces.
- **DSP / SSP** — Demand-Side / Supply-Side Platform; buy-side and sell-side AdTech.
- **CPM / CPC / CPA** — pricing by impression / click / action (outcome).
- **MCP** — Model Context Protocol; open standard connecting LLMs to external tools/data [3][4].
- **AdCP** — Ad Context Protocol; open standard for AI agents to plan, buy, and sell ads [5].
- **AAMP** — Agentic Advertising Management Protocols; IAB Tech Lab's umbrella initiative [6].
- **A2A** — agent-to-agent communication.
- **Agentic advertising** — goal-driven software agents planning, negotiating, and executing ad buys [18].
- **Contextual / conversational-intent targeting** — matching ads to inferred task/intent rather than literal keywords.

---

## 10. How to Contribute

This atlas is meant to be extended. Contributions that improve it most:
- Add primary sources (vendor docs, spec pages, peer-reviewed studies) with dates.
- Flag anything outdated; the space moves quickly.
- Keep claims sourced and separate opinion from fact.

Open an issue or pull request with proposed changes. Please cite sources and note the observation date.

---

## 11. References & Sources

*Numbering matches the inline markers above. Access dates are approximate; verify before citing. Several sources postdate common model knowledge cutoffs and were surfaced via live web search.*

**Standards & protocols**

1. IAB Tech Lab - "Agentic Advertising and AI Initiatives." https://iabtechlab.com/standards/agentic-advertising/
2. IAB Tech Lab - "Framing the Agentic Advertising Management Protocols (AAMP)." https://iabtechlab.com/
3. Model Context Protocol - "Specification." https://modelcontextprotocol.io/specification
4. Anthropic - "Introducing the Model Context Protocol" (Nov 25, 2024). https://www.anthropic.com/news/model-context-protocol
5. Ad Context Protocol - Official site. https://adcontextprotocol.org
6. IAB Tech Lab - "AAMP (Agentic Advertising Management Protocols)." https://iabtechlab.com/standards/
7. Ad Context Protocol - "Introduction to the Protocol." https://docs.adcontextprotocol.org/docs/intro
8. Scope3 - "Why AdCP Matters: Interoperability as AI Agents..." (Feb 10, 2026). https://scope3.com/

**LLM platforms**

9. OpenAI - "Testing ads in ChatGPT" (Feb 9, 2026). https://openai.com/index/testing-ads-in-chatgpt/
10. OpenAI Help Center - "Ads in ChatGPT" (Feb 9, 2026). https://help.openai.com/
11. Google Ads Help - "About ads and AI Overviews." https://support.google.com/google-ads/
12. Digiday - "OpenAI turns on cost-per-click ads inside ChatGPT" (Apr 21, 2026). https://digiday.com/
13. OpenAI Developers - "Ads" (conversions pixel & API). https://developers.openai.com/
14. Google (blog.google) - "A new generation of ads for the AI era of Search" (May 20, 2026). https://blog.google/

**Agencies**

15. WPP - "WPP Open - our agentic marketing platform." https://www.wpp.com/open
16. The Media Leader - "Agency groups' AI platforms, explained" (Apr 16, 2026). https://uk.themedialeader.com/
17. Ad Age - "How AI is transforming agencies..." (Jan 21, 2026). https://adage.com/

**AdTech & agents**

18. Scope3 - "Agentic advertising." https://scope3.com/agentic-advertising
19. INMA - "Advertising enters the agentic era as AI agents begin..." (Jan 14, 2026; Magnite/MiQ/Scope3 AdCP test buy). https://www.inma.org/
20. Yahoo Inc. - "Yahoo DSP Agentic AI." https://www.yahooinc.com/yahoo-dsp/agentic-ai
21. Yahoo Finance - "MiQ Sigma Expands with New Data, Capabilities..." (Jun 11, 2026). https://finance.yahoo.com/

**Analysis & academic**

22. "Ads in Conversations" - arXiv (Feb 5, 2025). https://arxiv.org/
23. Marketing Tech News - "ChatGPT ads test a new model for conversational advertising" (Jul 22, 2026). https://www.marketingtechnews.net/
24. Wu, A.J. et al. - "Ads in AI Chatbots? An Analysis of How LLMs..." - arXiv (2026). https://arxiv.org/
25. "Generative Auction towards LLM-Native Advertising" - arXiv (Dec 11, 2025). https://arxiv.org/
26. "LLM-OSDA: An Optimal-Stopping Dynamic Auction..." - arXiv (2026). https://arxiv.org/
27. Feizi, S. et al. - "Online Advertisements with LLMs: Opportunities and Challenges" (2023). https://arxiv.org/

---

*This report is an independent synthesis for research and educational purposes. It does not represent any company's official position. Verify time-sensitive claims against primary sources.*
