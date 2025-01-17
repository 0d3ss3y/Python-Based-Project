import datetime
from typing import Union


def find_next_birthday_day(birthday):
    pass


def determine_age(year):
    this_year = datetime.date.today().year
    age = this_year - year
    print(f"You are {age} years old")


def determine_zodiac(birthday):
    chart = {
        "Aries" : {
            "start" : "3/21",
            "end" : "4/19"
        },
        "Taurus" : {
            "start": "4/20",
            "end": "5/20"
        },
        "Gemini": {
            "start": "5/21",
            "end": "6/20"
        },
        "Cancer": {
            "start": "6/21",
            "end": "7/22"
        },
        "Leo": {
            "start": "7/23",
            "end": "8/22"
        },
        "Virgo": {
            "start": "8/23",
            "end": "9/22"
        },
        "Libra": {
            "start": "9/23",
            "end": "10/22"
        },
        "Scorpio": {
            "start": "10/22",
            "end": "11/21"
        },
        "Sagittarius": {
            "start": "11/22",
            "end": "12/21"
        },
        "Capricorn": {
            "start": "12/22",
            "end": "1/19"
        },
        "Aquarius": {
            "start": "1/20",
            "end": "2/18"
        },
        "Pisces": {
            "start": "2/19",
            "end": "3/20"
        }
    }




def option() -> Union[str,None]:
    try:
        options = ["Determine Age", "Determine Zodiac", "Determine Next Birthday","Quit"]
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
    def check_format(placeholder) -> bool:
        valid = False
        try:
            if "/" not in placeholder:
                raise ValueError(f"invalid Date: {placeholder}")
            else:
                year, month, day = placeholder.split("/")

                if len(year) == 4 and len(month) == 2 and (len(day) == 2 or len(day) == 1):
                    valid = True
                return valid

        except (ValueError,TypeError) as error:
            print(f"Error 404 - Not Found: {error}")
            return valid

    try:
        birthday = input("Enter your birthday [yyyy/mm/dd]: ")
        flag = check_format(birthday)

        if flag:
            year, month, day = birthday.split("/")
            return year, month, day
        else:
            raise ValueError(f"Invalid Date: {birthday}")

    except ValueError as error:
        print(f"Error 404 - Not Found: {error}")
        return None


def main():
    try:
        print("__Agelator__\n")

        while True:
            birth_year,birth_month,birth_day = retrieve_birthday()

    except ValueError as error:
        print(f"Error 404 - Not Found: {error}")

if __name__ == '__main__':
    main()