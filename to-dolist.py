import tkinter as tk
from tkinter import messagebox
import random

def add_task():
    task = task_entry.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_all_tasks():
    listbox_tasks.delete(0, tk.END)

def sort_ascending():
    tasks = list(listbox_tasks.get(0, tk.END))
    tasks.sort()
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        listbox_tasks.insert(tk.END, task)

def sort_descending():
    tasks = list(listbox_tasks.get(0, tk.END))
    tasks.sort(reverse=True)
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        listbox_tasks.insert(tk.END, task)

def choose_random():
    tasks = list(listbox_tasks.get(0, tk.END))
    if tasks:
        random_task = random.choice(tasks)
        messagebox.showinfo("Random Task", f"Your random task is:\n\n{random_task}")
    else:
        messagebox.showwarning("Warning", "No tasks available to choose from.")

def show_number_of_tasks():
    tasks = listbox_tasks.get(0, tk.END)
    messagebox.showinfo("Number of Tasks", f"Total number of tasks: {len(tasks)}")

def exit_app():
    root.destroy()

# Set up the main window
root = tk.Tk()
root.title("To-Do List")

# Create GUI components
frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=5)

button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()

button_clear_all = tk.Button(root, text="Clear All Tasks", width=48, command=clear_all_tasks)
button_clear_all.pack()

button_sort_asc = tk.Button(root, text="Sort Tasks (A-Z)", width=48, command=sort_ascending)
button_sort_asc.pack()

button_sort_desc = tk.Button(root, text="Sort Tasks (Z-A)", width=48, command=sort_descending)
button_sort_desc.pack()

button_random_task = tk.Button(root, text="Choose Random Task", width=48, command=choose_random)
button_random_task.pack()

button_number_of_tasks = tk.Button(root, text="Show Number of Tasks", width=48, command=show_number_of_tasks)
button_number_of_tasks.pack()

button_exit = tk.Button(root, text="Exit", width=48, command=exit_app)
button_exit.pack(pady=10)

# Run the main loop
root.mainloop()
