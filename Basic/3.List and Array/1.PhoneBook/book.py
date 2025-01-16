import os
import json
from time import sleep


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def display_menu(options):
    print("\n__Options__")
    for idx, option in enumerate(options, start=1):
        print(f"[{idx}] {option}")
    try:
        choice = int(input("Enter your choice: "))
        if 1 <= choice <= len(options):
            return options[choice - 1]
        else:
            raise ValueError
    except ValueError:
        print("Invalid choice. Please try again.")
        return None


def add_contact(contacts):
    name = input("Enter contact name: ").strip().capitalize()
    surname = input("Enter contact surname: ").strip().capitalize()
    contact_no = input("Enter contact number: ").strip()

    if not name or not surname or not contact_no:
        print("All fields are required!")
        return

    if name in contacts:
        print(f"Contact with name {name} already exists!")
        return

    contacts[name] = {"surname": surname, "contact_no": contact_no}
    print(f"Contact {name} added successfully!")


def search_contact(contacts):
    query = input("Enter name, surname, or number to search: ").strip().capitalize()
    results = [
        (name, details)
        for name, details in contacts.items()
        if query in name or query in details["surname"] or query in details["contact_no"]
    ]

    if results:
        for name, details in results:
            print(f"{name}: {details['surname']}, {details['contact_no']}")
    else:
        print("No matching contacts found.")


def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip().capitalize()
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found.")


def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ").strip().capitalize()
    if name not in contacts:
        print("Contact not found.")
        return

    print(f"Editing contact {name}: {contacts[name]}")
    new_name = input("Enter new name (or press Enter to keep current): ").strip().capitalize() or name
    surname = input("Enter new surname: ").strip().capitalize() or contacts[name]["surname"]
    contact_no = input("Enter new contact number: ").strip() or contacts[name]["contact_no"]

    if new_name != name:
        contacts.pop(name)
    contacts[new_name] = {"surname": surname, "contact_no": contact_no}
    print(f"Contact {new_name} updated successfully!")


def display_contacts(contacts):
    if not contacts:
        print("No contacts to display.")
        return

    print("\n__Contact List__")
    for name, details in sorted(contacts.items()):
        print(f"{name}: {details['surname']}, {details['contact_no']}")


def load_contacts(file_path="contacts.json"):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return {}


def save_contacts(contacts, file_path="contacts.json"):
    with open(file_path, "w") as file:
        json.dump(contacts, file, indent=4)


def main():
    contacts = load_contacts()
    options = ["Add Contact", "Search Contact", "Edit Contact", "Delete Contact", "Display Contacts", "Exit"]

    while True:
        clear_terminal()
        choice = display_menu(options)
        if choice == "Add Contact":
            add_contact(contacts)
        elif choice == "Search Contact":
            search_contact(contacts)
        elif choice == "Edit Contact":
            edit_contact(contacts)
        elif choice == "Delete Contact":
            delete_contact(contacts)
        elif choice == "Display Contacts":
            display_contacts(contacts)
        elif choice == "Exit":
            save_contacts(contacts)
            print("Goodbye!")
            break
        sleep(1)


if __name__ == "__main__":
    main()
