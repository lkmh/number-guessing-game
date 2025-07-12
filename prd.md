PRD (Product Requirements Document): Number Guessing Game
1. Introduction
Project Name: Number Guessing Game
Goal: To provide a simple, interactive command-line number guessing game.
Target Audience: Anyone who enjoys simple number games.
2. User Stories
As a player, I want to be able to start a new game.
As a player, I want to be prompted to enter a number.
As a player, I want to be told if my guess is too high or too low.
As a player, I want to be told when I have guessed the number correctly.
As a player, I want to know how many guesses it took me to win.
As a player, I want to be able to play again after winning.
3. Features
Core Functionality:
The game generates a random secret number within a predefined range (e.g., 1 to 100).
The player is prompted to enter a guess.
The game provides feedback: "Too high!", "Too low!", or "You guessed it!"
The game tracks the number of guesses.
When the player guesses correctly, the game displays the number of guesses taken and asks if the player wants to play again.
Gameplay:
The player can make multiple guesses until they guess the correct number.
The range of numbers to guess can be configurable.
4. Technical Design
Language: Python
Console Output: Displays information to the user (e.g., prompts, feedback, results).
Random Number Generation: Use the random module to generate the secret number.
Testing: pytest
Linting/Formatting: ruff
5. Implementation Details
Range Configuration: The range (minimum and maximum values) for the secret number should be configurable via command-line arguments.
Game Loop: The game should be implemented as a loop that continues until the player guesses correctly.
Input Validation: Validate user input to ensure it's a valid number.
Error Handling: Handle potential errors gracefully (e.g., invalid input).
clear Game history This should clear out past games.
**6. Test (edge and cases coverage)
* Test on correct guesses to see if everything is working or not
* Test for the logic that if too low it says too low
* Test for non interger being input, what error does it return.
