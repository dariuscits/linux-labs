# 🐧 Linux Labs — Systems Training Simulator

Welcome to CITS  Linux Labs.

This repository is a structured set of progressive system recovery and Linux command-line challenges. Each level simulates a real-world scenario where filesystems are broken, misconfigured, or partially corrupted.

Your job is to restore order using Linux commands.

---

##  How It Works

Each level is self-contained:

- You enter a level folder
- You run a setup script (`create_lab.py`)
- A broken file system is generated
- You repair it using Linux commands
- You validate your solution using `verify.py`

---

##  Level Structure

| Level | Focus |
|------|------|
| Level 1 | File navigation & organization |
| Level 2 | Permissions & access control |
| Level 3 | Process simulation & system repair |

---

##  Getting Started

Example workflow:

```bash
cd level-1
python create_lab.py
cd starbase_recovery
# fix the system
python verify.py
