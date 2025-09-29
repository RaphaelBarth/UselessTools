import random

TEXT = 0
AUTHOR = 1
COLOR = 2

phrases = [
    {
        TEXT: f"you got hacked !!\n pay {random.randint(0,1_000_000)}$ to get pack your computer",
        AUTHOR: "Anonymous Hacker",
        COLOR: "red",
    },
    {
        TEXT: "The monkey and the banana decided\nto switch places for a day,\nand chaos ensued in the jungle!",
        AUTHOR: "DeereAI",
        COLOR: "yellow",
    },
    {
        TEXT: "If you are not coffee,\nchocolate or bacon,\nI'm going to need you to go away",
        AUTHOR: "unknown",
        COLOR: "chocolate3",
    },
    {
        TEXT: "Water on Mars? Not impressed.\nBaywatch on Mars? Impressed.",
        AUTHOR: "Michael Ian Black",
        COLOR: "dodger blue",
    },
    {
        TEXT: "I told my computer I needed a break,\nand now it won't stop sending me to the beach.",
        AUTHOR: "Techie Humor",
        COLOR: "light sea green",
    },
    {
        TEXT: "Why don't scientists trust atoms?\nBecause they make up everything!",
        AUTHOR: "Science Jokes",
        COLOR: "medium orchid",
    }
]


def get_random_phrase() -> dict[int, str]:
    size = len(phrases) - 1
    index = random.randint(0, size)
    return phrases[index]
