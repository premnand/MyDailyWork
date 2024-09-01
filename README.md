# Mydailywork Repository

## Overview
This repository contains three Python command-line projects created for an internship. Each project is designed to solve a specific task: managing a to-do list, performing basic arithmetic calculations, and generating secure passwords.

## Projects

### 1. To-Do List CLI Application
- **Description**: A simple command-line interface (CLI) application for managing a to-do list. Users can add, view, update, and delete tasks. Each task is tracked with a unique ID and a status of either "pending" or "completed."
- **Features**:
  - Add Task
  - View Tasks
  - Update Task
  - Delete Task
  - Exit
- **Requirements**: Python 3.x
- **Usage**:
  - Run the Application.
  - Menu Options:
    - Add Task: Select option 1, then enter the task name.
    - View Tasks: Select option 2 to display all tasks.
    - Update Task: Select option 3, enter the task ID to update, and provide the new name or status.
    - Delete Task: Select option 4, then enter the task ID to delete.
    - Exit: Select option 5 to quit the application.

### 2. Simple Calculator
- **Description**: A command-line calculator implemented in Python. It evaluates arithmetic expressions and keeps a history of calculations.
- **Features**:
  - Basic Arithmetic Operations: Addition, subtraction, multiplication, and division.
  - Calculation History
  - Error Handling
  - Exit Command
  - History Command
- **Requirements**: Python 3.x
- **Usage**:
  - Run the Calculator.
  - Enter Calculations: Input arithmetic expressions like `2+2`, `5*3`, etc., and press Enter to see the result.
  - View History: Type `history` to display a list of previous calculations.
  - Exit the Program: Type `exit` to close the calculator.

### 3. Password Generator
- **Description**: A Python application that generates strong and random passwords based on user-defined length. The generated passwords use a combination of letters, digits, and special characters.
- **Features**:
  - User Input: Prompt the user to specify the desired length of the password.
  - Random Password Generation
  - Display Password
- **Requirements**: Python 3.x
- **Usage**:
  - Run the Application.
  - Specify Password Length: Enter the desired length when prompted.
  - View Generated Password: The application will generate and display a strong, random password.

## Error Handling
- **To-Do List CLI Application**:
  - Invalid Task ID: An appropriate error message is shown if a task ID does not exist.
  - Invalid Input: The application will prompt the user to try again if an invalid menu option is selected.
- **Simple Calculator**:
  - Invalid Syntax: An error message is shown for invalid syntax.
  - Invalid Characters: An error is returned for input containing invalid characters.
  - Division by Zero: Returns an appropriate error message.
- **Password Generator**:
  - Invalid Input: The application will prompt the user to try again if the input is not a positive integer.

## Security Considerations
- **Simple Calculator**: Uses `eval()` to evaluate expressions. While suitable for this simple example, be cautious with `eval()` in production environments.
- **Password Generator**: Uses Python's `random` module. For cryptographic purposes, consider using the `secrets` module instead.

## License
This repository is licensed under the MIT License.
