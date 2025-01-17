import datetime
import os
import sys
from time import sleep
from typing import Union

def clear_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')


def find_next_birthday_day(month, day):
    this_year = datetime.date.today().year
    birthday = datetime.date((this_year+1), month, day)
    print(birthday.strftime("%B"))


def determine_age(year):
    this_year = datetime.date.today().year
    age = this_year - year
    print(f"You are {age} years old")


def determine_zodiac(month, day):
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
    this_year = datetime.date.today().year
    selected_date = datetime.datetime(this_year,month,day)

    for symbol, dates in chart.items():
        starting = dates["start"]
        ending = dates["end"]

        start_month,start_day = starting.split("/")
        ending_month,ending_day = ending.split("/")

        starting_date = datetime.datetime(this_year,int(start_month),int(start_day))
        ending_date = datetime.datetime(this_year,int(ending_month),int(ending_day))

        if starting_date <= selected_date <= ending_date:
            print(f"You are a {symbol} charka hun")


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
            clear_terminal()
            opt = option()
            birth_year,birth_month,birth_day = retrieve_birthday()

            if opt == "Determine Age":
                determine_age(int(birth_year))
            elif opt == "Determine Zodiac":
                determine_zodiac(int(birth_month),int(birth_day))
            elif opt == "Determine Next Birthday":
                find_next_birthday_day(int(birth_month),int(birth_day))
            elif opt == "Quit":
                raise SystemExit(0)
            sleep(0.4)


    except ValueError as error:
        print(f"Error 404 - Not Found: {error}")

    except (KeyboardInterrupt, SystemExit):
        print("\n__Good Bye!__")
        sys.exit(0)


if __name__ == '__main__':
    main()