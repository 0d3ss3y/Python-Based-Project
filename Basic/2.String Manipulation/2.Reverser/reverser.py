import string

def reverse_word(text: str) -> str:
    """
    Reverse each word in the text while preserving punctuation and capitalization.
    """
    def add_punctuation(word: str, punc: dict) -> str:
        """
        Reinsert punctuation at its original position in the reversed word.
        """
        for char, idx in sorted(punc.items(), key=lambda x: x[1]):
            word = word[:idx] + char + word[idx:]
        return word

    words = text.split()
    reversed_words = []
    punctuation = string.punctuation

    for word in words:
        punctuation_positions = {}
        reversed_word = ""

        # Collect punctuation and reverse the word
        for i, char in enumerate(reversed(word)):
            if char in punctuation:
                # Store the original position of punctuation
                punctuation_positions[char] = len(word) - 1 - i
            else:
                reversed_word += char

        # Reinsert punctuation and capitalize the word
        if punctuation_positions:
            reversed_word = add_punctuation(reversed_word, punctuation_positions)

        reversed_words.append(reversed_word.capitalize())

    return ' '.join(reversed_words)


def reverse_sentence(sentence: str) -> str:
    """
    Reverse the entire sentence while keeping the word order intact.
    """
    words = sentence.split()
    return ' '.join(reversed(words))


def display_menu() -> int:
    """
    Display menu options and get the user's selection.
    """
    print("\n__Methods__:\n[1] Reverse words\n[2] Reverse sentence")
    try:
        selection = int(input("Select a method [1-2]: "))
        if selection not in [1, 2]:
            raise ValueError("Invalid choice. Please select 1 or 2.")
        return selection
    except ValueError as error:
        print(f"Error: {error}")
        return -1


def main():
    """
    Main program to interact with the user and reverse text based on their choice.
    """
    print("__Reverser__")

    try:
        selection = display_menu()
        if selection == -1:
            return

        text = input("Enter text: ").strip()
        if not text:
            print("Error: Text cannot be empty.")
            return

        if selection == 1:
            outcome = reverse_word(text)
        else:
            outcome = reverse_sentence(text)

        print(f"Outcome: {outcome}")

    except (ValueError, TypeError) as error:
        print(f"Error: {error}")

    except (KeyboardInterrupt, SystemExit):
        print("\nThank you for using the Reverser!")


if __name__ == '__main__':
    main()
