# 🛰️ Starbase Security
## Level 2 – Linux Permissions & File Security

Welcome to **Level 2** of the Starbase Linux Labs!

After successfully restoring the Starbase file system in Level 1, you've been promoted to the station's **Security Technician**.

Your next assignment is to restore access to critical files after a power surge corrupted the station's file permissions.

---

## Learning Objectives

By completing this lab, you will learn how to:

- View Linux file permissions
- Interpret permission strings
- Understand read, write, and execute permissions
- Change file permissions using `chmod`
- Verify file permissions
- Troubleshoot "Permission denied" errors

---

## Skills Practiced

- File Permissions
- File Security
- Command Line Navigation
- Troubleshooting
- Reading Documentation

---

## Linux Commands

You may find these commands helpful during this mission.

| Command | Purpose |
|---------|---------|
| `pwd` | Display your current working directory |
| `ls` | List files and directories |
| `ls -l` | View detailed file information and permissions |
| `cd` | Change directories |
| `cat` | Display the contents of a file |
| `chmod` | Change file permissions |

---

## Repository Structure

```
level-2/
│
├── create_lab.py
└── README.md
```

After running the setup script:

```
starbase_security/
│
├── bridge/
├── engineering/
├── crew_quarters/
├── hangar/
├── logs/
│
├── mission_log.txt
└── verify.py
```

---

## Getting Started

Generate the lab.

```bash
python create_lab.py
```
or

```bash
python3 create_lab.py
```

A new folder named **starbase_security** will be created containing the mission files.

---

## Student Instructions

1. Navigate into the generated lab directory.

2. Read the **Mission Log**.

3. Investigate the file permissions.

4. Restore the correct permissions using Linux commands.

5. Run the verification script.

```bash
python verify.py
```

or

```bash
python3 verify.py
```

---

## Success Criteria

You have completed the mission when:

- All required file permissions have been restored.
- The verification script reports success.
- No changes have been made to the verification program itself.

---

## Challenge Yourself

Can you complete the mission using only:

- `ls -l`
- `chmod`
- `cat`
- `cd`
- `pwd`

without referring back to the command reference?

---

## Previous Lab

- Level 1 – Starbase Recovery (Linux Navigation & File Management)

## Next Lab

- 🚀 Level 3 – Starbase Maintenance (Processes & System Repair)

---

Good luck, Commander.

Mission Control is counting on you.
