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

verify_script = '''
from pathlib import Path

root = Path(__file__).parent

errors = []

# REQUIRED FINAL STRUCTURE
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

for file in expected_files:
    if not (root / file).exists():
        errors.append(f"Missing file: {file}")

# CHECK DELETED FILES
for bad in ["virus.exe", "alien.tmp", "broken.dat", "old_backup.zip"]:
    if list(root.rglob(bad)):
        errors.append(f"Corrupted file still exists: {bad}")

# CHECK FOR EXTRA TOP LEVEL FOLDERS
allowed = {"logs", "crew", "systems", "cargo", "__pycache__"}

for item in root.iterdir():
    if item.is_dir() and item.name not in allowed:
        errors.append(f"Extra folder still exists: {item.name}")

# RESULT
if errors:
    print("\\nMISSION FAILED\\n")
    for e in errors:
        print("-", e)
else:
    print("\\nMISSION SUCCESSFUL — STARBASE RESTORED\\n")
'''

(root / "verify.py").write_text(verify_script)

print("Mission created!")