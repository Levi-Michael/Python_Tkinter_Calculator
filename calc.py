from tkinter import *

calc = Tk()
calc.title("Calculator")
calc.geometry("200x200")
calc.resizable(False, False)


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def bt_clear():
    global expression
    expression = ""
    input_text.set("")


def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""


expression = ""
input_text = StringVar()

calctxt = Entry(calc, width="25", textvariable=input_text)
calctxt.place(x=25, y=5)

button1 = Button(calc, text="1", width="2", height="1", command=lambda: btn_click(1))
button1.place(x=40, y=30)

button2 = Button(calc, text="2", width="2", height="1", command=lambda: btn_click(2))
button2.place(x=70, y=30)

button3 = Button(calc, text="3", width="2", height="1", command=lambda: btn_click(3))
button3.place(x=100, y=30)

button4 = Button(calc, text="4", width="2", height="1", command=lambda: btn_click(4))
button4.place(x=40, y=60)

button5 = Button(calc, text="5", width="2", height="1", command=lambda: btn_click(5))
button5.place(x=70, y=60)

button6 = Button(calc, text="6", width="2", height="1", command=lambda: btn_click(6))
button6.place(x=100, y=60)

button7 = Button(calc, text="7", width="2", height="1", command=lambda: btn_click(7))
button7.place(x=40, y=90)

button8 = Button(calc, text="8", width="2", height="1", command=lambda: btn_click(8))
button8.place(x=70, y=90)

button9 = Button(calc, text="9", width="2", height="1", command=lambda: btn_click(9))
button9.place(x=100, y=90)

button0 = Button(calc, text="0", width="2", height="1", command=lambda: btn_click(0))
button0.place(x=40, y=120)

# ----------------------------------------------------------------

Plusbutton = Button(calc, text="+", width="2", height="1", command=lambda: btn_click("+"))
Plusbutton.place(x=130, y=30)

Minusbutton = Button(calc, text="-", width="2", height="1", command=lambda: btn_click("-"))
Minusbutton.place(x=130, y=60)

Multiplybutton = Button(calc, text="*", width="2", height="1", command=lambda: btn_click("*"))
Multiplybutton.place(x=130, y=90)

Dividebutton = Button(calc, text="/", width="2", height="1", command=lambda: btn_click("/"))
Dividebutton.place(x=130, y=120)

Clearbutton = Button(calc, text="C", width="2", height="1", command=lambda: bt_clear())
Clearbutton.place(x=70, y=120)

Equalbutton = Button(calc, text="=", width="2", height="1", command=lambda: bt_equal())
Equalbutton.place(x=100, y=120)

calc.mainloop()
