from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x600')

L1 = Label(GUI,text='ธนาคารxxx',font=('Angsana New',30),fg='blue')
L1.place(x=180,y=20)

def Button2():
    text = 'ถอนเงินจำนวน 100 บาท'
    messagebox.showerror('100',text)

FB1 = Frame(GUI)
FB1.place(x=180,y=80)
B2 = ttk.Button(FB1,text='100',command=Button2)
B2.pack(ipadx=20,ipady=20)

def Button3():
    text = 'ถอนเงินจำนวน 200 บาท'
    messagebox.showerror('200',text)

FB2 = LabelFrame(GUI)
FB2.place(x=180,y=80)
B3 = ttk.Button(FB1,text='200',command=Button3)
B3.pack(ipadx=20,ipady=20)

def Button4():
    text = 'ถอนเงินจำนวน 500 บาท'
    messagebox.showerror('500',text)

FB3 = LabelFrame(GUI)
FB3.place(x=180,y=80)
B4 = ttk.Button(FB1,text='500',command=Button4)
B4.pack(ipadx=20,ipady=20)

def Button5():
    text = 'ถอนเงินจำนวน 1000 บาท'
    messagebox.showerror('1000',text)

FB4 = LabelFrame(GUI)
FB4.place(x=180,y=180)
B5 = ttk.Button(FB1,text='1000',command=Button5)
B5.pack(ipadx=20,ipady=20)
