# Skill: summarize-file
**Version:** 1.0
**Business:** Car Markaz
**Last Updated:** 2026-03-26

---

## Purpose
Read any document (email, WhatsApp chat, meeting notes, supplier message) and produce a clean summary.

## Trigger Conditions
Task file contains these keywords: `summarize`, `summary`, `brief`, `khulasa`, `batao kya hai`

## Input Requirements
- Task file must contain document content or a file reference

---

## Step-by-Step Instructions

**Step 1: Read the Document**
- Read the full content of the task file
- Identify the document type (email / WhatsApp / meeting notes / report / other)

**Step 2: Extract Key Information**
- What is the main topic?
- What are the 3–5 key points?
- Are there any action items?
- Are any deadlines mentioned?
- Is there a customer name or phone number? (important for Car Markaz)
- Is any vehicle name or price mentioned?

**Step 3: Write the Summary**
Use this format:

```markdown
## Summary
**Document Type:** [email / WhatsApp / meeting / report / other]
**Overview:** [entire document in one sentence]

**Key Points:**
- [point 1]
- [point 2]
- [point 3]

**Action Items:**
- [ ] [action if any]

**Important Names/Numbers:**
- [customer name / phone if found]

**Vehicle Mentions:**
- [any vehicle mentioned]

**Deadlines:**
- [any deadline mentioned]
```

**Step 4: Save Output**
- Save the summary file as `Done/SUMMARY_[original-filename]`

**Step 5: Cleanup**
- Move original task file to `Done/`
- Update Dashboard.md
- Write log entry

---

## Output Destination
`Done/SUMMARY_[taskname].md`

## Escalation Conditions
- If the document contains sensitive financial information → move to `Pending_Approval/`
- If customer contact details are found → also save a lead in `Plans/Leads/`

---

## Example Input
```
skill: summarize-file

Ahmed Bhai called. He wants to buy a Toyota Corolla 2022.
Budget is 45 lakh. Number 0300-1234567. He wants to visit the showroom tomorrow.
```

## Example Output
```markdown
## Summary
**Document Type:** Phone Call Note
**Overview:** Ahmed Bhai is looking to buy a Toyota Corolla 2022 with a budget of 45 lakh and plans to visit tomorrow.

**Key Points:**
- Looking for Toyota Corolla 2022
- Budget: PKR 45,00,000
- Showroom visit planned for tomorrow

**Action Items:**
- [ ] Call Ahmed Bhai to confirm
- [ ] Prepare Corolla 2022 options

**Important Names/Numbers:**
- Ahmed Bhai: 0300-1234567

**Vehicle Mentions:**
- Toyota Corolla 2022 — Budget 45 lakh
```
