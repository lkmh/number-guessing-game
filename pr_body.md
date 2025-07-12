This PR implements the core game logic for the Number Guessing Game and sets up the initial development environment.

**Summary:**
This PR introduces the fundamental game mechanics, including random number generation, user input handling, feedback (too high/too low/correct), and guess tracking. It also sets up the `requirements.txt` and updates `GEMINI.md` with new guidelines.

**Motivation:**
This is the first major feature implementation, addressing the core functionality outlined in the PRD and establishing best practices for future development.

**Detailed Changes:**
- `game.py`: Contains the `generate_secret_number`, `get_user_guess`, `provide_feedback`, `track_guess`, and `play_game` functions.
- `test_game.py`: Unit tests for `generate_secret_number`, `provide_feedback`, and `track_guess`.
- `requirements.txt`: Lists `ruff` and `pytest` as project dependencies.
- `GEMINI.md`: Updated to include guidelines for `requirements.txt` management and explicit ruff linting instructions.
- `plan.md`: Initial high-level development plan.

**Testing Details:**
- Unit tests in `test_game.py` cover the core functions.
- Local checks (`ruff check .`, `ruff format .`, `pytest`) were run and passed successfully using `python3.12 -m pytest` to address environment-specific issues.

**High-Level Plan:**
## High-Level Plan: Number Guessing Game Development

### 1. Description
This plan outlines the development process for the Number Guessing Game, focusing on core functionality, user interaction, and adherence to quality standards.

### 2. Proposed Technical Approach
The game will be developed in Python, utilizing the `random` module for number generation. `pytest` will be used for testing, and `ruff` for linting and formatting to ensure code quality.

### 3. Identified Subtasks (GitHub Issues)
Based on the PRD, the development will be broken down into the following key subtasks, each corresponding to a GitHub issue:

#### Subtask 1: Implement Core Game Logic
*   **Description:** Implement the fundamental game mechanics, including generating a random secret number, handling user input for guesses, providing feedback (too high, too low, correct), and tracking the number of guesses.
*   **Acceptance Criteria:**
    *   Game generates a random number within a default range (e.g., 1-100).
    *   Player is prompted for input.
    *   Game provides correct feedback for too high, too low, and correct guesses.
    *   Game accurately tracks and displays the number of guesses.

#### Subtask 2: Develop Game Flow and Replay Functionality
*   **Description:** Establish the overall game flow, allowing players to start a new game, play multiple rounds, and providing an option to play again after winning.
*   **Acceptance Criteria:**
    *   Game starts correctly.
    *   Game loop continues until the correct number is guessed.
    *   After winning, the player is asked if they want to play again.
    *   Game can be restarted for a new round.

#### Subtask 3: Add Input Validation and Error Handling
*   **Description:** Implement robust validation for user input to ensure it's a valid number and handle non-numeric or out-of-range inputs gracefully.
*   **Acceptance Criteria:**
    *   Non-numeric input is rejected with an informative error message.
    *   Input outside the defined range is handled appropriately (e.g., warning or rejection).
    *   Game does not crash due to invalid input.

#### Subtask 4: Set up Configuration and Testing Environment
*   **Description:** Make the number guessing range configurable (e.g., via command-line arguments) and set up the testing framework (`pytest`) and linting/formatting tool (`ruff`).
*   **Acceptance Criteria:**
    *   Game range can be specified via command-line arguments.
    *   `pytest` is configured and runs tests successfully.
    *   `ruff` is configured and can check/format code.
    *   Basic tests for core functionality are present.
