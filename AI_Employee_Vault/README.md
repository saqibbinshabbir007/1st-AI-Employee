# Car Markaz — AI Employee System
**Owner:** Sheikh Ali Kabir
**Business:** Car Markaz (Car Showroom)
**System:** Personal AI Employee powered by Claude Code

---

## What Is This System?

Car Markaz's AI Employee is a digital assistant that automatically handles your showroom's daily tasks:
- Processes customer inquiries
- Creates vehicle listings
- Generates sales reports
- Summarizes files
- Keeps a log of every action

---

## How To Submit a Task

1. Copy `Inbox/TASK_TEMPLATE.md`
2. Write your task and drop it into the `Inbox/` folder
3. The AI Employee will process it automatically

---

## Where To View Results

| Folder | Content |
|---|---|
| `Plans/` | Action plans created by the AI |
| `Plans/Leads/` | Customer lead records |
| `Plans/Listings/` | Vehicle listing drafts |
| `Plans/Reports/` | Sales reports |
| `Pending_Approval/` | Items waiting for your approval |
| `Done/` | Completed tasks |
| `Logs/` | Record of every action |

---

## How To Approve / Reject

- **Approve:** Move file from `Pending_Approval/` to `Approved/`
- **Reject:** Move file from `Pending_Approval/` to `Rejected/` (also add a note explaining why)

---

## Available Skills

| Skill | Use |
|---|---|
| `summarize-file` | Summarize any document |
| `process-task` | Process a general task |
| `customer-inquiry` | Handle a customer inquiry |
| `vehicle-listing` | Create a new vehicle listing |
| `sales-report` | Daily / weekly sales report |

---

## How To Run The System (2 Terminals)

**Terminal 1 — File Watcher (keep running at all times):**
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
                                         Approved/ or Rejected/
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

- `Inbox/`, `Logs/`, `Done/` folders will not be pushed to GitHub (they are in `.gitignore`)
- Do not share customer data outside the vault
- Do not sync the vault to any public cloud service

---

**Car Markaz © 2026 — Sheikh Ali Kabir**
