from tkinter import *
root = Tk()
import re

root.resizable(width=False, height=False)
root.geometry('212x220')
root.title('Calculator!')
root['bg'] = 'black'

def btnClick(number):
    global operator
    print(operator)
    operator = operator + str(number)
    text_Input.set(operator)


def evalFunc(operator):
    operator = eval(operator)
    text_Input.set(operator)


def clearFunc(operator):
    operator = re.sub(r"[\d,\D]", "", operator)
    print(operator)
    text_Input.set(operator)

operator = ""
text_Input = StringVar()

el = Entry(root, font='arial 14',width=19,insertwidth=4,justify='right', textvariable=text_Input).place(x=0,y=1)
b1 = Button(root, text="1", width=4, height=1, bg='#313233', fg='white', activebackground='#8a8683',font='arial 14',command = lambda:btnClick('1')).place(x=1,y=146)
b2 = Button(root, text="2", width=4, height=1, bg='#313233', fg='white', activebackground='#8a8683',font='arial 14',command = lambda:btnClick('2')).place(x=55,y=146)
b3 = Button(root, text="3", width=4, height=1, bg='#313233', fg='white', activebackground='#8a8683',font='arial 14',command = lambda:btnClick('3')).place(x=109,y=146)
b4 = Button(root, text="4", width=4, height=1, bg='#313233', fg='white', activebackground='#8a8683',font='arial 14',command = lambda:btnClick('4')).place(x=1,y=107)
b5 = Button(root, text="5", width=4, height=1, bg='#313233', fg='white', activebackground='#8a8683',font='arial 14',command = lambda:btnClick('5')).place(x=55,y=107)
b6 = Button(root, text="6", width=4, height=1, bg='#313233', fg='white', activebackground='#8a8683',font='arial 14',command = lambda:btnClick('6')).place(x=109,y=107)
b7 = Button(root, text="7", width=4, height=1, bg='#313233', fg='white', activebackground='#8a8683',font='arial 14',command = lambda:btnClick('7')).place(x=1,y=68)
b8 = Button(root, text="8", width=4, height=1, bg='#313233', fg='white', activebackground='#8a8683',font='arial 14',command = lambda:btnClick('8')).place(x=55,y=68)
b9 = Button(root, text="9", width=4, height=1, bg='#313233', fg='white', activebackground='#8a8683',font='arial 14',command = lambda:btnClick('9')).place(x=109,y=68)
b0 = Button(root, text="0", width=9, height=1, bg='#313233', fg='white', activebackground='#8a8683',font='arial 14',command = lambda:btnClick('0')).place(x=0,y=185)
bp = Button(root, text="+", width=4, height=1, bg='#ed7926', fg='white', activebackground='#f5a85b',font='arial 14',command = lambda:btnClick('+')).place(x=163,y=146)
bm = Button(root, text="-", width=4, height=1, bg='#ed7926', fg='white', activebackground='#f5a85b',font='arial 14',command = lambda:btnClick('-')).place(x=163,y=107)
bd = Button(root, text="/", width=4, height=1, bg='#ed7926', fg='white', activebackground='#f5a85b',font='arial 14',command = lambda:btnClick('/')).place(x=163,y=29)
bm = Button(root, text="*", width=4, height=1, bg='#ed7926', fg='white', activebackground='#f5a85b',font='arial 14',command = lambda:btnClick('*')).place(x=163,y=68)
be = Button(root, text="=", width=4, height=1, bg='#ed7926', fg='white', activebackground='#f5a85b',font='arial 14',command = lambda:evalFunc(operator)).place(x=163,y=185)
bc = Button(root, text="AC", width=4, height=1, bg='#808080', fg='white', activebackground='#b8b2ad',font='arial 14',command = lambda:clearFunc(operator)).place(x=1,y=29)
bk = Button(root, text="x2", width=4, height=1, bg='#808080', fg='white', activebackground='#b8b2ad',font='arial 14',command = lambda:btnClick('**')).place(x=55,y=29)
bp = Button(root, text="%", width=4, height=1, bg='#808080', fg='white', activebackground='#b8b2ad',font='arial 14',command = lambda:btnClick('%')).place(x=109,y=29)
bs = Button(root, text=".", width=4, height=1, bg='#313233', fg='white', activebackground='#b8b2ad',font='arial 14',command = lambda:btnClick('.')).place(x=109,y=185)






root.mainloop()