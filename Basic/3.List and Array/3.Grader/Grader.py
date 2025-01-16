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
        options = ["Store Grades", "Display Grades", "Quit"]
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


def display_grades(report_card: Dict[str, Dict[str, Union[float, str]]]):
    """Display the grades of all learners."""
    if not report_card:
        print("No grades to display.")
        return

    print("\n__Report Cards__")
    for learner, grades in report_card.items():
        print(f"\n{learner}'s Report Card:")
        for subject, grade in grades.items():
            print(f"  {subject}: {grade}")


def store_grades(report_card: Dict[str, Dict[str, Union[float, str]]]) -> Dict:
    """Store grades for a new learner."""
    template = {
        "Math": 0,
        "Science": 0,
        "English": 0,
        "History": 0,
        "Programming": 0,
        "Average": 0,
        "Letter": "F",
    }
    total = 0
    subjects = ["Math", "Science", "English", "History", "Programming"]
    learner_name = input("Enter learner name: ").strip().title()

    if learner_name in report_card:
        print(f"{learner_name} already exists in the report card.")
        return report_card

    try:
        for subject in subjects:
            percentage = float(input(f"Enter percentage received for {subject}: "))
            if not (0 <= percentage <= 100):
                raise ValueError(f"Percentage for {subject} must be between 0 and 100.")
            template[subject] = percentage
            total += percentage

        avg = total / len(subjects)
        letter = determine_level(avg)
        template["Average"] = avg
        template["Letter"] = letter
        report_card[learner_name] = template
        print(f"{learner_name}'s grades have been added.")
    except ValueError as error:
        print(f"Invalid input: {error}")

    return report_card


def determine_level(score: float) -> str:
    """Determine the letter grade based on the score."""
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"


def main():
    """Main function to run the grade system."""
    report_card = {}

    try:
        print("__Grade System__\n")
        while True:
            selection = option()

            if selection == "Store Grades":
                report_card = store_grades(report_card)
            elif selection == "Display Grades":
                display_grades(report_card)
            elif selection == "Quit":
                print("Exiting the Grade System. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

            sleep(1)
            clear_terminal()

    except (SystemExit, KeyboardInterrupt):
        print("Exiting the Grade System. Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
