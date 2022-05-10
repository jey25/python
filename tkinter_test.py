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
    btn.config(text=dnow)

def ent_p():
    a = ent.get()
    print(a)

ent = Entry(win)
ent.pack()

btn = Button(win, width=30, height=1, text="로또 번호 확인", command=ent_p)
btn.pack()

btn = Button(win, width=30, height=1, text="시간", command=time)
btn.pack()

win.mainloop()