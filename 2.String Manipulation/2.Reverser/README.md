# String Reverser

## Overview

The **String Reverser** is a Python program designed to reverse strings while maintaining the integrity of capitalization and special characters. It can reverse individual words, entire sentences, or both, providing a versatile tool for text manipulation.

## Features

- **Reverse Words**:
  - Reverse the letters in each word individually.
  - Maintain original capitalization and punctuation.
- **Reverse Sentences**:
  - Reverse the order of words in a sentence.
  - Preserve the capitalization of the first letter and punctuation placement.
- **Handle Special Characters**:
  - Retain non-alphabetic characters (e.g., `!`, `?`, `@`) in their original positions.

## Usage Details

### Reversing Words:

Input a single word or a sentence, and the program will reverse each word individually while maintaining its capitalization and special characters.

#### Example:
```
Input: Hello, World!
Output: Olleh, Dlrow!
```

### Reversing Sentences:

Input a sentence, and the program will reverse the order of the words while preserving punctuation and capitalization.

#### Example:
```
Input: Hello, World!
Output: World! Hello,
```

### Combined Mode:

Reverse both the letters in words and the order of the words.

#### Example:
```
Input: Hello, World!
Output: ,Olleh !Dlrow
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/string-reverser.git
   ```
2. Navigate to the project directory:
   ```bash
   cd string-reverser
   ```
3. Run the program:
   ```bash
   python string_reverser.py
   ```

## Input Validation

The program ensures:

- Handles empty input gracefully.
- Preserves non-alphabetic characters and spaces.
- Handles mixed-case input appropriately.

## Customization

- Add options for ignoring capitalization or special characters.
- Extend functionality to support reversing multi-line text inputs.
- Include a graphical user interface (GUI) for improved usability.

## Requirements

- Python 3.7 or later

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

---

Feel free to reach out with any questions or suggestions!