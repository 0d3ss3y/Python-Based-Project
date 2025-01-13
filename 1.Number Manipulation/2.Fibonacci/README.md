# Fibonacci Sequence Generator

## Overview

The **Fibonacci Sequence Generator** is a Python program that provides tools to work with the Fibonacci sequence. It allows users to generate the sequence up to a specified number of terms, find the Nth Fibonacci number, and visualize the growth of the sequence.

## Features

- **Generate Fibonacci Sequence**: Input the number of terms (N), and the program will generate the Fibonacci sequence up to the Nth term.
- **Find Nth Fibonacci Number**: Input a specific term number (N), and the program will return the corresponding Fibonacci number.

## Usage Details

### Generating the Sequence:

Input the number of terms, and the program will list the Fibonacci sequence up to that number.

#### Example:
```
Input: N = 10
Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Finding the Nth Fibonacci Number:

Input the desired term number (N), and the program will return the Fibonacci number at that position.

#### Example:
```
Input: N = 7
Output: 8
```

### Visualizing Growth:

The program generates a graphical representation of the sequence growth for the first N terms. The graph helps illustrate the exponential nature of Fibonacci numbers.

#### Example:

For N = 10, the program will display a line chart showing the values [0, 1, 1, 2, 3, 5, 8, 13, 21, 34].

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fibonacci-sequence-generator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd fibonacci-sequence-generator
   ```
3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the program:
   ```bash
   python fibonacci_generator.py
   ```
2. Select the desired operation:
   - Generate the sequence up to N terms.
   - Find the Nth Fibonacci number.
3. Follow the prompts to input the necessary data.

## Input Validation

The program ensures:

- N is a valid positive integer.
- Handles invalid or out-of-range inputs gracefully with error messages.


## Requirements

- Python 3.7 or later

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

---

Feel free to reach out with any questions or suggestions!
