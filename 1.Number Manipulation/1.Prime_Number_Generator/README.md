# Prime Number Generator

## Overview

The **Prime Number Generator** is a Python program designed to perform various operations related to prime numbers. It can:

1. Generate all prime numbers within a specified range.
2. Test whether a given number is a prime.
3. List the first N prime numbers.

This versatile tool is ideal for mathematical exploration and learning.

## Features

- **Find Prime Numbers in a Range**: Specify a start and end value to generate all primes within that range.
- **Check Primality**: Input a number to test if it is prime.
- **Generate First N Primes**: Provide a count to list the first N prime numbers.
- Efficient algorithms for fast computation.

## Usage Details

### Finding Primes in a Range:

Input a start and end value, and the program will list all prime numbers within that range.

#### Example:
```
Input: Start = 10, End = 50
Output: [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

### Testing for Primality:

Input a number, and the program will determine if it is a prime number.

#### Example:
```
Input: 29
Output: 29 is a prime number.

Input: 30
Output: 30 is not a prime number.
```

### Listing First N Primes:

Input the number of primes you want, and the program will list them in order.

#### Example:
```
Input: N = 10
Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/prime-number-generator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd prime-number-generator
   ```
3. Install any required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the program:
   ```bash
   python prime_generator.py
   ```
2. Select the desired operation:
   - Find primes in a range.
   - Test if a number is prime.
   - Generate the first N primes.
3. Follow the prompts to input the necessary data.

## Input Validation

The program ensures:

- Start and end values for ranges are valid integers, and start < end.
- Inputs for primality tests and counts are valid integers.
- Handles invalid or out-of-range inputs gracefully with error messages.

## Customization

- Modify the range limits or default values for quick testing.
- Implement additional features, such as prime factorization or twin prime detection.

## Requirements

- Python 3.7 or later

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to reach out with any questions or suggestions!
