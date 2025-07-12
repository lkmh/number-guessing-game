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


def get_user_guess() -> int:
    """Prompts the user to enter their guess and returns it as an integer.

    Returns:
        The user's guess as an integer.
    """
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
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


def play_game():
    """Main function to play the number guessing game."""
    min_range = 1
    max_range = 100

    while True:
        secret_number = generate_secret_number(min_range, max_range)
        guesses = 0
        guessed_correctly = False

        print(f"I'm thinking of a number between {min_range} and {max_range}.")

        while not guessed_correctly:
            guess = get_user_guess()
            guesses = track_guess(guesses)
            feedback = provide_feedback(guess, secret_number)
            print(feedback)

            if feedback == "You guessed it!":
                guessed_correctly = True
                print(f"It took you {guesses} guesses to win!")

        if not ask_to_play_again():
            break


if __name__ == "__main__":
    play_game()
