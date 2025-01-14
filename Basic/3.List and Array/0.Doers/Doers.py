import os
from time import sleep
from typing import List, Optional


def clear_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def display_opt() -> Optional[str]:
    options = ["Add", "Remove", "Show", "Exit"]
    print("__Options__:")

    for idx, opt in enumerate(options, start=1):
        print(f"[{idx}]. {opt}")

    try:
        action = int(input("Enter Number: "))
        if 1 <= action <= len(options):
            return options[action - 1]
        else:
            raise ValueError("Invalid choice.")
    except (ValueError, IndexError):
        print("Invalid input! Please try again.")
        return None


def set_priority() -> str:
    levels = ["emergency", "high", "medium", "low"]
    print("Priority Levels:")
    for idx, level in enumerate(levels, start=1):
        print(f"[{idx}]. {level.capitalize()}")

    while True:
        try:
            choice = input("Enter Priority [Number/Description]: ").lower()
            if choice.isdigit() and 1 <= int(choice) <= len(levels):
                return levels[int(choice) - 1]
            elif choice in levels:
                return choice
            else:
                raise ValueError("Invalid priority level.")
        except ValueError as e:
            print(e)


def add_item(tasks: List[Optional[str]]) -> List[Optional[str]]:
    task = input("Enter Task: ").strip()
    if not task:
        print("Task cannot be empty!")
        return tasks

    priority = set_priority()
    positions = {
        "emergency": [0],
        "high": range(1, 4),
        "medium": range(4, 7),
        "low": range(7, 10),
    }

    for pos in positions[priority]:
        if tasks[pos] == " ":
            tasks[pos] = task
            print(f"Task '{task}' added to {priority.capitalize()} priority.")
            return tasks

    print(f"No available slots in {priority.capitalize()} priority.")
    return tasks


def remove_item(tasks: List[Optional[str]]) -> List[Optional[str]]:
    print("Select Priority to Remove From:")
    categories = ["Emergency", "High", "Medium", "Low"]
    for idx, cat in enumerate(categories, start=1):
        print(f"[{idx}]. {cat}")

    try:
        priority_idx = int(input("Enter Priority Index: "))
        if 1 <= priority_idx <= len(categories):
            category = categories[priority_idx - 1].lower()
            positions = {
                "emergency": [0],
                "high": range(1, 4),
                "medium": range(4, 7),
                "low": range(7, 10),
            }[category]

            print(f"Tasks in {category.capitalize()} Priority:")
            for idx in positions:
                if tasks[idx] != " ":
                    print(f"[{idx}] {tasks[idx]}")

            task_idx = int(input("Enter Task Index to Remove: "))
            if task_idx in positions and tasks[task_idx] != " ":
                print(f"Removing Task: {tasks[task_idx]}")
                tasks[task_idx] = " "
            else:
                print("Invalid Task Index.")
        else:
            raise ValueError("Priority index out of range.")
    except (ValueError, IndexError):
        print("Invalid input!")
    return tasks


def show_item(tasks: List[Optional[str]]) -> None:
    categories = {
        "Emergency": [0],
        "High": range(1, 4),
        "Medium": range(4, 7),
        "Low": range(7, 10),
    }

    for category, positions in categories.items():
        print(f"{category}:")
        for pos in positions:
            task = tasks[pos]
            if task != " ":
                print(f"  [{pos}] {task}")
            else:
                print(f"  [{pos}] - Empty")
        print()


def main():
    tasks = [" " for _ in range(10)]
    clear_terminal()
    print("__Task Manager__")

    while True:
        option = display_opt()
        if option == "Add":
            tasks = add_item(tasks)
        elif option == "Remove":
            tasks = remove_item(tasks)
        elif option == "Show":
            show_item(tasks)
        elif option == "Exit":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")
        sleep(1)
        clear_terminal()


if __name__ == '__main__':
    main()
