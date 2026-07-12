from pathlib import Path
import shutil
import subprocess

root = Path("starbase_maintenance")

# Remove previous lab
if root.exists():
    shutil.rmtree(root)

root.mkdir()

# Create folders
folders = [
    "bridge",
    "engineering",
    "logs"
]

for folder in folders:
    (root / folder).mkdir()

# Create files
files = {
    "bridge/navigation.log": "Navigation systems online.\n",
    "engineering/reactor.log": "Reactor operating normally.\n",
    "logs/system.log": "System maintenance complete.\n",

    "mission_log.txt": """
==============================
STARBASE MAINTENANCE MISSION
==============================

Commander,

Mission Control has detected several maintenance programs that are still running.

Objectives

✓ Locate the running maintenance programs.

✓ Terminate the following processes:

sleep

Do NOT terminate any other processes.

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
# Launch Dummy Processes
# -----------------------------

processes = []

for _ in range(3):
    p = subprocess.Popen(["sleep", "600"])
    processes.append(str(p.pid))

(root / "pids.txt").write_text("\n".join(processes))

# -----------------------------
# Create verify.py
# -----------------------------

verify_script = r'''
from pathlib import Path
import subprocess

root = Path(__file__).parent

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

passed = 0
failed = 0

with open(root / "pids.txt") as f:
    expected_pids = [line.strip() for line in f if line.strip()]

try:
    running = subprocess.check_output(
        ["ps", "-p", ",".join(expected_pids)],
        text=True
    )
except subprocess.CalledProcessError:
    running = ""

alive = []

print(f"\n{CYAN}====================================")
print(" STARBASE MAINTENANCE VERIFICATION")
print(f"===================================={RESET}\n")

for pid in expected_pids:
    if pid in running:
        alive.append(pid)
        failed += 1
        print(f"{RED}✗ Process {pid} is still running{RESET}")
    else:
        passed += 1
        print(f"{GREEN}✓ Process {pid} terminated{RESET}")

print(f"\n{CYAN}===================================={RESET}")
print(f"{GREEN}Passed: {passed}{RESET}")
print(f"{RED}Failed: {failed}{RESET}")

if failed == 0:
    print(f"""
{GREEN}
====================================
 MISSION SUCCESSFUL

 Maintenance programs terminated.

 Starbase Orion is operating normally.

====================================
{RESET}
""")
else:
    print(f"""
{RED}
====================================
 MISSION FAILED

 Some maintenance processes
 are still running.

 Terminate the remaining
 sleep processes and try again.

====================================
{RESET}
""")
'''

(root / "verify.py").write_text(verify_script)

print("Starbase Maintenance Lab Created!")
print(f"Started {len(processes)} maintenance processes.")