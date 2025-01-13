import string
import base64

# Global Constants
METHODS = ["Caesar Cipher", "XOR Encryption", "Vigenère Encryption", "Base64 Encoding"]
LETTERS = list(string.ascii_lowercase)


# Utility Functions
def transform_character(character, msg, target_index):
    """Transform a character based on target index, maintaining case."""
    if character.isupper():
        msg += LETTERS[target_index].capitalize()
    else:
        msg += LETTERS[target_index]
    return msg


def wrap_around_index(index):
    """Handle index wrapping for Caesar and Vigenère ciphers."""
    return (index + len(LETTERS)) % len(LETTERS)


def caesar_cipher(text, option):
    """Perform Caesar Cipher Encryption or Decryption."""
    try:
        shifts = int(input("Enter shift value (0-25): "))
        if shifts < 0 or shifts >= len(LETTERS):
            raise ValueError(f"Shifts must be between 0 and {len(LETTERS) - 1}")

        shift_direction = 1 if option == "Encryption" else -1
        shifts *= shift_direction

        result = ""
        for char in text:
            if char.isalpha():
                index = wrap_around_index(LETTERS.index(char.lower()) + shifts)
                result = transform_character(char, result, index)
            else:
                result += char

        return result
    except ValueError as error:
        return f"Error: {error}"


def xor_encryption(text, option):
    """Perform XOR Encryption or Decryption."""
    try:
        if option == "Encryption":
            return "".join(f"{bin(ord(char))[2:].zfill(8)}" for char in text)
        else:
            binary_chunks = [text[i:i + 8] for i in range(0, len(text), 8)]
            return "".join(chr(int(chunk, 2)) for chunk in binary_chunks)
    except Exception as error:
        return f"Error: {error}"


def vigenere_cipher(text, option):
    """Perform Vigenère Cipher Encryption or Decryption."""
    try:
        key = input("Enter a key (alphabetic characters only): ").lower()
        if not key.isalpha():
            raise ValueError("Key must contain alphabetic characters only.")

        key_repeated = (key * (len(text) // len(key) + 1))[:len(text)]
        shift_direction = 1 if option == "Encryption" else -1

        result = ""
        for i, char in enumerate(text):
            if char.isalpha():
                key_index = LETTERS.index(key_repeated[i])
                shift = shift_direction * key_index
                index = wrap_around_index(LETTERS.index(char.lower()) + shift)
                result = transform_character(char, result, index)
            else:
                result += char

        return result
    except ValueError as error:
        return f"Error: {error}"


def base64_cipher(text, option):
    """Perform Base64 Encoding or Decoding."""
    try:
        if option == "Encryption":
            return base64.b64encode(text.encode("utf-8")).decode("utf-8")
        else:
            return base64.b64decode(text).decode("utf-8")
    except (ValueError, base64.binascii.Error) as error:
        return f"Error: Invalid Base64 input."


# Main Workflow Functions
def select_method():
    """Prompt user to select a cryptographic method."""
    print("\n__Methods__")
    for i, method in enumerate(METHODS, start=1):
        print(f"[{i}] {method}")

    try:
        choice = int(input(f"\nSelect a method [1-{len(METHODS)}]: "))
        if 1 <= choice <= len(METHODS):
            return METHODS[choice - 1]
        else:
            raise ValueError("Invalid selection.")
    except ValueError as error:
        return f"Error: {error}"


def select_option():
    """Prompt user to choose between Encryption and Decryption."""
    print("\nOptions:\n[D]ecryption\n[E]ncryption")
    option = input("Select an option [D/E]: ").strip().upper()
    if option.startswith("E"):
        return "Encryption"
    elif option.startswith("D"):
        return "Decryption"
    else:
        return "Error: Invalid option."


def process_method(method, option, text):
    """Process the selected cryptographic method."""
    if method == "Caesar Cipher":
        return caesar_cipher(text, option)
    elif method == "XOR Encryption":
        return xor_encryption(text, option)
    elif method == "Vigenère Encryption":
        return vigenere_cipher(text, option)
    elif method == "Base64 Encoding":
        return base64_cipher(text, option)
    else:
        return "Error: Unknown method."


def main():
    """Main program entry point."""
    print("__Safety Program__")
    try:
        option = select_option()
        if "Error" in option:
            print(option)
            return

        method = select_method()
        if "Error" in method:
            print(method)
            return

        text = input("\nEnter your text: ")
        result = process_method(method, option, text)
        print(f"\nResult ({option}): {result}")
    except (KeyboardInterrupt, EOFError):
        print("\nThank you for using the Safety Program!")


if __name__ == "__main__":
    main()
