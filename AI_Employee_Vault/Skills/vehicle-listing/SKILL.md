# Skill: vehicle-listing
**Version:** 1.0
**Business:** Car Markaz
**Last Updated:** 2026-03-26

---

## Purpose
Naye stock vehicle ke liye standardized listing banana. Muhammad Saqib raw notes drop kare, AI properly formatted listing banaye — WhatsApp, PakWheels, aur showroom display ke liye.

## Trigger Conditions
Task file mein yeh keywords hon: `vehicle`, `car`, `gaadi`, `listing`, `inventory`, `stock`, `naya`, `new arrival`

---

## Step-by-Step Instructions

**Step 1: Vehicle Data Parse Karo**
Task file se yeh information extract karo:

```
MANDATORY FIELDS (sab zaroori hain):
- Year: [saal]
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
- Negotiable: Haan / Nahi
- Photos Available: Haan / Nahi

OPTIONAL FIELDS:
- Interior Color:
- Condition Notes: [koi nuqs ya recently repaired]
- Features: [sunroof / push start / etc.]
```

**Step 2: Completeness Check**
Agar koi MANDATORY field missing hai:
- `Needs_Action/MISSING_INFO_[vehicle].md` mein move karo
- Clearly list karo kaunse fields missing hain
- STOP — incomplete listing mat banao

**Step 3: Teen Formats Mein Listing Banao**

### Format A: WhatsApp-Ready (Short)
```
🚗 *[Year] [Brand] [Model] [Variant]*
📍 Car Markaz | Muhammad Saqib

✅ [Color] | [Transmission]
✅ [Mileage] KM | [Registration City] Registered
✅ Condition: [Excellent/Good/Fair]

💰 *PKR [Price]*
[Negotiable: Haan/Nahi]

📸 Photos available: [Haan/Nahi]
📞 Call/WhatsApp: [Contact Number]

_Car Markaz — Aapka Bharosa, Hamaari Zimmedari_
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
Car Markaz | Muhammad Saqib
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
Har listing mein yeh disclaimer zaroori hai:
```
Car Markaz — Aapka Bharosa, Hamaari Zimmedari
Owner: Muhammad Saqib | [Contact]
Final price Muhammad Saqib se confirm karein.
```

**Step 5: Output Save Karo**
File name: `YYYY-MM-DD_[Brand]_[Model]_[Year]_PKR[price].md`
Save location: `Plans/Listings/`

**Step 6: Approval Ke Liye Bhejo**
- Listing ko `Pending_Approval/LISTING_[vehicle].md` mein bhi copy karo
- Muhammad Saqib review karen phir publish karen

**Step 7: Cleanup**
- Original task file `Done/` mein move karo
- Dashboard.md update karo: "New listing ready for approval: [vehicle]"
- Log entry karo

---

## Output Destinations
- Full listing: `Plans/Listings/YYYY-MM-DD_[Brand]_[Model].md`
- Pending approval: `Pending_Approval/LISTING_[vehicle].md`
- Missing info: `Needs_Action/MISSING_INFO_[vehicle].md`

## Escalation Conditions
- Koi mandatory field missing → Needs_Action
- Price 30 lakh se zyada → owner approval zaroori before publish
- Condition "Fair" ho → owner se confirm karo before listing

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
📍 Car Markaz | Muhammad Saqib

✅ White | Automatic
✅ 67,000 KM | Islamabad Registered 2022
✅ Condition: Excellent | Original Paint

💰 *PKR 52,00,000*
Negotiable: Haan

📸 Photos available: Haan
📞 Call/WhatsApp: [Contact Number]

_Car Markaz — Aapka Bharosa, Hamaari Zimmedari_
```
