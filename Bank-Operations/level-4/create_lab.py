from pathlib import Path
import shutil
import subprocess
import time
import os


# ==========================================
# Linux Bank Operations Lab
# Level 4 - System Recovery
# ==========================================

BANK = Path("bank_recovery")
VERIFY = Path("verify.py")


# ==========================================
# Ask Student Name
# ==========================================

name = input("Enter employee name: ")

print("\nCreating System Recovery Lab...\n")


# ==========================================
# Cleanup
# ==========================================

if BANK.exists():
    shutil.rmtree(BANK)

if VERIFY.exists():
    VERIFY.unlink()


# ==========================================
# Create Folder Structure
# ==========================================

folders = [
    "app",
    "config",
    "logs",
    "reports"
]

BANK.mkdir()

for folder in folders:
    (BANK / folder).mkdir()


# ==========================================
# Create Transaction Server
# ==========================================

transaction_code = """
import time
import os
from datetime import datetime

while True:

    with open("../logs/system_activity.log", "a") as log:
        log.write(
            f"{datetime.now()} Transaction Server Running PID={os.getpid()}\\n"
        )

    time.sleep(10)
"""

(BANK / "app/transaction_server.py").write_text(
    transaction_code.strip()
)


# ==========================================
# Create Suspicious Backup Process
# ==========================================

backup_code = """
import time
import os
from datetime import datetime

while True:

    with open("../logs/suspicious_activity.log", "a") as log:
        log.write(
            f"{datetime.now()} Suspicious Backup Process PID={os.getpid()}\\n"
        )

    time.sleep(10)
"""

(BANK / "app/suspicious_backup.py").write_text(
    backup_code.strip()
)


# ==========================================
# Create Configuration
# ==========================================

(BANK / "config/transaction.conf").write_text(
"""
SERVER=transaction-server
DATABASE_STATUS=FAILED
DATABASE_CONNECTION=INVALID
PORT=3306
""".strip()
)


# ==========================================
# Create Logs
# ==========================================

(BANK / "logs/system_errors.log").write_text(
"""
ERROR Transaction Server Failed
ERROR Database connection rejected
WARNING Unauthorized backup process detected
""".strip()
)


# ==========================================
# Start Processes
# ==========================================

transaction_process = subprocess.Popen(
    [
        "python3",
        "transaction_server.py"
    ],
    cwd=BANK / "app"
)


backup_process = subprocess.Popen(
    [
        "python3",
        "suspicious_backup.py"
    ],
    cwd=BANK / "app"
)


# Save PIDs for setup tracking
(BANK / "process_ids.txt").write_text(
f"""
Transaction Server PID: {transaction_process.pid}

Suspicious Backup PID: {backup_process.pid}
"""
)


time.sleep(2)


# ==========================================
# Create Task File
# ==========================================

tasks = f"""
BANK SYSTEM RECOVERY

Technician:
{name}


The bank transaction server is experiencing issues.

The monitoring team detected:

- A damaged transaction configuration
- A suspicious background process
- A system recovery event


Your mission is to investigate and repair the system.


==========================================

TASK 1 - Find Running Processes

Use:

ps aux

Locate:

- Transaction Server
- Suspicious Backup Process


Record the PID values.


==========================================

TASK 2 - Stop Suspicious Process

The security team identified the backup process as unauthorized.

Find the PID using:

ps aux | grep suspicious_backup


Stop the process:

kill PID


Verify it is no longer running.


==========================================

TASK 3 - Repair Configuration

Review:

config/transaction.conf


Review the errors:

logs/system_errors.log


Repair the configuration.


==========================================

TASK 4 - Create Recovery Report

Create:

reports/recovery_report.txt


Include:


Transaction Process:

Transaction PID:

Suspicious Process:

Configuration Fixed:

Recovery Status:


==========================================

Helpful Commands:

ps
grep
kill
cat
nano


Good luck Technician {name}!
"""


(BANK / "recovery_tasks.txt").write_text(
    tasks.strip()
)


# ==========================================
# Create Verification Script
# ==========================================

verify_code = r'''
from pathlib import Path
import os


GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"


BANK = Path("bank_recovery")

score = 0
total = 5


def check(task, result):

    global score

    if result:
        print(f"{GREEN}✔ {task:<35} PASS{RESET}")
        score += 1

    else:
        print(f"{RED}✘ {task:<35} FAIL{RESET}")


print()

print(
f"{CYAN}{BOLD}==================================="
)

print(
"SYSTEM RECOVERY VERIFICATION"
)

print(
f"==================================={RESET}"
)

print()


# Report Check

report = BANK / "reports/recovery_report.txt"


if report.exists():

    report_text = report.read_text().lower()

else:

    report_text = ""


check(
    "Recovery Report Created",
    report.exists()
)


# Configuration Check

config = BANK / "config/transaction.conf"


if config.exists():

    config_text = config.read_text().lower()

else:

    config_text = ""


check(
    "Configuration Repaired",
    "active" in config_text
    and "valid" in config_text
)


# Suspicious Process Check

processes = os.popen(
    "ps aux | grep suspicious_backup | grep -v grep"
).read()


check(
    "Suspicious Process Stopped",
    processes.strip() == ""
)


# Transaction Process Check

processes = os.popen(
    "ps aux | grep transaction_server | grep -v grep"
).read()


check(
    "Transaction Process Running",
    processes.strip() != ""
)


# Recovery Status

check(
    "Recovery Complete",
    "complete" in report_text
    or "recovered" in report_text
)


print()

print(
f"{CYAN}{BOLD}==================================={RESET}"
)

print(
f"Score: {score}/{total}"
)


if score == total:

    print(
    f"{GREEN}{BOLD}🎉 Recovery Complete!{RESET}"
    )

else:

    print(
    f"{RED}{BOLD}Mission Failed{RESET}"
    )


print(
f"{CYAN}{BOLD}==================================={RESET}"
)

'''


VERIFY.write_text(
    verify_code
)


# ==========================================
# Finished
# ==========================================

print("""
=========================================
 Level 4 System Recovery Created
=========================================

Created:

✓ bank_recovery/
✓ recovery_tasks.txt
✓ Real running processes
✓ Configuration files
✓ verify.py

Start:

cd bank_recovery

Read:

cat recovery_tasks.txt


When finished:

cd ..

python3 verify.py

=========================================
""")