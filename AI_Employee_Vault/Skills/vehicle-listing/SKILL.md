# Skill: vehicle-listing
**Version:** 1.0
**Business:** Car Markaz
**Last Updated:** 2026-03-26

---

## Purpose
Create a standardized listing for a new stock vehicle. Sheikh Ali Kabir drops raw notes, and the AI produces a properly formatted listing — ready for WhatsApp, PakWheels, and showroom display.

## Trigger Conditions
Task file contains these keywords: `vehicle`, `car`, `gaadi`, `listing`, `inventory`, `stock`, `naya`, `new arrival`

---

## Step-by-Step Instructions

**Step 1: Parse Vehicle Data**
Extract the following information from the task file:

```
MANDATORY FIELDS (all required):
- Year: [year]
- Brand: Toyota / Honda / Suzuki / Kia / Changan / MG / Other
- Model: [Corolla / Civic / Alto / Sportage / etc.]
- Variant: [GLi / XLi / 1.8 / Altis / etc.]
- Engine: [1000cc / 1300cc / 1800cc / etc.]
- Fuel Type: Petrol / Diesel / Hybrid / Electric
- Transmission: Manual / Automatic
- Color: [exterior color]
- Mileage: [km driven]
- Registration: [city] [year]
- Condition: Excellent / Good / Fair
- Price: PKR [amount]
- Negotiable: Yes / No
- Photos Available: Yes / No

OPTIONAL FIELDS:
- Interior Color:
- Condition Notes: [any defects or recent repairs]
- Features: [sunroof / push start / etc.]
```

**Step 2: Completeness Check**
If any MANDATORY field is missing:
- Move to `Needs_Action/MISSING_INFO_[vehicle].md`
- Clearly list which fields are missing
- STOP — do not create an incomplete listing

**Step 3: Create Listing in Three Formats**

### Format A: WhatsApp-Ready (Short)
```
🚗 *[Year] [Brand] [Model] [Variant]*
📍 Car Markaz | Sheikh Ali Kabir

✅ [Color] | [Transmission]
✅ [Mileage] KM | [Registration City] Registered
✅ Condition: [Excellent/Good/Fair]

💰 *PKR [Price]*
[Negotiable: Yes/No]

📸 Photos available: [Yes/No]
📞 Call/WhatsApp: [Contact Number]

_Car Markaz — Your Trust, Our Responsibility_
```

### Format B: PakWheels / Full Listing
```markdown
## [Year] [Brand] [Model] [Variant] — For Sale

**Price:** PKR [amount] [Negotiable/Fixed]

### Vehicle Details
| Field | Detail |
|---|---|
| Year | [year] |
| Make | [brand] |
| Model | [model] |
| Variant | [variant] |
| Engine | [cc] |
| Fuel Type | [type] |
| Transmission | [manual/auto] |
| Color | [color] |
| Mileage | [km] KM |
| Registered | [city], [year] |
| Condition | [condition] |

### Condition Notes
[any damage, recent repairs, or special features]

### Contact
Car Markaz | Sheikh Ali Kabir
[Contact Number]

*All information is accurate to the best of our knowledge.
Final price subject to confirmation.*
```

### Format C: CSV Row (Spreadsheet Tracking)
```
Year,Brand,Model,Variant,Engine,Fuel,Transmission,Color,Mileage,RegCity,RegYear,Condition,Price,Negotiable,Photos,DateAdded
[data row]
```

**Step 4: Car Markaz Branding Check**
Every listing must include this disclaimer:
```
Car Markaz — Your Trust, Our Responsibility
Owner: Sheikh Ali Kabir | [Contact]
Final price to be confirmed by Sheikh Ali Kabir.
```

**Step 5: Save Output**
File name: `YYYY-MM-DD_[Brand]_[Model]_[Year]_PKR[price].md`
Save location: `Plans/Listings/`

**Step 6: Send for Approval**
- Also copy the listing to `Pending_Approval/LISTING_[vehicle].md`
- Sheikh Ali Kabir must review before publishing

**Step 7: Cleanup**
- Move original task file to `Done/`
- Update Dashboard.md: "New listing ready for approval: [vehicle]"
- Write log entry

---

## Output Destinations
- Full listing: `Plans/Listings/YYYY-MM-DD_[Brand]_[Model].md`
- Pending approval: `Pending_Approval/LISTING_[vehicle].md`
- Missing info: `Needs_Action/MISSING_INFO_[vehicle].md`

## Escalation Conditions
- Any mandatory field missing → Needs_Action
- Price above 30 lakh → owner approval required before publishing
- Condition is "Fair" → confirm with owner before listing

---

## Example Input
```
skill: vehicle-listing

2022 Toyota Corolla Altis Grande 1.8
White color, automatic
67,000 km driven
Islamabad registered 2022
Excellent condition, original paint
Price: 5,200,000
Negotiable
Photos available
```

## Example Output (WhatsApp Format)
```
🚗 *2022 Toyota Corolla Altis Grande 1.8*
📍 Car Markaz | Sheikh Ali Kabir

✅ White | Automatic
✅ 67,000 KM | Islamabad Registered 2022
✅ Condition: Excellent | Original Paint

💰 *PKR 52,00,000*
Negotiable: Yes

📸 Photos available: Yes
📞 Call/WhatsApp: [Contact Number]

_Car Markaz — Your Trust, Our Responsibility_
```
