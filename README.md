# The LLM Advertising Ecosystem: An Atlas

*An independent research report mapping how advertising is emerging inside Large Language Models (LLMs) and AI answer engines. It distinguishes the roles of media agencies, AdTech companies, and the LLM platforms themselves, and explains the technical and economic frameworks that connect them.*

> Status: living document | Scope: strategic + technical | Audience: marketers, AdTech builders, agency strategists, researchers

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

---

## 1. Executive Summary

Advertising inside LLMs is a genuinely new channel rather than a re-skin of search. Traditional search advertising matches ads to discrete keywords; LLM advertising instead reasons over a conversation's context and the user's underlying intent, then decides whether a commercial answer is even appropriate. That single shift reshapes every layer of the value chain.

At a high level the chain runs from the brand or marketer, through planning and buying intermediaries (agencies and/or AdTech), into an ad-decisioning layer, and finally to a placement rendered inside a model's response. What is unusual is that several of these layers are being redesigned at once: new protocols are proposed for how buyers and sellers talk to each other, new economic models are debated (outcome-based rather than impression-based), and new "agentic" software can plan and execute buys with limited human touch.

This report separates three often-conflated groups. Media agencies own strategy, brand safety, and accountability. AdTech vendors (DSPs, SSPs, and emerging agent platforms) own the plumbing that targets, transacts, and measures. LLM platforms own the surface, the user relationship, and ultimately the rules for when an ad can appear at all.

---

## 2. Why LLM Advertising Is Different

**From keywords to intent.** A keyword auction assumes the query itself is the intent. In a conversation, intent accumulates over multiple turns and may never be stated as a keyword at all. The system must infer that a user comparing hiking boots for a rainy trip is a commercial opportunity, and choose whether a sponsored suggestion helps or annoys.

**From pages to answers.** Classic display and search place ads beside content. An LLM often *is* the content, synthesizing a single answer. An ad can therefore appear as a distinct sponsored element, or be woven into a recommendation, which raises sharper transparency and trust questions than a labeled sidebar unit.

**From position to timing.** In search, position on a results page is the scarce good. In a conversation, *timing* is scarce: showing a product suggestion at the wrong moment breaks the assistant's usefulness. Deciding *whether and when* to advertise becomes a first-class ranking problem, not just *which* ad to show.

**Trust is the constraint, not inventory.** Because users treat an assistant as an advisor, an ad that feels like a betrayal of that advice is far costlier than a skippable banner. This tends to push the ecosystem toward heavy labeling, conservative frequency, and outcome-based pricing.

---

## 3. The Ecosystem Map: Who Does What

Think of four primary actor groups plus the standards bodies that let them interoperate.

### 3.1 Brands & Marketers
The demand origin. They bring budgets, objectives, creative assets, and first-party data. The open strategic question for them is build vs. buy: run campaigns in-house against platform APIs, or delegate to an agency that abstracts the complexity.

### 3.2 Media Buying Agencies
Historically the primary executors of media plans. In an LLM world their tactical execution role is partly automated, but their strategic role — audience strategy, brand safety, measurement design, cross-channel orchestration, and accountability to the CMO — arguably grows. Rather than being disintermediated, many are repositioning as owners of the AI *operating system* a brand uses. Holding groups are building proprietary platforms (see Section 5) precisely to avoid becoming a thin layer on top of someone else's tech.

### 3.3 AdTech: DSPs, SSPs, and New Intermediaries
- **DSPs (Demand-Side Platforms)** buy inventory on behalf of advertisers. Incumbents are adapting by adding AI planning copilots and, increasingly, "agent" interfaces that can be instructed in natural language. Examples discussed in industry coverage include agent layers announced by large DSPs and network offerings positioned around AI-driven buying.
- **SSPs (Supply-Side Platforms)** represent the sell side. Their LLM analogue is any layer that packages, prices, and exposes model "ad opportunities" to buyers.
- **New specialized intermediaries** are appearing whose product *is* an AI agent that plans, negotiates, or executes buys, and vendors focused on making agent-to-agent advertising measurable and sustainable. These sit between classic DSP/SSP roles and the agentic protocols described in Section 4.

### 3.4 LLM Platforms (OpenAI, Google, and others)
The surface owners. Their posture is still forming and can resemble three different archetypes:
- a **publisher**, selling attention on its own property;
- a **walled garden**, controlling data, targeting, and measurement end to end;
- a **new platform/marketplace**, exposing APIs and protocols so third parties can transact against the surface.

Google's advantage is an existing ads stack it can extend into AI answer surfaces; a pure-play like OpenAI faces the harder question of how to introduce advertising without eroding the assistant relationship that makes the product valuable.

### 3.5 Standards Bodies
Interoperability is being worked on in the open — most visibly through industry initiatives aimed at agentic advertising, and proposed protocols for how agents and ad systems communicate. These matter because without shared standards each LLM becomes its own silo, which favors walled gardens over an open ecosystem.

---

## 4. How the System Works: Mechanics

### 4.1 Targeting & Placement
Two paradigms coexist. **Keyword-based** targeting matches a literal query to a bid. **Conversational-intent** targeting reads the accumulated dialogue — the task the user is trying to accomplish — and treats a relevant sponsored suggestion as one possible output. A useful mental model is a "contextual hint": the model is given signals about commercial context and may surface a sponsored card only when it improves the answer.

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

The novel part is the "should we advertise at all?" gate and the tight coupling between the ad server/DSP and the model's generation step, rather than a separate page-render pipeline.

### 4.3 Protocols & Interoperability
A cluster of emerging protocols aims to standardize how these components talk:
- **MCP (Model Context Protocol)** — a way to give models structured access to external tools and context, which advertising systems can use to expose catalogs, offers, or ad decisioning as tools.
- **AdCP-style ad protocols** — proposals for a common language so buyers, sellers, and agents can request and fulfill ad opportunities programmatically.
- **Agent-to-agent (A2A) communication** — patterns for a buyer's agent and a seller's agent to negotiate directly.
- **Industry initiatives** (e.g., agentic advertising working groups) — attempts to align the above into shared specs and Ad Management APIs.

### 4.4 Decisioning: When and What to Show
Placement becomes a ranking problem with an extra dimension. Beyond "which ad wins the auction," the system estimates the *cost to trust and usefulness* of interrupting, and may decline to show anything. Academic work (for example research examining advertising dynamics inside LLM conversations) explores auction design, disclosure, and how ad insertion affects answer quality and user welfare.

### 4.5 Economics & Pricing
No single model has won. Candidates include:
- **CPM (cost per mille)** — pay per thousand impressions; simple but weak fit for a low-frequency, trust-sensitive surface.
- **CPC (cost per click)** — familiar from search; works where a sponsored card invites a click.
- **CPA / cost-per-conversion or cost-per-action** — pay for outcomes; a strong conceptual fit because the assistant can often observe task completion, and it aligns incentives around usefulness rather than interruption.

The direction of travel favors outcome-based pricing, because it lets platforms show fewer, higher-quality ads while still monetizing.

### 4.6 Measurement & Optimization
The channel needs its own analogues of CTR and conversion rate. Likely metrics include sponsored-suggestion acceptance rate, assisted-conversion attribution across the conversation, downstream action completion, and *negative* signals such as trust erosion or session abandonment after an ad. Optimization loops resemble programmatic today (bid, measure, adjust) but must weight answer quality and retention far more heavily.

---

## 5. The Evolving Role of Media Buying Agencies

### 5.1 Holding Groups Are Building Platforms
The large holding groups are responding by investing in proprietary AI platforms rather than only reselling third-party tech — offerings positioned as an intelligence/operating layer that unifies data, planning, and activation across channels. The strategic goal is to own the interface the client uses, so the agency's value is not commoditized by any single AdTech or LLM vendor.

### 5.2 Build vs. Buy for Agencies
Agencies blend both: proprietary layers for data, identity, and orchestration; third-party AdTech and LLM APIs for reach and execution. Their differentiated value proposition is increasingly *governance and accountability* — brand safety, measurement integrity, and cross-channel strategy — rather than the mechanical act of buying.

### 5.3 The Changing Job of the Media Buyer
The classic "trader" role shifts from tactical button-pushing toward strategy, prompt/agent supervision, quality control, and interpreting outcomes. Human expertise moves up the stack: setting objectives and guardrails, auditing what agents do, and owning client trust — work that automation does not remove but reframes.

---

## 6. The Agentic Future

### 6.1 What "AI Agents" Mean in Advertising
Here an *agent* is software that can be given a goal ("acquire customers under a target CPA in these markets") and then plan, negotiate, execute, and optimize with limited step-by-step human instruction. Agents can operate on both sides: a buyer's agent seeking outcomes, a seller's agent maximizing yield.

### 6.2 Planning, Negotiation, Execution
- **Planning:** translate business goals into audience, budget, and channel strategy.
- **Negotiation:** buyer and seller agents settle price and terms directly, potentially in real time.
- **Execution & optimization:** launch, monitor, and adjust continuously against outcome signals.

### 6.3 Interoperability & Standards
For agents from different vendors to transact, they need shared rules: common ad protocols, agreed message formats, identity and authorization, and audit trails. This is the point of open initiatives and Ad Management APIs — without them, agentic buying fragments into incompatible walled gardens.

### 6.4 Governance
Agentic buying raises new questions: who is accountable when an agent misbehaves, how brand-safety rules are enforced at machine speed, how collusion between buyer/seller agents is prevented, and how humans stay meaningfully in the loop. Expect guardrails, spend caps, and human sign-off gates to be first-class features, not afterthoughts.

---

## 7. Practical Examples & Case Studies

*Illustrative categories of what LLM advertising looks like in practice. Treat specifics as fast-moving; verify against primary sources before citing.*

- **Sponsored cards in chat assistants** — discrete, labeled product suggestions surfaced within a conversational answer when commercial intent is detected.
- **Ads in AI answer/overview surfaces** — sponsored units placed above or within AI-generated summaries on search-style surfaces, extending existing search ad formats.
- **Shopping/comparison assists** — sponsored placements inside product research or comparison flows, where a recommendation naturally carries commercial weight.

### 7.1 Effectiveness — What to Look For
When evaluating case studies, separate three things: (1) *engagement* (did users click/accept the suggestion?), (2) *outcomes* (did it drive conversions or actions?), and (3) *trust cost* (did satisfaction, retention, or return usage decline?). Early results are mixed and highly format-dependent; a format that wins on clicks can still lose on trust. Insist on studies that report the trust/retention dimension, not just CTR.

---

## 8. Open Questions & Risks

- **Trust vs. monetization:** the core tension. Over-advertising can destroy the advisor relationship that makes assistants valuable.
- **Disclosure & regulation:** how must sponsored content be labeled inside a synthesized answer? Expect regulatory attention on deception and native-ad blurring.
- **Measurement legitimacy:** who verifies conversions and prevents self-marking by walled gardens?
- **Data & privacy:** conversational intent is deeply personal; targeting on it invites scrutiny.
- **Market structure:** does the value chain consolidate into a few walled gardens, or do open protocols keep it competitive?

---

## 9. Glossary

- **LLM** — Large Language Model; the engine behind AI answer/chat surfaces.
- **DSP / SSP** — Demand-Side / Supply-Side Platform; buy-side and sell-side AdTech.
- **CPM / CPC / CPA** — pricing by impression / click / action (outcome).
- **MCP** — Model Context Protocol; structured tool/context access for models.
- **AdCP** — proposed advertising context/commerce protocol for programmatic agent buying.
- **A2A** — agent-to-agent communication.
- **Agentic advertising** — goal-driven software agents planning, negotiating, and executing ad buys.
- **Contextual / conversational-intent targeting** — matching ads to inferred task/intent rather than literal keywords.

---

## 10. How to Contribute

This atlas is meant to be extended. Contributions that improve it most:
- Add primary sources (vendor docs, spec pages, peer-reviewed studies) with dates.
- Flag anything outdated; the space moves quickly.
- Keep claims sourced and separate opinion from fact.

Open an issue or pull request with proposed changes. Please cite sources and note the observation date.

---

*This report is an independent synthesis for research and educational purposes. It does not represent any company's official position. Verify time-sensitive claims against primary sources.*
