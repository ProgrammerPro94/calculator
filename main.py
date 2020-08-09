import tkinter as tk
import sympy as sp

# Making the window of our Calculator
root = tk.Tk()
root.wm_title('Calculator')
root.wm_geometry("1000x700")

# Text Variables
calc = tk.StringVar()
calc.set(0)

# Making the main text of our Calculator
text_frame = tk.Frame(root, bg="grey", width=1000, height=70, relief=tk.SUNKEN, borderwidth=3)
text_frame.pack(side=tk.TOP)

text_input = tk.Entry(text_frame, width=1000, justify=tk.RIGHT, font=("Times", 20, "bold"), textvariable=calc)
text_input.pack(fill=tk.BOTH)

# Making the frames of the buttons of our Calculator
but_frame = tk.Frame(root, width=400, height=600, relief=tk.RIDGE, borderwidth=2)
but_frame.pack(fill=tk.X, pady=10)


# Making the functions


def display_num(num):
    current_num = calc.get()
    if len(current_num) == 0:
        current_num = "0"
    if current_num[0] == "0":
        calc.set(current_num[1:] + str(num))
    else:
        calc.set(current_num + str(num))


def change_sign():
    current_num = calc.get()
    if current_num[0] != "0":
        if current_num[0] == "-":
            calc.set(current_num[1:])
        else:
            calc.set("-" + current_num)


def eval_expr():
    current_num = calc.get()
    try:
        calc.set(eval(current_num))
    except SyntaxError:
        calc.set("ERROR")


def empty_all():
    calc.set("0")


def delete_one():
    current_num = calc.get()
    calc.set(current_num[:-1])


def fact():
    n = int(eval(calc.get()))
    if n < 0:
        calc.set(sp.factorial(-n))
    else:
        calc.set(sp.factorial(n))


def square():
    calc.set(calc.get() + display_num('**2'))


def square_root():
    calc.set(pow(int(eval(calc.get())), (1/2)))


# Making Arithmetic Buttons
tk.Button(but_frame, width=10, height=2, text="(", command=lambda: display_num('(')).grid(row=0, column=0)
tk.Button(but_frame, width=10, height=2, text=")", command=lambda: display_num(')')).grid(row=0, column=1)
tk.Button(but_frame, width=10, height=2, text="C", command=delete_one).grid(row=0, column=2)
tk.Button(but_frame, width=10, height=2, text="/", command=lambda: display_num('/')).grid(row=0, column=3)

tk.Button(but_frame, width=10, height=2, text="7", command=lambda: display_num(7)).grid(row=1, column=0)
tk.Button(but_frame, width=10, height=2, text="8", command=lambda: display_num(8)).grid(row=1, column=1)
tk.Button(but_frame, width=10, height=2, text="9", command=lambda: display_num(9)).grid(row=1, column=2)

tk.Button(but_frame, width=10, height=2, text="4", command=lambda: display_num(4)).grid(row=2, column=0)
tk.Button(but_frame, width=10, height=2, text="5", command=lambda: display_num(5)).grid(row=2, column=1)
tk.Button(but_frame, width=10, height=2, text="6", command=lambda: display_num(6)).grid(row=2, column=2)

tk.Button(but_frame, width=10, height=2, text="1", command=lambda: display_num(1)).grid(row=3, column=0)
tk.Button(but_frame, width=10, height=2, text="2", command=lambda: display_num(2)).grid(row=3, column=1)
tk.Button(but_frame, width=10, height=2, text="3", command=lambda: display_num(3)).grid(row=3, column=2)

tk.Button(but_frame, width=10, height=2, text="±", command=change_sign).grid(row=4, column=0)
tk.Button(but_frame, width=10, height=2, text="0", command=lambda: display_num(0)).grid(row=4, column=1)
tk.Button(but_frame, width=10, height=2, text=".", command=lambda: display_num('.')).grid(row=4, column=2)

tk.Button(but_frame, width=10, height=2, text="+", command=lambda: display_num('+')).grid(row=1, column=3)
tk.Button(but_frame, width=10, height=2, text="-", command=lambda: display_num('-')).grid(row=2, column=3)
tk.Button(but_frame, width=10, height=2, text="X", command=lambda: display_num('*')).grid(row=3, column=3)
tk.Button(but_frame, width=10, height=2, text="=", command=eval_expr).grid(row=4, column=3)

tk.Button(but_frame, width=10, height=2, text="x!", command=fact).grid(row=1, column=4)
tk.Button(but_frame, width=10, height=2, text="x²", command=square).grid(row=2, column=4)
tk.Button(but_frame, width=10, height=2, text="√x", command=square_root).grid(row=3, column=4)

root.mainloop()
