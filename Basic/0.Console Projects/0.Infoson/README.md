# Personal Information Card Generator

## Overview

The **Personal Information Card Generator** is a Python-based program that takes user-provided details and formats them into a visually appealing digital card. This is a simple and customizable project ideal for creating personalized digital business cards or social profiles.

## Features

- User-friendly input prompts to collect information.
- Customizable output format and styles.
- Automatically validates user input for completeness.
- Outputs the card as a text-based display or saves it as an image file (optional).

## Input Details

The program collects the following user details:

- **Name**: First and last name.
- **Age**: User's age in years.
- **Hobbies**: A comma-separated list of hobbies.
- **Contact Information**: Email address or phone number.

## Output

The program generates a formatted digital card containing the provided information. You can customize the card's design in terms of layout, fonts, colors, and additional details. The card can be displayed on the console or saved as a file.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/personal-info-card-generator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd personal-info-card-generator
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the program:
   ```bash
   python main.py
   ```
2. Follow the prompts to enter your details.
3. View the generated digital card on the console or save it as an image (if configured).

## Example Output

### Console Display:
```
------------------------------
Name: John Doe
Age: 30
Hobbies: Reading, Hiking, Photography
Contact: john.doe@example.com
------------------------------
```

### Image File (Optional):
An image file named `personal_card.png` will be saved in the project directory.

## Customization

You can customize the card design by editing the following sections in the code:

- **Colors**: Modify the color scheme for the text and borders.
- **Font and Size**: Change the font style and size for the card's text.
- **Additional Fields**: Add more fields like address, social media links, etc.

## Requirements

- Python 3.7 or later
- Optional: `Pillow` library (for image generation)

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.
---

Feel free to reach out with any questions or suggestions!
