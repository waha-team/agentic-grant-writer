# INIT: Grant Writing Pipeline for Waha (v2)

> **Give this file to Claude Code to orient any new session.**

---

## What Is This?

An automated grant research and writing pipeline for **Waha** (waha.app), a 501(c)(3) nonprofit (EIN: 35-2894107) that builds a free Discovery Bible Study and disciple-making app. Used in 110+ countries, 41+ languages. We're diversifying funding from a single large grant into dozens of smaller foundation grants.

## Directory Structure

```
grant_writing/
├── CONTEXT/                        # Shared context (read EVERY session)
│   ├── OUR_ORGANIZATION.md         # Who Waha is, mission, stats, legal info
│   ├── PARTNERSHIPS.md             # Partner orgs for name-dropping in proposals
│   ├── IMPACT_DATA.md              # Evidence, testimonials, case studies
│   ├── PAST_GRANTS.md              # Grant history and lessons
│   ├── SEARCH_CRITERIA.md          # Funder targeting rules + 990 ask-sizing
│   ├── STYLE_GUIDE.md              # Voice, vocabulary, problem-first structure
│   └── FINANCIALS_SUMMARY.md       # Budget and financial health
│
├── WRITING_SAMPLES/                # Past successful proposals for reference
├── HUMAN_TODO.md                   # Escalation file for human decisions
│
├── 00-projects/                    # Entry: project briefs
├── 01-prospect-research/           # Find 15-30 foundations per project
├── 02-deep-research/               # Build foundation dossiers (numbered docs)
├── 03-application-prep/            # Gather requirements, checklists
├── 04-proposal-drafts/             # Write tailored proposals
├── 05-review/                      # Self-critique and submission prep
└── 06-submitted/                   # Track outcomes, follow up, learn
```

## Per-Foundation Dossier Structure (created in Stage 02)

Each foundation gets a subfolder with numbered documents:
```
kern-family-foundation/
├── 00-BRIEFING.md                  # Foundation overview, mission, history
├── 01-990-ANALYSIS.md              # Giving patterns, grant ranges, board members
├── 02-KEY-PEOPLE.md                # Decision maker profiles, LinkedIn, warm paths
├── 03-VOCABULARY-AND-FRAMING.md    # THEIR language mapped to ours
├── 04-APPLICATION-REQUIREMENTS.md  # What they need from us (Stage 03)
├── 05-PROPOSAL-DRAFT.md            # The proposal (Stage 04)
├── 06-COVER-LETTER.md              # Personalized letter (Stage 04)
├── 07-REVIEW-NOTES.md              # Self-critique (Stage 05)
└── 08-SUBMISSION-LOG.md            # Tracking (Stage 06, human-driven)
```

## Core Principles

1. **A grant application is a sales letter.** Lead with the problem. Make them care before they know who we are.
2. **Use THEIR vocabulary.** Every foundation gets a vocabulary mapping (03-VOCABULARY-AND-FRAMING.md). Proposals must mirror the funder's language.
3. **Size asks to 990 data.** Never ask for more than a foundation's typical grant. For first-time asks, go at or below median. Build relationships over time.
4. **Personalize everything.** Use names from 990s and websites. Reference their specific grants. Never "Dear Grant Administrator."
5. **Name-drop partners.** We work with 24:14, YWAM, Pioneers, Biblica, YouVersion, Meta. Use these to build credibility.
6. **Momentum over perfection.** Push forward. Escalate decisions to HUMAN_TODO.md but don't block.

## How to Run

**Process all stages:**
```
Read INIT.md, then CONTEXT/ files. Check each stage directory (01-06) for project
subfolders. Process the earliest stage with work. Follow that stage's INSTRUCTIONS.md.
```

**Target a specific stage:**
```
Read INIT.md, then process all projects in [02-deep-research] following INSTRUCTIONS.md.
```

## Key People

- **Josh** — Directs pipeline, answers strategic questions
- **Alycia** — Reviews proposals, manages grant relationships
- **Valeria** — Assists review and submission
- **Vince** — Partnerships Director — Consulted on relationship strategies
- **Jeff** — Strategic oversight

## Files Needing Human Input Before First Run

- [ ] `CONTEXT/PAST_GRANTS.md` — Your grant history
- [ ] `CONTEXT/OUR_ORGANIZATION.md` — Add team names and bios
- [ ] `CONTEXT/FINANCIALS_SUMMARY.md` — Budget breakdown
- [ ] At least one project brief in `00-projects/`
- [ ] Universal attachments gathered (501c3 letter, 990, board list)

---

## CRITICAL

**Your short-term memory isn't valuable. Only what's written is valuable.**

Always keep the project's directory well-updated with the results of your research, such that if you get interrupted part way through, future agents can pick up and continue your work.

---

*Pipeline v2 created: 2026-02-19*
