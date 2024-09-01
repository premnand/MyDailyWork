import tkinter as tk
from tkinter import messagebox
from models.task import Task
from models.task_manager import TaskManager

class MainWindow:
    def __init__(self, root):
        self.manager = TaskManager()
        self.root = root
        self.root.title("To-Do List Application")

        # Input Frame
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Task:").grid(row=0, column=0, padx=5)
        self.task_entry = tk.Entry(input_frame, width=40)
        self.task_entry.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Due Date:").grid(row=1, column=0, padx=5)
        self.due_entry = tk.Entry(input_frame, width=40)
        self.due_entry.grid(row=1, column=1, padx=5)

        tk.Label(input_frame, text="Priority:").grid(row=2, column=0, padx=5)
        self.priority_var = tk.StringVar(value="Normal")
        tk.OptionMenu(input_frame, self.priority_var, "Low", "Normal", "High").grid(row=2, column=1, padx=5, sticky='w')

        tk.Button(input_frame, text="Add Task", command=self.add_task).grid(row=3, column=1, pady=10, sticky='e')

        # Tasks List
        self.tasks_listbox = tk.Listbox(root, width=80)
        self.tasks_listbox.pack(pady=10)
        self.tasks_listbox.bind('<Double-1>', self.toggle_status)

        self.load_tasks()

    def load_tasks(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.manager.list_tasks():
            status = "✔" if task.status == "Complete" else "✘"
            self.tasks_listbox.insert(tk.END, f"[{status}] {task.description} (Due: {task.due_date}) [Priority: {task.priority}] ID: {task.id}")

    def add_task(self):
        description = self.task_entry.get()
        due_date = self.due_entry.get()
        priority = self.priority_var.get()
        if description:
            task = Task(description=description, due_date=due_date, priority=priority)
            self.manager.add_task(task)
            self.load_tasks()
            self.task_entry.delete(0, tk.END)
            self.due_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task description cannot be empty.")

    def toggle_status(self, event):
        selection = self.tasks_listbox.curselection()
        if selection:
            index = selection[0]
            task_str = self.tasks_listbox.get(index)
            task_id = task_str.split("ID: ")[1]
            task = self.manager.get_task(task_id)
            if task:
                new_status = "Complete" if task.status == "Incomplete" else "Incomplete"
                self.manager.update_task(task_id, status=new_status)
                self.load_tasks()
