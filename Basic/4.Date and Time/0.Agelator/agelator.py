import datetime
from typing import Union


def find_next_birthday_day(birthday):
    pass


def determine_age(birthday):
    pass


def determine_zodiac(birthday):
    pass


def option() -> Union[str,None]:
    try:
        options = ["Determine Age", "Determine Zodiac", "Determine Next Birthday"]
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


def retrieve_birthday():
    pass


def main():
    pass

if __name__ == '__main__':
    main()