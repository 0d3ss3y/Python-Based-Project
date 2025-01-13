# Mastermind

## Overview

**Mastermind** is an interactive Python-based number guessing game. The program generates a random number within a specified range, and the player must guess the number. The program provides hints like "higher" or "lower" after each guess and tracks the number of attempts made.

## Features

- Randomly generates a number within a user-defined range.
- Provides hints after each guess to guide the player:
  - "Higher" if the guess is too low.
  - "Lower" if the guess is too high.
- Tracks the total number of attempts made by the player.
- Validates user input to ensure guesses are valid numbers within the range.

## Gameplay

1. Define the range for the random number (e.g., 1 to 100).
2. The program generates a random number within that range.
3. Enter guesses until the correct number is found.
4. After each guess, receive feedback and hints.
5. Once the number is guessed, the program displays the total attempts made.

### Example:

#### Input:
```
Welcome to Mastermind!
Guess a number between 1 and 50:
Enter your guess: 25
```

#### Output:
```
Too low! Try again.
Enter your guess: 40
Too high! Try again.
Enter your guess: 35
Correct! You guessed the number in 3 attempts.
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mastermind.git
   ```
2. Navigate to the project directory:
   ```bash
   cd mastermind
   ```
3. Install any required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the program:
   ```bash
   python mastermind.py
   ```
2. Follow the prompts to define the range and start guessing.
3. Use the hints provided after each guess to narrow down the number.

## Input Validation

The program ensures:

- The range is valid (start is less than end).
- Guesses are numeric and within the specified range.
- Handles invalid inputs gracefully by prompting the user to re-enter.

## Customization

- Modify the default range in the code for quicker testing.
- Add difficulty levels with predefined ranges (e.g., Easy: 1-50, Hard: 1-500).
- Enable a "play again" option after completing a round.

## Requirements

- Python 3.7 or later

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

---

Feel free to reach out with any questions or suggestions!
