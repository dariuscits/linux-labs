from pathlib import Path

root = Path(__file__).parent

answers = (root / "answers.txt").read_text().lower()

checks = [
    "primary antenna",
    "2",
    "system.log",
    "reactor temperature rising"
]

score = 0

for item in checks:
    if item in answers:
        score += 1

print(f"\nScore: {score}/4\n")

if score == 4:
    print("""
****************************************

MISSION SUCCESSFUL

Communications Restored

Mission Control can once again contact
Starbase Orion.

****************************************
""")
else:
    print("Review your answers and investigate the logs again.")
