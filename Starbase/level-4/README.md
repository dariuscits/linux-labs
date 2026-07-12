# 🛰️ Starbase Communications
## Level 4 – Logs & System Investigation

Welcome to **Level 4** of the Starbase Linux Labs!

Starbase Orion has successfully launched, but shortly after entering orbit, Mission Control loses communication with the station.

Your mission is to investigate the system logs, determine what caused the communication failure, and answer the questions provided in the Mission Log.

---

## Learning Objectives

By completing this lab, you will learn how to:

- Search text files using `grep`
- View the beginning and end of files
- Count lines, words, and matches
- Locate files in the filesystem
- Analyze log files to solve problems

---

## Skills Practiced

- Reading log files
- Searching text
- Troubleshooting
- Command line navigation
- Investigating system events

---

## Linux Commands

| Command | Purpose |
|---------|---------|
| `pwd` | Show current directory |
| `ls` | List files |
| `cd` | Change directories |
| `cat` | Display file contents |
| `head` | View the beginning of a file |
| `tail` | View the end of a file |
| `grep` | Search for text |
| `find` | Search for files |
| `wc` | Count lines, words, and characters |

---

## Repository Structure

```
level-4/

create_lab.py
README.md
```

After running the setup script:

```
starbase_communications/

bridge/
communications/
engineering/
logs/

mission_log.txt
answers.txt
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
cd starbase_communications
```

Read the Mission Log and begin your investigation.

---

## Mission Goal

Use Linux commands to investigate the log files and answer the questions.

When you have completed your investigation, write your answers in:

```
answers.txt
```

Run:

```bash
python verify.py
```

Mission Control will evaluate your findings.

---

Good luck, Commander.
