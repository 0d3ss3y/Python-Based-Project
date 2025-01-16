# Inventory Management System

The **Inventory Management System** is a Python-based program designed to help users track and manage stock items. It includes functionality for checking inventory, tracking specific items, adding or removing stock, and identifying low-stock items.

---

## Features

### 1. **Track Item**
   - Search for a specific item by name.
   - View details such as category, current capacity, and maximum capacity.

### 2. **Check Inventory**
   - Display the complete list of items in inventory with their respective categories, current capacities, and maximum capacities.

### 3. **Stock Check**
   - Identify items that have fallen below 30% of their maximum capacity.
   - Provides a quick overview of low-stock items to prioritize restocking.

### 4. **Add Stock**
   - Add a specific amount of stock to an item.
   - Ensures stock does not exceed the maximum capacity.

### 5. **Pull Stock**
   - Remove a specific amount of stock from an item.
   - Prevents pulling more stock than what is currently available.

### 6. **Quit**
   - Exit the program gracefully.

---

## Usage

1. **Run the Program:**
   Execute the script using Python:
   ```bash
   python inventory_manager.py
