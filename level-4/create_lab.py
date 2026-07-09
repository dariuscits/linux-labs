from pathlib import Path
import shutil

# ==========================================
# Starbase Communications
# Level 4 - Log Analysis & Troubleshooting
# ==========================================

root = Path("starbase_communications")

# Remove old lab if it exists
if root.exists():
    shutil.rmtree(root)

root.mkdir()

# ------------------------------------------
# Create folders
# ------------------------------------------

folders = [
    "bridge",
    "communications",
    "engineering",
    "logs"
]

for folder in folders:
    (root / folder).mkdir()


# ------------------------------------------
# Create mission files
# ------------------------------------------

files = {

"bridge/navigation.log":
"""INFO Navigation system online
INFO Route calculation complete
WARNING Minor course correction required
INFO Course adjusted successfully
INFO Navigation stable
""",


"communications/transmission.log":
"""INFO Communication array initialized
INFO Signal check complete
ERROR Primary antenna connection lost
INFO Backup antenna activated
ERROR Signal strength below threshold
INFO Communication attempt failed
INFO Waiting for technician response
""",


"engineering/reactor.log":
"""INFO Reactor temperature normal
INFO Cooling system active
WARNING Reactor temperature rising
INFO Cooling adjustment completed
INFO Reactor stable
""",


"logs/system.log":
"""INFO Starbase operating normally
INFO Crew systems online
WARNING Communication delay detected
ERROR Communication failure detected
INFO Diagnostic scan started
INFO Awaiting maintenance crew
""",


"mission_log.txt":
"""
==============================
STARBASE COMMUNICATION MISSION
==============================

Commander,

Starbase Orion has lost communication
with Mission Control.

The station appears operational,
but the communication systems are
not responding correctly.

Your task is to investigate the
system logs and determine what caused
the communication failure.

Mission Objectives:

✓ Identify the source of the failure.

✓ Determine how many ERROR messages
  occurred.

✓ Identify the log files containing
  information about the communication
  failure.

✓ Identify the reactor warning.

Record your findings in:

answers.txt


Helpful commands:

cat
grep
head
tail
wc
find


When complete, execute:

python verify.py


Good luck.

-Admiral Vega
""",


"answers.txt":
"""
STARBASE COMMUNICATIONS INVESTIGATION

1. Which system caused the communication failure?

Answer:


2. How many ERROR messages were found?

Answer:


3. Which log files contained information about the communication failure? (Write Answer as 'example.log and example2.log')

Answer:


4. What warning was reported by the reactor system?

Answer:

"""
}


# ------------------------------------------
# Write mission files
# ------------------------------------------

for filename, contents in files.items():
    path = root / filename
    path.write_text(contents)


# ------------------------------------------
# Create verification script
# ------------------------------------------

verify = r'''
from pathlib import Path

root = Path(__file__).parent

answers = root / "answers.txt"

# Colors
GREEN = "\033[92m"
RED = "\033[91m"
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


print("""
====================================
 STARBASE COMMUNICATION REPORT
====================================
""")


if not answers.exists():

    fail("answers.txt is missing")

    print(f"""
{RED}
====================================
MISSION FAILED

Create your investigation report
and try again.

====================================
{RESET}
""")

    exit()


success("answers.txt found")


report = answers.read_text().lower()


print("\nChecking Investigation Answers...\n")


# ------------------------------------
# Question 1
# ------------------------------------

if "primary antenna" in report:
    success("Correct failure source: Primary antenna")
else:
    fail("Incorrect failure source")


# ------------------------------------
# Question 2
# ------------------------------------

if "2" in report:
    success("Correct ERROR count: 2")
else:
    fail("Incorrect ERROR count")


# ------------------------------------
# Question 3
# ------------------------------------

if "transmission.log" in report and "system.log" in report:
    success("Correct log files: transmission.log and system.log")
else:
    fail("Missing required log files")


# ------------------------------------
# Question 4
# ------------------------------------

if "reactor temperature rising" in report:
    success("Correct reactor warning: Reactor temperature rising")
else:
    fail("Incorrect reactor warning")


# ------------------------------------
# Summary
# ------------------------------------

print("""
====================================
 RESULTS
====================================
""")


print(f"{GREEN}Passed: {passed}{RESET}")
print(f"{RED}Failed: {failed}{RESET}")


if failed == 0:

    print(f"""
{GREEN}
====================================
COMMUNICATIONS RESTORED

Mission Control has regained contact
with Starbase Orion.

Investigation complete.

====================================
{RESET}
""")

else:

    print(f"""
{RED}
====================================
MISSION INCOMPLETE

Review the system logs and
update your report.

====================================
{RESET}
""")
'''


(root / "verify.py").write_text(verify)


print("Starbase Communications Lab Created!")