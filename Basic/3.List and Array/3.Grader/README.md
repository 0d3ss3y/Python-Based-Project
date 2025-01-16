# Grade Management System

This Python application is a simple terminal-based Grade Management System that allows users to store and display grades for learners. It supports calculating averages and determining letter grades based on input percentages.

---

## Features
- **Store Grades**: Input and save grades for various subjects.
- **Display Grades**: View saved grades and calculated averages for all learners.
- **Grade Calculation**: Automatically calculate averages and assign letter grades.
- **Clear Terminal**: Clean the screen for better readability.
- **Graceful Exit**: Quit the application anytime safely.

---

## Getting Started

### Prerequisites
- Python 3.x

### Installation
1. Clone this repository or copy the script.
2. Ensure Python 3.x is installed on your system.
3. Run the script using the command:
   ```bash
   python grade_management.py
   ```

---

## How to Use

### Menu Options
When you run the program, you'll be presented with three options:

1. **Store Grades**:
   - Enter a learner's name.
   - Input grades for predefined subjects (Math, Science, English, History, Programming).
   - Ensure percentages are between 0 and 100.
   - The program calculates the average and assigns a letter grade.

2. **Display Grades**:
   - View the grades, averages, and letter grades for all learners stored in the system.

3. **Quit**:
   - Exit the program gracefully.

### Example Usage
1. Run the program:
   ```bash
   python grade_management.py
   ```
2. Choose "Store Grades" to input grades for a learner.
3. Choose "Display Grades" to see all saved report cards.
4. Choose "Quit" to exit the program.

---

## Code Overview

### Key Functions
- `clear_terminal()`: Clears the terminal screen for better readability.
- `option()`: Displays menu options and handles user input.
- `display_grades(report_card)`: Displays grades for all learners.
- `store_grades(report_card)`: Stores grades for a new learner and calculates averages and letter grades.
- `determine_level(score)`: Determines letter grades based on average scores.
- `main()`: Main loop for interacting with the user.

---

## Grade Calculation

| Score Range  | Letter Grade |
|--------------|--------------|
| 90% and above | A+          |
| 80%-89%       | A           |
| 70%-79%       | B           |
| 60%-69%       | C           |
| 50%-59%       | D           |
| 40%-49%       | E           |
| Below 40%     | F           |

---

## Example Output

```plaintext
__Grade System__

__Options__
[1] Store Grades
[2] Display Grades
[3] Quit

Enter your selection [1-3]: 1
Enter learner name: John Doe
Enter percentage received for Math: 85
Enter percentage received for Science: 90
Enter percentage received for English: 75
Enter percentage received for History: 80
Enter percentage received for Programming: 95
John Doe's grades have been added.

__Options__
[1] Store Grades
[2] Display Grades
[3] Quit

Enter your selection [1-3]: 2

__Report Cards__

John Doe's Report Card:
  Math: 85
  Science: 90
  English: 75
  History: 80
  Programming: 95
  Average: 85.0
  Letter: A
```

---

## Error Handling
- Ensures percentages are within a valid range (0-100).
- Handles invalid menu selections gracefully.

---

## Author
This script was developed as a demonstration of a basic Grade Management System in Python.

---