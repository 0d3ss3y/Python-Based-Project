import string
import random
import sys


def get_separator() -> str:
    """
    Prompt the user for a separator or randomly select one.
    """
    separators = string.punctuation
    confirm = input("Do you want a custom separator? [Yes/No/Random]: ").strip().lower()

    if confirm.startswith('n'):  # Default separator
        print("Using default separator (no separator).")
        return ""
    elif confirm.startswith('r'):  # Random separator
        separator = random.choice(separators)
        print(f"Using random separator: {separator}")
        return separator
    elif confirm.startswith('y'):  # Custom separator
        custom_sep = input("Enter a custom separator (must be a punctuation mark): ").strip()
        if custom_sep in separators:
            print(f"Using custom separator: {custom_sep}")
            return custom_sep
        else:
            print("Invalid separator. Using default separator (no separator).")
            return ""
    else:
        print("Invalid input. Using default separator (no separator).")
        return ""


def get_case_rule() -> str:
    """
    Display case rules and get the user's selection.
    """
    case_options = ["All uppercase", "All lowercase", "First letter uppercase"]
    print("\n__Case Rules__:")
    for idx, option in enumerate(case_options, start=1):
        print(f"[{idx}] {option}")

    try:
        choice = int(input("\nSelect a rule [1-3]: ").strip())
        if 1 <= choice <= 3:
            return case_options[choice - 1]
        else:
            raise ValueError("Invalid selection. Please choose a number between 1 and 3.")
    except ValueError as e:
        print(f"Error: {e}. Defaulting to 'All uppercase'.")
        return "All uppercase"


def make_acronym(phrase: str, rule: str, separator: str) -> str:
    """
    Generate an acronym from the phrase based on the rule and separator.
    """
    exclude_words = {"and", "of", "the"}  # Words to exclude from the acronym
    words = phrase.split()
    acronym_letters = [word[0] for word in words if word.lower() not in exclude_words]

    acronym = separator.join(acronym_letters)
    if rule == "All uppercase":
        return acronym.upper()
    elif rule == "All lowercase":
        return acronym.lower()
    else:  # First letter uppercase
        return acronym.capitalize()


def main():
    """
    Main program loop for generating acronyms.
    """
    print("__Acronym Generator__\n")
    while True:
        try:
            phrase = input("\nEnter a phrase (or type 'Exit' or 'Quit' to stop): ").strip()
            if phrase.lower() in {'exit', 'quit'}:
                print("Thank you for using the Acronym Generator!")
                sys.exit()

            if not phrase:
                print("Error: Phrase cannot be empty.")
                continue

            rule = get_case_rule()
            separator = get_separator()
            acronym = make_acronym(phrase, rule, separator)
            print(f"Generated Acronym: {acronym}")

        except (KeyboardInterrupt, SystemExit):
            print("\nExiting the program. Goodbye!")
            sys.exit()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
