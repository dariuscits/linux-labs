from pathlib import Path
import shutil

# ==========================================
# Linux Bank Operations Lab
# Level 1 - Employee Onboarding
# ==========================================

BANK = Path("bank")
VERIFY = Path("verify.py")

# ==========================================
# Ask Student Name
# ==========================================

name = input("Enter employee name: ")

print("\nCreating Bank Employee Onboarding Lab...\n")


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
    "human_resources",
    "it",
    "operations",
    "public",
    "emergency"
]

BANK.mkdir()

for folder in folders:
    (BANK / folder).mkdir()


# ==========================================
# Create Bank Files
# ==========================================

files = {

"welcome.txt": """
Welcome to the Bank IT Department.

This Linux server contains important employee
and operational information.

Use your Linux skills to explore the system.
""",

"human_resources/employee_handbook.txt": """
Employee Handbook

All employees must follow company policies.

Customer information must remain confidential.

Employees are responsible for following
security procedures.
""",

"human_resources/benefits.txt": """
Employee Benefits

Health Insurance
Retirement Plan
Paid Time Off
Professional Development
""",

"it/password_policy.txt": """
Password Policy

Minimum Password Length: 12 characters.

Passwords expire every 90 days.

Multi-factor authentication is required
for all employee accounts.
""",

"it/workstation_setup.txt": """
New Employee Workstation Setup

Employee workstation has been prepared.

IT Manager:
Jordan Carter

Contact IT Support for technical issues.
""",

"public/department_directory.txt": """
Department Directory

Human Resources:
Extension 2100

Customer Accounts:
Extension 2200

Loans:
Extension 2300

IT Support:
Extension 2400
""",

"emergency/emergency_contacts.txt": """
Emergency Contacts

Medical Emergency:
9111

Security Office:
9000

Building Maintenance:
8800
""",

"operations/opening_checklist.txt": """
Daily Opening Checklist

1. Verify systems are online.
2. Check backup status.
3. Prepare employee workstations.

The bank opens to customers at 9:00 AM.
"""
}


for file, content in files.items():
    path = BANK / file
    path.write_text(content.strip())


# ==========================================
# Create Employee Task File
# ==========================================

employee_tasks = f"""
WELCOME TO YOUR FIRST DAY!

Congratulations {name} on joining the bank's Information Technology Department as a Junior IT Technician.

Before you are given administrator privileges, your supervisor would like to verify that you are comfortable navigating our system and locating important information.

Your assignment is to explore the bank's file system and answer the questions below.

---

TASKS

1. Create a directory named workspace.

2. Complete answers.txt.

3. Move or copy answers.txt into the workspace directory.

Examples:

cp answers.txt workspace/

or

mv answers.txt workspace/

---

QUESTIONS

1. Who is the IT Manager?

2. How many days before employee passwords expire?

3. Which department is responsible for customer account requests?

4. What extension should employees dial during an emergency?

5. What time does the bank open on weekdays?

---

SUBMISSION

When finished return to the level folder and run:

python3 verify.py

Good luck {name}!
"""

(BANK / "employee_tasks.txt").write_text(employee_tasks.strip())


# ==========================================
# Create Answer File
# ==========================================

answers = """
Question 1:

Question 2:

Question 3:

Question 4:

Question 5:
"""

(BANK / "answers.txt").write_text(answers.strip())


# ==========================================
# Create Verification Script
# ==========================================

verify_code = r'''
from pathlib import Path

# ==========================================
# Bank Operations Lab Verification
# Level 1
# ==========================================

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"


BANK = Path("bank")

score = 0
total = 7


def check(task, result):
    global score

    if result:
        print(f"{GREEN}✔ {task:<35} PASS{RESET}")
        score += 1
    else:
        print(f"{RED}✘ {task:<35} FAIL{RESET}")


print()
print(f"{CYAN}{BOLD}===================================")
print("      BANK LAB VERIFICATION")
print(f"==================================={RESET}")
print()


if not BANK.exists():
    print(f"{RED}Bank folder not found.{RESET}")
    exit()


# Workspace

check(
    "Workspace directory",
    (BANK / "workspace").exists()
)


check(
    "answers.txt moved/copied",
    (BANK / "workspace" / "answers.txt").exists()
)


# Answers

answer_file = BANK / "workspace" / "answers.txt"


if answer_file.exists():
    answers = answer_file.read_text().lower()
else:
    answers = ""


check(
    "IT Manager",
    "jordan carter" in answers
)


check(
    "Password Expiration",
    "90" in answers
)


check(
    "Customer Accounts",
    "customer accounts" in answers
)


check(
    "Emergency Extension",
    "9111" in answers
)


check(
    "Bank Opening Time",
    "9:00" in answers
)


print()
print(f"{CYAN}{BOLD}==================================={RESET}")

print(f"\nScore: {score}/{total}")


if score == total:
    print(f"\n{GREEN}{BOLD} Mission Complete!{RESET}")
    print("Employee onboarding has been approved.")
else:
    print(f"\n{RED}{BOLD}Mission Failed{RESET}")
    print(f"{YELLOW}Review the failed tasks and try again.{RESET}")


print(f"{CYAN}{BOLD}==================================={RESET}")
print()
'''


VERIFY.write_text(verify_code)


# ==========================================
# Finish
# ==========================================

print("""
=========================================
 Bank Linux Lab Created Successfully
=========================================

Created:

✓ bank/
✓ employee_tasks.txt
✓ answers.txt
✓ verify.py

Start:

cd bank

Read:

cat employee_tasks.txt

When finished:

cd ..
python3 verify.py

=========================================
""")