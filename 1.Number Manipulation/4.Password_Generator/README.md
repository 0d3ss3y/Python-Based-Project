# Random Password Generator

## Overview

The **Random Password Generator** is a Python program designed to create secure and random passwords. It supports generating passwords of specified lengths, including a mix of letters, numbers, and special characters, ensuring robust password security.

## Features

- **Generate Passwords**:
  - Create passwords with a customizable length (8 to 16 characters).
  - Ensure each password contains letters, numbers, and special characters.
- **Suggested Passwords**:
  - Quickly generate a strong 16-character password.
- **Custom Passwords**:
  - Specify a password length and generate a personalized password.
- **Interactive Interface**:
  - User-friendly command-line prompts for seamless interaction.

## Code Details

### Core Functions

1. **`numbers()`**: Generates a random numeric character.
2. **`letters()`**: Generates a random letter (uppercase or lowercase).
3. **`specials()`**: Generates a random special character from a predefined set.
4. **`generate_pwd(length)`**: Creates a random password of specified length, ensuring a mix of character types.
   - Minimum length requirement: 8 characters.
   - Includes at least one letter, number, and special character.
5. **`suggested_password()`**: Generates a 16-character password as a default suggestion.
6. **`custom_pwd()`**: Allows the user to input a custom password length and generate a corresponding password.

### User Interaction

- The program provides a suggested password upon launch.
- Users can choose to generate their own password with a length of their choice.
- Ensures input validation for password length and provides error messages for invalid entries.

## Example Usage

1. Run the program:
   ```bash
   python password_generator.py
   ```
2. View the suggested password:
   ```
   Suggested Password: aB1!xY9&Q3*pTz@
   ```
3. Choose to generate a custom password:
   ```
   Input: y
   How long do you want your password to be? (minimum 8, maximum 16): 12
   Your Custom Password: X@9qWr5!ZvP3
   ```
4. Accept the suggested password:
   ```
   Input: n
   Password confirmed: aB1!xY9&Q3*pTz@
   ```

## Input Validation

- Ensures password length is between 8 and 16 characters.
- Handles non-numeric and out-of-range inputs gracefully.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/random-password-generator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd random-password-generator
   ```
3. Run the program:
   ```bash
   python password_generator.py
   ```

## Customization

- Modify the `specials()` function to include/exclude specific special characters.
- Adjust the password length limits in the `custom_pwd()` function.
- Extend the program to save generated passwords securely to a file.

## Requirements

- Python 3.7 or later

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

---