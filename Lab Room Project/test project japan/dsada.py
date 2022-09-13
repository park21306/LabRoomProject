from tkinter import *
tk = Tk()
tk.geometry("1024x768")
#-------------------------------#
def open_text1():
    b1 = Button(tk,text = "Save",command=lambda:save1())
    b1.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change01())
    b5.place(x=600,y=110)
    f = open("lol.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save1 ():
    f = open("lol.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change ():
    b3 = Button(tk,text='Com1',command=open_text1,bg = "red")
    b3.place(x=100,y=150)
def change01 ():
    b3 = Button(tk,text='Com1',command=open_text1,bg = "green")
    b3.place(x=100,y=150)
#-------------------------------#
label1 = Label(tk,width = 15,text = "บันทึกข้อมูลเพิ่มเติม",bg = "blue",fg = "white")
label1.pack()
text = Text(tk,fg = "red",width = 50,height = 5)
text.pack()
#-------------------------------#
b3 = Button(tk,text='Com1',command=open_text1)
b3.place(x=100,y=150)
#-------------------------------#
tk.update()
tk.mainloop()
