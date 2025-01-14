import random

def search(contact):
    pass


def sort_contact(contact):
    pass


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
            print(f"[{key}]. {option}]")

        opt = int(input("\nEnter your option [1-6]: "))

        if 1 > opt > 6:
            raise ValueError("Illegal input")
        else:
            return options[opt-1]

    except ValueError as error:
        print(f"Error 404 - Not Found: {error}")


def main():
    print("__Contact Book__")
    contact = {}

    while True:
        opt = display_opt(contact)

        if opt == "Add":
            adding_contact(contact)
        elif opt == "Search":
            search(contact)
        elif opt == "Sort":
            sort_contact(contact)
        elif opt == "Edit":
            contact_edit(contact)
        elif opt == "Delete":
            delete_contact(contact)
        else:
            display_contact(contact)



if __name__ == '__main__':
    main()