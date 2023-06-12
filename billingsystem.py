from tkinter import *
from tkinter import messagebox
import tempfile
import os

root=Tk()
root.title('Billing Management System')
root.geometry('1280x720')
bg_color='#2D9290'

#==================Variable===================
Bread=IntVar()
Maggie=IntVar()
Chai=IntVar()
Coffee=IntVar()
Total1=IntVar()

cb1=StringVar()
cm1=StringVar()
ch1=StringVar()
cof1=StringVar()
Total1_cost=StringVar()

#================Functions===========
def Total():
    if Bread.get()==0 and Maggie.get()==0 and Chai.get()==0 and Coffee.get()==0:
        messagebox.showerror('Error','Please select number of quantity')
    else:
        b=Bread.get()
        m=Maggie.get()
        c=Chai.get()
        co=Coffee.get()

        t=float(b*8+m*50+c*15+co*25)
        Total1.set(b+m+c+co)
        Total1_cost.set('₹'+str(round(t,2)))

        cb1.set('₹'+str(round(b*8,2)))
        cm1.set('₹'+str(round(m*50,2)))
        ch1.set('₹'+str(round(c*15,2)))
        cof1.set('₹'+str(round(co*25,2)))

def receipt():
    textarea.delete(1.0,END)
    textarea.insert(END,'Items\tNumber of Items\tCost of Items')
    textarea.insert(END,f'\n\nBread\t\t{Bread.get()}\t {cb1.get()}')
    textarea.insert(END,f'\n\nMaggie\t\t{Maggie.get()}\t {cm1.get()}')
    textarea.insert(END,f'\n\nChai\t\t{Chai.get()}\t {ch1.get()}')
    textarea.insert(END,f'\n\nCoffee\t\t{Coffee.get()}\t {cof1.get()}')
    textarea.insert(END,'\n\n================================')
    textarea.insert(END,f'\n\nTotal\t\t{Total1.get()}\t {Total1_cost.get()}')
    textarea.insert(END,'\n\n================================')

def print():
    q=textarea.get('1.0','end-1c')
    filename=tempfile.mktemp('.txt')
    with open(filename,'w',encoding="utf-8") as f:
        f.write(q)
    os.startfile(filename,'Print')

def reset():
    textarea.delete(1.0,END)
    Bread.set(0)
    Maggie.set(0)
    Chai.set(0)
    Coffee.set(0)
    Total1.set(0)

    cb1.set('')
    cm1.set('')
    ch1.set('')
    cof1.set('')
    Total1_cost.set('')

def exit():
    if messagebox.askyesno('Exit','Do you really want to exit'):
        root.destroy()




title=Label(root,text='Billing Management System',bg=bg_color,fg='white',font=('times new romman',35,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)

#=====================Product Details===========================================
f1=LabelFrame(root,text='Product Details',font=('times new romman',18,'bold'),fg='gold',bg=bg_color,relief=RIDGE,bd=15)
f1.place(x=5,y=90,width=800,height=500)

#=====================Heading===================================

itm=Label(f1,text='Items',font=('Helvetic',25,'bold','underline'),fg='black',bg=bg_color)
itm.grid(row=0,column=0,padx=20,pady=15)

n=Label(f1,text='No. Of Items',font=('Helvetic',25,'bold','underline'),fg='black',bg=bg_color)
n.grid(row=0,column=1,padx=20,pady=15)

cost=Label(f1,text='Cost Of Items',font=('Helvetic',25,'bold','underline'),fg='black',bg=bg_color)
cost.grid(row=0,column=2,padx=20,pady=15)

#======================Product=====================

bread=Label(f1,text='Bread',font=('times new romman',20,'bold'),fg='lawngreen',bg=bg_color)
bread.grid(row=1,column=0,padx=20,pady=15)
b_txt=Entry(f1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Bread)
b_txt.grid(row=1,column=1,padx=20,pady=15)
cb_txt=Entry(f1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=cb1)
cb_txt.grid(row=1,column=2,padx=20,pady=15)

maggie=Label(f1,text='Maggie',font=('times new romman',20,'bold'),fg='lawngreen',bg=bg_color)
maggie.grid(row=2,column=0,padx=20,pady=15)
m_txt=Entry(f1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Maggie)
m_txt.grid(row=2,column=1,padx=20,pady=15)
cm_txt=Entry(f1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=cm1)
cm_txt.grid(row=2,column=2,padx=20,pady=15)

chai=Label(f1,text='Chai',font=('times new romman',20,'bold'),fg='lawngreen',bg=bg_color)
chai.grid(row=3,column=0,padx=20,pady=15)
c_txt=Entry(f1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Chai)
c_txt.grid(row=3,column=1,padx=20,pady=15)
ch_txt=Entry(f1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=ch1)
ch_txt.grid(row=3,column=2,padx=20,pady=15)

coffee=Label(f1,text='Coffee',font=('times new romman',20,'bold'),fg='lawngreen',bg=bg_color)
coffee.grid(row=4,column=0,padx=20,pady=15)
co_txt=Entry(f1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Coffee)
co_txt.grid(row=4,column=1,padx=20,pady=15)
cof_txt=Entry(f1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=cof1)
cof_txt.grid(row=4,column=2,padx=20,pady=15)

total=Label(f1,text='Total ',font=('times new romman',20,'bold'),fg='lawngreen',bg=bg_color)
total.grid(row=5,column=0,padx=20,pady=15)
t_txt=Entry(f1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Total1)
t_txt.grid(row=5,column=1,padx=20,pady=15)
to_txt=Entry(f1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Total1_cost)
to_txt.grid(row=5,column=2,padx=20,pady=15)

#======================Bill Area=======================

f2=Frame(root,relief=GROOVE,bd=10)
f2.place(x=820,y=90,width=430,height=500)
bill_title=Label(f2,text='Receipt',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
scrol=Scrollbar(f2,orient=VERTICAL)
scrol.pack(side=RIGHT,fill=Y)
textarea=Text(f2,font='arial 15 ',yscrollcommand=scrol.set)
textarea.pack(fill=BOTH)
scrol.config(command=textarea.yview)

#===================Button====================
f3=Frame(root,relief=GROOVE,bd=10,bg=bg_color)
f3.place(x=5,y=590,width=1270,height=120)

btn1=Button(f3,text='Total',font='arial 25 bold',bg='yellow',fg='crimson',padx=5,pady=5,width=10,command=Total)
btn1.grid(row=0,column=0,padx=10,pady=5)

btn2=Button(f3,text='Receipt',font='arial 25 bold',bg='yellow',fg='crimson',padx=5,pady=5,width=10,command=receipt)
btn2.grid(row=0,column=1,padx=10,pady=10)

btn3=Button(f3,text='Print',font='arial 25 bold',bg='yellow',fg='crimson',padx=5,pady=5,width=10,command=print)
btn3.grid(row=0,column=2,padx=10,pady=10)

btn4=Button(f3,text='Reset',font='arial 25 bold',bg='yellow',fg='crimson',padx=5,pady=5,width=10,command=reset)
btn4.grid(row=0,column=4,padx=10,pady=10)

btn5=Button(f3,text='Exit',font='arial 25 bold',bg='yellow',fg='crimson',padx=5,pady=5,width=10,command=exit)
btn5.grid(row=0,column=5,padx=10,pady=10)

root.mainloop() 
