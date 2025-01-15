import os
import random
from time import sleep


def clear_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')


def search(contact):
    def search_by_name(name, details):
        names = list(details.keys())
        if name in names:
            print(f"contact name: {name}\ncontact surname: {details[name]['surname']}\ncontact number: {details[name]['contact_no']}")
        else:
            print(f"Error 404 - Contact {name} not found")

    def search_by_surname(surname, details):
        for key,values in details.items():
            if values['surname'] == surname:
                print(f"contact name: {key}\ncontact surname: {values['surname']}\ncontact number: {values['contact_no']}")
        else:
            print(f"Error 404 - Contact {surname} not found")

    def search_by_number(number,details):
        for key, values in details.items():
            if values['contact_no'] == number:
                print(
                    f"contact name: {key}\ncontact surname: {values['surname']}\ncontact number: {values['contact_no']}")
        else:
            print(f"Error 404 - Contact {number} not found")


    categories = ["name", "surname", "number"]
    print("__Search Methods__")
    for category in categories:
        print(f"[{category[0].upper()}]{category[1::]}")

    search_by = input("\nSearch using: ").lower()

    if search_by not in categories:
        print(f"Illegal search: {search_by}")
    else:
        attempt = input(f"Enter target's {search_by}: ").lower().capitalize()

        if search_by == "name":
            search_by_name(attempt,contact)
        elif search_by == "surname":
            search_by_surname(attempt,contact)
        else:
            search_by_number(attempt, contact)


def sort_contact(contact):
    placeholder = contact.copy()
    contact.clear()
    placeholder_keys = sorted(list(placeholder.keys()))

    for key in placeholder_keys:
        value = placeholder[key]
        contact[key] = value
    return contact


def adding_contact(contact):
    try:
        first_name = input("Enter contact name: ").capitalize()
        surname = input("Enter contact surname: ").capitalize()
        contact_no = input("Enter contact number: ")

        if first_name == '' or surname == '' or contact_no == '':
            raise EOFError("Empty Arguments")

        elif first_name in list(contact.keys()):
            tag = random.randint(1,9)
            contact[f"{first_name}_{tag}"] = {
                "surname": surname,
                "contact_no": contact_no
            }

        else:
            contact[first_name] = {
                "surname": surname,
                "contact_no": contact_no
            }

        return contact


    except (ValueError,EOFError) as error:
        print(f"Error 404 - Not Found: {error}")


def contact_edit(contact):
    pass


def delete_contact(contact):
    pass


def display_contact(contact):
    pass


def display_opt(contact):
    try:
        options = ["Add", "Search", "Sort", "Edit", "Delete", "Display"]
        print("\n__Options__:")

        for key, option in enumerate(options, start=1):
            print(f"[{key}]. {option}")

        opt = int(input("\nEnter your option [1-6]: "))

        if 1 > opt > 6:
            raise ValueError("Illegal input")
        else:
            return options[opt-1]

    except ValueError as error:
        print(f"Error 404 - Not Found: {error}")


def main():
    print("__Contact Book__")
    contact = {
        "Dummy":{
            "surname":"Data",
            "contact_no":"12345",
        },
        "Asta":{
            "surname":"Data",
            "contact_no":"12345",
        }
    }

    while True:
        opt = display_opt(contact)

        if opt == "Add":
            contact = adding_contact(contact)
            print("Contact Added")
        elif opt == "Search":
            search(contact)
        elif opt == "Sort":
            sort_contact(contact)
            print("Successfully Sorted")
        elif opt == "Edit":
            contact_edit(contact)
        elif opt == "Delete":
            delete_contact(contact)
        else:
            display_contact(contact)

        sleep(0.2)
        clear_terminal()

 
if __name__ == '__main__':
    main()