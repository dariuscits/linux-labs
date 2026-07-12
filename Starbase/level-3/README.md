# 🛰️ Starbase Maintenance
## Level 3 – Processes & System Repair

Welcome to **Level 3** of the Starbase Linux Labs!

The Starbase Orion file system has been restored and secured, but Mission Control has detected several maintenance programs that were accidentally left running.

Your mission is to locate the unnecessary processes, terminate them safely, and verify that the station is ready for launch.

---

## Learning Objectives

By completing this lab, you will learn how to:

- View running processes
- Identify Process IDs (PIDs)
- Terminate running processes
- Understand how Linux manages running programs

---

## Skills Practiced

- Process Management
- Linux Troubleshooting
- Command Line Navigation

---

## Linux Commands

| Command | Purpose |
|---------|---------|
| `pwd` | Display your current working directory |
| `ls` | List files and folders |
| `cd` | Change directories |
| `cat` | Display file contents |
| `ps` | Show running processes |
| `ps -ef` | Show all running processes |
| `kill` | Stop a running process |

---

## Repository Structure

```
level-3/

create_lab.py
README.md
```

After running the setup script:

```
starbase_maintenance/

bridge/
engineering/
logs/

mission_log.txt
verify.py
```

---

## Getting Started

Generate the lab.

```bash
python create_lab.py
```

Navigate into the generated directory.

```bash
cd starbase_maintenance
```

Read the Mission Log and begin your investigation.

---

## Mission Goal

Locate the maintenance programs that should no longer be running.

Terminate only the processes identified in the Mission Log.

When finished, execute:

```bash
python verify.py
```

---

Good luck, Commander.
