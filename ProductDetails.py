import tkinter as tk
from tkinter import ttk
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from Code import *
import mysql.connector as mc
import Code as c



def create_Details(id):

    
    #window attributes 
    app = customtkinter.CTkToplevel() #creating tkinter window
    app.geometry("620x620") #window dimension
    app.title('Products Details') #window title 

    # Create a custom style
    style = ttk.Style()
    style.configure('Custom.TLabel', background='#630000') # Set the background color for the label
    style.configure('Custom.TEntry', fieldbackground='#FFFFFF',font=("default", 40 )) # Set the background color for the entry field


    LoginBg = ImageTk.PhotoImage(Image.open('DetailsBg.png')) #open the image 
    L1 = customtkinter.CTkLabel(master=app, image=LoginBg,text="") #append img as Label
    L1.pack()


    # Create the label 1
    label = Label(L1, text='Product name:',font=("bold",15) ,fg='white',bg="#630000")
    label.place(relx=0.1, rely=0.1)


    # Create the entry field 1
    nom = Entry(L1, width=30, font="Helvetica 18",bg="#D8B6A4",)
    nom.place(relx=0.1, rely=0.15,width=208, height=50)

    # Create the label 2
    label = Label(L1, text='Product price:',font=("bold",15) ,fg='white',bg="#630000")
    label.place(relx=0.1, rely=0.3)


    # Create the entry field 2
    price = Entry(L1, width=30, font="Helvetica 18",bg="#D8B6A4",)
    price.place(relx=0.1, rely=0.35,width=208, height=50)

    # Create the label 3
    label = Label(L1, text='Product Stock:',font=("bold",15) ,fg='white',bg="#630000")
    label.place(relx=0.1, rely=0.5)


    # Create the entry field 3
    stock = Entry(L1, width=30,font="Helvetica 18",bg="#D8B6A4",)
    stock.place(relx=0.1, rely=0.55,width=208, height=50)

    # Create the label 4
    label = Label(L1, text='Date dentrer de stock:',font=("bold",15) ,fg='white',bg="#630000")
    label.place(relx=0.1, rely=0.7)


    # Create the entry field 4
    De = Entry(L1,font="Helvetica 18",bg="#D8B6A4")
    De.place(relx=0.1, rely=0.75, width=208, height=50)

    
    
    delete_btn=Button(master=L1,width=12,height=2, text='Update',bg="#D8B6A4",fg="white" , font="bold",command=lambda : UpdateQuit(nom,price,stock,De,app))
    delete_btn.place(relx=0.71, rely=0.85)
    

    #Looking for data in database:



    
    
    try:
        db = c.Database()
        db.connect()
        cursor = db.conn.cursor()
        sql = "SELECT nom, price, stock, date_dentrer ,description FROM products WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        results = cursor.fetchall()
        for row in results:
            name = row[0]
            pricev = row[1]
            stockv = row[2]
            dateX = row[3]
            des = row[4]
        nom.delete(0, END)
        nom.insert(0, name)
        price.delete(0, END)
        price.insert(0, pricev)
        stock.delete(0, END)
        stock.insert(0, stockv)
        De.delete(0, END)
        De.insert(0,dateX)
        

    
    except Exception as error:
        print(f"Error retrieving data: {error}")

    
    
    
    app.mainloop()










def UpdateQuit(entry_widget1,entry_widget2,entry_widget3,entry_widget4,app):
    nom = entry_widget1.get()
    price = entry_widget2.get()
    stock = entry_widget3.get()
    dateE = entry_widget4.get()
    c.update_product(nom,price,stock,dateE)
    app.destroy()