import os
import random
from time import sleep
from typing import Union, Any


def clear_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')


def search(contact):
    def search_by_name(name, details)-> Union[None,Any]:
        names = list(details.keys())
        if name in names:
            print(f"\nContact name: {name}\nContact surname: {details[name]['surname']}\nContact number: {details[name]['contact_no']}")
            return f"{name},{details[name]['surname']},{details[name]['contact_no']}"
        else:
            print(f"Error 404 - Contact {name} not found")

    def search_by_surname(surname, details) -> Union[None,Any]:
        for key,values in details.items():
            if values['surname'] == surname:
                print(f"\nContact name: {key}\nContact surname: {values['surname']}\nContact number: {values['contact_no']}")
                return f"{key},{values['surname']},{values['contact_no']}"
        else:
            print(f"Error 404 - Contact {surname} not found")
            return None

    def search_by_number(number,details) -> Union[None,Any]:
        for key, values in details.items():
            if values['contact_no'] == number:
                print(f"\nContact name: {key}\nContact surname: {values['surname']}\nContact number: {values['contact_no']}")
                return f"{key},{values['surname']},{values['contact_no']}"
        else:
            print(f"Error 404 - Contact {number} not found")
            return None


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
            result = search_by_name(attempt,contact)
        elif search_by == "surname":
            result = search_by_surname(attempt,contact)
        else:
            result = search_by_number(attempt, contact)

        return result


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
    def edit_name(user_name, details):
        headers = list(details.keys())
        info = details[user_name]
        del details[user_name]

        new_contact_name = input("Enter new details user_name: ").capitalize()
        if new_contact_name in headers:
            print(f"{new_contact_name} already exists adding random number")
            num = random.randint(0,9)
            new_contact_name = f"{new_contact_name}_{num}"

        details[new_contact_name] = info
        return details


    def edit_surname(user_name,user_surname,details):
        new_surname = input("Enter new surname: ").capitalize()

        if new_surname == " ":
            new_surname = user_surname

        details[user_name]["surname"] = new_surname

        return details


    def edit_number(username,user_no,details):
        new_contact_no = input("Enter new contact number: ")

        if new_contact_no == " ":
            new_contact_no = user_no

        details[username]["contact_no"] = new_contact_no

        return details


    try:
        topics = ["Name","Surname","Number"]
        parts = search(contact)
        if parts is None:
            raise EOFError("Contact not found")

        name, surname, contact_no = parts.split(",")

        for idx,topic in enumerate(topics,start=1):
            print(f"[{idx}].{topic}")

        selection = int(input("\nEnter your selection [1-3]: "))

        if selection not in range(1,3):
            raise EOFError("Invalid Selection")
        elif selection == 1:
            contact = edit_name(name, contact)
        elif selection == 2:
            contact = edit_surname(surname, contact)
        else:
            contact = edit_number(name, contact_no, contact)

        return contact


    except (ValueError,EOFError) as error:
        print(f"Error 404 - Not Found: {error}")
        return contact


def delete_contact(contact):
    try:
        name = input("Enter contact name: ").capitalize()

        if name in list(contact.keys()):
            del contact[name]
        else:
            raise EOFError("Contact not found")

        return contact

    except (ValueError,EOFError) as error:
        print(f"Error 404 - Not Found: {error}")


def display_contact(contact):
    print("\n__Contact Details__\n")
    for key,values in (contact.items()):
        print(f"{key.upper()}:")
        for name,info in values.items():
            print(f"\t{name.capitalize()}: {info}")
        print()


def display_opt():
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
        opt = display_opt()

        if opt == "Add":
            contact = adding_contact(contact)
            print("Contact Added")
        elif opt == "Search":
            _ = search(contact)
        elif opt == "Sort":
            contact = sort_contact(contact)
            print("Successfully Sorted")
        elif opt == "Edit":
            contact = contact_edit(contact)
        elif opt == "Delete":
            delete_contact(contact)
            print("Successfully Deleted")
        else:
            display_contact(contact)

        sleep(0.2)
        clear_terminal()

 
if __name__ == '__main__':
    main()