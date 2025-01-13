# Mad Libs Generator

## Overview

The **Mad Libs Generator** is a Python program that brings fun and creativity to storytelling. It allows users to create customizable story templates, collect specific word types from the user (e.g., nouns, verbs, adjectives), and generate amusing and unpredictable stories.

## Features

- **Story Templates**:
  - Predefined and user-defined story templates.
  - Support for placeholders like `<noun>`, `<verb>`, and `<adjective>`.
- **Word Collection**:
  - Prompt users for specific types of words (e.g., plural nouns, past-tense verbs).
  - Ensure user inputs match the requested word types.
- **Funny Story Generation**:
  - Replace placeholders with user-provided words.
  - Generate hilarious and unpredictable results.

## Usage Details

### Creating a Story:

1. Choose a story template:
   - Use one of the predefined templates.
   - Provide your own custom story with placeholders.
2. Input the required words when prompted.
3. View the generated Mad Libs story.

#### Example:

**Template:**
```
Today I went to the <place> and saw a <adjective> <animal> <verb>ing.
```

**User Input:**
```
Place: park
Adjective: funny
Animal: dog
Verb: dance
```

**Generated Story:**
```
Today I went to the park and saw a funny dog dancing.
```

### Customization:

- Add your own story templates by including placeholders in the text.
- Customize placeholder names to match specific themes (e.g., `<superhero>` or `<food>`).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mad-libs-generator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd mad-libs-generator
   ```
3. Run the program:
   ```bash
   python mad_libs_generator.py
   ```

## Input Validation

The program ensures:

- Handles empty or invalid inputs with prompts to try again.
- Strips extra spaces and corrects basic formatting issues.

## Customization

- Add options to randomize user input or select from preloaded word banks.
- Extend the program to support saving and sharing generated stories.
- Include themes like holidays, superheroes, or historical events for specialized templates.

## Requirements

- Python 3.7 or later

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Enjoy creating hilarious stories with the Mad Libs Generator! Let me know if you have any questions or suggestions!
