# Car Markaz — AI Employee System
**Owner:** Muhammad Saqib
**Business:** Car Markaz (Car Showroom)
**System:** Personal AI Employee powered by Claude Code

---

## Yeh System Kya Hai?

Car Markaz ka AI Employee ek digital assistant hai jo aapke showroom ke daily kaam automatically karta hai:
- Customer inquiries process karta hai
- Vehicle listings banata hai
- Sales reports generate karta hai
- Files summarize karta hai
- Har kaam ka log rakhta hai

---

## Task Submit Kaise Karo

1. `Inbox/TASK_TEMPLATE.md` ko copy karo
2. Apna kaam likh kar `Inbox/` folder mein drop karo
3. AI Employee automatically process karega

---

## Results Kahan Dekhein

| Folder | Content |
|---|---|
| `Plans/` | AI ke banaye hue action plans |
| `Plans/Leads/` | Customer lead records |
| `Plans/Listings/` | Vehicle listing drafts |
| `Plans/Reports/` | Sales reports |
| `Pending_Approval/` | Aapki approval chahiye in cheezon ko |
| `Done/` | Completed tasks |
| `Logs/` | Har action ka record |

---

## Approve / Reject Kaise Karo

- **Approve:** File ko `Pending_Approval/` se `Approved/` mein move karo
- **Reject:** File ko `Pending_Approval/` se `Rejected/` mein move karo (note bhi likh do kyun reject kiya)

---

## Available Skills

| Skill | Use |
|---|---|
| `summarize-file` | Koi bhi document summarize karna |
| `process-task` | General task process karna |
| `customer-inquiry` | Customer ka inquiry handle karna |
| `vehicle-listing` | Naya vehicle listing banana |
| `sales-report` | Daily / weekly sales report |

---

## System Chalane Ka Tarika (2 Terminals)

**Terminal 1 — File Watcher (hamesha chalta rahe):**
```bash
cd C:\Users\PMLS\Documents\AI_Employee_Vault
python file_watcher.py
```

**Terminal 2 — Claude Code:**
```bash
cd C:\Users\PMLS\Documents\AI_Employee_Vault
claude
```

---

## File Flow

```
Inbox/ → (file_watcher.py) → Needs_Action/ → (Claude) → Plans/ → Done/
                                                    ↓
                                           Pending_Approval/
                                                    ↓
                                         Approved/ ya Rejected/
```

---

## Technical Setup

**Requirements:**
- Python 3.14+
- Node.js v24+
- Claude Code CLI

**Install watchdog:**
```bash
pip install watchdog
```

---

## Security Note

- `Inbox/`, `Logs/`, `Done/` folders GitHub pe push nahi hongi (`.gitignore` mein hain)
- Customer data vault ke bahar share na karo
- Vault kisi public cloud service pe sync mat karo

---

**Car Markaz © 2026 — Muhammad Saqib**
