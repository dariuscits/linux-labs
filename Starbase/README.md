# 🐧 Linux Labs — Starbase Recovery

Welcome to Starbase.

This lab is a structured set of progressive system recovery and Linux command-line challenges. Each level simulates a realistic scenario where filesystems are broken, misconfigured, or partially corrupted.

Your job is to restore order using Linux commands.

---

##  How It Works

Each level is self-contained:

- You enter a level folder
- You run a setup script (`create_lab.py`)
- The lab is generated
- You repair it using Linux commands
- You validate your solution using `verify.py`

---

##  Level Structure

| Level | Focus |
|------|------|
| Level 1 | File Navigation & Organization |
| Level 2 | Permissions & Access Control |
| Level 3 | Process Simulation & System Repair |
| Level 4 | Logs & System Investigation |
| Level 5 | Bash Scripting & Automation |

---

##  Getting Started

Example workflow:

```bash
cd level-1
python create_lab.py
cd starbase_recovery
# fix the system
python verify.py
