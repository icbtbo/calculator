from tkinter import *
import tkinter.font as tkFont
import os
from functools import partial
# from PIL import Image, ImageTk

def get_input(entry, argu):
    entry.insert(END, argu)

def backspace(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)

def clear(entry):
    entry.delete(0, END)

def calculate(entry):
    input = entry.get()
    output = str(eval(input.strip()))
    clear(entry)
    entry.insert(END, output)
def hello(e1):
    print(e1.get())

def calcu_tax(e1, e2, e3, e4, e5):
    result = 0
    salary = float(e1.get().strip())  # 获取“月工资”数值
    argu1 = float(e2.get().strip())  # 获取“个人社保” 数值
    argu2 = float(e3.get().strip())  # 获取“个人住房公积金”数值
    argu3 = float(e4.get().strip())  # 获取“年终奖”数值
    temp = salary - 3500 - argu1 - argu2
    temp1 = argu3 / 12
    if 3500 < salary <= 5000:
        result = temp * 0.03
    elif 5000 < salary <= 8000:
        result = temp * 0.1 - 105
    elif 8000 < salary <= 12500:
        result =temp * 0.20 - 555
    elif 12500 < salary <= 38500:
        result = temp * 0.25 - 1005
    elif 38500 < salary <= 58500:
        result = temp * 0.3 - 2775
    elif 58500 < salary <= 83500:
        result = temp * 0.35 - 5505
    elif salary > 83500:
        result = temp * 0.45 - 13505
    # 计算年终奖应纳税额
    if 3500 < temp1 + 3500 <= 5000:
        result += argu3 * 0.03
    elif 5000 < temp1 + 3500 <= 8000:
        result += argu3 * 0.1 - 105
    elif 8000 < temp1 +3500 <= 12500:
        result += argu3 * 0.20 - 555
    elif 12500 < temp1 + 3500 <= 38500:
        result += argu3 * 0.25 - 1005
    elif 38500 < temp1 + 3500 <= 58500:
        result += argu3 * 0.3 - 2775
    elif 58500 < temp1 + 3500 <= 83500:
        result += argu3 * 0.35 - 5505
    elif temp1 + 3500 > 83500:
        result += argu3 * 0.45 - 13505
    get_input(e5, str(result))


def extra():
    tl = Toplevel()
    tl.title("个人所得税计算")
    tl.geometry('400x300')
    Label(tl, text="月工资").grid(row=0, sticky=W)
    Label(tl, text="个人社保部分").grid(row=1, sticky=W)
    Label(tl, text="个人住房公积金部分").grid(row=2, sticky=W)
    Label(tl, text="年终奖").grid(row=3, sticky=W)
    Label(tl, text="个人所得税").grid(row=4, pady=10, sticky=W)

    e1 = Entry(tl)
    e1.grid(row=0, column=1)
    e2 = Entry(tl)
    e2.grid(row=1, column=1)
    e3 = Entry(tl)
    e3.grid(row=2, column=1)
    e4 = Entry(tl)
    e4.grid(row=3, column=1)
    e5 = Entry(tl)
    e5.grid(row=4, column=1)


    button = Button(tl, text="计算", pady=10, command=lambda: calcu_tax(e1, e2, e3, e4, e5))
    # button = Button(tl, text="calculate", pady=10, command=lambda: hello(e1))
    button.grid(row=5, column=1)

def calculator():
    root = Tk()
    root.title("Calculator")
    root.resizable(0, 0)

    menubar = Menu(root)
    menu = Menu(menubar, tearoff=0)
    menu.add_command(label='个人所得税计算', command=extra)
    menubar.add_cascade(label="扩展功能", menu=menu)

    root.config(menu=menubar)
    entry_font = tkFont.Font(size=12)
    entry = Entry(root, justify="right", font=entry_font)
    entry.grid(row=0, column=0, columnspan=4, sticky=N+W+S+E, padx=5, pady=5)

    button_font = tkFont.Font(size=10, weight=tkFont.BOLD)
    button_bg = '#D5E0EE'
    button_active_bg = '#E5E35B'

    myButton = partial(Button, root, bg=button_bg, padx=10, pady=3, activebackground=button_active_bg)

    button7 = myButton(text='7', command=lambda: get_input(entry, '7'))
    button7.grid(row=1, column=0, padx=1, pady=5)

    button8 = myButton(text='8', command=lambda: get_input(entry, '8'))
    button8.grid(row=1, column=1, padx=1, pady=5)

    button9 = myButton(text='9', command=lambda: get_input(entry, '9'))
    button9.grid(row=1, column=2, padx=1,  pady=5)

    button10 = myButton(text='+', command=lambda: get_input(entry, '+'))
    button10.grid(row=1, column=3, padx=1,  pady=5)

    button4 = myButton(text='4', command=lambda: get_input(entry, '4'))
    button4.grid(row=2, column=0, padx=1,  pady=5)

    button5 = myButton(text='5', command=lambda: get_input(entry, '5'))
    button5.grid(row=2, column=1, padx=1,  pady=5)

    button6 = myButton(text='6', command=lambda: get_input(entry, '6'))
    button6.grid(row=2, column=2, padx=1,  pady=5)

    button11 = myButton(text='-', command=lambda: get_input(entry, '-'))
    button11.grid(row=2, column=3, padx=1,  pady=5)

    button1 = myButton(text='1', command=lambda : get_input(entry, '1'))
    button1.grid(row=3, column=0, padx=1,  pady=5)

    button2 = myButton(text='2', command=lambda: get_input(entry, '2'))
    button2.grid(row=3, column=1, padx=1,  pady=5)

    button3 = myButton(text='3', command=lambda: get_input(entry, '3'))
    button3.grid(row=3, column=2, padx=2,  pady=5)

    button12 = myButton(text='*', command=lambda: get_input(entry, '*'))
    button12.grid(row=3, column=3, padx=1,  pady=5)

    button0 = myButton(text='0', command=lambda: get_input(entry, '0'))
    button0.grid(row=4, column=0, pady=5, columnspan=2, padx=3, sticky=N+S+E+W)

    button13 = myButton(text='.', command=lambda: get_input(entry, '.'))
    button13.grid(row=4, column=2, pady=5)

    button14 = myButton(text='/', command=lambda: get_input(entry, '/'))
    button14.grid(row=4, column=3, pady=5)

    button15 = myButton(text='<-', command=lambda: backspace(entry))
    button15.grid(row=5, column=0, pady=5)

    button16 = myButton(text='Clear', command=lambda: clear(entry))
    button16.grid(row=5, column=1, pady=5)

    button17 = myButton(text='=', command=lambda: calculate(entry))
    button17.grid(row=5, column=2, columnspan=2, pady=5, padx=3, sticky=N+S+E+W)

    root.mainloop()

if __name__ ==  '__main__':
    calculator()