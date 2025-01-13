import sys

# Valid commands and operators
valid_commands = ["memory", "recall"]
valid_operators = ["*", "/", "+", "-"]

memory = 0

def save_memory(result):
    global memory
    memory = result


def clear_memory():
    global memory
    memory = 0


def handle_operations(expression):
    """
    Handle mathematical operations or memory commands.
    """
    global memory

    if expression in valid_commands:
        if expression.lower() == "clear":
            clear_memory()
            return None
        elif expression.lower() == "recall":
            print(f"Recalled value from memory: {memory}")
            return memory
    else:
        # Parse and evaluate a mathematical expression
        num_1 = float(expression[0])
        operator = expression[1]
        num_2 = float(expression[2])

        if operator in valid_operators:
            match operator:
                case "*":
                    return num_1 * num_2
                case "/":
                    return num_1 / num_2
                case "+":
                    return num_1 + num_2
                case "-":
                    return num_1 - num_2


def validate_input(express):
    """
    Validate input characters.
    """
    if express in valid_operators or express.isdigit() or express in valid_commands:
        return True
    return False


def rules():
    """
    Display usage rules.
    """
    print("\nWelcome to the Calculator!")
    print("Commands:")
    print("  - Enter basic arithmetic expressions (e.g., 2+3, 4*5).")
    print("  - Result if the arithmetic expression is stored automatically within memory.")
    print("  - Use 'Clear' to clear the memory.")
    print("  - Use 'Recall' to retrieve the stored memory value.")
    print("  - Press Ctrl+C or enter 'exit' to quit.\n")


def get_input():
    """
    Get user input and validate it.
    """
    expression = input("Enter expression or command: ").strip()

    if expression.lower() == "exit":
        print("Goodbye!")
        sys.exit()

    if expression in valid_commands:
        return expression

    # Ensure the expression is valid
    if len(expression) == 3 and validate_input(expression[0]) and validate_input(expression[1]) and validate_input(expression[2]):
        return expression
    else:
        print("Error: Invalid Entry. Please follow the rules.")
        return None


def main():
    """
    Main function to run the calculator.
    """
    global memory
    rules()
    while True:
        expression = get_input()
        if not expression:
            continue

        result = handle_operations(expression)
        if result is not None:
            print(f"Result: {result}\n")
            memory = result
            print(f"Memory Saved.")


if __name__ == '__main__':
    main()
