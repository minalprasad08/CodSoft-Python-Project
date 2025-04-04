import json
import tkinter as tk
from tkinter import ttk, messagebox

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from JSON
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save tasks to JSON
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Delete selected task
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        task_listbox.delete(index)
        del tasks[index]
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Update selected task
def update_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        new_task = task_entry.get()
        if new_task:
            tasks[index] = new_task
            task_listbox.delete(index)
            task_listbox.insert(index, new_task)
            task_entry.delete(0, tk.END)
            save_tasks()
        else:
            messagebox.showwarning("Warning", "Updated task cannot be empty!")
    else:
        messagebox.showwarning("Warning", "Please select a task to update!")

# Create main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")
root.configure(bg="#3F51B5")  # Deep Blue Background

# Load tasks
tasks = load_tasks()

# UI Elements
frame = ttk.Frame(root, padding=10)
frame.pack(pady=20)

task_entry = ttk.Entry(frame, width=40)
task_entry.pack(side=tk.LEFT, padx=5)

add_button = ttk.Button(frame, text="Add Task", command=add_task, style="Accent.TButton")
add_button.pack(side=tk.LEFT)

# Task Listbox
list_frame = ttk.Frame(root)
list_frame.pack(pady=20)

task_listbox = tk.Listbox(list_frame, width=50, height=15, bg="#9575CD", fg="white", font=("Arial", 12))  # Purple Background with White Text
task_listbox.pack(side=tk.LEFT)

# Scrollbar
scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=task_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.config(yscrollcommand=scrollbar.set)

# Load tasks into Listbox
for task in tasks:
    task_listbox.insert(tk.END, task)

# Buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

delete_button = ttk.Button(button_frame, text="Delete Task", command=delete_task, style="Danger.TButton")
delete_button.pack(side=tk.LEFT, padx=5)

update_button = ttk.Button(button_frame, text="Update Task", command=update_task, style="Accent.TButton")
update_button.pack(side=tk.LEFT, padx=5)

# Style Configuration
style = ttk.Style()
style.configure("Accent.TButton", background="#536DFE", foreground="black", font=("Arial", 10, "bold"))  # Light Blue Buttons
style.configure("Danger.TButton", background="#D500F9", foreground="black", font=("Arial", 10, "bold"))  # Bright Purple Buttons

# Run the application
root.mainloop()
