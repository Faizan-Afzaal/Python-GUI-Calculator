from tkinter import *
from tkinter import messagebox
from math import sqrt

# ================= WINDOW =================

root = Tk()
root.title("Advanced Python Calculator")
root.geometry("430x700")
root.configure(bg="#121212")
root.resizable(False, False)

# ================= VARIABLES =================

equation = ""
history = []

input_text = StringVar()

# ================= INPUT FIELD =================

title = Label(
    root,
    text="Advanced Calculator",
    font=("Arial", 24, "bold"),
    bg="#121212",
    fg="#ffffff"
)

title.pack(pady=10)

input_frame = Frame(root, bg="#121212")
input_frame.pack()

input_field = Entry(
    input_frame,
    textvariable=input_text,
    font=("Arial", 30),
    bd=0,
    bg="#1e1e1e",
    fg="white",
    justify=RIGHT,
    width=16
)

input_field.grid(row=0, column=0)
input_field.pack(ipady=20)

# ================= FUNCTIONS =================

def button_click(item):
    global equation
    equation += str(item)
    input_text.set(equation)


def clear():
    global equation
    equation = ""
    input_text.set("")


def calculate():
    global equation

    try:
        result = str(eval(equation))
        history.append(equation + " = " + result)

        input_text.set(result)
        equation = result

    except:
        input_text.set("Error")
        equation = ""


def square():
    global equation

    try:
        result = str(eval(equation) ** 2)

        history.append(f"Square({equation}) = {result}")

        input_text.set(result)
        equation = result

    except:
        input_text.set("Error")
        equation = ""


def square_root():
    global equation

    try:
        result = str(sqrt(eval(equation)))

        history.append(f"Sqrt({equation}) = {result}")

        input_text.set(result)
        equation = result

    except:
        input_text.set("Error")
        equation = ""


def percentage():
    global equation

    try:
        result = str(eval(equation) / 100)

        history.append(f"{equation}% = {result}")

        input_text.set(result)
        equation = result

    except:
        input_text.set("Error")
        equation = ""


def backspace():
    global equation

    equation = equation[:-1]
    input_text.set(equation)


def show_history():

    if not history:
        messagebox.showinfo("History", "No History Available")

    else:
        history_text = "\n".join(history)
        messagebox.showinfo("Calculation History", history_text)

# ================= BUTTONS FRAME =================

buttons_frame = Frame(root, bg="#121212")
buttons_frame.pack(pady=15)

button_style = {
    "font": ("Arial", 16, "bold"),
    "bd": 0,
    "fg": "white",
    "width": 6,
    "height": 2
}

# ================= ROW 1 =================

Button(buttons_frame, text="C", bg="#ff3b30",
       command=clear, **button_style).grid(row=0, column=0, padx=5, pady=5)

Button(buttons_frame, text="⌫", bg="#ff9500",
       command=backspace, **button_style).grid(row=0, column=1, padx=5, pady=5)

Button(buttons_frame, text="%", bg="#5856d6",
       command=percentage, **button_style).grid(row=0, column=2, padx=5, pady=5)

Button(buttons_frame, text="/", bg="#ff9500",
       command=lambda: button_click("/"), **button_style).grid(row=0, column=3, padx=5, pady=5)

# ================= ROW 2 =================

Button(buttons_frame, text="7", bg="#2c2c2e",
       command=lambda: button_click(7), **button_style).grid(row=1, column=0, padx=5, pady=5)

Button(buttons_frame, text="8", bg="#2c2c2e",
       command=lambda: button_click(8), **button_style).grid(row=1, column=1, padx=5, pady=5)

Button(buttons_frame, text="9", bg="#2c2c2e",
       command=lambda: button_click(9), **button_style).grid(row=1, column=2, padx=5, pady=5)

Button(buttons_frame, text="*", bg="#ff9500",
       command=lambda: button_click("*"), **button_style).grid(row=1, column=3, padx=5, pady=5)

# ================= ROW 3 =================

Button(buttons_frame, text="4", bg="#2c2c2e",
       command=lambda: button_click(4), **button_style).grid(row=2, column=0, padx=5, pady=5)

Button(buttons_frame, text="5", bg="#2c2c2e",
       command=lambda: button_click(5), **button_style).grid(row=2, column=1, padx=5, pady=5)

Button(buttons_frame, text="6", bg="#2c2c2e",
       command=lambda: button_click(6), **button_style).grid(row=2, column=2, padx=5, pady=5)

Button(buttons_frame, text="-", bg="#ff9500",
       command=lambda: button_click("-"), **button_style).grid(row=2, column=3, padx=5, pady=5)

# ================= ROW 4 =================

Button(buttons_frame, text="1", bg="#2c2c2e",
       command=lambda: button_click(1), **button_style).grid(row=3, column=0, padx=5, pady=5)

Button(buttons_frame, text="2", bg="#2c2c2e",
       command=lambda: button_click(2), **button_style).grid(row=3, column=1, padx=5, pady=5)

Button(buttons_frame, text="3", bg="#2c2c2e",
       command=lambda: button_click(3), **button_style).grid(row=3, column=2, padx=5, pady=5)

Button(buttons_frame, text="+", bg="#ff9500",
       command=lambda: button_click("+"), **button_style).grid(row=3, column=3, padx=5, pady=5)

# ================= ROW 5 =================

Button(buttons_frame, text="√", bg="#5856d6",
       command=square_root, **button_style).grid(row=4, column=0, padx=5, pady=5)

Button(buttons_frame, text="x²", bg="#5856d6",
       command=square, **button_style).grid(row=4, column=1, padx=5, pady=5)

Button(buttons_frame, text="History", bg="#34c759",
       command=show_history, **button_style).grid(row=4, column=2, padx=5, pady=5)

Button(buttons_frame, text="=", bg="#34c759",
       command=calculate, **button_style).grid(row=4, column=3, padx=5, pady=5)

# ================= FOOTER =================

footer = Label(
    root,
    text="Made with Python & Tkinter",
    font=("Arial", 10),
    bg="#121212",
    fg="#777777"
)

footer.pack(pady=10)

# ================= RUN =================

root.mainloop()