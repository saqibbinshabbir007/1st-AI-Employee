# Skill: customer-inquiry
**Version:** 1.0
**Business:** Car Markaz
**Last Updated:** 2026-03-26

---

## Purpose
Car Markaz mein aane wali customer inquiries handle karna — WhatsApp messages, phone call notes, walk-in notes, ya online form submissions.

## Trigger Conditions
Task file mein yeh keywords hon: `customer`, `inquiry`, `buyer`, `lead`, `grahak`, `client`, `kharidaar`, `interested`

---

## Step-by-Step Instructions

**Step 1: Customer Profile Extract Karo**
Task file se yeh information nikalo:

```
- Naam: [agar diya ho]
- Phone Number: [agar diya ho]
- Inquiry Source: WhatsApp / Phone / Walk-in / Online
- Date & Time: [kab aaya inquiry]
```

**Step 2: Customer Requirement Identify Karo**
```
- Vehicle Type: Sedan / SUV / Hatchback / Pickup / Van / Other
- Brand Preference: Toyota / Honda / Suzuki / Kia / Changan / MG / Koi bhi
- Budget Range: PKR [amount]
- New ya Used: New / Used / Dono chalein
- Urgency: Abhi lena hai / Dekh raha hoon / Future planning
- Specific Model: [agar bataya ho]
- Color Preference: [agar bataya ho]
- Variant: [agar bataya ho]
```

**Step 3: Company Handbook Se Match Karo**
- Kya Car Markaz is type ki vehicle carry karta hai?
- Kya budget realistic hai available stock ke liye?
- Agar requirement out of stock → note karo

**Step 4: Lead Category Decide Karo**
| Category | Condition | Action |
|---|---|---|
| HOT LEAD | Aaj ya kal finalize karna chahta hai | Turant Pending_Approval mein bhejo |
| WARM LEAD | Serious interest, ek hafte mein | Plans/Leads/ mein save karo |
| COLD LEAD | Sirf dekh raha hai | Plans/Leads/ mein save karo |

**Step 5: WhatsApp Response Draft Banao**
Yeh format use karo:

```
Assalam-o-Alaikum [Customer Name]! 🙏

Car Markaz mein khush amdeed!

Aapki [Vehicle Type] ki requirement note kar li hai.
Budget: PKR [amount]

Hamare paas [matching options] available hain.
Aap kab showroom tashreef la sakte hain?

*Final prices Muhammad Saqib se confirm hongi.*

Shukriya!
Car Markaz | Muhammad Saqib
```

**Step 6: Lead Record Banao**
`Plans/Leads/LEAD_[date]_[customername].md` mein save karo:

```markdown
# Lead Record: [Customer Name]
**Date:** YYYY-MM-DD
**Source:** WhatsApp / Phone / Walk-in
**Status:** HOT / WARM / COLD
**Follow-up Date:** YYYY-MM-DD

## Customer Profile
- Name:
- Phone:
- Requirement:
- Budget: PKR
- Urgency:

## Matching Vehicles
- [vehicle 1]
- [vehicle 2]

## Notes
[koi extra info]
```

**Step 7: Response Approval Ke Liye Bhejo**
- Response draft ko `Pending_Approval/RESPONSE_[customername].md` mein save karo
- Muhammad Saqib approve karein phir bhejein
- KABHI bhi khud response mat bhejo without approval

**Step 8: HOT LEAD Escalation**
Agar HOT LEAD hai:
- `Needs_Action/URGENT_[customername].md` mein move karo
- Yeh note likho: "HOT LEAD — Muhammad Saqib ki turant attention chahiye!"

**Step 9: Cleanup**
- Original task file `Done/` mein move karo
- Dashboard.md update karo
- Log entry karo

---

## Output Destinations
- Lead record: `Plans/Leads/LEAD_[date]_[name].md`
- Response draft: `Pending_Approval/RESPONSE_[name].md`
- HOT LEAD: `Needs_Action/URGENT_[name].md`

## Escalation Conditions
- Customer aaj ya kal deal finalize karna chahta ho → Needs_Action URGENT
- Customer ne competitor ka naam liya → note karo, owner ko batao
- Customer ne price negotiate karna shuru kiya → Pending_Approval
- Customer ka naam ya number nahi mila → Needs_Action with clarification request

---

## Example Input
```
skill: customer-inquiry

Hassan Bhai ne WhatsApp kiya. Toyota Corolla 2022 2.0 Altis Grande
chahiye. Budget 55 lakh hai. Color: white prefer hai. Kal 3 baje
showroom aana chahte hain. Number: 0321-9876543
```

## Example Output — Lead Record
```markdown
# Lead Record: Hassan Bhai
**Date:** 2026-03-26
**Source:** WhatsApp
**Status:** HOT LEAD
**Follow-up Date:** 2026-03-27

## Customer Profile
- Name: Hassan Bhai
- Phone: 0321-9876543
- Requirement: Toyota Corolla 2022 2.0 Altis Grande, White
- Budget: PKR 55,00,000
- Urgency: Kal showroom visit — HOT

## Notes
- Kal 3 PM appointment confirm karni hai
```
