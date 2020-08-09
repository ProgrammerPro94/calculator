import tkinter as tk
from tkinter import simpledialog as force
from tkinter import *
import sympy as sp
from sympy.abc import x, k, a
from sympy import *
from sympy.parsing.sympy_parser import parse_expr, \
    standard_transformations, implicit_multiplication_application
import numpy as np
import matplotlib.pyplot as plt
import random




# TODO: Configuring window
root = tk.Tk()
root.geometry("1000x450")
# root.minsize(1000, 450)
# root.maxsize(1000, 450)
root.title("Calculator")
root.configure(bg="cadet blue")


# TODO: FUNCTION
def stat():
    root2 = Tk()
    root2.geometry("400x600")
    root2.configure(bg="cadet blue")

    scroll = Scrollbar(root2)
    scroll.pack(fill=Y, side=RIGHT)
    view = Listbox(root2, yscrollcommand=scroll.set, bg="powder blue")
    view.pack(fill=X)

    scroll.config(command=view.yview)

    text2 = StringVar()
    Entry(root2, bg="powder blue", textvariable=text2, font="lacinda 16 bold").pack(fill=X)

    buttonF = Frame(root2, bg="powder blue")
    buttonF.pack(fill="both")

    # Functions
    global mylist
    mylist = []

    def add():
        if text2.get() != "":
            num = text2.get()
            mylist.append(int(num))
            view.insert(END, num)
        else:
            text2.set(0)

    def delete():
        try:
            index = view.index(ACTIVE)
            view.delete(index)
            mylist.pop(int(index))
            print(mylist)
        except Exception as e:
            text2.set(0)

    def randoml():
        view.delete(0, END)
        mylist.clear()
        rand_list = []
        for i in range(10):
            rand = random.randint(0, 1000)
            rand_list.append(rand)
        for i in rand_list:
            mylist.append(i)
            view.insert(END, i)

    def remove():
        view.delete(0, END)
        mylist.clear()

    def sumAll():
        text2.set(sum(mylist))
        root2.update()

    def count():
        text2.set(len(mylist))

    def mean():
        text2.set(np.mean(mylist))
        return np.mean(mylist)

    def median():
        text2.set(np.median(mylist))
        return np.median(mylist)

    def mode():
        answer = 3 * (median()) - 2 * (mean())

        text2.set(answer)

    def plot2():
        plt.plot(mylist)
        plt.show()

    def number(num):
        text2.set(text2.get() + str(num))

    def back():
        try:
            go = text2.get()
            go_list = list(go)
            length = len(go_list)
            go_list.pop(length - 1)
            final = go_list[0]
            for i in go_list[1:]:
                final = final + i
            text2.set(final)
        except Exception as e:
            text2.set("")

    # Buttons
    Button(buttonF, text="add", command=add, bg="powder blue", width=10).grid(row=0, column=0)
    Button(buttonF, text="delete", command=delete, bg="powder blue", width=10).grid(row=0, column=1)
    Button(buttonF, text="random", command=randoml, bg="powder blue", width=10).grid(row=0, column=2)
    Button(buttonF, text="remove", command=remove, bg="powder blue", width=10).grid(row=0, column=3)

    Button(buttonF, text="sum", command=sumAll, bg="powder blue", width=10).grid(row=1, column=0)
    Button(buttonF, text="count", command=count, bg="powder blue", width=10).grid(row=2, column=0)
    Button(buttonF, text="mean", command=mean, bg="powder blue", width=10).grid(row=3, column=0)
    Button(buttonF, text="median", command=median, bg="powder blue", width=10).grid(row=4, column=0)

    Button(buttonF, text="mode", command=mode, bg="powder blue", width=10).grid(row=5, column=0)
    Button(buttonF, text="plot", command=plot2, bg="powder blue", width=10).grid(row=6, column=0)

    Button(buttonF, text="1", command=lambda: number(1), bg="powder blue", width=10).grid(row=1, column=1)
    Button(buttonF, text="2", command=lambda: number(2), bg="powder blue", width=10).grid(row=1, column=2)
    Button(buttonF, text="3", command=lambda: number(3), bg="powder blue", width=10).grid(row=1, column=3)
    Button(buttonF, text="4", command=lambda: number(4), bg="powder blue", width=10).grid(row=2, column=1)
    Button(buttonF, text="5", command=lambda: number(5), bg="powder blue", width=10).grid(row=2, column=2)
    Button(buttonF, text="6", command=lambda: number(6), bg="powder blue", width=10).grid(row=2, column=2)
    Button(buttonF, text="7", command=lambda: number(7), bg="powder blue", width=10).grid(row=2, column=3)
    Button(buttonF, text="8", command=lambda: number(8), bg="powder blue", width=10).grid(row=3, column=1)
    Button(buttonF, text="9", command=lambda: number(9), bg="powder blue", width=10).grid(row=3, column=2)
    Button(buttonF, text="0", command=lambda: number(0), bg="powder blue", width=10).grid(row=3, column=3)

    Button(buttonF, text="<--", command=back, bg="powder blue", width=10).grid(row=4, column=1)
    root2.mainloop()


def date():
    import tkinter as tk
    from tkinter import ttk
    # import tkcalendar as tc
    import datetime

    win = tk.Tk()
    win.geometry("700x500")
    win.title("Date Calculation")
    win.configure(bg="cadet blue")

    things = ['difference between two dates', 'add or subtract two dates']
    combo = tk.StringVar()

    ttk.Combobox(win, values=things, width=40, textvariable=combo).pack()

    def diff():
        button_f = tk.Frame(win, bg="cadet blue")
        button_f.pack(pady=40, anchor="w")
        starting_date = tk.StringVar()
        ending_date = tk.StringVar()
        ans = tk.StringVar()
        tk.Label(button_f, bg="powder blue", textvariable=ans, font="lacinda 16 bold", width=20) \
            .grid(row=3, column=1, padx=5)

        def get_difference(fd, sd):
            day, month, year = fd.split("/")
            day1, month1, year1 = sd.split("/")
            d1 = datetime.date(year=int(year), month=int(month), day=int(day))
            d2 = datetime.date(year=int(year1), month=int(month1), day=int(day1))
            difference = d2 - d1
            ans.set(str(difference.days) + "day(s)")

        tk.Label(button_f, bg="powder blue", text="Enter the starting date: ", font="lacinda 16 bold") \
            .grid(row=0, column=0, padx=5)
        tk.Entry(button_f, bg="powder blue", textvariable=starting_date, font="lacinda 16 bold") \
            .grid(row=0, column=1)
        tk.Label(button_f, bg="powder blue", text="Enter the ending date: ", font="lacinda 16 bold") \
            .grid(row=1, column=0, padx=5, pady=20)
        tk.Entry(button_f, bg="powder blue", textvariable=ending_date, font="lacinda 16 bold") \
            .grid(row=1, column=1, pady=20)
        tk.Button(button_f, bg="powder blue", text="difference", font="lacinda 16 bold",
                  command=lambda: get_difference(starting_date.get(), ending_date.get())) \
            .grid(row=2, column=1, pady=20)

    def to_date():

        ch1 = tk.IntVar()
        starting_date = tk.StringVar()
        days = tk.IntVar()
        starting_date1 = tk.StringVar()
        days1 = tk.IntVar()
        addlabel = tk.StringVar()
        b2f = tk.Frame(bg="cadet blue")
        b2f.pack(pady=20)
        tk.Radiobutton(b2f, variable=ch1, value=1, text="add", bg="powder blue", font="lacinda 12 bold") \
            .grid(row=0, column=0, padx=30)
        tk.Radiobutton(b2f, variable=ch1, value=2, text="subtract", bg="powder blue",
                       font="lacinda 12 bold").grid(row=0, column=1, padx=60)

        def cr():
            sub.configure(state=tk.DISABLED)
            tk.Label(b2f, bg="powder blue", text="Enter the starting date: ", width=10, font="lacinda 16 bold",
                     textvariable=addlabel) \
                .grid(row=5, column=0, pady=5)

            def add(fd, fnday):
                day, month, year = fd.split("/")
                day1 = datetime.date(year=int(year), month=int(month), day=int(day))
                answer = day1 + datetime.timedelta(days=fnday)
                answer1 = str(answer)
                # answer_day = datetime.datetime.strptime(answer1, '%Y-%d-%B').strftime('%A')
                addlabel.set(f"{str(answer)}")

            def subtract(fd, fnday):
                day, month, year = fd.split("/")
                day1 = datetime.date(year=int(year), month=int(month), day=int(day))
                answer = day1 - datetime.timedelta(days=fnday)
                answer1 = str(answer)
                # answer_day = datetime.datetime.strptime(answer1, '%Y-%d-%B').strftime('%A')
                addlabel.set(f"{str(answer)}")

            if ch1.get() == 1:
                tk.Label(b2f, bg="powder blue", text="Enter the starting date: ", font="lacinda 16 bold") \
                    .grid(row=2, column=0, pady=5)
                tk.Entry(b2f, bg="powder blue", textvariable=starting_date, font="lacinda 16 bold") \
                    .grid(row=2, column=1)
                tk.Label(b2f, bg="powder blue", text="Enter the number of days: ", font="lacinda 16 bold") \
                    .grid(row=3, column=0, pady=5)
                tk.Entry(b2f, bg="powder blue", textvariable=days, font="lacinda 16 bold") \
                    .grid(row=3, column=1)
                tk.Button(b2f, text="getdate", bg="powder blue",
                          font="lacinda 12 bold", command=lambda: add(starting_date.get(), days.get())).grid(row=4,
                                                                                                             column=1,
                                                                                                             pady=10)

            if ch1.get() == 2:
                tk.Label(b2f, bg="powder blue", text="Enter the starting date: ", font="lacinda 16 bold") \
                    .grid(row=2, column=0, pady=5)
                tk.Entry(b2f, bg="powder blue", textvariable=starting_date1, font="lacinda 16 bold") \
                    .grid(row=2, column=1)
                tk.Label(b2f, bg="powder blue", text="Enter the number of days: ", font="lacinda 16 bold") \
                    .grid(row=3, column=0, pady=5)
                tk.Entry(b2f, bg="powder blue", textvariable=days1, font="lacinda 16 bold") \
                    .grid(row=3, column=1)
                tk.Button(b2f, text="getdate", bg="powder blue",
                          font="lacinda 12 bold", command=lambda: subtract(starting_date1.get(), days1.get())).grid(
                    row=4,
                    column=1,
                    pady=10)

        sub = tk.Button(b2f, text="submit", bg="powder blue", font="lacinda 12 bold", command=cr)
        sub.grid(row=1, column=1, pady=10)

    def go():

        if combo.get() == things[0]:
            diff()
        else:
            to_date()

    submit = tk.Button(win, text="submit", bg="powder blue", font="lacinda 12 bold", command=go)
    submit.pack()
    win.mainloop()


def text_view(args):
    if args == "zoo":
        force.messagebox.showerror("error", "your answer is string which is "
                                            "infinity count be shown on screen")


def delete(func):
    try:
        func()
    except Exception as e:
        text.set("ERROR")


# TODO: Frames and TextView and variables and status bar
Text_f = tk.Frame(root)
Text_f.pack(side=tk.TOP)

text = tk.StringVar()
status_val = tk.StringVar()
strtext = tk.StringVar()
view = tk.Entry(Text_f, bg="powder blue", relief=tk.RIDGE, bd=20, fg="dark blue", width=1000,
                font="comicsans 14 bold", textvariable=text)
view.pack()

status = tk.Label(root, bg="powder blue", fg="black", relief=tk.SUNKEN, font="lacinda 14 bold",
                  text="Ready", justify=tk.LEFT)
status.pack(fill=tk.X, side=tk.BOTTOM)

# TODO: Other frames

button_f = tk.Frame(root, bd=10, bg="powder blue", relief=tk.RIDGE)
button_f.pack(side=tk.TOP, anchor=tk.W)


# TODO: functions
def asin(num):
    return text.set((sp.asin(num) * 180 / sp.pi).evalf())


def atan(num):
    return text.set((sp.atan(num) * 180 / sp.pi).evalf())


def acos(num):
    return text.set((sp.acos(num) * 180 / sp.pi).evalf())


def sin(num):
    return text.set((sp.sin(float(num) * sp.pi / 180)).evalf())


def cos(num):
    return text.set((sp.cos(float(num) * sp.pi / 180)).evalf())


def tan(num):
    return text.set((sp.tan(float(num) * sp.pi / 180)).evalf())


def asinh(num):
    return text.set((sp.asinh(num) * sp.pi / 180).evalf())


def atanh(num):
    return text.set((sp.acosh(num) * sp.pi / 180).evalf())


def acosh(num):
    return text.set((sp.atanh(num) * sp.pi / 180).evalf())


def sinh(num):
    return text.set((sp.sinh(deg(float(num)))).evalf())


def cosh(num):
    return text.set((sp.cosh(float(num) * 180 / sp.pi)).evalf())


def tanh(num):
    return text.set((sp.tanh(float(num) * 180 / sp.pi)).evalf())


def log(num):
    base = force.askstring("LOG", "Enter the base of the log")

    return text.set(sp.log(float(num), base).evalf())


def ln(num):
    text.set((sp.ln(num)).evalf())


def pi():
    text.set(text.get() + str(sp.pi.evalf()))


def e(num):
    text.set((sp.exp(num)).evalf())


def integrate():
    x = sp.Symbol('x')
    function1 = force.askstring("integrate", "Enter the function we will ∫ with respect to x:")
    transformations = (standard_transformations + (implicit_multiplication_application,))
    string3 = parse_expr(function1, transformations=transformations)
    integ = sp.integrate(string3, x)
    root.update()
    status_val.set("Busy in integrating")

    force.messagebox.showinfo("integrate", f"your answer is {integ}")


def clear():
    text.set("")


def solve_eq():
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r = sp.symbols("a,b,c,d,e,f,g,h,i,j,k, l, m, n, o, p, q, r")
    s, t, u, v, w, x, y, z = sp.symbols("s,t,u,v,w,x,y,z")

    no_eq = force.askinteger("solve", "Enter the number of equations you have: ")
    equations = []
    while no_eq != 0:
        dialog = force.askstring(no_eq, "Enter the equation: ")
        split = dialog.split("=")
        transformations = (standard_transformations + (implicit_multiplication_application,))
        string3 = parse_expr(split[0], transformations=transformations)
        transformations = (standard_transformations + (implicit_multiplication_application,))
        string4 = parse_expr(split[1], transformations=transformations)
        Equation = Eq(string3, string4)
        equations.append(Equation)
        no_eq -= 1
    solved = sp.solve((equations))
    force.messagebox.showinfo("solve", solved)


def derivative():
    x = sp.Symbol('x')
    function = force.askstring("derivative", "Enter the function we will derivative"
                                             " with respect to x:")
    transformations = (standard_transformations + (implicit_multiplication_application,))
    string3 = parse_expr(function, transformations=transformations)
    integ = sp.diff(string3, x)
    force.messagebox.showinfo("derivative", f"your answer is {integ}")


def number(num):
    try:
        if num == "=":

            transformations = (standard_transformations + (implicit_multiplication_application,))
            string3 = parse_expr(text.get(), transformations=transformations)


            half = ((sp.simplify(string3)).evalf())
            # half2 = ((sp.factor(half)).evalf())
            half2 = sp.expand(half)
            text.set(sp.simplify(half2))
        else:
            text.set((text.get() + str(num)))
    except:
        text.set("ERROR")


def simplify():
    function = force.askstring("simplify", "Enter the algebra")
    transformations = (standard_transformations + (implicit_multiplication_application,))
    string3 = parse_expr(function, transformations=transformations)
    answer = sp.factor(string3)
    answer1 = sp.simplify(answer)
    force.messagebox.showinfo("simplify", f"answer is {answer1}")


def plot():
    function = force.askstring("plot", "Enter the function: ")
    transformations = (standard_transformations + (implicit_multiplication_application,))
    string3 = parse_expr(function, transformations=transformations)
    # force.messagebox.showinfo("plot", "Your plot is shown in console")
    sp.plotting.plot(string3)


def backspace():
    try:
        go = text.get()
        go_list = list(go)
        length = len(go_list)
        go_list.pop(length - 1)
        final = go_list[0]
        for i in go_list[1:]:
            final = final + i
        text.set(final)
    except Exception as e:
        text.set("")


def powerk():
    r = text.get()
    if 'x' in text.get():
        g = force.askstring("power", f"Enter the power of {r}")
        num = "(" + str(r) + ")" + "**" + str(g)
        transformations = (standard_transformations + (implicit_multiplication_application,))
        string3 = parse_expr(num, transformations=transformations)
        text.set(sp.expand(string3))


    else:
        g = force.askfloat("power", f"Enter the power of {r}")

        text.set(float(r)**g)



def hcf():
    strig = force.askstring("hcf", "Enter the numbers")
    text.set(sp.gcd((strig)))


def lcm():
    strig = force.askstring("lcm", "Enter the numbers")
    text.set(sp.lcm((strig)))


def ap():
    global formula
    formula = force.askstring("A.p", "Enter the formula")
    if text.get() == "":
        force.messagebox.showerror("error", "nothing in text view")
    else:
        aps.configure(state=tk.NORMAL)


def sub_formula(formulas):
    list_n = list(formulas)
    stop = 0
    for i in list_n:
        if i == "x":
            list_n.pop(stop)
            list_n.insert(stop, float(text.get()))
        stop += 1
    final = list_n[0]
    for i in list_n[1:]:
        final = str(final) + str(i)

    transformations = (standard_transformations + (implicit_multiplication_application,))
    string3 = parse_expr(final, transformations=transformations)
    text.set((sp.simplify(string3)).evalf())


def ap2():
    sub_formula(formula)


def si_trans():
    fun = force.askstring("sine_transform", "Enter the function with x and a")
    force.messagebox.showinfo("sine_transform", f"{sp.sine_transform(fun, x, k)}")


def cos_trans():
    fun = force.askstring("cosine_transform", "Enter the function with x and a")
    force.messagebox.showinfo("cosine_transform", f"{sp.cosine_transform(fun, x, k)}")


def laplace_trans():
    fun = force.askstring("laplace_transform", "Enter the function with x and a")
    force.messagebox.showinfo("laplace_transform", f"{sp.laplace_transform(fun, x, k)}")


def series():
    fun = force.askstring("series", "Enter the function: ")
    force.messagebox.showinfo("series", f"{sp.series(fun)}")


def frac(num):
    dec_length = len(str(num).split(".")[1])
    string = 1
    for i in range(dec_length):
        string = str(string) + str(0)
    num = str(num).replace(".", "")
    hcf1 = sp.gcd(int(num), int(string))
    frac_num = int(num) // int(hcf1)
    frac_denum = int(string) // int(hcf1)
    fstring = f"numerator is {frac_num} and denomerator is {frac_denum}"
    force.messagebox.showinfo("fraction", fstring)


# TODO:  Trig Buttons

tk.Button(button_f, text="sin", font="comicsans 14 bold", fg="black",
          command=lambda: sin(text.get()), width=7, bg="powder blue").grid(row=0, column=0)
tk.Button(button_f, text="cos", font="comicsans 14 bold", fg="black",
          command=lambda: cos(text.get()), width=7, bg="powder blue").grid(row=1, column=0)
tk.Button(button_f, text="tan", font="comicsans 14 bold", fg="black",
          command=lambda: tan(text.get()), width=7, bg="powder blue").grid(row=2, column=0)

tk.Button(button_f, text="asin", font="comicsans 14 bold", fg="black",
          command=lambda: asin(text.get()), width=7, bg="powder blue").grid(row=0, column=1)
tk.Button(button_f, text="acos", font="comicsans 14 bold", fg="black",
          command=lambda: acos(text.get()), width=7, bg="powder blue").grid(row=1, column=1)
tk.Button(button_f, text="atan", font="comicsans 14 bold", fg="black",
          command=lambda: atan(text.get()), width=7, bg="powder blue").grid(row=2, column=1)

tk.Button(button_f, text="sinh", font="comicsans 14 bold", fg="black",
          command=lambda: sinh(text.get()), width=7, bg="powder blue").grid(row=3, column=0)
tk.Button(button_f, text="cosh", font="comicsans 14 bold", fg="black",
          command=lambda: cosh(text.get()), width=7, bg="powder blue").grid(row=4, column=0)
tk.Button(button_f, text="tanh", font="comicsans 14 bold", fg="black",
          command=lambda: tanh(text.get()), width=7, bg="powder blue").grid(row=5, column=0)

tk.Button(button_f, text="asinh", font="comicsans 14 bold", fg="black",
          command=lambda: asinh(text.get()), width=7, bg="powder blue").grid(row=3, column=1)
tk.Button(button_f, text="acosh", font="comicsans 14 bold", fg="black",
          command=lambda: acosh(text.get()), width=7, bg="powder blue").grid(row=4, column=1)
tk.Button(button_f, text="atanh", font="comicsans 14 bold", fg="black",
          command=lambda: atanh(text.get()), width=7, bg="powder blue").grid(row=5, column=1)

tk.Button(button_f, text="log", font="comicsans 14 bold",
          command=lambda: log(text.get()), width=7, bg="powder blue").grid(row=0, column=2)
tk.Button(button_f, text="ln", font="comicsans 14 bold",
          command=lambda: ln(text.get()), width=7, bg="powder blue").grid(row=1, column=2)
tk.Button(button_f, text="π", font="comicsans 14 bold",
          command=pi, width=7, bg="powder blue").grid(row=2, column=2)
tk.Button(button_f, text="e", font="comicsans 14 bold",
          command=lambda: e(text.get()), width=7, bg="powder blue").grid(row=3, column=2)

tk.Button(button_f, text="clear", font="comicsans 14 bold",
          command=clear, width=7, bg="powder blue").grid(row=4, column=2)
tk.Button(button_f, text="plot", font="comicsans 14 bold",
          command=plot, width=7, bg="powder blue").grid(row=5, column=2)

# TODO: THE SYMPY COMPLEX FUNCTIONS

tk.Button(button_f, text="∫", font="lacinda 14 bold", fg="black", bg="powder blue",
          width=7, command=integrate). \
    grid(row=0, column=3)

tk.Button(button_f, text="d/dx", font="lacinda 14 bold", fg="black", bg="powder blue",
          width=7, command=derivative). \
    grid(row=1, column=3)

tk.Button(button_f, text="solve", font="lacinda 14 bold", fg="black", bg="powder blue",
          width=7, command=solve_eq). \
    grid(row=2, column=3)

tk.Button(button_f, text="X", font="lacinda 14 bold", fg="black", bg="powder blue",
          width=7, command=lambda: number("x")). \
    grid(row=3, column=3)

tk.Button(button_f, text="Simplify", font="lacinda 14 bold", fg="black", bg="powder blue",
          width=7, command=simplify). \
    grid(row=4, column=3)

tk.Button(button_f, text="<--", font="comicsans 14 bold", fg="black", bg="powder blue",
          width=7, command=backspace). \
    grid(row=5, column=3)

# TODO: simple calculator
tk.Button(button_f, text=7, font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: number(7)).grid(row=0, column=5)
tk.Button(button_f, text=8, font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: number(8)).grid(row=0, column=6)
tk.Button(button_f, text=9, font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: number(9)).grid(row=0, column=7)

tk.Button(button_f, text=4, font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: number(4)).grid(row=1, column=5)
tk.Button(button_f, text=5, font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: number(5)).grid(row=1, column=6)
tk.Button(button_f, text=6, font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: number(6)).grid(row=1, column=7)

tk.Button(button_f, text=1, font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: number(1)).grid(row=2, column=5)
tk.Button(button_f, text=2, font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: number(2)).grid(row=2, column=6)
tk.Button(button_f, text=3, font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: number(3)).grid(row=2, column=7)
tk.Button(button_f, text=".", font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: number(".")).grid(row=3, column=5)
tk.Button(button_f, text=0, font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: number(0)).grid(row=3, column=6)
tk.Button(button_f, text="+", font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: number("+")).grid(row=3, column=7)
tk.Button(button_f, text="-", font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: number("-")).grid(row=4, column=5)
tk.Button(button_f, text="*", font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: number("*")).grid(row=4, column=6)
tk.Button(button_f, text="/", font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: number("/")).grid(row=4, column=7)
tk.Button(button_f, text="=", font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: number("=")).grid(row=5, column=6)
tk.Button(button_f, text="fact", font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: text.set(sp.factorial(text.get()))).grid(row=5, column=7)
tk.Button(button_f, text="pow", font="lacinda 14 bold", bg="powder blue", width=5,
          command=powerk).grid(row=5, column=5)
# TODO: Other buttons

tk.Button(button_f, text="hcf", font="lacinda 14 bold", bg="powder blue", width=5,
          command=hcf).grid(row=0, column=8)
tk.Button(button_f, text="lcm", font="lacinda 14 bold", bg="powder blue", width=5,
          command=lcm).grid(row=0, column=9)
tk.Button(button_f, text="floor", font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: text.set(sp.floor(text.get()))).grid(row=0, column=10)
tk.Button(button_f, text="ceil", font="lacinda 14 bold", bg="powder blue", width=4,
          command=lambda: text.set(sp.ceiling(text.get()))).grid(row=0, column=11)

tk.Button(button_f, text="sqrt", font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: text.set(sp.sqrt(float(text.get())))).grid(row=1, column=8)
tk.Button(button_f, text="cbrt", font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: text.set(sp.cbrt(float(text.get())))).grid(row=1, column=9)
tk.Button(button_f, text="sq.", font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: text.set(pow(float(text.get()), 2))).grid(row=1, column=10)
tk.Button(button_f, text="cube", font="lacinda 14 bold", bg="powder blue", width=4,
          command=lambda: text.set(pow(float(text.get()), 3))).grid(row=1, column=11)

tk.Button(button_f, text="abs", font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: text.set(abs(float(text.get())))).grid(row=2, column=8)
tk.Button(button_f, text="tofrac", font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: frac(text.get())).grid(row=2, column=9)
tk.Button(button_f, text="(", font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: number("(")).grid(row=2, column=10)
tk.Button(button_f, text=")", font="lacinda 14 bold", bg="powder blue", width=4,
          command=lambda: number(")")).grid(row=2, column=11)

tk.Button(button_f, text="A.P", font="lacinda 14 bold", bg="powder blue", width=5,
          command=ap).grid(row=3, column=8)
aps = tk.Button(button_f, text="OK(ap)", font="lacinda 14 bold", bg="powder blue", width=5,
                command=ap2, state=tk.DISABLED)
aps.grid(row=3, column=9)
tk.Button(button_f, text="gamma", font="lacinda 14 bold", bg="powder blue", width=5,
          command=lambda: text.set(sp.gamma(text.get()))).grid(row=3, column=10)
tk.Button(button_f, text="Si", font="lacinda 14 bold", bg="powder blue", width=4,
          command=lambda: text.set(sp.Si(text.get()).evalf())).grid(column=11, row=3)

tk.Button(button_f, text="sine tranform", font="lacinda 14 bold", bg="powder blue", width=11,
          command=si_trans).grid(row=4, column=8, columnspan=2)
tk.Button(button_f, text="cos tranform", font="lacinda 14 bold", bg="powder blue", width=10,
          command=cos_trans).grid(column=10, row=4, columnspan=2)

tk.Button(button_f, text="laplace tranform", font="lacinda 11 bold", bg="powder blue", width=14,
          command=laplace_trans).grid(row=5, column=8, columnspan=2)
tk.Button(button_f, text="taylor series", font="lacinda 14 bold", bg="powder blue", width=10,
          command=series).grid(column=10, row=5, columnspan=2)
tk.Button(button_f, text="taylor series", font="lacinda 14 bold", bg="powder blue", width=10,
          command=series).grid(column=10, row=5, columnspan=2)
tk.Button(button_f, text="Statistics", font="lacinda 14 bold", bg="powder blue", width=10,
          command=stat).grid(column=10, row=6, columnspan=2)
tk.Button(button_f, text="date", font="lacinda 14 bold", bg="powder blue", width=10,
          command=date).grid(column=10, row=7, columnspan=2)

# TODO: THE END



root.mainloop()
