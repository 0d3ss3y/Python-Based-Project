import os
import sys
from typing import Union


def clear_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')


def load_notes():
    pass


def download_notes():
    pass


def save_notes():
    pass


def create_notes():
    pass


def delete_notes():
    pass


def edit_notes():
    pass


def option() -> Union[str,None]:
    try:
        print("\n__Options__:")
        options = ["Load Notes", "Download Notes", "Save Notes", "Create Notes", "Delete Notes"]

        for key, opt in enumerate(options,start=1):
            print(f"[{key}]. {opt}")

        selection = int(input(f"Select an option [1-{len(options)}]: "))

        if 1 > selection > len(options):
            raise ValueError("Invalid selection")
        return options[selection - 1]

    except ValueError as error:
        print(f"Error 404 - {error}")
        return None


def main():
    print("__Note Maker__\n")

    try:
        notes = {}
        while True:
            opt = option()

            if opt == "Load Notes":
                notes = load_notes()
            elif opt == "Download Notes":
                download_notes(notes)
                print("Download Complete")
            elif opt == "Save Notes":
                save_notes(notes)
                print("Notes successfully saved")
            elif opt == "Create Notes":
                notes = create_notes(notes)
                print("Notes successfully created")
            elif opt == "Delete Notes":
                notes = delete_notes(notes)
                print("Notes successfully deleted")
            elif opt == "Edit Notes":
                notes = edit_notes(notes)
            elif opt == "Exit":
                raise SystemExit(0)

    except (KeyboardInterrupt, SystemExit):
        print("\nExiting...")
        sys.exit()



if __name__ == '__main__':
    main()