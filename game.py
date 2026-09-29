import random


def play_guessing_game():
    """Play a simple number guessing game."""

    secret_number = random.randint(1, 10)
    attempts = 3

    print("\nI have chosen a number between 1 and 10.")
    print(f"You have {attempts} attempts to guess it.")

    for attempt in range(1, attempts + 1):
        user_input = input(f"Attempt {attempt}: ")

        try:
            guess = int(user_input)

            if guess == secret_number:
                print("Correct! You guessed the number!\n")
                return

            if guess < secret_number:
                print("Too low!")

            else:
                print("Too high!")

        except ValueError:
            print("Please enter a whole number.")

    print(f"Game over! The number was {secret_number}.\n")


def get_game_help():
    """Return instructions for the guessing game."""
    return (
        "Guessing game: I choose a number from 1 to 10. "
        "You get 3 attempts to guess it."
    )