# Basic Calculator

## Overview

The **Basic Calculator** is a Python program that performs fundamental arithmetic operations, supports memory functions, and handles decimal numbers. It is a simple yet versatile tool for quick calculations.

## Features

- **Basic Arithmetic Operations**:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
- **Memory Functions**:
  - Save a result to memory.
  - Recall the saved value from memory.
  - Clear memory.
- **Decimal Support**:
  - Perform calculations with decimal numbers for precise results.

## Usage Details

### Performing Calculations:

Input two numbers and an operation to perform basic arithmetic.

#### Example:
```
Input: 5 + 3
Output: 8

Input: 7.5 / 2.5
Output: 3.0
```

### Using Memory Functions:

- **Save to Memory**: Store the current result in memory.
- **Recall from Memory**: Retrieve the saved value.
- **Clear Memory**: Erase the stored value.

#### Example:
```
Input: 15 * 2
Output: 30

Memory Saved.
Input: Recall Memory
Output: 30

Input: Clear Memory
Output: Memory Cleared.
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/basic-calculator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd basic-calculator
   ```
3. Install any required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the program:
   ```bash
   python calculator.py
   ```
2. Follow the prompts to input numbers and select operations.
3. Use memory functions as needed to store and retrieve results.

## Input Validation

The program ensures:

- Numbers are valid integers or decimals.
- Division by zero is not allowed.
- Handles invalid operations gracefully by displaying error messages.

## Customization

- Extend the program to include advanced operations (e.g., exponentiation, square root).
- Add a graphical user interface (GUI) for improved usability.

## Requirements

- Python 3.7 or later

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

---

Feel free to reach out with any questions or suggestions!
