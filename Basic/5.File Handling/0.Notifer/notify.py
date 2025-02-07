import json
import os
import sys
from datetime import datetime
from time import sleep
from typing import Union

script_dir = os.path.dirname(os.path.abspath(__file__))

def clear_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')


def load_notes():
    load_dir = os.path.join(script_dir, '.Saved')
    os.makedirs(load_dir, exist_ok=True)
    files = os.listdir(load_dir)

    def load_json(name):
        file_path = os.path.join(load_dir, name)
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
            print(f"JSON data loaded from {file_path}")
            return data
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {file_path}: {e}")
            return None

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


def save_notes(notes,topic):
    save_path = os.path.join(script_dir, '.Saved')
    os.makedirs(save_path, exist_ok=True)

    try:
        name = topic

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


def create_notes(notes):

    try:
        print("\n__Creating Note__\n")
        Topic = input("Enter Topic: ").strip()
        date = datetime.now().strftime("%m/%d/%Y")
        time = datetime.now().strftime("%H:%M:%S")
        title = input("Enter Note Title: ").strip()
        note = input("Enter Note\n>").strip()

        template ={
            'Topic': Topic,
            'date': date,
            'time': time,
            'note': note
        }

        notes[f"{title}"] = template
        return notes,Topic

    except ValueError as error:
        print(f"Error 404 - {error}")


def delete_notes():
    try:
        scripts = os.path.join(script_dir, '.Saved')
        files = os.listdir(scripts)

        for key,file in enumerate(files):
            print(f"[{key}]. {file}")

        selection = int(input("Pick Note [1-{len(files)}]: "))

        if 1 > selection > len(files):
            raise FileNotFoundError("Selected Note Not Found")
        else:
            os.remove(os.path.join(scripts, files[selection-1]))

    except FileNotFoundError as error:
        print(f"Error 404 - {error}")


def edit_notes():
    def get_notes(details):
        topics = {}
        for inx,(key, value) in enumerate(details.items(), start=1):
            print(f"[{inx}]. {key}: {value["Topic"]}")
            topic = value["Topic"]
            topics[topic] = value["note"]

        keys = list(topics.keys())
        selection = int(input(f"Pick Note [1-{len(keys)}]: "))

        if 1 > selection > len(keys):
            raise FileNotFoundError("Selected Note Not Found")
        else:
            selected = keys[selection-1]
            return topics[selected],selected


    def editor(note):
        print(f"\n__Editing Note__\n")
        print(f"Original note:\n{note}")
        new_note = input("\nEnter New Note\n>").strip()

        if len(new_note) == 0:
            return note
        else:
            return new_note


    def update_note(details, note, topic):
        for key, value in details.items():
            if value["Topic"] == topic:
                value["note"] = note

        return details


    details = load_notes()

    if details is not None:
        note,topic = get_notes(details)
        updated_notes = editor(note)
        return update_note(details, updated_notes, topic)


def option() -> Union[str,None]:
    try:
        print("\n__Options__:")
        options = ["Load Notes", "Edit Notes", "Download Notes", "Create Notes", "Delete Notes","Exit"]

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
            elif opt == "Create Notes":
                notes,Topic = create_notes(notes)
                save_notes(notes,Topic)
                print("Notes successfully created")
            elif opt == "Delete Notes":
                notes = delete_notes()
                print("Notes successfully deleted")
            elif opt == "Edit Notes":
                notes = edit_notes()
            elif opt == "Exit":
                raise SystemExit(0)

            sleep(2)
            clear_terminal()

    except (KeyboardInterrupt, SystemExit):
        print("\nExiting...")
        sys.exit()


if __name__ == '__main__':
    main()