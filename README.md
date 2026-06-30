---

# ️ How to Run the Starbase Recovery Lab

## 1. Clone or Download the Project

If this is on GitHub:

```bash
git clone <your-repo-url>
cd starbase-recovery
```

Or just download the ZIP and extract it.

---

## 2. Generate the Mission Filesystem

Run the setup script:

```bash
python create_lab.py
```

### What this does:

* Creates a folder called `starbase_recovery`
* Builds the broken starbase file system
* Drops files into the wrong places (this is intentional)
* Creates `verify.py` (your checker script)

---

## 3. Enter the Mission Folder

```bash
cd starbase_recovery
```

You should now see folders like:

```
alpha/
beta/
gamma/
delta/
epsilon/
storage/
junk/
```

---

## 4. Complete the Mission

Use Linux / terminal commands to:

* Move files into correct folders
* Delete corrupted files
* Remove empty directories

You can use commands like:

```bash
ls
mv
rm
rmdir
```

---

## 5. Verify Your Solution

When you think everything is fixed, run:

```bash
python verify.py
```

---

## 6. Success / Failure Output

###  If correct:

```
MISSION SUCCESSFUL — STARBASE RESTORED
```

###  If something is wrong:

You’ll see a list of:

* missing files
* leftover corrupted files
* incorrect folder structure

---

## ️ Important Notes

* Do NOT edit `verify.py`
* Do NOT rename required files
* The goal is **file system recovery**, not rewriting code

---

