import re
from typing import List, Any


def find_palindromes(text: str) -> List[str]:
    """Find all palindromic words in the given text."""
    words = text.split()
    palindromes = [word for word in words if is_palindrome(word)]
    return palindromes


def is_palindrome_word(word: str) -> bool:
    """Check if a single word is a palindrome."""
    return word == word[::-1]


def is_palindrome(text: str) -> bool:
    """Check if the given text is a palindrome, ignoring non-alphanumeric characters."""
    sanitized = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return sanitized == sanitized[::-1]


def display_menu() -> int:
    """Display menu options and get the user's selection."""
    print("\n__Methods__:\n[1] Check if a word/sentence is a palindrome\n[2] Find palindromic words in a sentence")
    try:
        selection = int(input("Select a method [1-2]: "))
        if selection not in [1, 2]:
            raise ValueError("Invalid choice. Please select 1 or 2.")
        return selection
    except ValueError as error:
        print(f"Error: {error}")
        return -1


def main():
    """Main program to handle user interaction."""
    print("__Palindrome Checker__")
    try:
        selection = display_menu()
        if selection == -1:
            return

        text = input("Enter text: ").strip()

        if selection == 1:
            if is_palindrome(text):
                print("The text is a palindrome.")
            else:
                print("The text is not a palindrome.")
        elif selection == 2:
            palindromes = find_palindromes(text)
            if palindromes:
                print(f"Palindromic words found: {', '.join(palindromes)}")
            else:
                print("No palindromic words found in the text.")

    except (KeyboardInterrupt, SystemExit):
        print("\nThank you for using the Palindrome Checker!")

    except Exception as error:
        print(f"An unexpected error occurred: {error}")


if __name__ == '__main__':
    main()
