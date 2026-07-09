from pathlib import Path
import shutil

root = Path("starbase_recovery")

if root.exists():
    shutil.rmtree(root)

root.mkdir()

folders = [
    "alpha",
    "beta",
    "gamma",
    "delta",
    "epsilon",
    "storage",
    "junk"
]

for folder in folders:
    (root / folder).mkdir()

files = {
    "alpha/commander.txt": "Commander Nova",
    "alpha/engine.cfg": "Engine Settings",
    "alpha/random.txt": "Delete me if desired",

    "beta/scientist.txt": "Scientist Vega",
    "beta/virus.exe": "CORRUPTED",
    "beta/minerals.txt": "Iron\nCopper",

    "gamma/reactor.cfg": "Reactor Config",
    "gamma/alien.tmp": "Take me to your leader",

    "delta/oxygen.cfg": "Oxygen Settings",
    "delta/captain_log.txt": "Captain Log",

    "epsilon/engineer.txt": "Chief Engineer",
    "epsilon/broken.dat": "Broken",

    "storage/supplies.txt": "Medical Kits",
    "storage/navigation.log": "Navigation Log",

    "junk/food.txt": "Food Inventory",
    "junk/old_backup.zip": "Old Backup",

    "mission_log.txt": """
==============================
STARBASE RECOVERY MISSION
==============================

Commander,

The automated backup system malfunctioned during evacuation.

Several files have been misplaced.

Mission Control needs the station restored before launch.

Objectives

✓ Create these folders:

logs
crew
systems
cargo

✓ Move the correct files into those folders.

✓ Delete these corrupted files:

virus.exe
alien.tmp
broken.dat
old_backup.zip

✓ Remove every empty directory.

When complete, execute:

python verify.py

Good luck.

-Admiral Vega
"""
}

for filename, contents in files.items():
    path = root / filename
    path.write_text(contents)

# -----------------------------
# AUTO-GENERATE VERIFY SCRIPT
# -----------------------------

verify_script = r'''
from pathlib import Path

root = Path(__file__).parent

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

passed = 0
failed = 0

def success(message):
    global passed
    passed += 1
    print(f"{GREEN}✓ {message}{RESET}")

def fail(message):
    global failed
    failed += 1
    print(f"{RED}✗ {message}{RESET}")

print("\n===================================")
print(" STARBASE RECOVERY VERIFICATION")
print("===================================\n")

# -----------------------------
# REQUIRED FILES
# -----------------------------

expected_files = {
    "logs/mission_log.txt",
    "logs/captain_log.txt",
    "logs/navigation.log",

    "crew/commander.txt",
    "crew/scientist.txt",
    "crew/engineer.txt",

    "systems/engine.cfg",
    "systems/reactor.cfg",
    "systems/oxygen.cfg",

    "cargo/supplies.txt",
    "cargo/food.txt"
}

print("Checking required files...\n")

for file in sorted(expected_files):
    if (root / file).exists():
        success(f"{file}")
    else:
        fail(f"Missing: {file}")

# -----------------------------
# CORRUPTED FILES
# -----------------------------

print("\nChecking corrupted files...\n")

for bad in ["virus.exe", "alien.tmp", "broken.dat", "old_backup.zip"]:
    if list(root.rglob(bad)):
        fail(f"{bad} still exists")
    else:
        success(f"{bad} removed")

# -----------------------------
# EXTRA FOLDERS
# -----------------------------

print("\nChecking folders...\n")

allowed = {"logs", "crew", "systems", "cargo", "__pycache__"}

extras = []

for item in root.iterdir():
    if item.is_dir() and item.name not in allowed:
        extras.append(item.name)

if extras:
    for folder in sorted(extras):
        fail(f"Extra folder still exists: {folder}")
else:
    success("No extra folders remain")

# -----------------------------
# SUMMARY
# -----------------------------

print("\n===================================")
print(" RESULTS")
print("===================================\n")

print(f"{GREEN}Passed: {passed}{RESET}")
print(f"{RED}Failed: {failed}{RESET}")

if failed == 0:
    print(f"\n{GREEN}MISSION SUCCESSFUL — STARBASE RESTORED!{RESET}\n")
else:
    print(f"\n{RED}MISSION FAILED{RESET}\n")
'''

(root / "verify.py").write_text(verify_script)

print("Mission created!")