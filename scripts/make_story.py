import sys
import random

title = open(sys.argv[1], encoding="utf-8").read().strip()

intros = [
    "Everything started in a way that seemed completely normal.",
    "At first, no one thought this would turn into a real problem.",
    "It looked like just another ordinary situation."
]

developments = [
    "As time went on, the tension slowly started to build.",
    "Small decisions began to have serious consequences.",
    "What seemed minor at first quickly escalated."
]

climaxes = [
    "The turning point changed everything.",
    "The truth came out in an unexpected way.",
    "That moment completely shifted the situation."
]

endings = [
    "In the end, the lesson was impossible to ignore.",
    "The experience changed how everything was viewed.",
    "Nothing felt the same after that moment."
]

extra = [
    "Looking back, the signs were always there.",
    "At the time, emotions mattered more than logic.",
    "Not every decision is right, but every decision teaches something."
]

story = (
    f"{random.choice(intros)} "
    f"The situation can be summed up like this: {title}. "
    f"{random.choice(developments)} "
    f"{random.choice(climaxes)} "
    f"{random.choice(endings)} "
    + " ".join(random.sample(extra, 3))
)

print(story)
