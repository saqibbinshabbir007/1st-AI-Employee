# Skill: summarize-file
**Version:** 1.0
**Business:** Car Markaz
**Last Updated:** 2026-03-26

---

## Purpose
Koi bhi document (email, WhatsApp chat, meeting notes, supplier message) ko parh kar ek clean summary banana.

## Trigger Conditions
Task file mein yeh keywords hon: `summarize`, `summary`, `brief`, `khulasa`, `batao kya hai`

## Input Requirements
- Task file mein document content ya file reference hona chahiye

---

## Step-by-Step Instructions

**Step 1: Document Parho**
- Task file ki puri content parho
- Document type identify karo (email / WhatsApp / meeting notes / report / other)

**Step 2: Key Information Nikalo**
- Main topic kya hai?
- 3–5 key points kya hain?
- Koi action items hain?
- Koi deadlines mention hain?
- Koi customer ka naam ya phone number hai? (Car Markaz ke liye important)
- Koi vehicle ka naam ya price mention hai?

**Step 3: Summary Likho**
Yeh format use karo:

```markdown
## Summary
**Document Type:** [email / WhatsApp / meeting / report / other]
**Overview:** [ek sentence mein pura document]

**Key Points:**
- [point 1]
- [point 2]
- [point 3]

**Action Items:**
- [ ] [action agar koi ho]

**Important Names/Numbers:**
- [customer name / phone agar mila]

**Vehicle Mentions:**
- [koi gaadi ka zikar agar hua]

**Deadlines:**
- [koi deadline agar mention ki]
```

**Step 4: Output Save Karo**
- Summary file ko `Done/SUMMARY_[original-filename]` ke naam se save karo

**Step 5: Cleanup**
- Original task file `Done/` mein move karo
- Dashboard.md update karo
- Log entry karo

---

## Output Destination
`Done/SUMMARY_[taskname].md`

## Escalation Conditions
- Agar document mein koi sensitive financial information ho → `Pending_Approval/` mein move karo
- Agar customer contact details milein → lead bhi `Plans/Leads/` mein save karo

---

## Example Input
```
skill: summarize-file

Ahmed Bhai ne call kiya tha. Woh Toyota Corolla 2022 lena chahte hain.
Budget 45 lakh hai. Number 0300-1234567. Kal showroom aana chahte hain.
```

## Example Output
```markdown
## Summary
**Document Type:** Phone Call Note
**Overview:** Ahmed Bhai Toyota Corolla 2022 kharidna chahte hain, budget 45 lakh, kal visit.

**Key Points:**
- Toyota Corolla 2022 ki talash mein hain
- Budget: PKR 45,00,000
- Kal showroom visit planned

**Action Items:**
- [ ] Ahmed Bhai ko confirm call karein
- [ ] Corolla 2022 options ready karein

**Important Names/Numbers:**
- Ahmed Bhai: 0300-1234567

**Vehicle Mentions:**
- Toyota Corolla 2022 — Budget 45 lakh
```
