from pathlib import Path
import shutil
import os

# ==========================================
# Starbase Automation
# Level 5 - Bash Scripting & Automation
# ==========================================

root = Path("starbase_automation")

# Remove old lab if it exists
if root.exists():
    shutil.rmtree(root)

root.mkdir()

# ------------------------------------------
# Create folders
# ------------------------------------------

folders = [
    "bridge",
    "engineering",
    "logs"
]

for folder in folders:
    (root / folder).mkdir()

# ------------------------------------------
# Create files
# ------------------------------------------

files = {

    "bridge/navigation.log":
"""Navigation System Online
Destination Locked
Course Calculated
""",

    "engineering/reactor.log":
"""Reactor Online
Coolant Stable
Power Output Nominal
""",

    "logs/system.log":
"""System Boot Complete
Maintenance Required
Awaiting Technician
""",

    "maintenance.sh":
"""#!/bin/bash

ecoh "===== Starbase Maintenance ====="

pwd

lss

echo ""

ecoh "Checking Logs..."

ls log

ecoh ""

ecoh "Maintenance Complete"
""",

    "mission_log.txt":
"""
==============================
STARBASE AUTOMATION MISSION
==============================

Commander,

Mission Control's automated maintenance system has stopped working.

The maintenance script contains several errors that must be repaired before routine maintenance can continue.

Objectives

✓ Inspect the maintenance script.

✓ Correct every error.

✓ Make the script executable.

✓ Execute the script successfully.

When complete, execute:

python verify.py

Good luck.

-Admiral Vega
"""
}

for filename, contents in files.items():
    path = root / filename
    path.write_text(contents)

# ------------------------------------------
# Remove execute permission from script
# ------------------------------------------

os.chmod(root / "maintenance.sh", 0o644)

# ------------------------------------------
# Create verify.py
# ------------------------------------------

verify_script = r'''
from pathlib import Path
import subprocess

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
print(" STARBASE AUTOMATION VERIFICATION")
print("===================================\n")

script = root / "maintenance.sh"

# ------------------------------------------
# Check if script exists
# ------------------------------------------

if not script.exists():
    fail("maintenance.sh is missing")

else:

    success("maintenance.sh exists")

    # --------------------------------------
    # Check executable permission
    # --------------------------------------

    if script.stat().st_mode & 0o111:
        success("maintenance.sh is executable")
    else:
        fail("maintenance.sh is not executable")

    # --------------------------------------
    # Execute script
    # --------------------------------------

    try:

        output = subprocess.check_output(
            [str(script)],
            cwd=root,
            stderr=subprocess.STDOUT,
            text=True
        )

        success("maintenance.sh executed successfully")

        print("\nChecking script output...\n")

        required_output = [
            "===== Starbase Maintenance =====",
            "Checking Logs...",
            "Maintenance Complete"
        ]

        for line in required_output:

            if line in output:
                success(f'Output contains "{line}"')
            else:
                fail(f'Missing output: "{line}"')

        if "system.log" in output:
            success("Logs directory displayed")
        else:
            fail("The script did not display the logs directory")

    except Exception:
        fail("maintenance.sh did not execute successfully")

# ------------------------------------------
# Summary
# ------------------------------------------

print("\n===================================")
print(" RESULTS")
print("===================================\n")

print(f"{GREEN}Passed: {passed}{RESET}")
print(f"{RED}Failed: {failed}{RESET}")

if failed == 0:

    print(f"""{GREEN}

****************************************

MISSION SUCCESSFUL

Maintenance automation restored.

Routine maintenance has resumed.

Starbase Orion is fully operational.

Mission Control thanks you for your service.

****************************************

{RESET}""")

else:

    print(f"\n{RED}MISSION FAILED{RESET}\n")
'''

(root / "verify.py").write_text(verify_script)

print()
print("=======================================")
print(" Starbase Automation Lab Created!")
print("=======================================")
print()
print(f"Location: {root.resolve()}")
print()
print("Students should:")
print("1. Read mission_log.txt")
print("2. Repair maintenance.sh")
print("3. Make it executable")
print("4. Run ./maintenance.sh")
print("5. Run python verify.py")