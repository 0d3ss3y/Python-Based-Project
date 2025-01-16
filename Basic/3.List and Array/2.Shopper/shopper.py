import random


def options():
    """Display menu options and get the user's choice."""
    try:
        option = ["Add Item", "Calculate Total", "Apply Discount", "Display List"]
        print("\n__Options__\n")
        for key, opt in enumerate(option, start=1):
            print(f"[{key}] {opt}")
        selection = int(input("\nSelect an option: "))
        if 1 <= selection <= len(option):
            return option[selection - 1]
        else:
            raise ValueError("Selection out of range.")
    except ValueError as error:
        print(f"Invalid input: {error}")
        return None


def add_item(shopping_list):
    """Add an item to the shopping list."""
    try:
        item_name = input("Enter item name: ").strip().capitalize()
        item_price = float(input("Enter item price: "))
        item_count = int(input("Enter item count: "))

        if item_name not in shopping_list:
            subtotal = item_price * item_count
            shopping_list[item_name] = {
                "Count": item_count,
                "Price": item_price,
                "SubTotal": subtotal,
            }
        else:
            shopping_list[item_name]["Count"] += item_count
            shopping_list[item_name]["SubTotal"] = (
                shopping_list[item_name]["Count"] * shopping_list[item_name]["Price"]
            )
        print(f"Item '{item_name}' added/updated successfully.")
    except ValueError:
        print("Invalid input. Please enter numeric values for price and count.")


def calculate_total(shopping_list):
    """Calculate and display the total cost."""
    total = sum(item["SubTotal"] for item in shopping_list.values())
    print(f"\nCurrent Total: {total:.2f}")
    return total


def apply_discount(total):
    """Apply a discount to the total based on membership or lucky draw."""
    try:
        store_member = int(input("Do you have a store card? [0 for No, 1 for Yes]: "))
        if store_member not in [0, 1]:
            raise ValueError("Invalid input. Enter 0 or 1.")

        if store_member == 1:
            discount_percentage = 0.08
            print(f"Applying member discount of {discount_percentage * 100:.0f}%.")
        else:
            print("Lucky Draw activated!")
            random_discount = random.randint(0, 10)
            if random_discount == 0:
                print("Congratulations! You won the grand prize. Total is now 0.00!")
                return 0.00
            discount_percentage = random_discount / 100
            print(f"Applying lucky draw discount of {discount_percentage * 100:.0f}%.")

        discount_amount = total * discount_percentage
        total -= discount_amount
        print(f"Discount applied. Total after discount: {total:.2f}")
        return total
    except ValueError as error:
        print(f"Invalid input: {error}")
        return total


def display_shopping_list(shopping_list):
    """Display the shopping list."""
    if not shopping_list:
        print("Shopping list is empty.")
        return

    print("\n__Shopping List__")
    for idx, (item, details) in enumerate(shopping_list.items(), start=1):
        print(
            f"[{idx}] {details['Count']} x {item} @ {details['Price']:.2f} each = {details['SubTotal']:.2f}"
        )


def main():
    """Main function to run the shopping list program."""
    print("__Shopping List__")
    shopping_list = {
        "Bread": {"Count": 1, "Price": 13.45, "SubTotal": 13.45},
        "Coke": {"Count": 6, "Price": 23.99, "SubTotal": 143.94},
    }
    total = 0.00

    while True:
        choice = options()
        if choice == "Add Item":
            add_item(shopping_list)
        elif choice == "Calculate Total":
            total = calculate_total(shopping_list)
        elif choice == "Apply Discount":
            total = apply_discount(total)
        elif choice == "Display List":
            display_shopping_list(shopping_list)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()