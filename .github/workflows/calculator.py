import tkinter as tk
from tkinter import messagebox
import math
import sympy as sp

# Initialize the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")
root.config(bg="#2E2E2E")  # Dark theme background color

# Configure display
display_text = tk.StringVar()
display_entry = tk.Entry(root, textvar=display_text, font=("Arial", 18), bg="#333333", fg="white", bd=10, insertbackground="white")
display_entry.grid(row=0, column=0, columnspan=5, pady=20, sticky="nsew")

# Define button functions
def button_click(value):
    current_text = display_text.get()
    display_text.set(current_text + str(value))

def clear_display():
    display_text.set("")

def calculate():
    try:
        result = eval(display_text.get())
        display_text.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")

# Scientific functions
def factorial():
    try:
        result = math.factorial(int(display_text.get()))
        display_text.set(result)
    except:
        messagebox.showerror("Error", "Invalid Input")

def sin():
    result = math.sin(math.radians(float(display_text.get())))
    display_text.set(result)

def cos():
    result = math.cos(math.radians(float(display_text.get())))
    display_text.set(result)

def tan():
    result = math.tan(math.radians(float(display_text.get())))
    display_text.set(result)

def power():
    display_text.set(display_text.get() + "")

def square_root():
    try:
        result = math.sqrt(float(display_text.get()))
        display_text.set(result)
    except:
        messagebox.showerror("Error", "Invalid Input")

# Dark theme button style
button_config = {"font": ("Arial", 14), "bg": "#555555", "fg": "white", "width": 5, "height": 2, "bd": 5}

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('Clear', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('(', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), (')', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('^', 4, 3), ('=', 4, 4),
    ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('√', 5, 3), ('x!', 5, 4),
]

# Create buttons
for (text, row, col) in buttons:
    action = lambda x=text: button_click(x) if x not in ["=", "Clear", "sin", "cos", "tan", "√", "x!", "^"] else None
    if text == '=':
        btn = tk.Button(root, text=text, command=calculate, **button_config)
    elif text == 'Clear':
        btn = tk.Button(root, text=text, command=clear_display, **button_config)
    elif text == 'sin':
        btn = tk.Button(root, text=text, command=sin, **button_config)
    elif text == 'cos':
        btn = tk.Button(root, text=text, command=cos, **button_config)
    elif text == 'tan':
        btn = tk.Button(root, text=text, command=tan, **button_config)
    elif text == '√':
        btn = tk.Button(root, text=text, command=square_root, **button_config)
    elif text == 'x!':
        btn = tk.Button(root, text=text, command=factorial, **button_config)
    elif text == '^':
        btn = tk.Button(root, text=text, command=power, **button_config)
    else:
        btn = tk.Button(root, text=text, command=action, **button_config)
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
