import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        todo_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def update_task():
    selected_task_index = todo_list.curselection()
    if selected_task_index:
        task = task_entry.get()
        if task:
            todo_list.delete(selected_task_index)
            todo_list.insert(selected_task_index, task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")
    else:
        messagebox.showwarning("Warning", "Select a task to update!")

def delete_task():
    selected_task_index = todo_list.curselection()
    if selected_task_index:
        todo_list.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Select a task to delete!")

app = tk.Tk()
app.title("To-Do List")
app.geometry("400x400")

app.configure(bg="#2e4053")

title_label = tk.Label(app, text="To-Do List", font=("Helvetica", 18), bg="#f0f0f0", fg="#333333")
title_label.pack(pady=10)

todo_list = tk.Listbox(app, width=50, bg="#ffffff", fg="#333333", selectbackground="#a6a6a6", selectforeground="#ffffff")
todo_list.pack(padx=10, pady=5)

task_entry = tk.Entry(app, width=50, bg="#ffffff", fg="#333333")
task_entry.pack(padx=10, pady=5)

add_button = tk.Button(app, text="Add Task", bg="#4caf50", fg="#ffffff", command=add_task)
add_button.pack(padx=10, pady=5)

update_button = tk.Button(app, text="Update Task", bg="#ffa500", fg="#ffffff", command=update_task)
update_button.pack(padx=10, pady=5)

delete_button = tk.Button(app, text="Delete Task", bg="#f44336", fg="#ffffff", command=delete_task)
delete_button.pack(padx=10, pady=5)

app.mainloop()
