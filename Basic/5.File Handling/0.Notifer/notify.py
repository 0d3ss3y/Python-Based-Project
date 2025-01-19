import json
import os
import sys
from time import sleep
from typing import Union

script_dir = os.path.dirname(os.path.abspath(__file__))

def clear_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')


def load_notes():
    load_dir = os.path.join(script_dir, '.Saved')
    files = os.listdir(load_dir)

    def load_json(name):
        file_path = os.path.join(load_dir, name)
        with open(file_path, "w") as file:
            data = json.load(file)
        print(f"Note Downloaded to {file_path}")
        return data

    try:
        print("\n__Loading File__:")

        if len(files) == 0:
            raise FileNotFoundError("No Saved Notes Found")
        else:
            for num,file_name in enumerate(files,start=1):
                file = file_name.removesuffix(".json")
                print(f"[{num}]. {file}")

                selection = int(input(f"Pick Note [1-{len(files)}]: "))

                if 1 > selection > len(files):
                    raise FileNotFoundError("Selected Note Not Found")
                else:
                    return load_json(files[selection-1])

    except FileNotFoundError as e:
        print(f"Error 404 - {e}")
        return None


def download_notes(notes):
    download_path = os.path.join(script_dir, 'Downloads')
    os.makedirs(download_path, exist_ok=True)

    try:
        name = input("Enter Note Name: ").strip()

        if len(name) == 0:
            raise ValueError("Name cannot be empty")

        file_path = os.path.join(download_path, f"{name}.json")
        with open(file_path,"w") as file:
            json.dump(notes,file)
        print(f"Note Downloaded to {file_path}")

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def save_notes(notes):
    save_path = os.path.join(script_dir, '.Saved')
    os.makedirs(save_path, exist_ok=True)

    try:
        name = input("Enter Note Name: ").strip()

        if len(name) == 0:
            raise ValueError("Name cannot be empty")

        file_path = os.path.join(save_path, f"{name}.json")
        with open(file_path, "w") as file:
            json.dump(notes, file)
        print(f"Note Downloaded to {file_path}")

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


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

            sleep(2)
            clear_terminal()

    except (KeyboardInterrupt, SystemExit):
        print("\nExiting...")
        sys.exit()



if __name__ == '__main__':
    main()