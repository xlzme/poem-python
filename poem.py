import random

openers = [
    "In the quiet dawn,",
    "Beneath the moonlit sky,",
    "When the city finally sleeps,",
    "On a windy afternoon,"
]

subjects = [
    "a small hope",
    "a lonely streetlamp",
    "an old memory",
    "a paper boat"
]

actions = [
    "drifts through time,",
    "glows like a secret,",
    "turns into song,",
    "waits for morning,"
]

endings = [
    "and the world becomes softer.",
    "until the night lets go.",
    "as if it never hurt at all.",
    "with every breath you take."
]

opener = random.choice(openers)
subject = random.choice(subjects)
action = random.choice(actions)
ending = random.choice(endings)

poem = f"{opener} {subject} {action} {ending}"
print(poem)
