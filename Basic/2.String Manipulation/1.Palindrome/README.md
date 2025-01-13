# Palindrome Checker

## Overview

The **Palindrome Checker** is a Python program that allows users to verify whether a word, phrase, or sentence is a palindrome. It also identifies palindromic words in larger text inputs. The program ignores spaces, punctuation, and capitalization to ensure accurate palindrome detection.

## Features

- **Palindrome Validation**:
  - Check if a word, sentence, or phrase is a palindrome.
- **Palindromic Word Finder**:
  - Identify individual palindromic words in a given text.
- **User-Friendly Menu**:
  - Simple interface to select functionality.

## How It Works

1. **Input Processing**:
   - Users can input any text (e.g., single word, phrase, or sentence).
   - Program sanitizes the input by removing non-alphanumeric characters and converting it to lowercase.

2. **Palindrome Check**:
   - Reverses the sanitized text and compares it to the original.

3. **Word Analysis**:
   - Splits the input text into individual words.
   - Identifies and returns words that are palindromes.

## Usage Details

### Menu Options

- **Option 1**: Check if a word or sentence is a palindrome.
- **Option 2**: Find all palindromic words in a sentence.

### Examples

#### Option 1: Palindrome Validation
```
Input: "A man, a plan, a canal, Panama"
Output: "The text is a palindrome."

Input: "Hello World"
Output: "The text is not a palindrome."
```

#### Option 2: Palindromic Word Finder
```
Input: "Madam Arora teaches malayalam."
Output: "Palindromic words found: Madam, Arora, malayalam"

Input: "This is a test."
Output: "No palindromic words found in the text."
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/palindrome-checker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd palindrome-checker
   ```
3. Run the program:
   ```bash
   python palindrome_checker.py
   ```

## Requirements

- Python 3.7 or later

## Example Code Snippet

```python
import re

def is_palindrome(text: str) -> bool:
    sanitized = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return sanitized == sanitized[::-1]

def find_palindromes(text: str):
    words = text.split()
    return [word for word in words if is_palindrome_word(word)]

def is_palindrome_word(word: str) -> bool:
    return word == word[::-1]

text = "Madam Arora teaches malayalam."
print("Palindromic words:", find_palindromes(text))
```

## Customization

- Extend the program to handle multilingual text.
- Include more advanced palindrome analysis (e.g., phrases within phrases).
- Add a GUI for enhanced interactivity.

## Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.


---

Feel free to reach out with any questions or suggestions!
