from typing import Union


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


def option() -> Union[str,None]:
    try:
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


if __name__ == '__main__':
    main()