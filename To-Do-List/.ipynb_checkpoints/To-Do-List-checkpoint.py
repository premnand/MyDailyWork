tasks = {}

def add_task(tasks, task_name):
    task_id = len(tasks) + 1
    tasks[task_id] = {'name': task_name, 'status': 'pending'}
    print(f"Task '{task_name}' added with ID {task_id}.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task_id, details in tasks.items():
            print(f"ID: {task_id}, Name: {details['name']}, Status: {details['status']}")

def update_task(tasks, task_id, new_name=None, new_status=None):
    if task_id in tasks:
        if new_name:
            tasks[task_id]['name'] = new_name
        if new_status:
            tasks[task_id]['status'] = new_status
        print(f"Task ID {task_id} updated.")
    else:
        print("Task not found.")

def delete_task(tasks, task_id):
    if task_id in tasks:
        del tasks[task_id]
        print(f"Task ID {task_id} deleted.")
    else:
        print("Task not found.")

def main():
    while True:
        print("\nTo-Do List CLI")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task_name = input("Enter task name: ")
            add_task(tasks, task_name)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            new_name = input("Enter new task name (or press Enter to skip): ")
            new_status = input("Enter new status (pending/completed): ")
            update_task(tasks, task_id, new_name, new_status)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(tasks, task_id)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
