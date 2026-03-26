# Skill: process-task
**Version:** 1.0
**Business:** Car Markaz
**Last Updated:** 2026-03-26

---

## Purpose
General task processor. This fallback skill is used when no other specific skill matches. It breaks down the task and creates a plan.

## Trigger Conditions
Task file contains these keywords: `task`, `todo`, `action`, `kaam`, `karo`, or no specific skill tag is present

---

## Step-by-Step Instructions

**Step 1: Read the Task**
- Read the full content of the task file
- Confirm business rules from Company_Handbook.md

**Step 2: Analyze the Task**
Identify:
- What needs to be done? (main objective)
- Who will do it? (AI / Owner Sheikh Ali Kabir / both)
- When does it need to be done? (deadline)
- What is the priority?

**Priority Rules:**
| Priority | Condition |
|---|---|
| HIGH | Customer same day / urgent / owner requested |
| MEDIUM | Within 24 hours |
| LOW | Within 1 week |

**Step 3: Check If a Specific Skill Matches**
- Mention of a customer → suggest `customer-inquiry` skill
- Mention of a vehicle / car → suggest `vehicle-listing` skill
- Mention of report / sales → suggest `sales-report` skill
- Summary needed → suggest `summarize-file` skill

If a match is found → note in the plan: "This task would be better handled by the [skill-name] skill"

**Step 4: Create a Plan**
Use this format in `Plans/PLAN_[taskname].md`:

```markdown
# Plan: [Task Name]
**Created:** YYYY-MM-DD HH:MM
**Priority:** HIGH / MEDIUM / LOW
**Skill Used:** process-task
**Estimated Steps:** [number]

## Objective
[what needs to be achieved]

## Steps
- [ ] Step 1: ...
- [ ] Step 2: ...
- [ ] Step 3: ...

## Owner Decision Required?
YES / NO — [reason if yes]

## Status: In Progress
```

**Step 5: Execute**
- Follow the plan steps one by one
- If any step requires an owner decision → STOP, move file to `Pending_Approval/`

**Step 6: Complete**
- Move original task to `Done/`
- Move plan file to `Done/` as well
- Update Dashboard.md
- Write log entry

---

## Output Destination
- Plan: `Plans/PLAN_[taskname].md`
- If owner decision required: `Pending_Approval/`
- Complete: `Done/`

## Escalation Conditions
- Any financial decision → `Pending_Approval/`
- Any customer commitment → `Pending_Approval/`
- Task is unclear → `Needs_Action/` with clarification request

---

## Example Input
```
skill: process-task
priority: medium

Need to arrange showroom cleaning for tomorrow and
take photos of the 3 newly arrived vehicles.
```

## Example Output Plan
```markdown
# Plan: Showroom Cleaning & Vehicle Photos
**Created:** 2026-03-26 14:00
**Priority:** MEDIUM

## Steps
- [ ] Step 1: Call cleaning staff (Owner task)
- [ ] Step 2: Identify the 3 new vehicles
- [ ] Step 3: Take photos of each vehicle (front, back, interior)
- [ ] Step 4: Save photos in the photos folder

## Owner Decision Required?
YES — Cleaning staff contact number is with the owner
```
