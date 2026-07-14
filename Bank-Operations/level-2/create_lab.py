from pathlib import Path
import shutil
import os
import stat

# ==========================================
# Linux Bank Operations Lab
# Level 2 - Secure the Vault
# ==========================================

BANK = Path("bank_security")
VERIFY = Path("verify.py")


# ==========================================
# Ask Student Name
# ==========================================

name = input("Enter employee name: ")

print("\nCreating Bank Security Lab...\n")


# ==========================================
# Remove Previous Lab
# ==========================================

if BANK.exists():
    shutil.rmtree(BANK)

if VERIFY.exists():
    VERIFY.unlink()


# ==========================================
# Create Folder Structure
# ==========================================

folders = [
    "vault/customer_records",
    "vault/executive",
    "reports",
    "temp",
    "backups"
]

BANK.mkdir()

for folder in folders:
    (BANK / folder).mkdir(parents=True)


# ==========================================
# Create Files
# ==========================================

files = {

"vault/customer_records/customers.csv":
"""
Customer_ID,Name,Account_Type
1001,Alice Johnson,Checking
1002,Michael Smith,Savings
1003,David Brown,Business
""",

"vault/executive/executive_notes.txt":
"""
Executive Meeting Notes

Upcoming security improvements:
- Upgrade authentication systems
- Review access controls
- Audit employee permissions
""",

"reports/audit_report.txt":
"""
Security Audit Report

Issue Found:

Confidential files have incorrect permissions.

Required Action:

Secure vault directories and protect customer information.
""",

"reports/security_summary.txt":
"""
Security Summary

The bank must maintain proper Linux permissions
to protect sensitive information.
""",

"temp/old_backup.txt":
"""
Old backup file.

This file is no longer needed.
""",

"temp/test_file.txt":
"""
Temporary testing file.
Delete before completing the mission.
"""
}


for file, content in files.items():
    (BANK / file).write_text(content.strip())


# ==========================================
# Set Incorrect Starting Permissions
# ==========================================

os.chmod(BANK / "vault", 0o777)
os.chmod(BANK / "vault/customer_records", 0o777)
os.chmod(BANK / "vault/executive", 0o777)


# ==========================================
# Create Security Task File
# ==========================================

tasks = f"""
BANK SECURITY ALERT

Employee: {name}

Congratulations on your continued work in the bank's IT department.

During a security audit, the IT team discovered that confidential banking files have incorrect permissions.

Your mission is to secure the vault and protect sensitive information.

------------------------------------------

TASKS

1. Secure the main vault.

The main vault contains sensitive bank information.

Only the owner should be able to:
- Read files
- Modify files
- Access the directory

Remove access from all other users.


2. Secure customer records.

Customer records contain private customer information.

The owner should have full access.

Employees in the approved group should be able to:
- View files
- Access the directory

All other users should have no access.


3. Secure executive documents.

Executive documents require the highest level of protection.

Only the owner should be able to:
- Read files
- Modify files
- Access the directory

All other users should have no permissions.


4. Create a backup copy of:

reports/audit_report.txt

Place the copy inside:

backups/


5. Remove all files inside:

temp/

------------------------------------------

USEFUL COMMANDS

Check permissions:

ls -l

Change permissions:

chmod

Copy files:

cp

Remove files:

rm


When complete, return to the Level 2 folder and run:

python3 verify.py


Good luck {name}!
"""

(BANK / "security_tasks.txt").write_text(tasks.strip())


# ==========================================
# Create Verification Script
# ==========================================

verify_code = r'''
from pathlib import Path
import stat


# Colors

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"


BANK = Path("bank_security")

score = 0
total = 5


def check(task, result):
    global score

    if result:
        print(f"{GREEN}✔ {task:<35} PASS{RESET}")
        score += 1
    else:
        print(f"{RED}✘ {task:<35} FAIL{RESET}")


def permission(path):

    mode = path.stat().st_mode
    return oct(mode & 0o777)[-3:]


print()
print(f"{CYAN}{BOLD}===================================")
print("     BANK SECURITY VERIFICATION")
print(f"==================================={RESET}")
print()


if not BANK.exists():
    print(f"{RED}ERROR: bank_security folder missing{RESET}")
    exit()


# Permission checks

check(
    "Vault Security Settings",
    permission(BANK / "vault") == "700"
)

check(
    "Customer Records Security",
    permission(BANK / "vault/customer_records") == "750"
)

check(
    "Executive Document Security",
    permission(BANK / "vault/executive") == "700"
)

# Backup check

check(
    "Audit Backup Created",
    (BANK / "backups/audit_report.txt").exists()
)


# Temp check

temp_files = list((BANK / "temp").iterdir())

check(
    "Temporary Files Removed",
    len(temp_files) == 0
)


print()
print(f"{CYAN}{BOLD}==================================={RESET}")

print(f"\nScore: {score}/{total}")


if score == total:
    print(f"\n{GREEN}{BOLD} Mission Complete!{RESET}")
    print("The bank vault has been secured.")
else:
    print(f"\n{RED}{BOLD}Mission Failed{RESET}")
    print(f"{YELLOW}Review the failed tasks and try again.{RESET}")


print(f"{CYAN}{BOLD}==================================={RESET}")
print()
'''


VERIFY.write_text(verify_code)


# ==========================================
# Complete
# ==========================================

print("""
=========================================
 Bank Level 2 Created Successfully
=========================================

Created:

✓ bank_security/
✓ security_tasks.txt
✓ verify.py

Start:

cd bank_security

Read:

cat security_tasks.txt

When complete:

cd ..

python3 verify.py

=========================================
""")
