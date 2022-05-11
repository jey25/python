import re
from tkinter import *
from datetime import datetime

win = Tk()

win.geometry("300x300")
win.title("Tool")
win.option_add('*Font', '맑은고딕 15')
win.configure(bg="beige")

def time():
    dnow = datetime.now()
    b[2].config(text=dnow)

def ent_p():
    a = ent.get()
    print(a)

ent = Entry(win)
ent.pack()

b = [None]*3
b[0]=Button(win, text="But1")
b[1]=Button(win, text="로또 번호 확인", command=ent_p)
b[2]=Button(win, text="시간", command=time)

for a in b:
    a.pack(side=RIGHT)

win.mainloop()