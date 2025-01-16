import os
import sys
from time import sleep
from typing import Dict, Union


def clear_terminal():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def option() -> Union[str, None]:
    """Display menu options and return the user's choice."""
    try:
        options = ["Track Item", "Check Inventory", "Stock Check", "Add Stock", "Pull Stock", "Quit"]
        print("\n__Options__")
        for key, opt in enumerate(options, start=1):
            print(f"[{key}] {opt}")

        selection = int(input(f"Enter your selection [1-{len(options)}]: "))
        if 1 <= selection <= len(options):
            return options[selection - 1]
        else:
            raise ValueError("Selection out of range.")
    except ValueError as error:
        print(f"Invalid input: {error}")
        return None


def full_inventory(inventory: Dict):
    """Display the full inventory."""
    print("\n__Inventory Check__")
    for category, items in inventory.items():
        print(f"\nCategory: {category}")
        for item, details in items.items():
            max_cap = details['Max Capacity']
            curr_cap = details['Current Capacity']
            print(f"  {item}: Max {max_cap}, Current {curr_cap}")


def track_item(inventory: Dict):
    """Track a specific item."""
    try:
        item_name = input("Enter the item name to track: ").strip().title()
        found = False

        for category, items in inventory.items():
            if item_name in items:
                found = True
                details = items[item_name]
                print(f"\nCategory: {category}")
                print(f"  {item_name}: Max Capacity: {details['Max Capacity']}, Current Capacity: {details['Current Capacity']}")

        if not found:
            print(f"{item_name} not found in inventory.")
    except Exception as error:
        print(f"Error: {error}")


def stock_check(inventory: Dict):
    """Check for low stock items."""
    print("\n__Low Stock Items__")
    low_stock_threshold = 0.3
    found = False

    for category, items in inventory.items():
        for item, details in items.items():
            max_cap = details['Max Capacity']
            curr_cap = details['Current Capacity']
            if curr_cap <= max_cap * low_stock_threshold:
                found = True
                print(f"  {item} (Category: {category}) - Current: {curr_cap}, Max: {max_cap}")

    if not found:
        print("All items are sufficiently stocked.")


def adding_stock(inventory: Dict):
    """Add stock to an item."""
    try:
        item_name = input("Enter the item name to add stock: ").strip().title()
        found = False

        for category, items in inventory.items():
            if item_name in items:
                found = True
                details = items[item_name]
                max_cap = details['Max Capacity']
                curr_cap = details['Current Capacity']
                if curr_cap == max_cap:
                    print(f"{item_name} is already fully stocked.")
                    return

                print(f"Current Capacity: {curr_cap}, Max Capacity: {max_cap}")
                amount = int(input("Enter the amount to add: "))
                if curr_cap + amount > max_cap:
                    print(f"Cannot add {amount}. Exceeds max capacity by {curr_cap + amount - max_cap}.")
                else:
                    details['Current Capacity'] += amount
                    print(f"Added {amount} units to {item_name}. New Capacity: {details['Current Capacity']}")

        if not found:
            print(f"{item_name} not found in inventory.")
    except ValueError as error:
        print(f"Invalid input: {error}")


def remove_stock(inventory: Dict):
    """Remove stock from an item."""
    try:
        item_name = input("Enter the item name to pull stock: ").strip().title()
        found = False

        for category, items in inventory.items():
            if item_name in items:
                found = True
                details = items[item_name]
                curr_cap = details['Current Capacity']
                if curr_cap == 0:
                    print(f"{item_name} is out of stock.")
                    return

                print(f"Current Capacity: {curr_cap}")
                amount = int(input("Enter the amount to pull: "))
                if amount > curr_cap:
                    print(f"Cannot pull {amount}. Only {curr_cap} units available.")
                else:
                    details['Current Capacity'] -= amount
                    print(f"Pulled {amount} units from {item_name}. New Capacity: {details['Current Capacity']}")

        if not found:
            print(f"{item_name} not found in inventory.")
    except ValueError as error:
        print(f"Invalid input: {error}")


def main():
    """Main function to run the inventory system."""
    inventory = {
        "Electronics": {
            "Laptop": {"Max Capacity": 50, "Current Capacity": 30},
            "Smartphone": {"Max Capacity": 100, "Current Capacity": 80},
        },
        "Groceries": {
            "Apples": {"Max Capacity": 200, "Current Capacity": 50},
            "Bananas": {"Max Capacity": 150, "Current Capacity": 20},
        },
    }

    try:
        print("__Inventory Management System__\n")
        while True:
            selection = option()

            if selection == "Track Item":
                track_item(inventory)
            elif selection == "Check Inventory":
                full_inventory(inventory)
            elif selection == "Stock Check":
                stock_check(inventory)
            elif selection == "Add Stock":
                adding_stock(inventory)
            elif selection == "Pull Stock":
                remove_stock(inventory)
            elif selection == "Quit":
                print("Exiting the Inventory Management System. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

            sleep(1)
            clear_terminal()

    except (SystemExit, KeyboardInterrupt):
        print("\nExiting the Inventory Management System. Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
