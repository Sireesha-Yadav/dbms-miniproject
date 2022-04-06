from tkinter import *
import sqlite3
import tkinter  as tk
from tkinter import messagebox

a_692 = Tk()
a_692.geometry("1200x1000")
a_692.title("Car Rental System" )


date=IntVar()
receipt=IntVar()
company=StringVar()
rep=StringVar()
loc=StringVar()
csz=StringVar()
phone=IntVar()
name=StringVar()
license=StringVar()
address=StringVar()
csz1=StringVar()
phone1=IntVar()
VIN1=StringVar()
make=StringVar()
year=IntVar()
color=StringVar()
reg=StringVar()
model=StringVar()
milg=IntVar()
cash=IntVar()
deb=IntVar()
cred=IntVar()
oth=IntVar()
rp_name=StringVar()
sig=StringVar()



def Database():
    
    dat=date.get()
    recp=receipt.get()
    comp=company.get()
    repnt=rep.get()
    locn=loc.get()
    city=csz.get()
    phn=phone.get()
    nm=name.get()
    lic=license.get()
    adds=address.get()
    sz1=csz1.get()
    phn1=phone1.get()
    vehic=VIN1.get()
    mk=make.get()
    yr=year.get()
    clr=color.get()
    regis=reg.get()
    mdl=model.get()
    mileage=milg.get()
    cs=cash.get()
    tx=deb.get()
    ttl=cred.get()
    amount=oth.get()
    repres=rp_name.get()
    sign=sig.get()
    
    
    db = sqlite3.connect('car1.db')
    cursor=db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS CAR1(date INT,receipt INT,company TEXT,rep TEXT,loc TEXT,csz TEXT,phone INT,name TEXT,license TEXT,address TEXT,csz1 TEXT,phone1 INT,VIN1 TEXT,make TEXT,year INT,color TEXT,reg TEXT,model TEXT,milg INT,cash INT,deb INT,cred INT,oth INT,rp_name TEXT,sig TEXT)')
    cursor.execute('INSERT INTO CAR1(date,receipt,company,rep,loc,csz,phone,name,license,address,csz1,phone1,VIN1,make,year,color,reg,model,milg,cash,deb,cred,oth,rp_name,sig) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                  (dat,recp,comp,repnt,locn,city,phn,nm,lic,sz1,phn1,adds,vehic,mk,yr,clr,regis,mdl,mileage,cs,tx,ttl,amount,repres,sign))
    db.commit()
    msg = messagebox.showinfo( "DB Demo","SUBMITTED SUCCESSFULLY")
    


def display():
    db = sqlite3.connect('car1.db')
    with db:
      cursor=db.cursor()
      my_w = tk.Tk()
      my_w.geometry("400x250") 

      r_set=cursor.execute('''SELECT * from CAR1 ''');
      i=0  
      for CAR1 in r_set: 
            for j in range(len(CAR1)):
                e = Entry(my_w, width=10, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, CAR1[j])
            i=i+1  
   
title = Label(a_692,text="CAR RENTAL RECEIPT",foreground="blue",font=("Calibri Bold",30),anchor=N).grid(row=0,column=2)
date = Label(a_692,text="DATE:- ").grid(row=3,column=0)
date = Entry(a_692)
date.grid(row=3,column=1)

receipt = Label(a_692,text="RECEIPT#:- ").grid(row=3,column=3)
receipt = Entry(a_692)
receipt.grid(row=3,column=4)

subhd1 = Label(a_692,text="COMPANY INFO",foreground="red",font=("Calibri Bold",16)).grid(row=7,column=1)

company = Label(a_692,text="COMPANY:- ").grid(row=9,column=0)
company = Entry(a_692)
company.grid(row=9,column=1)

rep = Label(a_692,text="REPRESENTATIVE:-").grid(row=10,column=0)
rep = Entry(a_692)
rep.grid(row=10,column=1)

loc = Label(a_692,text="LOCATION:-").grid(row=11,column=0)
loc = Entry(a_692)
loc.grid(row=11,column=1)

csz = Label(a_692,text="CITY/STATE/ZIP:-").grid(row=12,column=0)
csz = Entry(a_692)
csz.grid(row=12,column=1)

phone = Label(a_692,text="PHONE:-").grid(row=13,column=0)
phone = Entry(a_692)
phone.grid(row=13,column=1)

subhd2 = Label(a_692,text="LESSEE INFO",foreground="red",font=("Calibri Bold",16)).grid(row=7,column=4)

name = Label(a_692,text="NAME:-").grid(row=9,column=3)
name = Entry(a_692)
name.grid(row=9,column=4)

license = Label(a_692,text="LICENSE#:-").grid(row=10,column=3)
license = Entry(a_692)
license.grid(row=10,column=4)

address = Label(a_692,text="ADDRESS:-").grid(row=11,column=3)
address = Entry(a_692)
address.grid(row=11,column=4)

csz1 = Label(a_692,text="CITY/STATE/ZIP:-").grid(row=12,column=3)
csz1 = Entry(a_692)
csz1.grid(row=12,column=4)

phone1 = Label(a_692,text="PHONE:-").grid(row=13,column=3)
phone1 = Entry(a_692)
phone.grid(row=13,column=4)

vi = Label(a_692,text="VEHICLE INFORMATION",foreground="blue",font=("Calibri Bold",26)).grid(row=16,column=2)

VIN1 = Label(a_692,text="VIN:-").grid(row=18,column=0)
VIN1 = Entry(a_692)
VIN1.grid(row=18,column=1)

make = Label(a_692,text="MAKE:-").grid(row=19,column=0)
make = Entry(a_692)
make.grid(row=19,column=1)

year = Label(a_692,text="YEAR:-").grid(row=20,column=0)
year = Entry(a_692)
year.grid(row=20,column=1)

color = Label(a_692,text="COLOR:-").grid(row=21,column=0)
color = Entry(a_692)
color.grid(row=21,column=1)

reg = Label(a_692,text="REGISTRATION#:-").grid(row=18,column=3)
reg = Entry(a_692)
reg.grid(row=18,column=4)

model = Label(a_692,text="MODEL:-").grid(row=19,column=3)
model = Entry(a_692)
model.grid(row=19,column=4)

milg = Label(a_692,text="MILEAGE:-").grid(row=20,column=3)
milg = Entry(a_692)
milg.grid(row=20,column=4)

VIN = Label(a_692,text="VIN",foreground="orange",font=("Calibri Bold",16)).grid(row=50,column=0)
cd = Label(a_692,text="COST/DAY",foreground="orange",font=("Calibri Bold",16)).grid(row=50,column=1)
of = Label(a_692,text="OF DAYS#",foreground="orange",font=("Calibri Bold",16)).grid(row=50,column=2)
ac = Label(a_692,text="ADDITIONAL COST",foreground="orange",font=("Calibri Bold",16)).grid(row=50,column=3)
lc = Label(a_692,text="LINE COST",foreground="orange",font=("Calibri Bold",16)).grid(row=50,column=4)

pm = Label(a_692,text="PAYMENT METHOD:-",foreground="purple",font=("Calibri Bold",14)).grid(row=57,column=0)
st = Label(a_692,text="SUBTOTAL:-",font=("Calibri",14)).grid(row=57,column=2)
st = Entry(a_692).grid(row=57,column=3)

tax= Label(a_692,text="TAX(5%):-",font=("Calibri",12)).grid(row=58,column=2)
tax = Entry(a_692)
tax.grid(row=58,column=3)

total= Label(a_692,text="TOTAL:-",font=("Calibri",12)).grid(row=59,column=2)
total= Entry(a_692)
total.grid(row=59,column=3)

ap = Label(a_692,text="AMOUNT PAID:-",font=("Calibri",12)).grid(row=60,column=2)
ap = Entry(a_692)
ap.grid(row=60,column=3)

sig = Label(a_692,text="AUTHORIZED SIGNATURE:-",font=("Calibri",12)).grid(row=62,column=3)
sig = Entry(a_692)
sig.grid(row=62,column=4)

rp_name = Label(a_692,text="REPRESENTATIVE NAME:-",font=("Calibri",12)).grid(row=63,column=3)
rp_name = Entry(a_692)
rp_name.grid(row=63,column=4)

a=Checkbutton(a_692,text="CASH:-",font=("Calibri",12)).grid(row=58,column=0)
b=Checkbutton(a_692,text="DEBIT:-",font=("Calibri",12)).grid(row=59,column=0)
c=Checkbutton(a_692,text="CREDIT:-",font=("Calibri",12)).grid(row=60,column=0)
d=Checkbutton(a_692,text="OTHER:-",font=("Calibri",12)).grid(row=61,column=0)

cash=Entry(a_692)
cash.grid(row=58,column=1)
deb=Entry(a_692)
deb.grid(row=59,column=1)
cred=Entry(a_692)
cred.grid(row=60,column=1)
oth=Entry(a_692)
oth.grid(row=61,column=1)

e=Entry(a_692)
e.grid(row=51,column=0)
f=Entry(a_692)
f.grid(row=52,column=0)
g=Entry(a_692)
g.grid(row=53,column=0)

h=Entry(a_692)
h.grid(row=51,column=1)
i=Entry(a_692)
i.grid(row=52,column=1)
j=Entry(a_692)
j.grid(row=53,column=1)

k=Entry(a_692)
k.grid(row=51,column=2)
l=Entry(a_692)
l.grid(row=52,column=2)
m=Entry(a_692)
m.grid(row=53,column=2)

n=Entry(a_692)
n.grid(row=51,column=3)
o=Entry(a_692)
o.grid(row=52,column=3)
p=Entry(a_692)
p.grid(row=53,column=3)

q=Entry(a_692)
q.grid(row=51,column=4)
r=Entry(a_692)
r.grid(row=52,column=4)
s=Entry(a_692)
s.grid(row=53,column=4)
t=Entry(a_692)
t.grid(row=54,column=4)
u=Entry(a_692)
u.grid(row=55,column=4)
v=Entry(a_692)
v.grid(row=56,column=4)
w=Entry(a_692)
w.grid(row=60,column=4)

msg=Button(a_692, text='SUBMIT',command=Database,width=20).place(x=1150,y=430)
msg=Button(a_692,text="DISPLAY RECORD(s)",command=display,width=20).place(x=1150,y=530) 

a_692.mainloop()