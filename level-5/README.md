# 🛰️ Starbase Automation
## Level 5 – Bash Scripting & Automation

Welcome to the final Starbase Linux Lab!

Mission Control has automated many routine maintenance tasks using Bash scripts. Unfortunately, the station's maintenance script was damaged during a software update and no longer works correctly.

Your mission is to inspect the script, repair the errors, and successfully complete the automated maintenance routine.

---

## Learning Objectives

By completing this lab, you will learn how to:

- Read a Bash script
- Identify and fix syntax errors
- Execute shell scripts
- Make scripts executable
- Understand basic Bash commands

---

## Skills Practiced

- Bash scripting
- Linux automation
- Script debugging
- Command-line navigation
- Troubleshooting

---

## Linux Commands

| Command | Purpose |
|---------|---------|
| `pwd` | Show current directory |
| `ls` | List files |
| `cd` | Change directories |
| `cat` | Display a file |
| `chmod` | Change file permissions |
| `nano` | Edit a file |
| `./script.sh` | Execute a script |

---

## Repository Structure

```
starbase_automation/

create_lab.py
README.md
student_guide.md
```

After running the setup script:

```
starbase_automation/

bridge/
engineering/
logs/

maintenance.sh
mission_log.txt
verify.py
```

---

## Getting Started

Generate the lab.

```bash
python create_lab.py
```

Navigate into the generated folder.

```bash
cd starbase_automation
```

Read the Mission Log before making any changes.

---

## Mission Goal

Repair the maintenance script so it completes successfully.

When finished, run:

```bash
./maintenance.sh
```

Then verify your work:

```bash
python verify.py
```

Good luck, Commander.