# 🚜 Farm Rescue Mission

## Emergency!

A powerful storm swept through our Farm last night.

The wind knocked down fences, damaged animal pens, and scattered animals across the property.

Some animals wandered into the wrong pens.

Others became lost in the woods, hills, lakes, and fields.

Even worse...

Predators have been spotted roaming the land.

The farmer needs your Linux skills to restore the farm before sunset!

---

# The Farm

Search every location on the property.

```
Farm/
├── farm/
│   ├── cows/
│   ├── pigs/
│   ├── chickens/
│   └── sheep/
├── woods/
├── hills/
├── lake/
└── fields/
```

Some locations have even more subfolders.

Don't assume the animals are nearby!

---

# 🐄 Mission 1: Rescue Every Animal

Twenty animals are missing.

Find every animal and return it to the correct pen.

| Animal | Correct Pen |
|---------|-------------|
| cow_* | farm/cows |
| pig_* | farm/pigs |
| chicken_* | farm/chickens |
| sheep_* | farm/sheep |

Some animals may have wandered into another animal's pen.

Others may be deep inside the woods, hills, lakes, or fields.

No animal should remain outside its proper pen.

---

# 🦊 Mission 2: Deal With Predators

Predators have also entered the property.

You'll encounter:

- 🦊 Foxes
- 🐺 Coyotes
- 🦝 Raccoons
- 🦅 Hawks

Each predator is a text file.

Read each file before deciding what to do.

### If the file contains food

Example:

```
berries
fish
corn
rabbit
```

The predator hasn't attacked any farm animals.

It should be **scared away** by moving it somewhere **outside the `farm` directory**.

---

### If the file contains the name of a farm animal

Example:

```
cow_bessie
```

or

```
pig_peppa
```

That predator attacked livestock.

It must be **removed** from the farm permanently.

---

# 🔒 Mission 3: Secure the Pens

Once every animal is safely home, repair the damaged pens.

Set permissions so that:

- 👨‍🌾 The farmer (owner) has full control.
- 👀 Everyone else can look inside the pen.
- 🚫 No one else can make changes.


Apply this to:

- farm/cows
- farm/pigs
- farm/chickens
- farm/sheep

---

# Mission Complete

Run

```bash
python3 verify.py
```

If everything is correct, you'll see a success message.

Good luck, Farmer!

The animals are counting on you.
