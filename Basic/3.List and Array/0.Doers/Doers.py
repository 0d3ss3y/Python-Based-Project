import os
from typing import Union, Any


def clear_terminal() -> Union[Any, None]:
    return os.system('cls' if os.name == 'nt' else 'clear')


def display_opt():
    try:
        options = ["Add", "Remove", "Show", "Exit"]
        print("__Option__:")

        for idx, opt in enumerate(options, start=1):
            print(f"{idx}. {opt}")

        action: int = int(input("Enter Number: "))

        if len(options)< action < 0:
            raise IndexError("Illegal input")
        else:
            return options[action-1]

    except IndexError as error:
        print(f"Error 404 - Not Found: {error}")
        return None


def add_item(tasks) -> list:
    pass


def remove_item(tasks) -> list:
    pass

def show_item(tasks):
    pass


def main():
    tasks = []
    clear_terminal()
    print("__Task Manager__")

    try:
        while True:
            option = display_opt()

            if option == "Add":
                tasks = add_item(tasks)
            elif option == "Remove":
                tasks = remove_item(tasks)
            elif option == "Show":
                show_item(tasks)
            else:
                raise SystemExit

    except (KeyboardInterrupt, SystemExit):
        print("\nExiting...")



if __name__ == '__main__':
    main()