# from random import randint
import random


DIFFICULTY = [("Easy", 10), ("Medium", 5), ("Hard", 3)]


def _input_int(message: str = "", bound: tuple[int, int] | None = None) -> int:
    while True:
        s = input(message).strip()
        try:
            integer = int(s)
        except ValueError:
            print(f"Invalid input, {s} is not an integer.")
            continue
        if bound and not bound[0] <= integer <= bound[1]:
            print(f"Invalid input, {integer} isn't in the range {list(bound)} (including both end points).")
            continue
        return integer


def set_difficulty_level() -> int:
    print("Please select the difficulty level:")
    for i, (level, chances) in enumerate(DIFFICULTY, 1):
        print(f"{i}. {level} ({chances} chances)")
    print()
    choice = _input_int("Enter your choice: ", (1, len(DIFFICULTY)))
    level, chances = DIFFICULTY[choice - 1]
    print()
    print(
        f"Great! You have selected the {level} difficulty level. You have {chances} chances.\nLet's start the game!\n"
    )
    return chances


def guess(secret: int, chances: int) -> None:
    for i in range(chances):
        answer = _input_int("Enter your guess: ")
        if answer == secret:
            print(f"Congratulations! You guessed the correct number in {i + 1} attempts.")
            break
        if answer < secret:
            print(f"Incorrect! The number is greater than {answer}")
        else:
            print(f"Incorrect! The number is less than {answer}")
    else:
        print(f"Sorry, you have run out of chances! The secret number is {secret}.")


def play_game() -> None:
    print(
        "Welcome to the Number Guessing Game!\n"
        "I'm thinking of a number between 1 and 100.\n"
        "You have several chances to guess the correct number.\n"
    )
    chances = set_difficulty_level()
    secret_number = random.randint(1, 100)
    guess(secret_number, chances)
