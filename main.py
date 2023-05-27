import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equals():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_operator(operator):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + operator)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the entry widget
entry = tk.Entry(window, width=20, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for button_text, row, column in buttons:
    button = tk.Button(window, text=button_text, width=5, height=2, font=("Arial", 12))
    button.grid(row=row, column=column, padx=5, pady=5)

    if button_text.isdigit() or button_text == ".":
        button.config(command=lambda number=button_text: button_click(number))
    elif button_text == "C":
        button.config(command=button_clear)
    elif button_text == "=":
        button.config(command=button_equals)
    else:
        button.config(command=lambda operator=button_text: button_operator(operator))

# Start the main loop
window.mainloop()
