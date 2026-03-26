# Muhammad Saqib — My To-Do Guide
**Car Markaz AI Employee System**
_Read this file to remember everything_

---

## Where Is The System
```
E:\Agentic_PIAIC\Bronze_Tier\AI_Employee_Vault\
```

---

## How To Run The System Daily

### Terminal 1 — Start the File Watcher:
```
cd E:\Agentic_PIAIC\Bronze_Tier\AI_Employee_Vault
python file_watcher.py
```

### Terminal 2 — Start Claude:
```
cd E:\Agentic_PIAIC\Bronze_Tier\AI_Employee_Vault
claude
```

### Open Obsidian:
- Vault: `E:\Agentic_PIAIC\Bronze_Tier\AI_Employee_Vault`
- Every morning open **Dashboard.md** to check status

---

## How To Use Daily

### 1. Customer Inquiry Received:
- Copy `Inbox/TASK_TEMPLATE.md` → rename it
- Write `skill: customer-inquiry`
- Add customer details (name, phone, requirement, budget)
- Save — Atlas will process it automatically

### 2. List a New Vehicle:
- Create new file in `Inbox/`
- Write `skill: vehicle-listing`
- Add vehicle details (year, brand, model, price, mileage etc.)
- Save — Atlas will create the listing

### 3. Need a Daily/Weekly Report:
- Create new file in `Inbox/`
- Write `skill: sales-report`
- Add today's sales data
- Save — Atlas will generate the report

### 4. Summarize Any Document:
- Create new file in `Inbox/`
- Write `skill: summarize-file`
- Paste the content
- Save — Atlas will summarize it

---

## How To Approve / Reject

| Action | Where To Go |
|---|---|
| Check Atlas's response | `Pending_Approval/` folder |
| To approve | Move file to `Approved/` |
| To reject | Move file to `Rejected/` (add a reason) |
| Urgent tasks | Check `Needs_Action/` folder |

---

## Available Skills (5 Skills)

| Skill | When To Use |
|---|---|
| `customer-inquiry` | Any customer inquiry |
| `vehicle-listing` | List a new vehicle |
| `sales-report` | Daily or weekly report |
| `summarize-file` | Summarize any document |
| `process-task` | Any general task |

---

## Important Files

| File | Purpose |
|---|---|
| `Dashboard.md` | Open every morning — all status here |
| `Company_Handbook.md` | Business rules — edit when needed |
| `CLAUDE.md` | Atlas's instructions — do not modify |
| `file_watcher.py` | Watcher script — just run it |

---

## Today's Pending Tasks

- [ ] `Pending_Approval/RESPONSE_AliRaza.md` — Approve Ali Raza's WhatsApp response
- [ ] Call Ali Raza: **0300-1234567** — Confirm tomorrow's visit
- [ ] Check Toyota Corolla 2022 stock availability
- [ ] Install **Dataview plugin** in Obsidian (Dashboard will look better)
  - Settings → Community Plugins → Browse → "Dataview" → Install & Enable

---

## Troubleshooting

| Problem | Solution |
|---|---|
| `python` command not working | Try `python3 file_watcher.py` |
| `claude` command not working | Close terminal and reopen |
| Files not showing in Obsidian | Click another folder and come back |
| Watcher not detecting files | Check Terminal 1 is still running |

---

## Questions For Jani (Claude)

- [ ] How to save updates to GitHub
- [ ] How to create more skills
- [ ] How to use from mobile
- [ ] Anything else...

---

_This file was created by Claude Code (Jani) for Muhammad Saqib — 2026-03-26_
_Car Markaz — Your Trust, Our Responsibility_
