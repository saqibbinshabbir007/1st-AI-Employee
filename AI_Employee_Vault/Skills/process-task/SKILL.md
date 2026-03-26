# Skill: process-task
**Version:** 1.0
**Business:** Car Markaz
**Last Updated:** 2026-03-26

---

## Purpose
General task processor. Jab koi aur specific skill match nahi hoti toh yeh fallback skill use hoti hai. Task break down karke plan banata hai.

## Trigger Conditions
Task file mein yeh keywords hon: `task`, `todo`, `action`, `kaam`, `karo`, ya koi specific skill tag nahi ho

---

## Step-by-Step Instructions

**Step 1: Task Parho**
- Task file ki puri content parho
- Company_Handbook.md se business rules confirm karo

**Step 2: Task Analyze Karo**
Identify karo:
- Kya karna hai? (main objective)
- Kaun karega? (AI / Owner Muhammad Saqib / dono)
- Kab tak karna hai? (deadline)
- Priority kya hai?

**Priority Rules:**
| Priority | Condition |
|---|---|
| HIGH | Customer same day / urgent / owner ne kaha |
| MEDIUM | 24 ghante ke andar |
| LOW | 1 week ke andar |

**Step 3: Check Karo Koi Specific Skill Match Hoti Hai?**
- Customer ka zikar → `customer-inquiry` skill suggest karo
- Vehicle / car ka zikar → `vehicle-listing` skill suggest karo
- Report / sales ka zikar → `sales-report` skill suggest karo
- Summary chahiye → `summarize-file` skill suggest karo

Agar match mile → note karo plan mein ke "Yeh task [skill-name] skill se better handle hoga"

**Step 4: Plan Banao**
`Plans/PLAN_[taskname].md` mein yeh format use karo:

```markdown
# Plan: [Task Name]
**Created:** YYYY-MM-DD HH:MM
**Priority:** HIGH / MEDIUM / LOW
**Skill Used:** process-task
**Estimated Steps:** [number]

## Objective
[kya achieve karna hai]

## Steps
- [ ] Step 1: ...
- [ ] Step 2: ...
- [ ] Step 3: ...

## Owner Decision Required?
YES / NO — [reason agar yes]

## Status: In Progress
```

**Step 5: Execute Karo**
- Plan ke steps ek ek follow karo
- Agar koi step owner decision maange → RUKO, file `Pending_Approval/` mein move karo

**Step 6: Complete**
- Original task `Done/` mein move karo
- Plan file bhi `Done/` mein move karo
- Dashboard.md update karo
- Log entry karo

---

## Output Destination
- Plan: `Plans/PLAN_[taskname].md`
- Agar owner decision chahiye: `Pending_Approval/`
- Complete: `Done/`

## Escalation Conditions
- Koi bhi financial decision → `Pending_Approval/`
- Koi bhi customer commitment → `Pending_Approval/`
- Task unclear ho → `Needs_Action/` with clarification request

---

## Example Input
```
skill: process-task
priority: medium

Kal ke liye showroom ki cleaning arrange karni hai aur
naye aaye hue 3 vehicles ki photos leni hain.
```

## Example Output Plan
```markdown
# Plan: Showroom Cleaning & Vehicle Photos
**Created:** 2026-03-26 14:00
**Priority:** MEDIUM

## Steps
- [ ] Step 1: Cleaning staff ko call karein (Owner task)
- [ ] Step 2: 3 naye vehicles identify karein
- [ ] Step 3: Har vehicle ki photos lein (front, back, interior)
- [ ] Step 4: Photos folder mein save karein

## Owner Decision Required?
YES — Cleaning staff contact number owner ke paas hai
```
