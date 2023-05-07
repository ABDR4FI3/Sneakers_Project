import tkinter 
from tkinter import  messagebox
import customtkinter
from PIL import ImageTk, Image
import ProductDetails as pd
import pymysql
import mysql.connector as mc

class Database :
    def __init__(self):
        self.host="localhost"
        self.user="root"
        self.password=""
        self.data="pfa"
        self.conn=None
        self.cursor=None
    def connect(self):
        try:
            self.conn = mc.connect(host=self.host ,database = self.data , user = self.user, password = self.password )
            self.cursor = self.conn.cursor()
            messagebox.showinfo('SUCCES',"connected to DataBase succesfully")
        except mc.Error as er:
            messagebox.showerror("error","failed to connect to database")
            print(er)

def connection():

    database = Database()
    database.connect() 
    return database.connect

def Show_Product(id,entry_widget,app):
    num = id
    app.destroy()
    pd.create_Details(id)

    
def Entry_check(User,password):
    db = Database()
    db.connect()
    try:
        db.cursor = db.conn.cursor()
        sql = f"SELECT * FROM users WHERE nom='{User}' AND password='{password}'"
        db.cursor.execute(sql)
        result = db.cursor.fetchone()
        if result is not None:
            return True
        else:
            messagebox.showerror("Error", "Incorrect username or password")
    except mc.Error as er:
        print(er)


    #Create new User :

def insert_user(username, password):
    #messagebox.showinfo("Success", f"Username: {username}\nPassword: {password}") 
    try:
        db = Database()
        db.connect()
        cursor = db.conn.cursor()
        sql = "INSERT INTO users (nom, password) VALUES (%s, %s)"
        values = (username, password)
        db.cursor.execute(sql, values)
        db.conn.commit()
        messagebox.showinfo("succes","User inserted successfully!")
        return True
    except Exception as error:
        print(f"Error inserting user: {error}")


def update_product(nom, price, stock, date_entry):
    try:
        db = Database()
        db.connect()
        cursor = db.conn.cursor()
        sql = "UPDATE products SET price=%s, stock=%s, date_dentrer=%s WHERE nom=%s"
        values = (price, stock, date_entry, nom)
        db.cursor.execute(sql, values)
        db.conn.commit()
        messagebox.showinfo("Success", "Product updated successfully!")
        return True
    except Exception as error:
        print(f"Error updating product: {error}")