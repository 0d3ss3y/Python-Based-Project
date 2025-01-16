# Shopping List Manager

## Overview

The **Shopping List Manager** is a Python program designed to help users manage their shopping items efficiently. It allows users to add items, calculate totals, apply discounts, and display the shopping list in a clear and organized manner.

## Features

- **Add Items**:
  - Add new items to the shopping list with details like name, price, and quantity.
  - Automatically updates existing items with new quantities and prices.
- **Calculate Total**:
  - Compute the total cost of items in the shopping list.
- **Apply Discount**:
  - Apply discounts to the total, including a lucky draw feature for store members.
  - Discounts range from 0% to 10%.
- **Display Shopping List**:
  - View all items in the shopping list with their quantities, prices, and subtotals.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/shopping-list-manager.git
   ```
2. Navigate to the project directory:
   ```bash
   cd shopping-list-manager
   ```
3. Run the program:
   ```bash
   python shopping_list_manager.py
   ```

## Usage

1. **Main Menu**:
   - The program displays a menu of options:
     - Add Item
     - Calculate Total
     - Apply Discount
     - Display List

2. **Adding Items**:
   - Input the item's name, price, and quantity when prompted.
   - Example:
     ```
     Enter item's name: Milk
     Enter item's price: 12.50
     Enter number of items: 2
     ```

3. **Calculating Total**:
   - Select the "Calculate Total" option to compute the current total of all items.
   - Example output:
     ```
     Current Total: 45.00
     ```

4. **Applying Discounts**:
   - Choose whether to use a store card.
   - If a store card is used, a lucky draw determines the discount percentage.
   - Example output:
     ```
     Lucky Draw
     Applying Discount of 5%
     Total: 42.75
     ```

5. **Displaying the Shopping List**:
   - View all items with their details.
   - Example output:
     ```
     [1]. 2x Milk per item is 12.50 so 25.00
     [2]. 1x Bread per item is 10.00 so 10.00
     ```

## Requirements

- Python 3.7 or later
- No additional dependencies

## Customization

- Extend the program to include categories or tags for items.
- Allow exporting the shopping list to a file (e.g., CSV or JSON).
- Implement additional discount rules or promotions.

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

---

Manage your shopping efficiently with the Shopping List Manager! Let me know if you have any questions or suggestions.
