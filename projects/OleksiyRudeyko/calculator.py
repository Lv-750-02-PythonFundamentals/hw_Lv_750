import tkinter
from tkinter import *

root=Tk()
root.title("Calculator")
root.geometry("355x360+500+200")
root.resizable(False, False)
root.config(bg="#33ffe6")

equation = ""

calculated = False
def show(value):
    global equation, calculated
    if calculated:
        calculated = False
        clear()
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation, calculated
    result = ""
    if equation != "":
        try:
            equation = equation.replace('%', '/100*')
            result = eval(equation)
            calculated = True
        except:
            result = "Error"
            equation = ""
    label_result.config(text=result)

label_result=Label(root, width=29, height=2,
                    text="", font=("Casio fx-115ES Plus", 30))
label_result.pack()

Button(root, text="C", width=5, height=2, font=("bold"), bd=1, command=lambda: clear()).place(x=10, y=100)
Button(root, text="/", width=5, height=2, font=("bold"), bd=1, command=lambda: show("/")).place(x=95, y=100)
Button(root, text="%", width=5, height=2, font=("bold"), bd=1, command=lambda: show("%")).place(x=180, y=100)
Button(root, text="*", width=5, height=2, font=("bold"), bd=1, command=lambda: show("*")).place(x=265, y=100)

Button(root, text="7", width=5, height=2, font=("bold"), bd=1, command=lambda: show("7")).place(x=10, y=150)
Button(root, text="8", width=5, height=2, font=("bold"), bd=1, command=lambda: show("8")).place(x=95, y=150)
Button(root, text="9", width=5, height=2, font=("bold"), bd=1, command=lambda: show("9")).place(x=180, y=150)
Button(root, text="-", width=5, height=2, font=("bold"), bd=1, command=lambda: show("-")).place(x=265, y=150)

Button(root, text="4", width=5, height=2, font=("bold"), bd=1, command=lambda: show("4")).place(x=10, y=200)
Button(root, text="5", width=5, height=2, font=("bold"), bd=1, command=lambda: show("5")).place(x=95, y=200)
Button(root, text="6", width=5, height=2, font=("bold"), bd=1, command=lambda: show("6")).place(x=180, y=200)
Button(root, text="+", width=5, height=2, font=("bold"), bd=1, command=lambda: show("+")).place(x=265, y=200)

Button(root, text="1", width=5, height=2, font=("bold"), bd=1, command=lambda: show("1")).place(x=10, y=250)
Button(root, text="2", width=5, height=2, font=("bold"), bd=1, command=lambda: show("2")).place(x=95, y=250)
Button(root, text="3", width=5, height=2, bd=1, font=("bold"), command=lambda: show("3")).place(x=180, y=250)
Button(root, text="0", width=14, height=2, font=("bold"), bd=1, command=lambda: show("0")).place(x=10, y=298)

Button(root, text=".", width=5, height=2, font=("bold"), bd=1, command=lambda: show(".")).place(x=180, y=298)
Button(root, text="=", width=5, height=5, font=("bold"), bd=1, command=lambda: calculate()).place(x=265, y=250)

root.mainloop()