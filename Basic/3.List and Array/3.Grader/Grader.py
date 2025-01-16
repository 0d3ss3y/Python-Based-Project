import os
import sys
from time import sleep
from typing import Union, Any

report_card = {
    "Alice Johnson": {
        "Math": 85,
        "Science": 90,
        "English": 88,
        "History": 78,
        "Programming": 92,
        "Average": 86.6,
        "Letter" : "A+"
    },
    "Bob Smith": {
        "Math": 79,
        "Science": 82,
        "English": 74,
        "History": 85,
        "Programming": 80,
        "Average": 80.0,
        "Letter" : "A+"
    },
    "Catherine Lee": {
        "Math": 92,
        "Science": 89,
        "English": 91,
        "History": 87,
        "Programming": 95,
        "Average": 90.8,
        "Letter": "A+"
    },
    "David Brown": {
        "Math": 68,
        "Science": 72,
        "English": 75,
        "History": 70,
        "Programming": 65,
        "Average": 70.0,
        "Letter": "A"
    },
    "Eva Martinez": {
        "Math": 88,
        "Science": 85,
        "English": 87,
        "History": 84,
        "Programming": 90,
        "Average": 86.8,
        "Letter": "A+"
    },
    "Franklin Harris": {
        "Math": 95,
        "Science": 93,
        "English": 96,
        "History": 89,
        "Programming": 94,
        "Average": 93.4,
        "Letter": "A+"
    },
    "Grace Patel": {
        "Math": 78,
        "Science": 80,
        "English": 82,
        "History": 76,
        "Programming": 79,
        "Average": 79.0,
        "Letter": "A"
    },
}


def clear_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')


def option() -> Union[str,Any]:
    try:
        options = ["Store Grades", "Calculate Average", "Determine Letter","Display Grades","Quit"]

        for key, opt in enumerate(options):
            print(f"[{key}]. {opt}")

        selection = int(input(f"Enter your selection [1-{len(options)}]: "))

        if 1 <= selection <= len(options):
            return options[selection - 1]
        else:
            raise ValueError(f"Illegal Section {selection}")
    except ValueError as error:
        print(f"Error 404 - Not Found: {error}")
        return None


def display_grades():
    for learner,grades in report_card.items():
        print(f"{learner}'s Report Card")
        for subject, grade in grades.items():
            print(f"{subject}: {grade}")


def main():
    try:
        print("__Grade System__\n")

        while True:
            selection = option()

            if selection == "Store Grades":
                pass
            elif selection == "Calculate Average":
                pass
            elif selection == "Determine Letter":
                pass
            elif selection == "Display Grades":
                display_grades()
            elif selection == "Quit":
                raise SystemExit(0)
            else:
                raise ValueError(f"Illegal Section")

            sleep(0.5)
            clear_terminal()

    except(SystemExit, KeyboardInterrupt):
        print("Bye Bye...!")
        sys.exit(0)

    except ValueError as error:
        print(f"Error 404 - Not Found: {error}")


if __name__ == '__main__':
    main()