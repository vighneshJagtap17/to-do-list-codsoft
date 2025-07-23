import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# GUI Setup
root = tk.Tk()
root.title("To-Do List")

# Input field
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack()

delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

# Listbox to display tasks
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Run the app
root.mainloop()
