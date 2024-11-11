import tkinter as tk
from tkinter import messagebox, simpledialog
import math
import statistics
import cmath

# Initialize the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("500x700")
root.config(bg="#2E2E2E")  # Dark theme background color

# Display Entry
display_text = tk.StringVar()
display_entry = tk.Entry(root, textvar=display_text, font=("Arial", 18), bg="#333333", fg="white", bd=10, insertbackground="white")
display_entry.grid(row=0, column=0, columnspan=5, pady=20, sticky="nsew")

# Button functions
def button_click(value):
    display_text.set(display_text.get() + str(value))

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

def sinh():
    result = math.sinh(float(display_text.get()))
    display_text.set(result)

def cosh():
    result = math.cosh(float(display_text.get()))
    display_text.set(result)

def tanh():
    result = math.tanh(float(display_text.get()))
    display_text.set(result)

def power():
    display_text.set(display_text.get() + "")

def square_root():
    try:
        result = math.sqrt(float(display_text.get()))
        display_text.set(result)
    except:
        messagebox.showerror("Error", "Invalid Input")

def log():
    try:
        result = math.log(float(display_text.get()))
        display_text.set(result)
    except:
        messagebox.showerror("Error", "Invalid Input")

def exp():
    result = math.exp(float(display_text.get()))
    display_text.set(result)

def permutations():
    n = int(display_text.get())
    r = int(simpledialog.askstring("Input", "Enter r for P(n, r):"))
    result = math.perm(n, r)
    display_text.set(result)

def combinations():
    n = int(display_text.get())
    r = int(simpledialog.askstring("Input", "Enter r for C(n, r):"))
    result = math.comb(n, r)
    display_text.set(result)

# Statistical functions
def mean():
    data = [float(num) for num in display_text.get().split(',')]
    display_text.set(statistics.mean(data))

def median():
    data = [float(num) for num in display_text.get().split(',')]
    display_text.set(statistics.median(data))

def std_dev():
    data = [float(num) for num in display_text.get().split(',')]
    display_text.set(statistics.stdev(data))

# Dark theme button style
button_config = {"font": ("Arial", 12), "bg": "#555555", "fg": "white", "width": 5, "height": 2, "bd": 5}

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('Clear', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('(', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), (')', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('^', 4, 3), ('=', 4, 4),
    ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('√', 5, 3), ('x!', 5, 4),
    ('sinh', 6, 0), ('cosh', 6, 1), ('tanh', 6, 2), ('log', 6, 3), ('exp', 6, 4),
    ('Perm', 7, 0), ('Comb', 7, 1), ('Mean', 7, 2), ('Med', 7, 3), ('Std', 7, 4),
]

# Create buttons
for (text, row, col) in buttons:
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
    elif text == 'sinh':
        btn = tk.Button(root, text=text, command=sinh, **button_config)
    elif text == 'cosh':
        btn = tk.Button(root, text=text, command=cosh, **button_config)
    elif text == 'tanh':
        btn = tk.Button(root, text=text, command=tanh, **button_config)
    elif text == '√':
        btn = tk.Button(root, text=text, command=square_root, **button_config)
    elif text == 'x!':
        btn = tk.Button(root, text=text, command=factorial, **button_config)
    elif text == 'log':
        btn = tk.Button(root, text=text, command=log, **button_config)
    elif text == 'exp':
        btn = tk.Button(root, text=text, command=exp, **button_config)
    elif text == 'Perm':
        btn = tk.Button(root, text=text, command=permutations, **button_config)
    elif text == 'Comb':
        btn = tk.Button(root, text=text, command=combinations, **button_config)
    elif text == 'Mean':
        btn = tk.Button(root, text=text, command=mean, **button_config)
    elif text == 'Med':
        btn = tk.Button(root, text=text, command=median, **button_config)
    elif text == 'Std':
        btn = tk.Button(root, text=text, command=std_dev, **button_config)
    else:
        action = lambda x=text: button_click(x)
        btn = tk.Button(root, text=text, command=action, **button_config)
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
