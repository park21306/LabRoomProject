from tkinter import *
import time, threading
g = 0
f = Tk()
f.title("frame")
f.minsize(1000,200)
f.maxsize(1000,2000)
i1 = PhotoImage(file="d.png")
i2 = PhotoImage(file="c.png")
def change():
 global g
 if g % 2 == 0:
      b1["image"] = i1
 else:
      b1["image"] = i2
 g = g + 1
b1 = Button(f,image=i1,text='OK',command=change,width=500,height=1100)
b1.place(x=50,y=50)
f.mainloop()

def change ():
    b3 = Button(tk,text='Com1',command=open_text1,bg = "red")
    b3.place(x=100,y=150)
def change01 ():
    b3 = Button(tk,text='Com1',command=open_text1,bg = "green")
    b3.place(x=100,y=150)
