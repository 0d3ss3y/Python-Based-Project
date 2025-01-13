# TempVertor

## Overview

**TempVertor** is a Python-based program designed to easily convert temperatures between Celsius, Fahrenheit, and Kelvin. With support for decimal points and negative temperatures, it ensures accurate conversions and robust input validation.

## Features

- Convert temperatures between:
  - Celsius to Fahrenheit and Kelvin
  - Fahrenheit to Celsius and Kelvin
  - Kelvin to Celsius and Fahrenheit
- Supports decimal and negative temperature inputs.
- Includes input validation to handle invalid or out-of-range inputs gracefully.

## Input Details

The program accepts:

- A numeric temperature value (e.g., `25`, `-40`, `100.5`).
- A unit of measurement for the input temperature: `C` (Celsius), `F` (Fahrenheit), or `K` (Kelvin).
- The desired target unit for conversion: `C`, `F`, or `K`.

## Output

The program displays the converted temperature value along with the input and output units for clarity.

### Example:

#### Input:
```
Temperature: 25
From Unit: C
To Unit: F
```

#### Output:
```
25°C is equal to 77°F
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tempvertor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd tempvertor
   ```
3. Install any required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the program:
   ```bash
   python tempvertor.py
   ```
2. Follow the prompts to enter:
   - Temperature value
   - Input unit (`C`, `F`, or `K`)
   - Target unit (`C`, `F`, or `K`)
3. View the converted temperature displayed in the console.

## Input Validation

The program ensures:

- The temperature value is a valid number.
- The input and target units are valid (`C`, `F`, or `K`).
- Kelvin temperatures are not negative (absolute zero limit).

If invalid input is provided, the program will display an error message and prompt the user to re-enter the data.

## Customization

- You can add more features or refine existing functionality by editing the main code file.
- The conversion formulas are clearly defined in the code, making it easy to modify or extend.

## Requirements

- Python 3.7 or later

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

---

Feel free to reach out with any questions or suggestions!
