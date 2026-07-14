import os
import random



GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"


# SETTINGS

ROOT = "Farm Rescue Mission"


folders = [
    "farm/cows",
    "farm/pigs",
    "farm/chickens",
    "farm/sheep",

    "woods/north",
    "woods/south",

    "lake/east",
    "lake/west",

    "hills/high",
    "hills/low",

    "fields/north",
    "fields/south"
]


animals = {

    "cows": [
        "cow_bessie.txt",
        "cow_daisy.txt",
        "cow_buttercup.txt",
        "cow_mooana.txt",
        "cow_hazel.txt"
    ],

    "pigs": [
        "pig_peppa.txt",
        "pig_porky.txt",
        "pig_hamlet.txt",
        "pig_truffles.txt",
        "pig_rosie.txt"
    ],

    "chickens": [
        "chicken_henrietta.txt",
        "chicken_nugget.txt",
        "chicken_clucky.txt",
        "chicken_sunny.txt",
        "chicken_goldie.txt"
    ],

    "sheep": [
        "sheep_wooly.txt",
        "sheep_cloud.txt",
        "sheep_fluffy.txt",
        "sheep_cotton.txt",
        "sheep_snowball.txt"
    ]
}


predators = [
    "fox",
    "coyote",
    "hawk",
    "raccoon"
]


safe_food = [
    "berries",
    "fish",
    "corn",
    "acorns",
    "fruit"
]



# CREATE FOLDERS

def create_folders():

    os.makedirs(ROOT, exist_ok=True)

    for folder in folders:

        os.makedirs(
            os.path.join(ROOT, folder),
            exist_ok=True
        )


    print(
        f"{GREEN}✓ Farm property created{RESET}"
    )


# SCATTER ANIMALS
 
def scatter_animals():

    animal_list = []

    for pen in animals.values():

        for animal in pen:

            animal_list.append(animal)


    random.shuffle(animal_list)


    for animal in animal_list:

        location = random.choice(folders)


        with open(
            os.path.join(
                ROOT,
                location,
                animal
            ),
            "w"
        ) as file:

            file.write(
                animal.replace(".txt","")
            )


    print(
        f"{GREEN}✓ Animals escaped and scattered{RESET}"
    )


# CREATE PREDATORS


def create_predators():

    animal_names = []


    for pen in animals.values():

        for animal in pen:

            animal_names.append(
                animal.replace(".txt","")
            )


    predator_files = []


    for predator in predators:

        for number in range(1,4):

            predator_files.append(
                f"{predator}_{number}.txt"
            )


    random.shuffle(predator_files)


    for index, predator in enumerate(predator_files):

        location = random.choice(folders)


        # First 6 attack animals
        if index < 6:

            content = random.choice(
                animal_names
            )

        else:

            content = random.choice(
                safe_food
            )


        with open(
            os.path.join(
                ROOT,
                location,
                predator
            ),
            "w"
        ) as file:

            file.write(content)


    print(
        f"{GREEN}✓ Predators entered the land{RESET}"
    )


# CREATE VERIFY.PY

def create_verify():

    verify_code = r'''
import os
import stat


GREEN="\033[92m"
RED="\033[91m"
RESET="\033[0m"


ROOT="."


pens = {

    "cows": [
        "cow_bessie.txt",
        "cow_daisy.txt",
        "cow_buttercup.txt",
        "cow_mooana.txt",
        "cow_hazel.txt"
    ],

    "pigs": [
        "pig_peppa.txt",
        "pig_porky.txt",
        "pig_hamlet.txt",
        "pig_truffles.txt",
        "pig_rosie.txt"
    ],

    "chickens": [
        "chicken_henrietta.txt",
        "chicken_nugget.txt",
        "chicken_clucky.txt",
        "chicken_sunny.txt",
        "chicken_goldie.txt"
    ],

    "sheep": [
        "sheep_wooly.txt",
        "sheep_cloud.txt",
        "sheep_fluffy.txt",
        "sheep_cotton.txt",
        "sheep_snowball.txt"
    ]

}


success=True


print("""
==============================
🚜 FARM INSPECTION REPORT
==============================
""")


# Check animals

for pen, animals in pens.items():

    location=os.path.join(
        ROOT,
        "farm",
        pen
    )


    if not os.path.exists(location):

        print(
            RED+
            f"✗ Missing pen: {pen}"
            +RESET
        )

        success=False
        continue


    found=os.listdir(location)


    missing=[
        animal for animal in animals
        if animal not in found
    ]


    if not missing:

        print(
            GREEN+
            f"✓ {pen} restored"
            +RESET
        )

    else:

        print(
            RED+
            f"✗ Missing from {pen}: {missing}"
            +RESET
        )

        success=False



# Check permissions

print("\nChecking pen security...")


for pen in pens:

    location=os.path.join(
        ROOT,
        "farm",
        pen
    )


    permissions=stat.S_IMODE(
        os.stat(location).st_mode
    )


    if permissions == 0o744:

        print(
            GREEN+
            f"✓ {pen} secured"
            +RESET
        )

    else:

        print(
            RED+
            f"✗ {pen} unsecured"
            +RESET
        )

        success=False



# Predator check

print("\nChecking predators...")


remaining_predators=[]


for root,dirs,files in os.walk(ROOT):

    for file in files:

        if any(
            predator in file
            for predator in [
                "fox",
                "coyote",
                "hawk",
                "raccoon"
            ]
        ):

            remaining_predators.append(file)



if len(remaining_predators) == 6:

    print(
        GREEN+
        "✓ Safe predators relocated"
        +RESET
    )

else:

    print(
        RED+
        "✗ Predators still lurking around.."
        +RESET
    )

    success=False



if success:

    print(
        GREEN+
"""
==============================
FARM RESTORED!
MISSION COMPLETE
==============================
"""
        +
        RESET
    )

else:

    print(
        RED+
"""
==============================
The farm still needs work.
==============================
"""
        +
        RESET
    )

'''


    with open(
        os.path.join(ROOT,"verify.py"),
        "w"
    ) as file:

        file.write(verify_code)


    print(
        f"{GREEN}✓ Verification system created{RESET}"
    )


## MAIN
#
print(
BLUE+
"""
=================================
🚜 FARM RESCUE MISSION
=================================
"""
+
RESET
)


create_folders()

scatter_animals()

create_predators()

create_verify()


print(
GREEN+
"""
=================================

Setup Complete!

Enter:

cd "Farm Rescue Mission"

When complete:

python3 verify.py

=================================
"""
+
RESET
)