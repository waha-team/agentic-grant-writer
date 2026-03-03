# Folder Naming Convention

This project uses a standardized prefix system for foundation folders to indicate their status in the pipeline.

---

## Prefixes

| Prefix             | Meaning                 | Definition                                                                                                                                                            |
|--------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `01-`, `02-`, etc. | **Ready**               | Proposal drafted and ready for review/submission. No blockers. Number indicates priority (01 = highest).                                                              |
| `R-`               | **Relationship Needed** | Open application process, but warm introduction is strongly preferred or required before submitting. Draft the proposal, but wait to submit until intro is secured. |
| `H-`               | **Human Action Needed** | Open application process, but waiting on specific information or decision from Josh/Alycia before submitting.                                                         |
| `CL-`              | **Cycle Closed**        | Foundation's grant cycle is closed. Waiting for next application cycle to open.                                                                                       |
| `S-`               | **Suspended**           | Foundation has paused applications (e.g., strategic planning). Monitor for reopening.                                                                                 |
| `IO-`              | **Invite Only**         | No public application process. Requires connection to get invited to apply.                                                                                           |
| `NA-`              | **Not Applicable**      | Cannot apply directly (wrong org type, geography, etc.). May have alternative approach.                                                                               |

---

## Status Documents

Each folder (except `01-`, `02-`, etc.) should contain a status document explaining the situation:

| Status | Document Name                      |
|--------|------------------------------------|
| `R-`   | `00-STATUS-RELATIONSHIP-NEEDED.md` |
| `H-`   | `00-STATUS-ACTION-NEEDED.md`       |
| `CL-`  | `00-STATUS-CYCLE-CLOSED.md`        |
| `S-`   | `00-STATUS-SUSPENDED.md`           |
| `IO-`  | `00-STATUS-INVITE-ONLY.md`         |
| `NA-`  | `00-STATUS-NOT-APPLICABLE.md`      |

---

## Examples

```
urdu-dmc/
├── 01-chatlos-foundation/         # Ready to submit
├── 02-crowell-trust/              # Ready to submit (after intro)
├── R-tyndale-house-foundation/    # Relationship needed
├── CL-global-christian-relief/    # Cycle closed
├── IO-first-fruit/                # Invite only
└── NA-mustard-seed-foundation/    # Can't apply
```

---

## Priority Within Categories

When multiple foundations share the same prefix, add a secondary number:

- `R-01-tyndale-house-foundation/` — Higher priority
- `R-02-another-foundation/` — Lower priority

Or use folder sorting (alphabetical) to indicate priority within the same category.
