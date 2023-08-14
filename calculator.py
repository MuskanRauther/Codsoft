from tkinter import *

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(number))

def button_clear():
    entry.delete(0, END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result))
    except Exception:
        entry.delete(0, END)
        entry.insert(END, "Error")

def button_memory_add():
    memory["value"] += float(entry.get())

def button_memory_subtract():
    memory["value"] -= float(entry.get())

def button_memory_recall():
    entry.delete(0, END)
    entry.insert(END, str(memory["value"]))

def button_memory_clear():
    memory["value"] = 0

def button_sqrt():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result ** 0.5))
    except Exception:
        entry.delete(0, END)
        entry.insert(END, "Error")

root = Tk()
root.title("Calculator")

entry = Entry(root, width=40, justify=RIGHT)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

frame = Frame(root)
frame.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("M+", 1, 4),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("M-", 2, 4),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("MR", 3, 4),
    ("0", 4, 0),
    (".", 4, 1),
    ("=", 4, 2),
    ("+", 4, 3),
    ("MC", 4, 4),
    ("(", 5, 0),
    (")", 5, 1),
    ("√", 5, 2),
]

for button_text, row, column in buttons:
    button = Button(frame, text=button_text, width=7, padx=10, pady=10)
    button.grid(row=row, column=column)
    if button_text == "M+":
        button.config(command=button_memory_add)
    elif button_text == "M-":
        button.config(command=button_memory_subtract)
    elif button_text == "MR":
        button.config(command=button_memory_recall)
    elif button_text == "MC":
        button.config(command=button_memory_clear)
    elif button_text == "=":
        button.config(command=button_equal)
    elif button_text == "√":
        button.config(command=button_sqrt)
    else:
        button.config(command=lambda text=button_text: button_click(text))

clear_button = Button(frame, text="C", width=7, padx=10, pady=10, command=button_clear)
clear_button.grid(row=5, column=3)

root.mainloop()
