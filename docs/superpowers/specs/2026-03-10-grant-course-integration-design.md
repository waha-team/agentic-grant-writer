# Design: Grant Course Integration — Pipeline Enrichment & Search Improvements

*Date: 2026-03-10*
*Status: Approved for implementation planning*
*Source: Grantly course comparison report (`~/grant_course/COURSE_COMPARISON_REPORT.md`)*

---

## Overview

Integrate lessons from the Grantly grant-writing course into the Waha grants pipeline. The primary goals are:

1. **Maximize AI pre-work** — Claude does as much heavy lifting as possible, so humans review polished output rather than doing research themselves
2. **Improve search breadth** — break the pattern of the same 3-5 foundations surfacing across every project
3. **Improve people research quality** — deeper, more actionable key-people dossiers
4. **Better cross-project coordination** — avoid submitting uncoordinated proposals to the same foundation

The approach is **Option C (Enrichment-first)** from the brainstorming session. Option B (Attio as coordination hub with full write-back) is deferred to a future dedicated session.

---

## Design Principles

These apply across all changes:

- **Never punt to the human with "needs further research."** When uncertain, present the options found with links and let the human pick. This applies to LinkedIn matches, foundation fit assessments, grant type classification — everything.
- **Tokens are cheap, hours are not.** Maximize AI pre-work. No arbitrary caps on prospect lists or dossier counts. Let quality gates define scope.
- **Auto-move between stages** unless human input is genuinely needed. The agent asks when it must, proceeds when it can.
- **Enrich in-place, not in separate files.** The brief IS the project definition — enrichment makes it complete, not a separate layer.

---

## Stage 00: Brief Creation + Enrichment

### Current Behavior
Human creates a brief (from Attio or manually), moves it to `01-prospect-research/`.

### New Behavior
When Claude is invoked to process the pipeline (or a specific project), the first thing it does for any project in `00-projects/` is run the enrichment pass on the brief. This is not a file-watcher or cron job — it is the first step Claude executes when a human starts a pipeline session. The enrichment targets the project's `00-PROJECT_BRIEF.md` file (or the equivalent loose `.md` file, which should first be moved into a properly named project subfolder per existing Stage 00 conventions).

### Enrichment Process

**Step 1: Staleness check**
- Check `CONTEXT/IMPACT_DATA.md` last-modified date
- If older than 30 days → warn the human: "IMPACT_DATA.md hasn't been updated in [N] days. Consider updating before proposals are written."
- Log this to `HUMAN_TODO.md` and **proceed with enrichment** (do not hard-block — per INIT.md Principle 6: "Momentum over perfection")

**Step 2: Attio deep dive (project-facing)**
- Search Attio contacts, notes, tasks related to this project's language, geography, people group, and partners
- Surface relational intelligence (e.g., "Aychi is leading an Amharic movement — see note on her Attio record")
- Search the Funding Applications object for any already-submitted applications to foundations that might be relevant to this project

**Step 3: Attio deep dive (foundation-facing)**
- Check Funding Applications object for anything already submitted
- Cross-reference PROSPECTIVE_PARTNERS.md for in-progress research on foundations
- Flag any cross-project conflicts: "Foundation X is already being pursued in Project Y (Stage 03)"

**Step 4: Enrich the brief in-place**

Add the following sections to the brief, clearly labeled as AI-enriched with a timestamp:

```markdown
---
## Enrichment (added by Claude, YYYY-MM-DD)

### PRINT Analysis
- **Project Idea:** [core concept and what sets it apart]
- **Impact:** [what change this creates in the community]
- **Need:** [specific community need being addressed — what happens if nothing changes]
- **Target Population:** [who benefits, how specifically]

### Unique Value Proposition
[2-3 sentence compelling narrative of why this project matters — the "sales letter" hook]

### Keyword Matrix
| Dimension | Terms |
|-----------|-------|
| Geography | [city, region, country] |
| Grant type | [program / equipment / capacity building / operational / seed] |
| Organization type | [501c3, faith-based, missions org] |
| Problem addressed | [e.g., Scripture access, digital literacy] |
| Service type | [e.g., app localization, DBS facilitation] |
| Target audience | [e.g., Hausa speakers, unreached people groups] |
| Community type | [e.g., majority-Muslim, rural, urban diaspora] |

### Grant Type Classification
[Program / Equipment / Capacity Building / Operational / Seed — with reasoning]

### Funder Type Priority
[Ranked tiers from SEARCH_CRITERIA.md with reasoning for this specific project]

### Relevant Partnerships
[From PARTNERSHIPS.md + Attio — which partners are specifically relevant and why]

### Project-Specific External Data
[Population stats, language data, existing Scripture resources, literacy rates — from web research]

### Attio Intelligence
[Summary of relevant contacts, notes, relationships, and any existing Funding Applications found]

### Cross-Project Conflicts
[Any foundations already being pursued in other projects, with stage and status]
```

**Step 5: Quality gate**
- If anything is genuinely ambiguous and can't be resolved from CONTEXT, website, Attio, or web research → ask the human inline using `[HUMAN: ...]` markers
- If the human is present in conversation → ask directly and wait for response
- If all sections are complete → auto-move to `01-prospect-research/`

---

## Stage 01: Prospect Research — Search Breadth Improvements

### Current Behavior
Hardcoded search queries (7 static queries used for every project). Target 15-40 prospects.

### New Behavior
Search queries generated from the keyword matrix. No arbitrary cap — quality gate defines scope.

### Search Strategy

**Method 1: Keyword-matrix-driven searches**
- For each row in the keyword matrix, generate 2-3 search queries combining that dimension with relevant funder-type terms
- Example for a Hausa DBS project: "Nigeria Christian foundation grants", "Hausa ministry funding", "Scripture access underserved languages grants", "Bible app localization foundation"
- Target: 15-20+ unique search queries per project (vs. 7 static today)

**Method 2: Funded-organization search (NEW)**
- On grantmakers.io and ProPublica, search for organizations similar to Waha or Waha's partners that have received grants
- Identify who funded them — these are foundations with demonstrated interest through action, not just stated mission
- This is the single biggest source of new foundations the current system misses

**Method 3: Community foundations search (NEW)**
- For each project, identify 3-5 community foundations in relevant geographies:
  - Waha's headquarters location (from `CONTEXT/OUR_ORGANIZATION.md`)
  - Partner organization locations (from `CONTEXT/PARTNERSHIPS.md`)
  - Project-relevant diaspora community locations (if applicable — use web research to identify diaspora concentrations for the project's target language/people group)
- Community foundations don't require mission match — only local impact demonstration

**Method 4: Partner-based searches (EXISTING — keep)**
- Search ProPublica for foundations that have granted to Waha's partners (YWAM, Pioneers, Biblica, etc.)
- This is already in the system and is high-value

### Prospect Ranking

The keyword-count ranking maps onto the existing tier system in PROSPECTS.md:

- Foundations matching 4+ keywords → **Tier 1: Strong Alignment**
- 3 keywords → **Tier 2: Moderate Alignment**
- 2 keywords → **Tier 3: Worth Watching**
- 1 keyword → excluded
- Within each tier, rank by: mission alignment strength → 990 grant history to similar orgs → open application process

If a project produces fewer than 15 qualifying prospects (2+ keywords), this is a signal to broaden searches — try additional keyword combinations, relax geographic constraints, or explore adjacent funder types. Flag in HUMAN_TODO.md if broadening still yields thin results.

### No Arbitrary Cap
- Do not limit to 15-40 prospects
- Include every foundation that passes the 2+ keyword quality gate
- The ranked list naturally prioritizes — humans read top-to-bottom and stop when they've seen enough

---

## Stage 02: Deep Research — Uncapped + Improved People Research

### Dossier Count
- Remove the "top 8-12" limit
- Research all foundations that passed Stage 01's quality gate
- Natural prioritization: start with highest-ranked (Tier 1) foundations, work down through Tier 2 and Tier 3
- SHORTLIST.md becomes a generated summary of all researched foundations (not a selection gate) — it serves as the at-a-glance dashboard for the project

### Key People Research Improvements

**Tiered research depth:**

**Tier 1 — Decision-makers (board chair, executive director, program officer):**
1. Attio lookup — do we already know this person?
2. Social links: LinkedIn, Instagram, other socials found (always provide links, or "not found")
3. Other 990 board memberships (ProPublica search) — what else are they involved in?
4. Cross-reference other board memberships against Waha's board (`BOARD_OF_DIRECTORS.md`) and partners (`PARTNERSHIPS.md`)
5. Conference/publication search in ministry networks
6. Personal foundation or giving history if available
7. Warm path analysis with specific connection identified

**Tier 2 — Other board members and staff:**
1. Attio lookup
2. Social links: LinkedIn, Instagram, other socials found
3. Other 990 board memberships
4. Brief background

**"Show your work" rule for all people:**
- If multiple possible LinkedIn/social matches are found, list ALL of them with profile links
- Example: "3 possible LinkedIn matches: [John Smith - Foundation Director](url1), [John Smith - Retired](url2), [John Smith - Pastor](url3)"
- Never write "Multiple profiles found, needs further research"
- This rule applies to every field: provide the answer OR provide the options found with links

**Per-person entry format:**
```markdown
### Jane Smith, Board Chair
- **LinkedIn:** [link] (or "3 possible matches: [link1], [link2], [link3]")
- **Instagram:** [link] (or "not found")
- **Other socials:** [any found]
- **Attio:** [found — summary of relationship / not found]
- **Background:** [professional bio, areas of interest]
- **Other boards (from 990s):** [list with links]
- **Waha network overlap:** [shared affiliations with Waha board, partners, or contacts]
- **Notes for engagement:** [what might resonate with this person]
```

---

## Stage 04: Proposal Drafts — Reference Enriched Brief

### Changes
- Add explicit instruction: "Use the UVP statement from the enriched project brief as the seed for your Statement of Need section"
- Add explicit instruction: "Use the PRINT analysis (especially Impact and Need) to frame the opening problem statement"
- Add explicit instruction: "Reference the keyword matrix to ensure the proposal touches on all relevant dimensions of the project"
- The existing vocabulary mapping (03-VOCABULARY-AND-FRAMING) continues to drive language choices

---

## Stage 06: Submitted — Attio Funding Applications Check

### Changes
- Add instruction: Before marking a submission complete, check Attio's Funding Applications object to see if this submission has already been logged
- If not logged, flag to human: "This submission hasn't been recorded in Attio's Funding Applications. Please add it."
- Future (Option B): Claude would write this record directly. For now, it's a human prompt.

---

## Pipeline-Wide Changes

### Auto-Movement Between Stages
- When a stage completes successfully with no blockers, the agent moves the project folder to the next stage automatically
- When a stage hits a genuine blocker requiring human input, the agent asks immediately rather than silently stalling
- The act of a human answering a question is sufficient to proceed — no separate "move" action required

### "Never Punt" Principle
- Applies to all stages, all documents
- When Claude encounters ambiguity: present options with links, not vague flags
- Examples:
  - Foundation fit unclear → "This foundation is a possible fit because X, but might not work because Y. Recommend: [include / exclude / flag for human review]"
  - Multiple LinkedIn matches → list all with links
  - Grant type ambiguous → "This could be framed as a program grant or capacity building grant. Here's the trade-off: [explanation]. Recommend: [choice]"

### ACTIVE_PIPELINE.md (Stopgap for Cross-Project Coordination)
- Add `CONTEXT/ACTIVE_PIPELINE.md` — a simple table showing which projects are in which stage and which foundations are being pursued
- Updated by Claude at the end of each stage transition
- Serves as a lightweight cross-project view until Option B (Attio as hub) is implemented

```markdown
# Active Pipeline

*Last updated: YYYY-MM-DD*

| Project | Stage | Foundations in Progress | Status |
|---------|-------|----------------------|--------|
| malagasy-dbs | 05-review | Murdock Trust, E91, Templeton | Proposals under review |
| urdu-dmc | 05-review | [foundations] | Proposals under review |
| hausa-dmc | 01-prospect-research | — | Searching |
```

---

## What This Design Does NOT Cover (Deferred)

- **Option B: Attio as coordination hub** — full bidirectional CRM integration with write-back at multiple pipeline stages. Needs its own design session.
- **Custom branding / pandoc integration** — converting output to branded documents. Nice-to-have, separate effort.
- **Brief creation UI** — a chat-based interface for teams to collaboratively create briefs. Mentioned as a future possibility.
- **Google Alerts / ongoing monitoring** — automated discovery of new funding opportunities. Low-effort setup but separate from this design.
- **Funder calendar** — centralized deadline tracking across projects.
- **IO/CL foundation cultivation playbook** — structured approach for invite-only and cycle-closed foundations.

---

## Implementation Notes

- All changes will be implemented by **updating the existing INSTRUCTIONS.md files** for each affected stage (00, 01, 02, 04, 06), as well as INIT.md where it references prospect counts or stage descriptions.
- The `00-projects/_TEMPLATE/` will be updated to reflect the enriched brief structure (so humans can see what a complete brief looks like).
- The `CREATE_PROJECT_BRIEF_FROM_ATTIO_INSTRUCTIONS.md` workflow remains unchanged — the enrichment step runs AFTER brief creation regardless of source.
- `CONTEXT/ACTIVE_PIPELINE.md` will be created as a new file in CONTEXT/ (appropriate location since INIT.md instructs Claude to read all CONTEXT/ files each session).

---

*Design approved in brainstorming session, 2026-03-10.*
*Revised after spec review, 2026-03-10.*
