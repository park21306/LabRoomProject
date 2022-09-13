from tkinter import *
tk = Tk()
tk.geometry("800x600")
tk.title("โปรแกรมเก็บข้อมูลห้องLab")
#-------------------------------#com1
def open_text1():
    b1 = Button(tk,text = "Save",command=lambda:save1())
    b1.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change01())
    b5.place(x=600,y=110)
    f = open("1.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save1 ():
    f = open("1.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change ():
    b3 = Button(tk,text='Com1',command=open_text1,bg = "red")
    b3.place(x=100,y=150)
def change01 ():
    b3 = Button(tk,text='Com1',command=open_text1,bg = "green")
    b3.place(x=100,y=150)
#-------------------------------#com2
def open_text2():
    b2 = Button(tk,text = "Save",command=lambda:save2())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change2())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change02())
    b5.place(x=600,y=110)
    f = open("2.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save2 ():
    f = open("2.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change2 ():
    b3 = Button(tk,text='Com2',command=open_text2,bg = "red")
    b3.place(x=150,y=150)
def change02 ():
    b3 = Button(tk,text='Com2',command=open_text2,bg = "green")
    b3.place(x=150,y=150)
#-------------------------------#
def open_text3():
    b2 = Button(tk,text = "Save",command=lambda:save3())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change3())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change03())
    b5.place(x=600,y=110)
    f = open("3.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save3 ():
    f = open("3.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change3 ():
    b3 = Button(tk,text='Com3',command=open_text3,bg = "red")
    b3.place(x=300,y=150)
def change03 ():
    b3 = Button(tk,text='Com3',command=open_text3,bg = "green")
    b3.place(x=300,y=150)
#-------------------------------#
def open_text4():
    b2 = Button(tk,text = "Save",command=lambda:save4())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change4())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change04())
    b5.place(x=600,y=110)
    f = open("4.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save4 ():
    f = open("4.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change4 ():
    b3 = Button(tk,text='Com4',command=open_text4,bg = "red")
    b3.place(x=350,y=150)
def change04 ():
    b3 = Button(tk,text='Com4',command=open_text4,bg = "green")
    b3.place(x=350,y=150)
#-------------------------------#
def open_text5():
    b2 = Button(tk,text = "Save",command=lambda:save5())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change5())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change05())
    b5.place(x=600,y=110)
    f = open("5.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save5 ():
    f = open("5.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change5 ():
    b3 = Button(tk,text='Com5',command=open_text5,bg = "red")
    b3.place(x=500,y=150)
def change05 ():
    b3 = Button(tk,text='Com5',command=open_text5,bg = "green")
    b3.place(x=500,y=150)
#-------------------------------#
def open_text6():
    b2 = Button(tk,text = "Save",command=lambda:save6())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change6())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change06())
    b5.place(x=600,y=110)
    f = open("6.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save6 ():
    f = open("6.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change6 ():
    b3 = Button(tk,text='Com6',command=open_text6,bg = "red")
    b3.place(x=550,y=150)
def change06 ():
    b3 = Button(tk,text='Com6',command=open_text6,bg = "green")
    b3.place(x=550,y=150)
#-------------------------------#
def open_text7():
    b2 = Button(tk,text = "Save",command=lambda:save7())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change7())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change07())
    b5.place(x=600,y=110)
    f = open("7.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save7 ():
    f = open("7.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change7 ():
    b3 = Button(tk,text='Com7',command=open_text7,bg = "red")
    b3.place(x=700,y=150)
def change07 ():
    b3 = Button(tk,text='Com7',command=open_text7,bg = "green")
    b3.place(x=700,y=150)
#-------------------------------#
def open_text8():
    b2 = Button(tk,text = "Save",command=lambda:save8())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change8())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change08())
    b5.place(x=600,y=110)
    f = open("8.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save8 ():
    f = open("8.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change8 ():
    b3 = Button(tk,text='Com8',command=open_text8,bg = "red")
    b3.place(x=750,y=150)
def change08 ():
    b3 = Button(tk,text='Com8',command=open_text8,bg = "green")
    b3.place(x=750,y=150)
#-------------------------------#
def open_text9():
    b2 = Button(tk,text = "Save",command=lambda:save9())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change9())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change09())
    b5.place(x=600,y=110)
    f = open("9.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save9 ():
    f = open("9.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change9 ():
    b3 = Button(tk,text='Com9',command=open_text9,bg = "red")
    b3.place(x=100,y=200)
def change09 ():
    b3 = Button(tk,text='Com9',command=open_text9,bg = "green")
    b3.place(x=100,y=200)
#-------------------------------#
def open_text10():
    b2 = Button(tk,text = "Save",command=lambda:save10())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change10())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change010())
    b5.place(x=600,y=110)
    f = open("10.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save10 ():
    f = open("10.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change10 ():
    b3 = Button(tk,text='Com10',command=open_text10,bg = "red")
    b3.place(x=150,y=200)
def change010 ():
    b3 = Button(tk,text='Com10',command=open_text10,bg = "green")
    b3.place(x=150,y=200)
#-------------------------------#
def open_text11():
    b2 = Button(tk,text = "Save",command=lambda:save11())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change11())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change011())
    b5.place(x=600,y=110)
    f = open("11.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save11 ():
    f = open("11.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change11 ():
    b3 = Button(tk,text='Com11',command=open_text11,bg = "red")
    b3.place(x=300,y=200)
def change011 ():
    b3 = Button(tk,text='Com11',command=open_text11,bg = "green")
    b3.place(x=300,y=200)
#-------------------------------#
def open_text12():
    b2 = Button(tk,text = "Save",command=lambda:save12())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change12())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change012())
    b5.place(x=600,y=110)
    f = open("12.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save12 ():
    f = open("12.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change12 ():
    b3 = Button(tk,text='Com12',command=open_text12,bg = "red")
    b3.place(x=350,y=200)
def change012 ():
    b3 = Button(tk,text='Com12',command=open_text12,bg = "green")
    b3.place(x=350,y=200)
#-------------------------------#
def open_text13():
    b2 = Button(tk,text = "Save",command=lambda:save13())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change13())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change013())
    b5.place(x=600,y=110)
    f = open("13.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save13 ():
    f = open("13.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change13 ():
    b3 = Button(tk,text='Com13',command=open_text13,bg = "red")
    b3.place(x=500,y=200)
def change013 ():
    b3 = Button(tk,text='Com13',command=open_text13,bg = "green")
    b3.place(x=500,y=200)
#-------------------------------#
def open_text14():
    b2 = Button(tk,text = "Save",command=lambda:save14())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change14())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change014())
    b5.place(x=600,y=110)
    f = open("14.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save14 ():
    f = open("14.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change14 ():
    b3 = Button(tk,text='Com14',command=open_text14,bg = "red")
    b3.place(x=550,y=200)
def change014 ():
    b3 = Button(tk,text='Com14',command=open_text14,bg = "green")
    b3.place(x=550,y=200)
#-------------------------------#
def open_text15():
    b2 = Button(tk,text = "Save",command=lambda:save15())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change15())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change015())
    b5.place(x=600,y=110)
    f = open("15.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save15 ():
    f = open("15.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change15 ():
    b3 = Button(tk,text='Com15',command=open_text15,bg = "red")
    b3.place(x=700,y=200)
def change015 ():
    b3 = Button(tk,text='Com15',command=open_text15,bg = "green")
    b3.place(x=700,y=200)
#-------------------------------#
def open_text16():
    b2 = Button(tk,text = "Save",command=lambda:save16())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change16())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change016())
    b5.place(x=600,y=110)
    f = open("16.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save16 ():
    f = open("16.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change16 ():
    b3 = Button(tk,text='Com16',command=open_text16,bg = "red")
    b3.place(x=750,y=200)
def change016 ():
    b3 = Button(tk,text='Com16',command=open_text16,bg = "green")
    b3.place(x=750,y=200)
#-------------------------------#
def open_text17():
    b2 = Button(tk,text = "Save",command=lambda:save17())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change17())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change017())
    b5.place(x=600,y=110)
    f = open("17.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save17 ():
    f = open("17.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change17 ():
    b3 = Button(tk,text='Com17',command=open_text17,bg = "red")
    b3.place(x=100,y=250)
def change017 ():
    b3 = Button(tk,text='Com17',command=open_text17,bg = "green")
    b3.place(x=100,y=250)
#-------------------------------#
def open_text18():
    b2 = Button(tk,text = "Save",command=lambda:save18())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change18())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change018())
    b5.place(x=600,y=110)
    f = open("18.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save18 ():
    f = open("18.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change18 ():
    b3 = Button(tk,text='Com18',command=open_text18,bg = "red")
    b3.place(x=150,y=250)
def change018 ():
    b3 = Button(tk,text='Com18',command=open_text18,bg = "green")
    b3.place(x=150,y=250)
#-------------------------------#
def open_text19():
    b2 = Button(tk,text = "Save",command=lambda:save19())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change19())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change019())
    b5.place(x=600,y=110)
    f = open("19.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save19 ():
    f = open("19.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change19 ():
    b3 = Button(tk,text='Com19',command=open_text19,bg = "red")
    b3.place(x=300,y=250)
def change019 ():
    b3 = Button(tk,text='Com19',command=open_text19,bg = "green")
    b3.place(x=300,y=250)
#-------------------------------#
def open_text20():
    b2 = Button(tk,text = "Save",command=lambda:save20())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change20())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change020())
    b5.place(x=600,y=110)
    f = open("20.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save20 ():
    f = open("20.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change20 ():
    b3 = Button(tk,text='Com20',command=open_text20,bg = "red")
    b3.place(x=350,y=250)
def change020 ():
    b3 = Button(tk,text='Com20',command=open_text20,bg = "green")
    b3.place(x=350,y=250)
#-------------------------------#
def open_text21():
    b2 = Button(tk,text = "Save",command=lambda:save21())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change21())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change021())
    b5.place(x=600,y=110)
    f = open("21.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save21 ():
    f = open("21.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change21 ():
    b3 = Button(tk,text='Com21',command=open_text21,bg = "red")
    b3.place(x=500,y=250)
def change021 ():
    b3 = Button(tk,text='Com21',command=open_text21,bg = "green")
    b3.place(x=500,y=250)
#-------------------------------#
def open_text22():
    b2 = Button(tk,text = "Save",command=lambda:save22())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change22())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change022())
    b5.place(x=600,y=110)
    f = open("22.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save22 ():
    f = open("22.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change22 ():
    b3 = Button(tk,text='Com22',command=open_text22,bg = "red")
    b3.place(x=550,y=250)
def change022 ():
    b3 = Button(tk,text='Com22',command=open_text22,bg = "green")
    b3.place(x=550,y=250)
#-------------------------------#
def open_text23():
    b2 = Button(tk,text = "Save",command=lambda:save23())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change23())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change023())
    b5.place(x=600,y=110)
    f = open("23.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save23 ():
    f = open("23.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change23 ():
    b3 = Button(tk,text='Com23',command=open_text23,bg = "red")
    b3.place(x=700,y=250)
def change023 ():
    b3 = Button(tk,text='Com23',command=open_text23,bg = "green")
    b3.place(x=700,y=250)
#-------------------------------#
def open_text24():
    b2 = Button(tk,text = "Save",command=lambda:save24())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change24())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change024())
    b5.place(x=600,y=110)
    f = open("24.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save24 ():
    f = open("24.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change24 ():
    b3 = Button(tk,text='Com24',command=open_text24,bg = "red")
    b3.place(x=750,y=250)
def change024 ():
    b3 = Button(tk,text='Com24',command=open_text24,bg = "green")
    b3.place(x=750,y=250)
#-------------------------------#
def open_text25():
    b2 = Button(tk,text = "Save",command=lambda:save25())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change25())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change025())
    b5.place(x=600,y=110)
    f = open("25.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save25 ():
    f = open("25.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change25 ():
    b3 = Button(tk,text='Com25',command=open_text25,bg = "red")
    b3.place(x=100,y=300)
def change025 ():
    b3 = Button(tk,text='Com25',command=open_text25,bg = "green")
    b3.place(x=100,y=300)
#-------------------------------#
def open_text26():
    b2 = Button(tk,text = "Save",command=lambda:save26())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change26())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change026())
    b5.place(x=600,y=110)
    f = open("26.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save26 ():
    f = open("26.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change26 ():
    b3 = Button(tk,text='Com26',command=open_text26,bg = "red")
    b3.place(x=150,y=300)
def change026 ():
    b3 = Button(tk,text='Com26',command=open_text26,bg = "green")
    b3.place(x=150,y=300)
#-------------------------------#
def open_text27():
    b2 = Button(tk,text = "Save",command=lambda:save27())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change27())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change027())
    b5.place(x=600,y=110)
    f = open("27.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save27 ():
    f = open("27.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change27 ():
    b3 = Button(tk,text='Com27',command=open_text27,bg = "red")
    b3.place(x=300,y=300)
def change027 ():
    b3 = Button(tk,text='Com27',command=open_text27,bg = "green")
    b3.place(x=300,y=300)
#-------------------------------#
def open_text28():
    b2 = Button(tk,text = "Save",command=lambda:save28())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change28())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change028())
    b5.place(x=600,y=110)
    f = open("28.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save28 ():
    f = open("28.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change28 ():
    b3 = Button(tk,text='Com28',command=open_text28,bg = "red")
    b3.place(x=350,y=300)
def change028 ():
    b3 = Button(tk,text='Com28',command=open_text28,bg = "green")
    b3.place(x=350,y=300)
#-------------------------------#
def open_text29():
    b2 = Button(tk,text = "Save",command=lambda:save29())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change29())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change029())
    b5.place(x=600,y=110)
    f = open("29.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save29 ():
    f = open("29.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change29 ():
    b3 = Button(tk,text='Com29',command=open_text29,bg = "red")
    b3.place(x=500,y=300)
def change029 ():
    b3 = Button(tk,text='Com29',command=open_text29,bg = "green")
    b3.place(x=500,y=300)
#-------------------------------#
def open_text30():
    b2 = Button(tk,text = "Save",command=lambda:save30())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change30())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change030())
    b5.place(x=600,y=110)
    f = open("30.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save30 ():
    f = open("30.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change30 ():
    b3 = Button(tk,text='Com30',command=open_text30,bg = "red")
    b3.place(x=550,y=300)
def change030 ():
    b3 = Button(tk,text='Com30',command=open_text30,bg = "green")
    b3.place(x=550,y=300)
#-------------------------------#
def open_text31():
    b1 = Button(tk,text = "Save",command=lambda:save31())
    b1.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change31())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change031())
    b5.place(x=600,y=110)
    f = open("31.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save31 ():
    f = open("31.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change31 ():
    b3 = Button(tk,text='Com31',command=open_text31,bg = "red")
    b3.place(x=700,y=300)
def change031 ():
    b3 = Button(tk,text='Com31',command=open_text31,bg = "green")
    b3.place(x=700,y=300)
#-------------------------------#com2
def open_text32():
    b2 = Button(tk,text = "Save",command=lambda:save32())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change32())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change032())
    b5.place(x=600,y=110)
    f = open("32.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save32 ():
    f = open("32.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change32 ():
    b3 = Button(tk,text='Com32',command=open_text32,bg = "red")
    b3.place(x=750,y=300)
def change032 ():
    b3 = Button(tk,text='Com32',command=open_text32,bg = "green")
    b3.place(x=750,y=300)
#-------------------------------#
def open_text33():
    b2 = Button(tk,text = "Save",command=lambda:save33())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change33())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change033())
    b5.place(x=600,y=110)
    f = open("33.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save33 ():
    f = open("33.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change33 ():
    b3 = Button(tk,text='Com33',command=open_text33,bg = "red")
    b3.place(x=100,y=350)
def change033 ():
    b3 = Button(tk,text='Com33',command=open_text33,bg = "green")
    b3.place(x=100,y=350)
#-------------------------------#
def open_text34():
    b2 = Button(tk,text = "Save",command=lambda:save34())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change34())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change034())
    b5.place(x=600,y=110)
    f = open("34.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save34 ():
    f = open("34.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change34 ():
    b3 = Button(tk,text='Com34',command=open_text34,bg = "red")
    b3.place(x=150,y=350)
def change034 ():
    b3 = Button(tk,text='Com34',command=open_text34,bg = "green")
    b3.place(x=150,y=350)
#-------------------------------#
def open_text35():
    b2 = Button(tk,text = "Save",command=lambda:save35())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change35())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change035())
    b5.place(x=600,y=110)
    f = open("35.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save35 ():
    f = open("35.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change35 ():
    b3 = Button(tk,text='Com35',command=open_text35,bg = "red")
    b3.place(x=300,y=350)
def change035 ():
    b3 = Button(tk,text='Com35',command=open_text35,bg = "green")
    b3.place(x=300,y=350)
#-------------------------------#
def open_text36():
    b2 = Button(tk,text = "Save",command=lambda:save36())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change36())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change036())
    b5.place(x=600,y=110)
    f = open("36.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save36 ():
    f = open("36.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change36 ():
    b3 = Button(tk,text='Com36',command=open_text36,bg = "red")
    b3.place(x=350,y=350)
def change036 ():
    b3 = Button(tk,text='Com36',command=open_text36,bg = "green")
    b3.place(x=350,y=350)
#-------------------------------#
def open_text37():
    b2 = Button(tk,text = "Save",command=lambda:save37())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change37())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change037())
    b5.place(x=600,y=110)
    f = open("37.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save37 ():
    f = open("37.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change37 ():
    b3 = Button(tk,text='Com37',command=open_text37,bg = "red")
    b3.place(x=500,y=350)
def change037 ():
    b3 = Button(tk,text='Com37',command=open_text37,bg = "green")
    b3.place(x=500,y=350)
#-------------------------------#
def open_text38():
    b2 = Button(tk,text = "Save",command=lambda:save38())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change38())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change038())
    b5.place(x=600,y=110)
    f = open("38.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save38 ():
    f = open("38.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change38 ():
    b3 = Button(tk,text='Com38',command=open_text38,bg = "red")
    b3.place(x=550,y=350)
def change038 ():
    b3 = Button(tk,text='Com38',command=open_text38,bg = "green")
    b3.place(x=550,y=350)
#-------------------------------#
def open_text39():
    b2 = Button(tk,text = "Save",command=lambda:save39())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change39())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change039())
    b5.place(x=600,y=110)
    f = open("39.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save39 ():
    f = open("39.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change39 ():
    b3 = Button(tk,text='Com39',command=open_text39,bg = "red")
    b3.place(x=700,y=350)
def change039 ():
    b3 = Button(tk,text='Com39',command=open_text39,bg = "green")
    b3.place(x=700,y=350)
#-------------------------------#
def open_text40():
    b2 = Button(tk,text = "Save",command=lambda:save40())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change40())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change040())
    b5.place(x=600,y=110)
    f = open("40.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save40 ():
    f = open("40.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change40 ():
    b3 = Button(tk,text='Com40',command=open_text40,bg = "red")
    b3.place(x=750,y=350)
def change040 ():
    b3 = Button(tk,text='Com40',command=open_text40,bg = "green")
    b3.place(x=750,y=350)
#-------------------------------#
def open_text41():
    b2 = Button(tk,text = "Save",command=lambda:sav41())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change41())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change041())
    b5.place(x=600,y=110)
    f = open("41.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save41 ():
    f = open("41.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change41 ():
    b3 = Button(tk,text='Com41',command=open_text41,bg = "red")
    b3.place(x=300,y=400)
def change041 ():
    b3 = Button(tk,text='Com41',command=open_text41,bg = "green")
    b3.place(x=300,y=400)
#-------------------------------#
def open_text42():
    b2 = Button(tk,text = "Save",command=lambda:save42())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change42())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change042())
    b5.place(x=600,y=110)
    f = open("42.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save42 ():
    f = open("42.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change42():
    b3 = Button(tk,text='Com42',command=open_text42,bg = "red")
    b3.place(x=350,y=400)
def change042 ():
    b3 = Button(tk,text='Com42',command=open_text42,bg = "green")
    b3.place(x=350,y=400)
#-------------------------------#
def open_text43():
    b2 = Button(tk,text = "Save",command=lambda:save43())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change43())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change043())
    b5.place(x=600,y=110)
    f = open("43.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save43 ():
    f = open("43.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change43 ():
    b3 = Button(tk,text='Com43',command=open_text43,bg = "red")
    b3.place(x=500,y=400)
def change043 ():
    b3 = Button(tk,text='Com43',command=open_text43,bg = "green")
    b3.place(x=500,y=400)
#-------------------------------#
def open_text44():
    b2 = Button(tk,text = "Save",command=lambda:save44())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change44())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change044())
    b5.place(x=600,y=110)
    f = open("44.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save44 ():
    f = open("44.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change44 ():
    b3 = Button(tk,text='Com44',command=open_text44,bg = "red")
    b3.place(x=550,y=400)
def change044 ():
    b3 = Button(tk,text='Com44',command=open_text44,bg = "green")
    b3.place(x=550,y=400)
#-------------------------------#
def open_text45():
    b2 = Button(tk,text = "Save",command=lambda:save45())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change45())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change045())
    b5.place(x=600,y=110)
    f = open("45.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save45 ():
    f = open("45.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change45 ():
    b3 = Button(tk,text='Com45',command=open_text45,bg = "red")
    b3.place(x=700,y=400)
def change045 ():
    b3 = Button(tk,text='Com45',command=open_text45,bg = "green")
    b3.place(x=700,y=400)
#-------------------------------#
def open_text46():
    b2 = Button(tk,text = "Save",command=lambda:save46())
    b2.place(x=500,y=110)
    b4 = Button(tk,text = "ไม่สามารถใช้งานได้",command=lambda:change46())
    b4.place(x=650,y=110)
    b5 = Button(tk,text = "ใช้งานได้",command=lambda:change046())
    b5.place(x=600,y=110)
    f = open("46.txt","r")
    a = f.read()
    f.close()
    text.insert(INSERT,a)
def save46 ():
    f = open("46.txt","w")
    a = text.get("1.0","end-1c")
    f.write(a)
    f.close()
def change46 ():
    b3 = Button(tk,text='Com46',command=open_text46,bg = "red")
    b3.place(x=750,y=400)
def change046():
    b3 = Button(tk,text='Com46',command=open_text46,bg = "green")
    b3.place(x=750,y=400)
#-------------------------------#

label1 = Label(tk,width = 15,text = "บันทึกข้อมูลเพิ่มเติม",bg = "blue",fg = "white")
label1.pack()
text = Text(tk,fg = "red",width = 50,height = 5)
text.pack()
#-------------------------------#button
b00 = Button(tk,text='Com1',command=open_text1)
b00.place(x=100,y=150)
b01 = Button(tk,text='Com2',command=open_text2)
b01.place(x=150,y=150)
b02 = Button(tk,text='Com3',command=open_text3)
b02.place(x=300,y=150)
b03 = Button(tk,text='Com4',command=open_text4)
b03.place(x=350,y=150)
b04 = Button(tk,text='Com5',command=open_text5)
b04.place(x=500,y=150)
b05 = Button(tk,text='Com6',command=open_text6)
b05.place(x=550,y=150)
b06 = Button(tk,text='Com7',command=open_text7)
b06.place(x=700,y=150)
b07 = Button(tk,text='Com8',command=open_text8)
b07.place(x=750,y=150)
b08 = Button(tk,text='Com9',command=open_text9)
b08.place(x=100,y=200)
b09 = Button(tk,text='Com10',command=open_text10)
b09.place(x=150,y=200)
b010 = Button(tk,text='Com11',command=open_text11)
b010.place(x=300,y=200)
b011 = Button(tk,text='Com12',command=open_text12)
b011.place(x=350,y=200)
b012 = Button(tk,text='Com13',command=open_text13)
b012.place(x=500,y=200)
b013 = Button(tk,text='Com14',command=open_text14)
b013.place(x=550,y=200)
b014 = Button(tk,text='Com15',command=open_text15)
b014.place(x=700,y=200)
b015 = Button(tk,text='Com16',command=open_text16)
b015.place(x=750,y=200)
b016 = Button(tk,text='Com17',command=open_text17)
b016.place(x=100,y=250)
b017 = Button(tk,text='Com18',command=open_text18)
b017.place(x=150,y=250)
b018 = Button(tk,text='Com19',command=open_text19)
b018.place(x=300,y=250)
b019 = Button(tk,text='Com20',command=open_text20)
b019.place(x=350,y=250)
b020 = Button(tk,text='Com21',command=open_text21)
b020.place(x=500,y=250)
b021 = Button(tk,text='Com22',command=open_text22)
b021.place(x=550,y=250)
b022 = Button(tk,text='Com23',command=open_text23)
b022.place(x=700,y=250)
b023 = Button(tk,text='Com24',command=open_text24)
b023.place(x=750,y=250)
b024 = Button(tk,text='Com25',command=open_text25)
b024.place(x=100,y=300)
b025 = Button(tk,text='Com26',command=open_text26)
b025.place(x=150,y=300)
b026 = Button(tk,text='Com27',command=open_text27)
b026.place(x=300,y=300)
b027 = Button(tk,text='Com28',command=open_text28)
b027.place(x=350,y=300)
b028 = Button(tk,text='Com29',command=open_text29)
b028.place(x=500,y=300)
b029 = Button(tk,text='Com30',command=open_text30)
b029.place(x=550,y=300)
b030 = Button(tk,text='Com31',command=open_text31)
b030.place(x=700,y=300)
b031 = Button(tk,text='Com32',command=open_text32)
b031.place(x=750,y=300)
b032 = Button(tk,text='Com33',command=open_text33)
b032.place(x=100,y=350)
b033 = Button(tk,text='Com34',command=open_text34)
b033.place(x=150,y=350)
b034 = Button(tk,text='Com35',command=open_text35)
b034.place(x=300,y=350)
b035 = Button(tk,text='Com36',command=open_text36)
b035.place(x=350,y=350)
b036 = Button(tk,text='Com37',command=open_text37)
b036.place(x=500,y=350)
b037 = Button(tk,text='Com38',command=open_text38)
b037.place(x=550,y=350)
b038 = Button(tk,text='Com39',command=open_text39)
b038.place(x=700,y=350)
b039 = Button(tk,text='Com40',command=open_text40)
b039.place(x=750,y=350)
b040 = Button(tk,text='Com41',command=open_text41)
b040.place(x=300,y=400)
b041 = Button(tk,text='Com42',command=open_text42)
b041.place(x=350,y=400)
b042 = Button(tk,text='Com43',command=open_text43)
b042.place(x=500,y=400)
b043 = Button(tk,text='Com44',command=open_text44)
b043.place(x=550,y=400)
b044 = Button(tk,text='Com45',command=open_text45)
b044.place(x=700,y=400)
b045 = Button(tk,text='Com46',command=open_text46)
b045.place(x=750,y=400)
#-------------------------------#
tk.mainloop()
