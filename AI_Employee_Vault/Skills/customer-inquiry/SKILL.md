# Skill: customer-inquiry
**Version:** 1.0
**Business:** Car Markaz
**Last Updated:** 2026-03-26

---

## Purpose
Handle incoming customer inquiries at Car Markaz — WhatsApp messages, phone call notes, walk-in notes, or online form submissions.

## Trigger Conditions
Task file contains these keywords: `customer`, `inquiry`, `buyer`, `lead`, `grahak`, `client`, `kharidaar`, `interested`

---

## Step-by-Step Instructions

**Step 1: Extract Customer Profile**
Pull the following information from the task file:

```
- Name: [if provided]
- Phone Number: [if provided]
- Inquiry Source: WhatsApp / Phone / Walk-in / Online
- Date & Time: [when the inquiry came in]
```

**Step 2: Identify Customer Requirement**
```
- Vehicle Type: Sedan / SUV / Hatchback / Pickup / Van / Other
- Brand Preference: Toyota / Honda / Suzuki / Kia / Changan / MG / Any
- Budget Range: PKR [amount]
- New or Used: New / Used / Either
- Urgency: Ready to buy now / Just looking / Future planning
- Specific Model: [if mentioned]
- Color Preference: [if mentioned]
- Variant: [if mentioned]
```

**Step 3: Match Against Company Handbook**
- Does Car Markaz carry this type of vehicle?
- Is the budget realistic for available stock?
- If requirement is out of stock → note it

**Step 4: Decide Lead Category**
| Category | Condition | Action |
|---|---|---|
| HOT LEAD | Wants to finalize today or tomorrow | Send to Pending_Approval immediately |
| WARM LEAD | Serious interest, within one week | Save in Plans/Leads/ |
| COLD LEAD | Just browsing | Save in Plans/Leads/ |

**Step 5: Draft WhatsApp Response**
Use this format:

```
Assalam-o-Alaikum [Customer Name]! 🙏

Welcome to Car Markaz!

Your requirement for a [Vehicle Type] has been noted.
Budget: PKR [amount]

We have [matching options] available.
When can you visit our showroom?

*Final prices will be confirmed by Sheikh Ali Kabir.*

Thank you!
Car Markaz | Sheikh Ali Kabir
```

**Step 6: Create Lead Record**
Save to `Plans/Leads/LEAD_[date]_[customername].md`:

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
[any extra info]
```

**Step 7: Send Response for Approval**
- Save response draft to `Pending_Approval/RESPONSE_[customername].md`
- Sheikh Ali Kabir must approve before sending
- NEVER send a response without approval

**Step 8: HOT LEAD Escalation**
If HOT LEAD:
- Move to `Needs_Action/URGENT_[customername].md`
- Write this note: "HOT LEAD — Sheikh Ali Kabir's immediate attention required!"

**Step 9: Cleanup**
- Move original task file to `Done/`
- Update Dashboard.md
- Write log entry

---

## Output Destinations
- Lead record: `Plans/Leads/LEAD_[date]_[name].md`
- Response draft: `Pending_Approval/RESPONSE_[name].md`
- HOT LEAD: `Needs_Action/URGENT_[name].md`

## Escalation Conditions
- Customer wants to finalize the deal today or tomorrow → Needs_Action URGENT
- Customer mentioned a competitor → note it, inform the owner
- Customer started price negotiation → Pending_Approval
- Customer name or number not found → Needs_Action with clarification request

---

## Example Input
```
skill: customer-inquiry

Hassan Bhai sent a WhatsApp message. He wants a Toyota Corolla 2022 2.0 Altis Grande.
Budget is 55 lakh. Color preference: white. He wants to visit the showroom tomorrow at 3 PM.
Number: 0321-9876543
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
- Urgency: Showroom visit tomorrow — HOT

## Notes
- Appointment for tomorrow at 3 PM needs to be confirmed
```
