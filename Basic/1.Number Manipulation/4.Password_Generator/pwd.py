import random
import string


def numbers() -> str:
    """
    Generate a random numeric character.
    """
    return str(random.randint(0, 9))


def letters() -> str:
    """
    Generate a random alphabetical character (uppercase or lowercase).
    """
    return random.choice(string.ascii_letters)


def specials() -> str:
    """
    Generate a random special character.
    """
    special_list = "!@#$%^&*()_+-={}[]:;<>,.?/"
    return random.choice(special_list)


def generate_pwd(length: int) -> str:
    """
    Generate a random password with the given length.
    Ensures the password contains a mix of letters, numbers, and special characters.
    """
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    # Ensure at least one of each type
    password_chars = [letters(), numbers(), specials()]

    # Fill the rest of the password randomly
    for _ in range(length - 3):
        choice = random.choice([letters, numbers, specials])
        password_chars.append(choice())

    # Shuffle to make the password more random
    random.shuffle(password_chars)
    return ''.join(password_chars)


def suggested_password() -> str:
    """
    Generate a suggested password of fixed length (16 characters).
    """
    return generate_pwd(16)


def custom_pwd() -> str:
    while True:
        try:
            length = int(input("How long do you want your password to be? (minimum 8, maximum 16): "))
            if 8 > length > 16:
                print("Password must be at least 8 characters long. Try again.")
                continue
            return generate_pwd(length)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    """
    Main function to interact with the user and generate passwords.
    """
    print("__Password Generator__")

    # Generate and display a suggested password
    google_algo = suggested_password()
    print(f"Suggested Password: {google_algo}")

    while True:
        confirmation = input("Do you want to generate your own password? (y/n): ").strip().lower()
        if confirmation.startswith("y"):
            custom_password = custom_pwd()
            print(f"Your Custom Password: {custom_password}")
            break
        elif confirmation.startswith("n"):
            print(f"Password confirmed: {google_algo}")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


if __name__ == '__main__':
    main()
