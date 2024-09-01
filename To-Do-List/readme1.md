# To-Do List CLI Application

## Overview

This is a simple command-line interface (CLI) application for managing a to-do list. The application allows users to add, view, update, and delete tasks. Each task is tracked with a unique ID and a status of either "pending" or "completed."

## Features

- **Add Task**: Add a new task to the to-do list with a unique ID.
- **View Tasks**: Display all tasks with their IDs, names, and statuses.
- **Update Task**: Modify the name or status of an existing task.
- **Delete Task**: Remove a task from the list by its ID.
- **Exit**: Close the application.

## Requirements

- Python 3.x

## Usage

1. **Run the Application**:
   - Execute the script using Python:
     ```bash
     python todolist.py
     ```

2. **Menu Options**:
   - **Add Task**: Select option `1`, then enter the task name.
   - **View Tasks**: Select option `2` to display all tasks.
   - **Update Task**: Select option `3`, enter the task ID to update, and provide the new name or status.
   - **Delete Task**: Select option `4`, then enter the task ID to delete.
   - **Exit**: Select option `5` to quit the application.

## Example
```
To-Do List CLI
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit 
    Enter your choice (1-5): 1 
    Enter task name: Buy groceries 
    Task 'Buy groceries' added with ID 1.

To-Do List CLI
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit 
    Enter your choice (1-5): 2 
    ID: 1, Name: Buy groceries, Status: pending

To-Do List CLI
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit 
    Enter your choice (1-5): 3 
    Enter task ID to update: 1 
    Enter new task name (or press Enter to skip): Buy groceries and milk 
    Enter new status (pending/completed): completed 
    Task ID 1 updated.

To-Do List CLI
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit 
    Enter your choice (1-5): 4 
    Enter task ID to delete: 1 
    Task ID 1 deleted.

To-Do List CLI
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit 
    Enter your choice (1-5): 5 
    Exiting the application. Goodbye!
```


## Error Handling

- **Invalid Task ID**: If a task ID does not exist, an appropriate error message will be shown.
- **Invalid Input**: If an invalid menu option is selected, the application will prompt the user to try again.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
