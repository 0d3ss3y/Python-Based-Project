# Word Counter

## Overview

The **Word Counter** is a Python program designed to analyze a block of text and provide useful statistics. It counts the total words, characters (with and without spaces), sentences, and paragraphs, making it an essential tool for writers, students, and anyone working with text.

## Features

- Count:
  - Total words in the text.
  - Total characters (including and excluding spaces).
  - Total sentences.
  - Total paragraphs.
- Handles multiline text inputs.
- Provides robust input validation.

## Input Details

The program accepts a block of text as input, which can be:

- A single line of text.
- Multiple lines or paragraphs.

## Output

The program provides a detailed analysis of the text, including:

1. **Total Words**: The number of words in the text.
2. **Total Characters (With Spaces)**: The number of characters, including spaces.
3. **Total Characters (Without Spaces)**: The number of characters, excluding spaces.
4. **Total Sentences**: The number of sentences in the text.
5. **Total Paragraphs**: The number of paragraphs in the text.

### Example:

#### Input:
```
This is a sample text.
It has two sentences and two paragraphs.

Here is the second paragraph.
```

#### Output:
```
Total Words: 17
Total Characters (With Spaces): 94
Total Characters (Without Spaces): 76
Total Sentences: 3
Total Paragraphs: 2
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/word-counter.git
   ```
2. Navigate to the project directory:
   ```bash
   cd word-counter
   ```
3. Install any required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the program:
   ```bash
   python word_counter.py
   ```
2. Enter or paste the text you want to analyze when prompted.
3. View the analysis results displayed in the console.

## Input Validation

The program ensures:

- Handles empty input gracefully by prompting the user to enter text.
- Handles large text blocks efficiently without performance issues.

## Customization

- You can extend the program to count additional metrics, such as unique words or average sentence length.
- Modify text parsing rules (e.g., handling of punctuation or special characters) to suit specific needs.

## Requirements

- Python 3.7 or later

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

---

Feel free to reach out with any questions or suggestions!
