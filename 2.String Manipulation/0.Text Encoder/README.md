# Safety: Text Encoder/Decoder

## Overview

**Safety** is a Python program designed to provide secure text encoding and decoding. It supports multiple encryption methods, including Caesar Cipher, XOR Encryption, Vigenère Encryption, and Base64 Encoding, ensuring flexible options for secure communication.

## Features

- **Encryption Methods**:
  - **Caesar Cipher**: Shifts text characters by a specified number of places.
  - **XOR Encryption**: Encodes text to binary or decodes binary to text.
  - **Vigenère Encryption**: Uses a keyword for substitution-based encryption.
  - **Base64 Encoding**: Encodes or decodes text using Base64.
- **User Interaction**:
  - Intuitive prompts to select methods and input options.
  - Options for encryption and decryption.
- **Error Handling**:
  - Validates input for each method.
  - Provides user-friendly error messages for invalid inputs.

## How It Works

1. **Select an Option**:
   - Choose between **Encryption** or **Decryption**.

2. **Choose a Method**:
   - Select one of the supported methods from a numbered list.

3. **Provide Input**:
   - Enter the text to be processed.
   - For some methods, additional inputs like shifts or keys are required.

4. **Receive Output**:
   - View the encrypted or decrypted result.

## Supported Methods

### 1. Caesar Cipher
- Shifts each letter in the text by a user-defined number.
- Handles both uppercase and lowercase letters.
- Example:
  - Input: `Hello`
  - Shift: `3`
  - Output: `Khoor` (Encryption) or `Ebiil` (Decryption).

### 2. XOR Encryption
- Converts text to binary or binary back to text.
- Example:
  - Input: `Hi`
  - Output: `0100100001101001` (Encryption).

### 3. Vigenère Encryption
- Uses a keyword for encoding and decoding text.
- Example:
  - Input: `HELLO`
  - Key: `KEY`
  - Output: `RIJVS` (Encryption).

### 4. Base64 Encoding
- Encodes or decodes text using Base64.
- Example:
  - Input: `Hello`
  - Output: `SGVsbG8=` (Encoding).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/safety-text-encoder-decoder.git
   ```
2. Navigate to the project directory:
   ```bash
   cd safety-text-encoder-decoder
   ```
3. Run the program:
   ```bash
   python safety.py
   ```

## Input Validation

- **Caesar Cipher**:
  - Ensures the shift value is between 0 and 25.
- **Vigenère Encryption**:
  - Validates that the key contains only alphabetic characters.
- **Base64 Encoding**:
  - Handles invalid Base64 input gracefully during decoding.

## Example Usage

1. Run the program:
   ```bash
   python safety.py
   ```
2. Select an option:
   ```
   Options:
   [E]ncryption
   [D]ecryption
   Select an option [D/E]: E
   ```
3. Choose a method:
   ```
   __Methods__
   [1] Caesar Cipher
   [2] XOR Encryption
   [3] Vigenère Encryption
   [4] Base64 Encoding
   Select a method [1-4]: 1
   ```
4. Provide input:
   ```
   Enter your text: Hello
   Enter shift value (0-25): 3
   Result (Encryption): Khoor
   ```

## Customization

- Add new encryption methods.
- Extend Base64 functionality for URL-safe encoding.
- Modify Caesar Cipher to support different alphabets.

## Requirements

- Python 3.7 or later

## Contributing

Contributions are welcome! Fork this repository, make improvements, and submit a pull request.

---

Feel free to reach out with any questions or suggestions!
