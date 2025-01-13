# Doers: To-Do List Manager

## Overview

**Doers** is a Python-based to-do list manager designed to help users efficiently manage their tasks. It allows users to add, remove, and mark tasks as completed, assign priority levels, and save tasks to a file for persistence. The program is ideal for organizing daily routines and keeping track of important tasks.

## Features

- **Task Management**:
  - Add new tasks with descriptions.
  - Remove tasks by their identifiers.
  - Mark tasks as completed.
- **Priority Levels**:
  - Assign priority levels (e.g., High, Medium, Low) to tasks.
  - Sort tasks by priority for better organization.
- **File Persistence**:
  - Save tasks to a file for future reference.
  - Load tasks from a saved file.
- **User-Friendly Interface**:
  - Intuitive commands for managing the to-do list.
  - Display tasks in an organized format.

## Usage Details

### Adding Tasks:

Input the task description and optionally specify a priority level. If no priority is given, a default level (e.g., "Medium") will be assigned.

#### Example:
```
Add Task: Buy groceries
Priority: High
```

### Removing Tasks:

Specify the task ID or description to remove it from the list.

#### Example:
```
Remove Task: 1
```

### Marking Tasks as Completed:

Mark a task as completed by its ID or description. Completed tasks will be visually distinguished.

#### Example:
```
Complete Task: 2
```

### Saving and Loading Tasks:

- Save the current tasks to a file:
  ```
  Save to File: tasks.txt
  ```
- Load tasks from a file:
  ```
  Load from File: tasks.txt
  ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/doers.git
   ```
2. Navigate to the project directory:
   ```bash
   cd doers
   ```
3. Run the program:
   ```bash
   python doers.py
   ```

## Input Validation

The program ensures:

- Task descriptions are non-empty.
- Priority levels match predefined options (e.g., High, Medium, Low).
- File paths are valid for saving and loading tasks.

## Improvements

- Extend to support recurring tasks with deadlines.
- Add a search feature to filter tasks by keyword or priority.
- Integrate with calendar applications for reminders.
- Include a graphical user interface (GUI) for enhanced usability.

## Requirements

- Python 3.7 or later

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

---

Organize your tasks efficiently with Doers! Let me know if you have any questions or suggestions.
