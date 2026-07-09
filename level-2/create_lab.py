from pathlib import Path
import shutil
import os

root = Path("starbase_security")

if root.exists():
    shutil.rmtree(root)

root.mkdir()

folders = [
    "bridge",
    "engineering",
    "crew_quarters",
    "hangar",
    "logs"
]

for folder in folders:
    (root / folder).mkdir()

files = {
    "bridge/captain_log.txt": "Captain's daily log...",

    "bridge/launch.sh": "#!/bin/bash\necho 'Launch sequence initiated.'",

    "engineering/engine.cfg": "engine_status=online",
    "engineering/reactor.cfg": "reactor_status=stable",
    "engineering/oxygen.cfg": "oxygen_level=100",

    "crew_quarters/crew_manifest.txt": "Commander Nova\nEngineer Vega",
    "crew_quarters/security_report.txt": "Security scan completed.",

    "hangar/navigation.cfg": "destination=Earth",

    "logs/system.log": "System startup complete.",

    "mission_log.txt": """==============================
STARBASE SECURITY MISSION
==============================

Commander,

The Starbase Orion file system has been successfully restored.

Unfortunately, a power surge corrupted several file permissions.

Mission Control requires the following fixes before launch:

OBJECTIVES

✓ Restore read access to all .txt files

✓ Restore execute permission to:

launch.sh

✓ Configuration files (.cfg) must be:
  - readable
  - writable
  - NOT executable by others

When complete, run:

python verify.py

Good luck.

-Admiral Vega
"""
}

# Write files
for filename, contents in files.items():
    (root / filename).write_text(contents)

# -----------------------------
# BROKEN PERMISSIONS (THE LAB)
# -----------------------------

os.chmod(root / "bridge/captain_log.txt", 0o000)
os.chmod(root / "bridge/launch.sh", 0o644)

os.chmod(root / "engineering/engine.cfg", 0o777)
os.chmod(root / "engineering/reactor.cfg", 0o755)
os.chmod(root / "engineering/oxygen.cfg", 0o666)

os.chmod(root / "crew_quarters/crew_manifest.txt", 0o200)
os.chmod(root / "crew_quarters/security_report.txt", 0o600)

os.chmod(root / "hangar/navigation.cfg", 0o777)

# -----------------------------
# CREATE VERIFY SCRIPT
# -----------------------------

verify_script = r'''
from pathlib import Path

root = Path(__file__).parent

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

passed = 0
failed = 0

checks = {
    "bridge/captain_log.txt": 0o644,
    "bridge/launch.sh": 0o755,

    "engineering/engine.cfg": 0o600,
    "engineering/reactor.cfg": 0o600,
    "engineering/oxygen.cfg": 0o600,

    "crew_quarters/crew_manifest.txt": 0o644,
    "crew_quarters/security_report.txt": 0o644,

    "hangar/navigation.cfg": 0o600,
}

print(f"\n{CYAN}====================================")
print(" STARBASE SECURITY VERIFICATION")
print(f"===================================={RESET}\n")

for file, expected in checks.items():

    path = root / file

    if not path.exists():
        failed += 1
        print(f"{RED}✗ Missing: {file}{RESET}")
        continue

    actual = path.stat().st_mode & 0o777

    if actual == expected:
        passed += 1
        print(f"{GREEN}✓ {file:<35} {oct(actual)}{RESET}")
    else:
        failed += 1
        print(
            f"{RED}✗ {file:<35} "
            f"Current: {oct(actual)}  Expected: {oct(expected)}{RESET}"
        )

print(f"\n{CYAN}===================================={RESET}")
print(f"{GREEN}Passed: {passed}{RESET}")
print(f"{RED}Failed: {failed}{RESET}")

if failed == 0:
    print(f"""
{GREEN}
====================================
 STARBASE SECURITY RESTORED

 All systems secure.
 Launch authorization granted.

 Mission Complete.
====================================
{RESET}
""")
else:
    print(f"""
{RED}
====================================
 MISSION FAILED

 Some permissions are still incorrect.

 Review the red entries above,
 fix them, then run:

    python verify.py

====================================
{RESET}
""")
'''

(root / "verify.py").write_text(verify_script)

print("Starbase Security Lab Created!")