# Restaurant Bill Calculator

## Overview

The **Restaurant Bill Calculator** is a Python program that helps you calculate the total cost of a meal, including tax and tip, and allows you to split the bill among multiple people. It supports customizable tip percentages and ensures accurate calculations.

## Features

- Calculate:
  - Subtotal of the meal
  - Tax based on a configurable tax rate
  - Tip based on a percentage chosen by the user
- Split the bill evenly among multiple people.
- Handles flexible tip percentages.
- Validates user inputs for amounts, percentages, and the number of people.

## Input Details

The program collects the following inputs:

1. **Meal Subtotal**: The total cost of the meal before tax and tip.
2. **Tax Rate**: A percentage representing the applicable tax rate.
3. **Tip Percentage**: A percentage for the tip (e.g., 10%, 15%, 20%).
4. **Number of People**: The number of people splitting the bill.

## Output

The program calculates and displays:

- Subtotal
- Tax amount
- Tip amount
- Total amount (Subtotal + Tax + Tip)
- Amount owed per person (if splitting the bill)

### Example:

#### Input:
```
Meal Subtotal: $100.00
Tax Rate: 8%
Tip Percentage: 15%
Number of People: 4
```

#### Output:
```
Subtotal: $100.00
Tax: $8.00
Tip: $15.00
Total: $123.00
Each person owes: $30.75
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/restaurant-bill-calculator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd restaurant-bill-calculator
   ```
3. Install any required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the program:
   ```bash
   python bill_calculator.py
   ```
2. Follow the prompts to enter:
   - Meal subtotal
   - Tax rate
   - Tip percentage
   - Number of people splitting the bill
3. View the calculated results displayed in the console.

## Input Validation

The program ensures:

- Subtotal, tax rate, and tip percentage are valid numbers.
- Number of people is a valid positive integer.
- Handles edge cases like splitting between one person or zero tip percentage.

If invalid input is provided, the program will display an error message and prompt the user to re-enter the data.

## Customization

- You can modify the default tax rate or suggest common tip percentages within the code.
- The program can be extended to include additional features like discounts or service charges.

## Requirements

- Python 3.7 or later

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to reach out with any questions or suggestions!
