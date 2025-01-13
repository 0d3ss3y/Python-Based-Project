# Acronym Generator

## Overview

The **Acronym Generator** is a Python program designed to create acronyms from phrases. It supports multiple customization options, allowing users to define specific rules for generating acronyms, such as including or excluding certain words or customizing the capitalization format.

## Features

- **Generate Acronyms**:
  - Create acronyms from multi-word phrases.
  - Automatically extract the first letter of each word.
- **Custom Rules**:
  - Exclude predefined words (e.g., articles like "a," "an," "the").
  - Customize capitalization (uppercase, lowercase, or mixed case).
- **Handle Special Characters**:
  - Remove special characters while forming the acronym.
  - Retain valid letters and spaces from the input phrase.

## Usage Details

### Generating Acronyms:

Input a phrase, and the program will generate an acronym based on the default or user-defined rules.

#### Example 1 (Default Rules):
```
Input: National Aeronautics and Space Administration
Output: NASA
```

#### Example 2 (Custom Rules):
```
Input: Hypertext Markup Language
Rules: Lowercase Acronym
Output: html
```

### Customization:

1. Exclude words such as "and," "of," "the."
2. Modify output format to:
   - All uppercase.
   - All lowercase.
   - First letter uppercase.
3. Specify separators for multi-word acronyms (e.g., `N-A-S-A`).

#### Example:
```
Input: Portable Network Graphics
Rules: Uppercase, Separator = "-"
Output: P-N-G
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/acronym-generator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd acronym-generator
   ```
3. Run the program:
   ```bash
   python acronym_generator.py
   ```

## Input Validation

The program ensures:

- Handles empty input gracefully.
- Strips special characters and extra spaces from the input phrase.
- Supports input phrases with varying case and spacing.

## Customization

- Extend to support language-specific rules (e.g., handling non-English articles).
- Add options for outputting acronyms in multiple formats (e.g., JSON, CSV).
- Include a graphical user interface (GUI) for enhanced user experience.

## Requirements

- Python 3.7 or later

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

---

Feel free to reach out with any questions or suggestions!
