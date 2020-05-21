from tkinter import *
root = Tk()

root.resizable(width=False, height=False)
root.geometry('212x220')
root.title('Calculator!')


def btnClick(number):
    global operator
    operator += str(number)
    if 'AC' in operator:
        operator = ""
        return text_Input.set(operator)
    else:
        text_Input.set(operator)


def evalFunc(operator):
    try:
        operator = eval(operator)
        text_Input.set(operator)
    except SyntaxError:
        text_Input.set('Erorr')


operator = ""
text_Input = StringVar()

el = Entry(root, font='arial 14', state="readonly", width=25, justify='right', textvariable=text_Input).place(x=0, y=1)
b1 = Button(root, text="1", width=4, height=1, activebackground='#8a8683', font='arial 14',
            command=lambda: btnClick('1')).place(x=1, y=146)
b2 = Button(root, text="2", width=4, height=1,  activebackground='#8a8683', font='arial 14',
            command=lambda: btnClick('2')).place(x=55, y=146)
b3 = Button(root, text="3", width=4, height=1, activebackground='#8a8683', font='arial 14',
            command=lambda: btnClick('3')).place(x=109, y=146)
b4 = Button(root, text="4", width=4, height=1, activebackground='#8a8683', font='arial 14',
            command=lambda: btnClick('4')).place(x=1, y=107)
b5 = Button(root, text="5", width=4, height=1, activebackground='#8a8683', font='arial 14',
            command=lambda: btnClick('5')).place(x=55, y=107)
b6 = Button(root, text="6", width=4, height=1,  activebackground='#8a8683', font='arial 14',
            command=lambda: btnClick('6')).place(x=109, y=107)
b7 = Button(root, text="7", width=4, height=1, activebackground='#8a8683', font='arial 14',
            command=lambda: btnClick('7')).place(x=1, y=68)
b8 = Button(root, text="8", width=4, height=1,  activebackground='#8a8683', font='arial 14',
            command=lambda: btnClick('8')).place(x=55, y=68)
b9 = Button(root, text="9", width=4, height=1,  activebackground='#8a8683', font='arial 14',
            command=lambda: btnClick('9')).place(x=109, y=68)
b0 = Button(root, text="0", width=11, height=1, activebackground='#8a8683', font='arial 14',
            command=lambda: btnClick('0')).place(x=0, y=185)
bp = Button(root, text="+", width=4, height=1,  activebackground='#f5a85b', font='arial 14',
            command=lambda: btnClick('+')).place(x=163, y=146)
bm = Button(root, text="-", width=4, height=1, activebackground='#f5a85b', font='arial 14',
            command=lambda: btnClick('-')).place(x=163, y=107)
bd = Button(root, text="/", width=4, height=1,  activebackground='#f5a85b', font='arial 14',
            command=lambda: btnClick('/')).place(x=163, y=29)
bm = Button(root, text="*", width=4, height=1, activebackground='#f5a85b', font='arial 14',
            command=lambda: btnClick('*')).place(x=163, y=68)
be = Button(root, text="=", width=4, height=1, activebackground='#f5a85b', font='arial 14',
            command=lambda: evalFunc(operator)).place(x=163, y=185)
bc = Button(root, text="AC", width=4, height=1, activebackground='#b8b2ad', font='arial 14',
            command=lambda: btnClick('AC')).place(x=1, y=29)
bk = Button(root, text="x2", width=4, height=1, activebackground='#b8b2ad', font='arial 14',
            command=lambda: btnClick('**')).place(x=55, y=29)
bp = Button(root, text="%", width=4, height=1, activebackground='#b8b2ad', font='arial 14',
            command=lambda: btnClick('%')).place(x=109, y=29)
bs = Button(root, text=".", width=4, height=1, activebackground='#b8b2ad', font='arial 14',
            command=lambda: btnClick('.')).place(x=109, y=185)

root.mainloop()