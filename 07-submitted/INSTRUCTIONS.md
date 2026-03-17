# Stage 07: Submitted & Tracking

> **Your job:** Verify the Funding Proposal record in Attio is 100% complete, check for any communications about the submission, update the prospective partners registry, and maintain a local submission log.

---

## Before You Start

1. Read `06-to-be-submitted/TOOLS_AND_APIS.md` for Attio API reference
2. Identify the foundation's Funding Proposal record in Attio (created during Stage 06 CRM sync)
3. Confirm you have access to `$ATTIO_ACCESS_TOKEN` (from `.env`)

## Folder Naming

Same as Stage 06: `{foundation-name}--{project-name}/`

---

## Step 1: Final CRM Verification

Verify the Funding Proposal record in Attio is 100% complete:

- [ ] `project_name` — proposal name is clear and accurate
- [ ] `status` — set to "Submitted Initial Inquiry" or "Submitted Full Proposal" (with submission date)
- [ ] `type` — correct application type
- [ ] `funding_requested` — correct ask amount
- [ ] `projects_this_proposal_is_funding` — linked to the correct Project
- [ ] `receiving_proposal` — linked to the correct Organization
- [ ] `loi_due` / `formal_proposal_due_date` — deadlines populated
- [ ] People linked to the Organization (from Stage 06 Step 3d)
- [ ] Organization on the Prospective Funding Orgs list with all fields populated
- [ ] Summary note exists on the Funding Proposal

Fix any gaps or broken links found during verification.

---

## Step 2: Read Communications

Check for responses, confirmations, or follow-up requests **since the submission date** via:
- Gmail (MCP tool) — search for foundation name and contact emails
- Attio email/interaction records on the Organization and People records
- Notes logged on the Funding Proposal or Organization records

Log any findings as a new note on the Funding Proposal record in Attio.

---

## Step 3: Update Prospective Partners Registry

Update `CONTEXT/PROSPECTIVE_PARTNERS.md`:
- Set the foundation's status to reflect submission (e.g., "Submitted LOI 2026-03-16")
- Note any response or follow-up status

---

## Step 4: Local Submission Log

Create or update `SUBMISSION-LOG.md` in the foundation folder:

```
# Submission Log: [Foundation Name]

- **Date submitted:** [DATE]
- **Submitted by:** [Name]
- **Method:** [online portal / email / mail]
- **Confirmation received?** [Y/N]
- **Ask amount:** $[X]
- **Expected response date:** [DATE or "unknown"]
- **Follow-up scheduled:** [DATE — typically 2-4 weeks after expected response date]

## Follow-Up Actions
- [ ] Send thank-you email within 48 hours of submission
- [ ] Calendar reminder for follow-up check-in at [DATE]
- [ ] Calendar reminder for expected decision at [DATE]

## Outcome
- **Decision:** [AWARDED / DECLINED / PENDING / NO RESPONSE]
- **Amount awarded:** $[X] (if different from ask)
- **Date of decision:** [DATE]
- **Feedback received:** [Any feedback from the foundation]

## If Awarded
- [ ] Send thank-you letter within 1 week
- [ ] Note reporting requirements and deadlines
- [ ] Update CONTEXT/PAST_GRANTS.md with award details
- [ ] Update CONTEXT/PROSPECTIVE_PARTNERS.md with award status
- [ ] Plan for renewal/growth: next ask of $[X] in [timeframe]

## If Declined
- [ ] Send gracious thank-you anyway
- [ ] Request feedback if appropriate
- [ ] Note lessons in "Rejection Analysis" below
- [ ] Update CONTEXT/PROSPECTIVE_PARTNERS.md with outcome
- [ ] Decide: reapply next cycle? Different project? Move on?

## Rejection Analysis (if declined)
- **Likely reason:** [Based on any feedback or our best guess]
- **What we'd change:** [For next application to this or similar funders]
- **Worth reapplying?** [Yes — next cycle / Yes — with different project / No — poor fit]
```

---

## Done Criteria

- Funding Proposal record in Attio is 100% complete with all links verified
- Any communications logged as notes
- `CONTEXT/PROSPECTIVE_PARTNERS.md` updated with submission status
- `SUBMISSION-LOG.md` created in the foundation folder

The Funding Proposal record being complete and accurate is the **primary deliverable**. The local submission log is secondary.

---

## Quarterly Review

Every quarter, review all foundations in `07-submitted/`:
1. Which applications are still pending? Follow up.
2. Which were awarded? Ensure reporting is on track.
3. Which were declined? Capture lessons.
4. Update `CONTEXT/PAST_GRANTS.md` with all outcomes.
5. Update `CONTEXT/PROSPECTIVE_PARTNERS.md` with final outcomes for each foundation.
