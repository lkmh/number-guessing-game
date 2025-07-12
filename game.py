import argparse
import random


def generate_secret_number(min_range: int, max_range: int) -> int:
    """Generates a random secret number within the specified range.

    Args:
        min_range: The minimum value for the secret number.
        max_range: The maximum value for the secret number.

    Returns:
        A random integer within the specified range.
    """
    return random.randint(min_range, max_range)


def get_user_guess(min_range: int, max_range: int) -> int:
    """Prompts the user to enter their guess and returns it as an integer.

    Args:
        min_range: The minimum allowed value for the guess.
        max_range: The maximum allowed value for the guess.

    Returns:
        The user's guess as an integer.
    """
    while True:
        try:
            guess = int(
                input(f"Enter your guess (between {min_range} and {max_range}): ")
            )
            if min_range <= guess <= max_range:
                return guess
            else:
                print(
                    f"Your guess is out of range. Please enter a number between {min_range} and {max_range}."
                )
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def provide_feedback(guess: int, secret_number: int) -> str:
    """Provides feedback to the user based on their guess.

    Args:
        guess: The user's current guess.
        secret_number: The secret number to be guessed.

    Returns:
        A string indicating if the guess was 'Too high!', 'Too low!', or 'You guessed it!'.
    """
    if guess < secret_number:
        return "Too low!"
    elif guess > secret_number:
        return "Too high!"
    else:
        return "You guessed it!"


def track_guess(current_guesses: int) -> int:
    """Increments the current guess count.

    Args:
        current_guesses: The current number of guesses.

    Returns:
        The incremented guess count.
    """
    return current_guesses + 1


def ask_to_play_again() -> bool:
    """Asks the user if they want to play again.

    Returns:
        True if the user wants to play again, False otherwise.
    """
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def play_game(min_range: int, max_range: int):
    """Main function to play the number guessing game."""
    while True:
        secret_number = generate_secret_number(min_range, max_range)
        guesses = 0
        guessed_correctly = False

        print(f"I'm thinking of a number between {min_range} and {max_range}.")

        while not guessed_correctly:
            guess = get_user_guess(min_range, max_range)
            guesses = track_guess(guesses)
            feedback = provide_feedback(guess, secret_number)
            print(feedback)

            if feedback == "You guessed it!":
                guessed_correctly = True
                print(f"It took you {guesses} guesses to win!")

        if not ask_to_play_again():
            break


def parse_arguments():
    """Parses command-line arguments for min_range and max_range."""
    parser = argparse.ArgumentParser(description="Play the Number Guessing Game.")
    parser.add_argument(
        "--min",
        type=int,
        default=1,
        help="Minimum number for the guessing range (default: 1)",
    )
    parser.add_argument(
        "--max",
        type=int,
        default=100,
        help="Maximum number for the guessing range (default: 100)",
    )
    args = parser.parse_args()
    return args.min, args.max


if __name__ == "__main__":
    min_range, max_range = parse_arguments()
    play_game(min_range, max_range)
