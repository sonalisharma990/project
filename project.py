from tkinter import*
from PIL import ImageTk, Image
import os
import random
import time
import sqlite3

master = Tk()
master.geometry("1600x700+0+0")
master.title("Restaurant Management System")

Tops = Frame(master,bg='white',width = 1600,height=60,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(master,width = 800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)
f2 = Frame(master ,width = 50,height=200,relief=SUNKEN)
f2.pack(side=RIGHT)
img=ImageTk.PhotoImage(Image.open("20180713_012621.png"))
panel=Label(master,image=img)
panel.pack(side="bottom",fill="both",expand="yes")

#DATA BASES
table2=sqlite3.connect("hotel.db")
#table2.execute('''CREATE TABLE ORDERS(ORDER_NUMBER INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,FRIES_MEAL TEXT,LUNCH_MEAL TEXT,BURGER_MEAL TEXT,PIZZA_MEAL TEXT,CHEESE_BURGER TEXT,DRINKS TEXT,COST TEXT,SERVICE_CHARGE TEXT,TAX TEXT,SUBTOTAL TEXT,TOTAL TEXT);''')
#table2.commit()

#TIME AT THE TOP
localtime=time.asctime(time.localtime(time.time()))

#HEADING AT THE TOP
lblinfo = Label(Tops, font=( 'algerian' ,30,'bold','underline' ),text="Restaurant Management System",fg="black",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'monotype' ,20, ),text=localtime,fg="black",anchor=W)
lblinfo.grid(row=1,column=0)


def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(Fries_Meal.get())
    colfries= float(Lunch_Meal.get())
    cob= float(Burger_Meal.get())
    cofi= float(Pizza_Meal.get())
    cochee= float(Cheese_Burger.get())
    codr= float(Drinks.get())

    cost_of_Fries_Meal = cof*25
    cost_of_Lunch_Meal = colfries*40
    cost_of_Burger_Meal = cob*35
    cost_of_Pizza_Meal = cofi*80
    cost_of_Cheese_Burger = cochee*40
    cost_of_Drinks = codr*35

    costofmeal = "Rs.", str('%.2f' % (cost_of_Fries_Meal + cost_of_Lunch_Meal + cost_of_Burger_Meal + cost_of_Pizza_Meal + cost_of_Cheese_Burger + cost_of_Drinks))
    PayTax = ((cost_of_Fries_Meal + cost_of_Lunch_Meal + cost_of_Burger_Meal + cost_of_Pizza_Meal + cost_of_Cheese_Burger + cost_of_Drinks) * 0.33)
    Totalcost = (cost_of_Fries_Meal + cost_of_Lunch_Meal + cost_of_Burger_Meal + cost_of_Pizza_Meal + cost_of_Cheese_Burger + cost_of_Drinks)
    Ser_Charge = ((cost_of_Fries_Meal + cost_of_Lunch_Meal + cost_of_Burger_Meal + cost_of_Pizza_Meal + cost_of_Cheese_Burger + cost_of_Drinks) / 99)
    Service = "Rs.", str('%.2f' % Ser_Charge)
    OverAllCost = "Rs.", str(PayTax + Totalcost + Ser_Charge)
    PaidTax = "Rs.", str('%.2f' % PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)


def exit():
    master.destroy()

def reset():
    rand.set("")
    Fries_Meal.set(0.0)
    Lunch_Meal.set(0.0)
    Burger_Meal.set(0.0)
    Pizza_Meal.set(0.0)
    Subtotal.set(0.0)
    Total.set(0.0)
    Service_Charge.set(0.0)
    Drinks.set(0.0)
    Tax.set(0.0)
    cost.set(0.0)
    Cheese_Burger.set(0.0)

rand = StringVar()
Fries_Meal = StringVar()
Lunch_Meal = StringVar()
Burger_Meal = StringVar()
Pizza_Meal = StringVar()
Cheese_Burger = StringVar()
Drinks = StringVar()
cost = StringVar()
Service_Charge = StringVar()
Tax = StringVar()
Subtotal = StringVar()
Total = StringVar()
reset()

def billsave():
    cof = float(Fries_Meal.get())
    colfries = float(Lunch_Meal.get())
    cob = float(Burger_Meal.get())
    cofi = float(Pizza_Meal.get())
    cochee = float(Cheese_Burger.get())
    codr = float(Drinks.get())

    cost_of_Fries_Meal = cof * 25
    cost_of_Lunch_Meal = colfries * 40
    cost_of_Burger_Meal = cob * 35
    cost_of_Pizza_Meal = cofi * 80
    cost_of_Cheese_Burger = cochee * 40
    cost_of_Drinks = codr * 35

    costofmeal = "Rs.", str('%.2f' % (cost_of_Fries_Meal + cost_of_Lunch_Meal + cost_of_Burger_Meal + cost_of_Pizza_Meal + cost_of_Cheese_Burger + cost_of_Drinks))
    PayTax = ((cost_of_Fries_Meal + cost_of_Lunch_Meal + cost_of_Burger_Meal + cost_of_Pizza_Meal + cost_of_Cheese_Burger + cost_of_Drinks) * 0.33)
    Totalcost = (cost_of_Fries_Meal + cost_of_Lunch_Meal + cost_of_Burger_Meal + cost_of_Pizza_Meal + cost_of_Cheese_Burger + cost_of_Drinks)
    Ser_Charge = ((cost_of_Fries_Meal + cost_of_Lunch_Meal + cost_of_Burger_Meal + cost_of_Pizza_Meal + cost_of_Cheese_Burger + cost_of_Drinks) / 99)
    Service = "Rs.", str('%.2f' % Ser_Charge)
    OverAllCost = "Rs.", str(PayTax + Totalcost + Ser_Charge)
    PaidTax = "Rs.", str('%.2f' % PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)
    table2.execute("INSERT INTO ORDERS(FRIES_MEAL,LUNCH_MEAL,BURGER_MEAL,PIZZA_MEAL,CHEESE_BURGER,DRINKS,COST,SERVICE_CHARGE,TAX,SUBTOTAL,TOTAL) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (str(cost_of_Fries_Meal),str(cost_of_Lunch_Meal),str(cost_of_Burger_Meal),str(cost_of_Pizza_Meal),str(cost_of_Cheese_Burger),str(cost_of_Drinks),str(costofmeal),str(Service),str(PaidTax ),str(Totalcost),str(OverAllCost),))
    table2.commit()
    for row in table2.execute("SELECT * FROM ORDERS"):
        print(row)


lblreference = Label(f1, font=( 'arial' ,16, 'bold','italic' ),text="Order No.",fg="black",bd=10,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('arial' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtreference.grid(row=0,column=1)

lblfries = Label(f1, font=( 'arial' ,16, 'bold','italic' ),text="Fries Meal",fg="black",bd=10,anchor='w')
lblfries.grid(row=1,column=0)
txtfries = Entry(f1,font=('arial' ,16,'bold'), textvariable=Fries_Meal , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtfries.grid(row=1,column=1)

lbllunch_meal = Label(f1, font=( 'arial' ,16, 'bold','italic' ),text="Lunch Meal",fg="black",bd=10,anchor='w')
lbllunch_meal.grid(row=2,column=0)
txtlunch_meal = Entry(f1,font=('arial' ,16,'bold'), textvariable=Lunch_Meal , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtlunch_meal.grid(row=2,column=1)

lblburger_meal = Label(f1, font=( 'arial' ,16, 'bold','italic' ),text="Burger Meal",fg="black",bd=10,anchor='w')
lblburger_meal.grid(row=3,column=0)
txtburger_meal = Entry(f1,font=('arial' ,16,'bold'), textvariable=Burger_Meal , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtburger_meal.grid(row=3,column=1)

lblpizza_meal = Label(f1, font=( 'arial' ,16, 'bold','italic' ),text="Pizza Meal",fg="black",bd=10,anchor='w')
lblpizza_meal.grid(row=4,column=0)
txtpizza_meal = Entry(f1,font=('arial' ,16,'bold'), textvariable=Pizza_Meal , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtpizza_meal.grid(row=4,column=1)

lblCheese_burger = Label(f1, font=( 'arial' ,16, 'bold','italic' ),text="Cheese Burger",fg="black",bd=10,anchor='w')
lblCheese_burger.grid(row=5,column=0)
txtCheese_burger = Entry(f1,font=('arial' ,16,'bold'), textvariable=Cheese_Burger , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtCheese_burger.grid(row=5,column=1)

lblDrinks = Label(f1, font=( 'arial' ,16, 'bold','italic' ),text="Drinks",fg="black",bd=10,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks = Entry(f1,font=('arial' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtDrinks.grid(row=0,column=3)



lblcost = Label(f1, font=( 'arial' ,16, 'bold','italic' ),text="cost",fg="black",bd=10,anchor='w')
lblcost.grid(row=1,column=2)
txtcost = Entry(f1,font=('arial' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtcost.grid(row=1,column=3)

lblService_Charge = Label(f1, font=( 'arial' ,16, 'bold','italic' ),text="Service Charge",fg="black",bd=10,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge = Entry(f1,font=('arial' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtService_Charge.grid(row=2,column=3)

lblTax = Label(f1, font=( 'arial' ,16, 'bold','italic' ),text="Tax",fg="black",bd=10,anchor='w')
lblTax.grid(row=3,column=2)
txtTax = Entry(f1,font=('arial' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTax.grid(row=3,column=3)

lblSubtotal = Label(f1, font=( 'arial' ,16, 'bold','italic' ),text="Subtotal",fg="black",bd=10,anchor='w')
lblSubtotal.grid(row=4,column=2)
txtSubtotal = Entry(f1,font=('arial' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtSubtotal.grid(row=4,column=3)

lblTotal = Label(f1, font=( 'arial' ,16, 'bold','italic' ),text="Total",fg="black",bd=10,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('arial' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTotal.grid(row=5,column=3)

#BUTTONS AT THE BOTTOM
btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('arial' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command=Ref)
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('arial' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)
btnreset.grid(row=7, column=3)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('arial' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=exit)
btnexit.grid(row=8, column=3)

btnbill=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('arial' ,16,'bold'),width=10, text="SAVE BILL", bg="powder blue",command=billsave)
btnbill.grid(row=8, column=1)

def price():
    root = Tk()
    root.geometry("600x300+0+0")
    root.title("PRICE")
    lblinfo = Label(root, font=('arial', 30, 'bold', 'underline'), text="MENU CARD", fg="black", bd=10, anchor='w')
    lblinfo.grid(row=0, column=1)
    lblinfo = Label(root, font=('arial', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(root, font=('arial', 15, 'bold'), text="  ..........  ", fg="black", anchor=W)
    lblinfo.grid(row=1, column=1)
    lblinfo = Label(root, font=('arial', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(root, font=('arial', 15, 'bold'), text="Fries Meal", fg="red", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(root, font=('arial', 15, 'bold'), text="  ..........  ", fg="red", anchor=W)
    lblinfo.grid(row=2, column=1)
    lblinfo = Label(root, font=('arial', 15, 'bold'), text="25/-", fg="red", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(root, font=('arial', 15, 'bold'), text="Lunch Meal", fg="red", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(root, font=('arial', 15, 'bold'), text="  ..........  ", fg="red", anchor=W)
    lblinfo.grid(row=3, column=1)
    lblinfo = Label(root, font=('arial', 15, 'bold'), text="40/-", fg="red", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(root, font=('arial', 15, 'bold'), text="Burger Meal", fg="red", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(root, font=('arial', 15, 'bold'), text="  ..........  ", fg="red", anchor=W)
    lblinfo.grid(row=4, column=1)
    lblinfo = Label(root, font=('arial', 15, 'bold'), text="35/-", fg="red", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(root, font=('arial', 15, 'bold'), text="Pizza Meal", fg="red", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(root, font=('arial', 15, 'bold'), text="  ..........  ", fg="red", anchor=W)
    lblinfo.grid(row=5, column=1)
    lblinfo = Label(root, font=('arial', 15, 'bold'), text="80/-", fg="red", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(root, font=('arial', 15, 'bold'), text="Cheese Burger", fg="red", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(root, font=('arial', 15, 'bold'), text="  ..........  ", fg="red", anchor=W)
    lblinfo.grid(row=6, column=1)
    lblinfo = Label(root, font=('arial', 15, 'bold'), text="40/-", fg="red", anchor=W)
    lblinfo.grid(row=6, column=3)
    lblinfo = Label(root, font=('arial', 15, 'bold'), text="Drinks", fg="red", anchor=W)
    lblinfo.grid(row=7, column=0)
    lblinfo = Label(root, font=('arial', 15, 'bold'), text="  ..........  ", fg="red", anchor=W)
    lblinfo.grid(row=7, column=1)
    lblinfo = Label(root, font=('arial', 15, 'bold'), text="35/-", fg="red", anchor=W)
    lblinfo.grid(row=7, column=3)
    root.mainloop()
btnprice = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('arial', 16, 'bold'), width=10, text="PRICE", bg="powder blue", command=price)
btnprice.grid(row=7, column=0)

master.mainloop()
