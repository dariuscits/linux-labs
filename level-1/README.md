````md
# 🧩 Level 1 — Starbase Recovery

## 🚀 Mission Brief

A critical starbase file system has been disrupted during an emergency evacuation. Files were scattered across multiple directories, and corrupted data was left behind.

Your task is to restore the system to a stable state so it can safely reboot for launch operations.

---

## 🎯 Mission Objectives

To complete this level, you must restore order across the system by:

- Organizing files into the correct directory structure
- Removing corrupted or unsafe files from the system
- Cleaning up any empty directories left behind

The final system must match a stable operational state before verification.

---

## 🧠 System Tools You Will Use

You will rely on standard Linux command-line tools:

- `ls` → inspect directory contents  
- `cd` → navigate between directories  
- `mv` → move files into correct locations  
- `rm` → remove corrupted or unwanted files  
- `rmdir` → remove empty directories  

These commands are part of the Linux filesystem toolkit used for managing files, directories, and system structure.

---

## 🛠️ Setup Instructions

Before beginning the mission, generate the corrupted filesystem:

```bash
python create_lab.py
````

This will create a broken starbase environment inside a working directory.

---

## 📁 Working Environment

After setup, you will find a folder containing multiple directories and files that are intentionally misplaced or corrupted.

Your job is to analyze the structure and restore logical organization.

---

## 🧪 Verification

Once you believe the system has been fully restored, run the verification script:

```bash
python verify.py
```

The system will evaluate:

* File placement accuracy
* Removal of corrupted files
* Directory structure integrity
* Cleanup of empty folders

---

## ⚠️ Rules of Engagement

* Do not modify `verify.py`
* Do not rename required files
* Do not skip corrupted file cleanup
* Use terminal commands only (no manual editing of file contents)

---

## 🛰️ Success Condition

If completed correctly, you will receive:

```
MISSION SUCCESSFUL — STARBASE RESTORED
```

---

## 🧭 Training Focus

This level focuses on:

* File system navigation
* Directory organization
* Safe file deletion
* Understanding Linux structure hierarchy

---

## 🔓 Next Step

After successful completion, proceed to Level 2 to face more advanced system control challenges.

```
```

