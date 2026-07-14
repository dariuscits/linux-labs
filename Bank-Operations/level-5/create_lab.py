from pathlib import Path
import shutil
import subprocess
import time


# ==========================================
# Linux Bank Operations Lab
# Level 5 - Bank Incident Response
# ==========================================

BANK = Path("bank_incident")
VERIFY = Path("verify.py")


# ==========================================
# Ask Employee Name
# ==========================================

name = input("Enter employee name: ")

print("\nCreating Bank Incident Response Lab...\n")


# ==========================================
# Cleanup
# ==========================================

if BANK.exists():
    shutil.rmtree(BANK)

if VERIFY.exists():
    VERIFY.unlink()


# ==========================================
# Create Structure
# ==========================================

folders = [
    "logs",
    "secure_files",
    "config",
    "processes",
    "reports"
]

BANK.mkdir()

for folder in folders:
    (BANK / folder).mkdir()


# ==========================================
# Create Security Logs
# ==========================================

(BANK / "logs/security.log").write_text(
"""
2026-07-12 09:01 FAILED user=admin_backup ip=45.22.10.5
2026-07-12 09:03 FAILED user=admin_backup ip=45.22.10.5
2026-07-12 09:05 FAILED user=admin_backup ip=45.22.10.5
2026-07-12 09:10 SUCCESS user=manager ip=192.168.1.20
""".strip()
)


(BANK / "logs/system_errors.log").write_text(
"""
ERROR Transaction database connection failed
ERROR Invalid configuration detected
WARNING Unauthorized backup process running
""".strip()
)


# ==========================================
# Create Secure Files
# ==========================================

(BANK / "secure_files/customer_data.txt").write_text(
"""
Customer Account Information

Sensitive Banking Data
""".strip()
)


(BANK / "secure_files/employee_records.txt").write_text(
"""
Employee Records

Confidential Information
""".strip()
)


# Set incorrect permissions intentionally

(BANK / "secure_files/customer_data.txt").chmod(0o777)

(BANK / "secure_files/employee_records.txt").chmod(0o777)


# ==========================================
# Create Broken Configuration
# ==========================================

(BANK / "config/transaction.conf").write_text(
"""
SERVER=transaction-server
DATABASE_STATUS=FAILED
DATABASE_CONNECTION=INVALID
""".strip()
)


# ==========================================
# Create Suspicious Process
# ==========================================

suspicious_code = """

import time
import os


while True:

    with open("../logs/process_activity.log","a") as log:
        log.write(
            f"Unauthorized process running PID={os.getpid()}\\n"
        )

    time.sleep(15)

"""


(BANK / "processes/suspicious_process.py").write_text(
    suspicious_code.strip()
)


# Start suspicious process

process = subprocess.Popen(
    [
        "python3",
        "suspicious_process.py"
    ],
    cwd=BANK / "processes"
)


(BANK / "process_pid.txt").write_text(
str(process.pid)
)


time.sleep(2)


# ==========================================
# Create Task File
# ==========================================

tasks = f"""
BANK INCIDENT RESPONSE

Investigator:
{name}


The bank security team has detected a possible system compromise.

Your mission is to investigate and recover the system.


==========================================

TASK 1 - Investigate Security Logs


Review:

logs/security.log


Find:

- Suspicious username
- Suspicious IP address
- Number of failed attempts


Helpful command:

grep FAILED logs/security.log


==========================================

TASK 2 - Secure Sensitive Files


Review:

secure_files/


Check permissions:

ls -l secure_files


Repair the permissions using:

chmod


Sensitive files should no longer be publicly accessible.


==========================================

TASK 3 - Remove Suspicious Process


Find running processes:

ps aux


Search:

ps aux | grep suspicious


Identify the PID.


Stop the process:

kill PID


Verify the process is no longer running.


==========================================

TASK 4 - Repair Configuration


Review:

config/transaction.conf


Review errors:

logs/system_errors.log


Repair the configuration.


==========================================

TASK 5 - Create Incident Report


Create:

reports/incident_report.txt


Include:


Investigator:

Suspicious User:

Suspicious IP:

Permissions Fixed:

Suspicious Process Removed:

Configuration Repaired:

Final Status:


==========================================

Useful Commands:

grep
ls
chmod
ps
kill
cat
nano


Good luck Investigator {name}!
"""


(BANK / "incident_tasks.txt").write_text(
    tasks.strip()
)


# ==========================================
# Create Verification Script
# ==========================================

verify_code = r'''
from pathlib import Path
import os


GREEN="\033[92m"
RED="\033[91m"
CYAN="\033[96m"
BOLD="\033[1m"
RESET="\033[0m"


BANK = Path("bank_incident")

score = 0
total = 6


def check(task,result):

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
"BANK INCIDENT RESPONSE VERIFICATION"
)

print(
f"==================================={RESET}"
)

print()


# Log Investigation

check(
"Security Log Investigation",
"admin_backup" in 
(BANK/"logs/security.log").read_text()
)


# Permission Check

customer = BANK/"secure_files/customer_data.txt"

employee = BANK/"secure_files/employee_records.txt"


check(
"Permissions Secured",
oct(customer.stat().st_mode)[-3:] != "777"
and
oct(employee.stat().st_mode)[-3:] != "777"
)


# Process Check

running = os.popen(
"ps aux | grep suspicious_process.py | grep -v grep"
).read()


check(
"Suspicious Process Removed",
running.strip()==""
)


# Configuration

config = (
BANK/"config/transaction.conf"
).read_text().lower()


check(
"Configuration Repaired",
"active" in config
and
"valid" in config
)


# Report

report = BANK/"reports/incident_report.txt"


if report.exists():

    report_text = report.read_text().lower()

else:

    report_text=""


check(
"Incident Report Created",
report.exists()
)


check(
"Incident Response Complete",
"resolved" in report_text
or
"complete" in report_text
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
    f"{GREEN}{BOLD}🎉 INCIDENT RESOLVED!{RESET}"
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
# Finish
# ==========================================

print("""
=========================================
 Level 5 Bank Incident Response Created
=========================================

Created:

✓ bank_incident/
✓ security logs
✓ broken configuration
✓ insecure files
✓ real suspicious process
✓ verify.py

Start:

cd bank_incident

Read:

cat incident_tasks.txt


When finished:

cd ..

python3 verify.py

=========================================
""")