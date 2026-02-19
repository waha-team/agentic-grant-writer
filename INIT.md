# INIT: Grant Writing Pipeline for Waha

> **Give this file to Claude Code to set up or orient a new session.**

---

## What Is This?

This is a grant research and writing pipeline for Waha (waha.app), a nonprofit that builds a free Discovery Bible Study and disciple-making app used in 110+ countries and 41+ languages. We're diversifying our funding from a single large grant into dozens of smaller foundation grants.

## Directory Structure

```
grant_writing/
├── CONTEXT/                        # Shared context files (read at every stage)
│   ├── FUNDER_ALIGNMENT_GUIDE.md   # A funder alignment guide, including details about what kinds of organizations would align with Waha
│   ├── OUR_ORGANIZATION.md         # Who Waha is, mission, stats, framing guide
│   ├── PAST_GRANTS.md              # Grant history (fill in with actual data)
│   ├── IMPACT_DATA.md              # Evidence, testimonials, case studies
│   ├── SEARCH_CRITERIA.md          # What funders to target, filters
│   └── STYLE_GUIDE.md              # Voice, tone, terminology for proposals
│
├── HUMAN_TODO.md                   # Escalation file for decisions needing human judgment
│
├── 00-projects/                    # Entry point: project briefs live here
│   ├── INSTRUCTIONS.md
│   └── _TEMPLATE/                  # Copy this to create a new project
│       └── PROJECT_BRIEF.md
│
├── 01-prospect-research/           # Find 15-30 foundations per project
│   └── INSTRUCTIONS.md
│
├── 02-alignment-analysis/          # Score and shortlist to top 8-12
│   └── INSTRUCTIONS.md
│
├── 03-contact-research/            # Find contacts and warm paths
│   └── INSTRUCTIONS.md
│
├── 04-application-prep/            # Gather requirements, gap analysis
│   └── INSTRUCTIONS.md
│
├── 05-proposal-drafts/             # Write tailored proposals
│   └── INSTRUCTIONS.md
│
├── 06-review/                      # Self-critique and submission prep
│   └── INSTRUCTIONS.md
```

## How the Pipeline Works

1. **Humans create project briefs** in `00-projects/` (copy the template, fill it in)
2. **Move the project folder** into the next stage directory when ready to proceed
3. **Claude Code reads the INSTRUCTIONS.md** for that stage and processes every project folder it finds there
4. **Each stage produces output files** inside the project's folder (PROSPECTS.md, ALIGNMENT_ANALYSIS.md, etc.)
5. **Claude Code moves the folder** to the next stage when done
6. **If Claude Code needs human help**, it adds an entry to `HUMAN_TODO.md` but keeps going on everything else

## Default Behavior

- **Momentum over perfection.** Push projects forward. Don't block on uncertainty.
- **Escalate via HUMAN_TODO.md.** If a decision requires human judgment, log it there and keep working.
- **Every stage reads CONTEXT/ first.** Always start by reading the relevant context files.
- **Tailor everything.** No generic proposals. Every funder gets a customized pitch.

## How to Run a Session

Give Claude Code this prompt:

```
Read INIT.md in the grant_writing directory, then read the CONTEXT/ files. 
Look for project folders that need processing — check each stage directory 
(01 through 06) for project subfolders. For each one you find, read that 
stage's INSTRUCTIONS.md and execute it. Start with the earliest stage that 
has work to do.
```

Or, to target a specific stage:

```
Read INIT.md in the grant_writing directory, then process all projects 
in [01-prospect-research / 02-alignment-analysis / etc.] following that 
stage's INSTRUCTIONS.md.
```

## Key People

- **Josh** — Directs the pipeline, answers strategic questions
- **Alycia** — Reviews proposals and manages grant relationships
- **Valeria** — Assists with review and submission logistics
- **Vince:** Partnerships Director — Consulted on relationship strategies

## Files That Need Human Input

Before running the pipeline for the first time, these files should be populated:

- [x] `CONTEXT/PAST_GRANTS.md` — Add your grant history
- [x] `CONTEXT/IMPACT_DATA.md` — Review and add any additional metrics/stories
- [x] `CONTEXT/OUR_ORGANIZATION.md` — Review and add team names, bios, precise budget figures
- [x] At least one project brief in `00-projects/`

## Important notes

Always keep the project's directory well-updated with the results of your research, such that if you get interupted part way though, future agents can pick up and continue your work.

Your short term memory isn't valuable. Only what's written is valuable.

---

*Pipeline created: 2026-02-18*
