import random
from typing import Union, Tuple, Any

story_templates = {
    "adventure": [
        "I ventured into the <place> and discovered a <adjective> <creature> <verb>ing.",
        "While climbing a <noun>, I found a <adjective> <object> <verb>ing at the top.",
        "In the middle of the <place>, a <adjective> <animal> started <verb>ing!",
        "I was exploring a <adjective> <place> when I stumbled upon a <noun> <verb>ing.",
        "The <adjective> trail led to a <animal> <verb>ing near the <place>.",
        "During the journey, I saw a <adjective> <object> <verb>ing in a <place>.",
        "While hiking, I met a <adjective> <person> who was <verb>ing a <animal>.",
        "In a mysterious <place>, a <adjective> <creature> was <verb>ing.",
        "The treasure map pointed to a <place> where a <adjective> <animal> was <verb>ing.",
        "I found a <adjective> <animal> <verb>ing near the edge of the <place>.",
    ],
    "sci-fi": [
        "On planet <place>, a <adjective> alien was <verb>ing a <object>.",
        "In the spaceship, a <adjective> robot started <verb>ing with a <noun>.",
        "The <adjective> laser gun was <verb>ing in the <place>.",
        "A <adjective> alien was <verb>ing in the <place> with a <object>.",
        "In a galaxy far away, a <adjective> <creature> was <verb>ing on a <object>.",
        "The AI system in the <place> began <verb>ing <adjective>ly.",
        "A <adjective> spaceship crash-landed on a <place> while <verb>ing.",
        "The <adjective> hologram was <verb>ing with a <noun> in the <place>.",
        "I saw a <adjective> starship captain <verb>ing a <animal> on the <place>.",
        "The alien’s <adjective> ship was <verb>ing lightyears through the <place>.",
    ],
    "fantasy": [
        "In the magical <place>, a <adjective> dragon was <verb>ing.",
        "The wizard’s <adjective> spellbook was <verb>ing on the <place>.",
        "A <adjective> unicorn was <verb>ing in the <place> with a <object>.",
        "The <adjective> knight was <verb>ing with a <animal> in the <place>.",
        "I saw a <adjective> goblin <verb>ing a <object> near the <place>.",
        "The enchanted <place> held a <adjective> <creature> that was <verb>ing.",
        "A <adjective> witch was <verb>ing on her broomstick in the <place>.",
        "The castle’s <adjective> gate started <verb>ing at midnight.",
        "A <adjective> phoenix was <verb>ing above the <place>.",
        "The magical forest was full of <adjective> creatures <verb>ing with joy.",
    ],
    "silly": [
        "Today I saw a <adjective> <animal> <verb>ing in my <place>.",
        "A <adjective> <object> was <verb>ing with my <animal> in the <place>.",
        "I found a <adjective> <noun> <verb>ing in the middle of the <place>.",
        "My <adjective> neighbor was <verb>ing with a <object> on the <place>.",
        "A <adjective> <animal> was <verb>ing upside down on the <object>.",
        "The <adjective> <object> started <verb>ing in my <place> for no reason.",
        "I saw a <adjective> <person> <verb>ing a <animal> on the <place>.",
        "A <adjective> <creature> was <verb>ing under my <object> in the <place>.",
        "The <adjective> <animal> was <verb>ing while balancing on a <object>.",
        "My <adjective> friend started <verb>ing with a <animal> in the <place>.",
    ],
    "school": [
        "In class, a <adjective> <object> started <verb>ing on the <place>.",
        "The teacher’s <adjective> <animal> was <verb>ing during the lesson.",
        "I saw a <adjective> <person> <verb>ing in the middle of the <place>.",
        "A <adjective> <object> fell and started <verb>ing in the classroom.",
        "The school’s <adjective> mascot was <verb>ing with a <animal> in the <place>.",
        "A <adjective> <creature> was <verb>ing in the hallway near the <place>.",
        "The lunch lady served a <adjective> meal that started <verb>ing.",
        "The <adjective> principal was <verb>ing on the <place> with a <object>.",
        "A <adjective> <animal> was <verb>ing near the lockers in the <place>.",
        "The <adjective> textbook started <verb>ing on its own in the <place>.",
    ],
}


def select_category() -> Union[str,None]:
    """
    Display the available categories and let the user select one.
    """
    try:
        print("\n__Template Categories__")
        categories = list(story_templates.keys())

        for idx,category in enumerate(categories, start=1):
            print(f"[{idx}].{category.capitalize()}")

        choice = int(input("Select a category by number: "))
        if 1 <= choice <= len(categories):
            return categories[choice - 1]
        else:
            raise ValueError("Invalid category selection.")


    except (ValueError, TypeError, EOFError) as error:
        print(f"Error 404 - Not Found: {error}")
        return None


def retrieve_template(selection :str) -> tuple[Any, dict]:
    """
    Retrieve a random story template and extract placeholders.
    """
    def extract_speeches(phrase):
        speech = {}
        words = phrase.split()
        for inx,word in enumerate(words):
            if word.startswith("<") and word.endswith(">"):
                speech[word] = inx
        return speech

    templates = story_templates.get(selection,[])
    story = random.choice(templates)
    parts_of_speech = extract_speeches(story)
    return story,parts_of_speech


def word_collection(speeches):
    """
    Prompt the user to provide words for each placeholder.
    """
    user_input = {}

    try:
        for speech in speeches:
            fill_word :str = input(f"{speech[1:-1]} : ")

            if fill_word.isalpha():
                user_input[fill_word] = speeches[speech]
            else:
                raise ValueError(f"Invalid input: {fill_word}")
        return user_input

    except (ValueError, EOFError) as error:
        print(f"Error 404 - Not Found: {error}")
        return {}


def generate_story(template,user_choices) -> str:
    """
    Replace placeholders in the template with user-provided words.
    """
    parts = [word for word in template.split()]

    for word,idx in user_choices.items():
        parts[idx] = word

    return " ".join(parts)


def main():
    """
    Main function to run the Mad Libs generator.
    """
    print("__Simple Mad Libs Generator__\n")
    while True:
        try:
            category = select_category()
            if not category:
                continue

            template, placeholders = retrieve_template(category)
            user_inputs = word_collection(placeholders)
            if not user_inputs:
                print("Story generation aborted due to missing inputs.")
                continue

            story = generate_story(template, user_inputs)
            print("\nYour Generated Story:")
            print(f"{story}\n")

            replay = input("Do you want to create another story? (yes/no): ").strip().lower()
            if replay not in {"yes", "y"}:
                print("Thank you for using the Mad Libs Generator!")
                break
        except KeyboardInterrupt:
            print("\nExiting the program. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()