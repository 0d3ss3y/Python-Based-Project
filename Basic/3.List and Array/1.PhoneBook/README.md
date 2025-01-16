# Contact Manager

## Overview

The **Contact Manager** is a Python program that helps users manage their personal contacts efficiently. It supports adding, editing, deleting, searching, and displaying contacts, with all data saved to a file for persistence.

## Features

- **Add Contacts**:
  - Create new contacts by entering a name, surname, and phone number.
  - Prevents duplicate names.
- **Search Contacts**:
  - Search by name, surname, or contact number.
  - Displays all matching results.
- **Edit Contacts**:
  - Modify an existing contact's details, including name, surname, or phone number.
  - Supports renaming contacts.
- **Delete Contacts**:
  - Remove unwanted contacts by name.
- **Display Contacts**:
  - View all contacts in a sorted and organized format.
- **File Persistence**:
  - Automatically saves contacts to `contacts.json`.
  - Loads contacts from the file on program start.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/contact-manager.git
   ```
2. Navigate to the project directory:
   ```bash
   cd contact-manager
   ```
3. Run the program:
   ```bash
   python contact_manager.py
   ```

## Usage

1. **Main Menu**:
   - The program displays a menu of options:
     - Add Contact
     - Search Contact
     - Edit Contact
     - Delete Contact
     - Display Contacts
     - Exit

2. **Adding a Contact**:
   - Input the name, surname, and phone number when prompted.
   - Example:
     ```
     Enter contact name: John
     Enter contact surname: Doe
     Enter contact number: 123-456-7890
     ```

3. **Searching for a Contact**:
   - Enter a keyword (name, surname, or number).
   - Example:
     ```
     Enter name, surname, or number to search: John
     ```

4. **Editing a Contact**:
   - Specify the contact name to edit.
   - Update any field or leave blank to keep the current value.
   - Example:
     ```
     Enter the name of the contact to edit: John
     Enter new name (or press Enter to keep current): Jonathan
     Enter new surname: Smith
     Enter new contact number: 987-654-3210
     ```

5. **Deleting a Contact**:
   - Enter the contact name to delete.
   - Example:
     ```
     Enter the name of the contact to delete: John
     ```

6. **Displaying Contacts**:
   - View all saved contacts in alphabetical order.
   - Example output:
     ```
     __Contact List__
     Jane: Doe, 111-222-3333
     John: Smith, 987-654-3210
     ```

## File Handling

- Contacts are stored in `contacts.json`.
- The file is updated automatically after any changes.
- The program creates the file if it doesn’t exist.

## Requirements

- Python 3.7 or later
- No additional dependencies

## Customization

- Add support for email addresses and additional contact fields.
- Implement categories or tags for contacts.
- Integrate with external APIs for syncing contacts.

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

---

Manage your contacts effortlessly with the Contact Manager! Let me know if you have any questions or suggestions.
