from pathlib import Path
import shutil

# ==========================================
# Linux Bank Operations Lab
# Level 3 - Fraud Investigation
# ==========================================

BANK = Path("bank_investigation")
VERIFY = Path("verify.py")


# ==========================================
# Ask Student Name
# ==========================================

name = input("Enter employee name: ")

print("\nCreating Fraud Investigation Lab...\n")


# ==========================================
# Remove Previous Lab
# ==========================================

if BANK.exists():
    shutil.rmtree(BANK)

if VERIFY.exists():
    VERIFY.unlink()


# ==========================================
# Create Directory Structure
# ==========================================

folders = [
    "logs",
    "reports",
    "evidence"
]

BANK.mkdir()

for folder in folders:
    (BANK / folder).mkdir()


# ==========================================
# Create Investigation Logs
# ==========================================

files = {

"logs/authentication.log":
"""
2026-07-12 08:01:22 SUCCESS user=jdoe ip=192.168.1.25
2026-07-12 08:05:14 SUCCESS user=asmith ip=192.168.1.40
2026-07-12 08:12:02 FAILED user=backup_admin ip=45.22.10.5
2026-07-12 08:12:15 FAILED user=backup_admin ip=45.22.10.5
2026-07-12 08:12:31 FAILED user=backup_admin ip=45.22.10.5
2026-07-12 08:13:05 FAILED user=backup_admin ip=45.22.10.5
2026-07-12 08:15:22 FAILED user=test_user ip=10.10.5.20
2026-07-12 08:17:41 SUCCESS user=manager ip=192.168.1.15
2026-07-12 08:20:12 FAILED user=test_user ip=10.10.5.20
""",

"logs/transactions.log":
"""
TX1001 ACCOUNT=5521 AMOUNT=250 STATUS=APPROVED
TX1002 ACCOUNT=8842 AMOUNT=500 STATUS=APPROVED
TX1003 ACCOUNT=9921 AMOUNT=15000 STATUS=FLAGGED
TX1004 ACCOUNT=7712 AMOUNT=1200 STATUS=APPROVED
TX1005 ACCOUNT=3321 AMOUNT=25000 STATUS=APPROVED
TX1006 ACCOUNT=4498 AMOUNT=18000 STATUS=APPROVED
TX1007 ACCOUNT=6654 AMOUNT=700 STATUS=APPROVED
""",

"logs/firewall.log":
"""
2026-07-12 BLOCK IP=45.22.10.5 PORT=22
2026-07-12 ALLOW IP=192.168.1.25 PORT=443
2026-07-12 BLOCK IP=10.10.5.20 PORT=22
""",

"logs/system.log":
"""
2026-07-12 SYSTEM START
2026-07-12 DATABASE BACKUP COMPLETE
2026-07-12 SECURITY MONITOR ACTIVE
"""
}


for file, content in files.items():
    (BANK / file).write_text(content.strip())


# ==========================================
# Create Task File
# ==========================================

tasks = f"""
BANK FRAUD INVESTIGATION

Investigator:
{name}


The fraud department has detected suspicious activity.

Your job is to analyze the available logs and create an investigation report.


------------------------------------------

TASKS


1. Analyze Failed Login Attempts.

The security team believes unauthorized login attempts may have occurred.

Search the authentication logs for security keywords.

Look for:

FAILED

Determine:

- The user account with the suspicious login activity.
- The number of failed attempts.


2. Identify the Suspicious IP Address.

Use the failed login entries to determine which IP address generated the most suspicious activity.

Look for repeated IP addresses connected to failed login attempts.


3. Find the Flagged Transaction.

The fraud department marked suspicious financial activity in the transaction logs.

Search the transaction logs using the keyword:

FLAGGED

Record:

- Transaction ID
- Account number
- Transaction amount


4. Investigate Security Alerts.

The firewall logs contain network security events.

Search for the keyword:

BLOCK

Determine if any blocked connections match the suspicious activity found in the authentication logs.


5. Find Large Transactions.

Review:

logs/transactions.log

Identify transactions that exceed $10,000.


6. Create Investigation Report.

Create:

reports/investigation_report.txt


Include:

Suspicious User:
Suspicious IP:
Flagged Transaction:
Account Number:
Transaction Amount:
Large Transactions:
Firewall Alert:


------------------------------------------

Helpful Investigation Commands:

Search for keywords:

grep keyword filename


Examples:

grep FAILED logs/authentication.log

grep FLAGGED logs/transactions.log

grep BLOCK logs/firewall.log


Count results:

grep keyword filename | wc -l


Find repeated entries:

sort file | uniq -c


Good luck Investigator {name}!
"""

(BANK / "investigation_tasks.txt").write_text(tasks.strip())


# ==========================================
# Create Verification Script
# ==========================================

verify_code = r'''
from pathlib import Path

# ==========================================
# Fraud Investigation Verification
# ==========================================

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"


BANK = Path("bank_investigation")

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
print(f"{CYAN}{BOLD}===================================")
print(" FRAUD INVESTIGATION VERIFICATION")
print(f"==================================={RESET}")
print()


report = BANK / "reports/investigation_report.txt"


if report.exists():
    content = report.read_text().lower()
else:
    content = ""


check(
    "Investigation Report Created",
    report.exists()
)


check(
    "Suspicious User Identified",
    "backup_admin" in content
)


check(
    "Suspicious IP Identified",
    "45.22.10.5" in content
)


check(
    "Flagged Transaction Found",
    "tx1003" in content
    and "9921" in content
    and "15000" in content
)


check(
    "Large Transactions Counted",
    "3" in content
)


print()
print(f"{CYAN}{BOLD}==================================={RESET}")

print(f"\nScore: {score}/{total}")


if score == total:
    print(f"\n{GREEN}{BOLD} Investigation Complete!{RESET}")
    print("The fraud investigation report has been accepted.")
else:
    print(f"\n{RED}{BOLD}Mission Failed{RESET}")
    print(f"{YELLOW}Review your investigation report and try again.{RESET}")


print(f"{CYAN}{BOLD}==================================={RESET}")
print()
'''


VERIFY.write_text(verify_code)


# ==========================================
# Complete
# ==========================================

print("""
=========================================
 Level 3 Fraud Investigation Created
=========================================

Created:

✓ bank_investigation/
✓ investigation_tasks.txt
✓ logs/
✓ verify.py

Start:

cd bank_investigation

Read:

cat investigation_tasks.txt

When complete:

cd ..

python3 verify.py

=========================================
""")
