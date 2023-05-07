import tkinter 
import tkinter as tk
from tkinter import *
import customtkinter
from PIL import ImageTk, Image 
from Code import Show_Product
import Code as c
import ProductDetails as pd


def create_Products():
    #window attributes 
    app = tk.Toplevel() #creating tkinter window
    app.geometry("900x500") #window dimension
    app.title('Products') #window title 
    print("frame created")
    LoginBg = ImageTk.PhotoImage(Image.open('Group 11.png')) #open the image 
    L1 = customtkinter.CTkLabel(master=app, image=LoginBg,text="") #append img as Label
    L1.pack()
    #row 1
    #----------------------------------------------------------------------------
    #button 1,1
    Transparent = Image.open('BG Sneakers/Basket-PUMA-Shuffle-removebg-preview.png')
    Transparent =Transparent.resize((130,100))
    photoTransparent = ImageTk.PhotoImage(Transparent)
    button = Button(master=L1,image=photoTransparent,command=lambda: Show_Product(1,inp1,app))
    button.place(relx=0.35,rely=0.05)
    #----------------------------------------------------------------------------
    #button 1,2
    SN2 = Image.open('BG Sneakers/Baskets-basses-RBD-Game-removebg-preview.png')
    SN2 =SN2.resize((130,100))
    photoSN2 = ImageTk.PhotoImage(SN2)
    button = Button(master=L1,image=photoSN2 ,command=lambda: Show_Product(2,inp1,app))
    button.place(relx=0.56,rely=0.05)
    #----------------------------------------------------------------------------
    #button 1,3
    SN3 = Image.open('BG Sneakers/Chaussure_Gazelle_85_Vert_GY2532-removebg-preview.png')
    SN3 =SN3.resize((130,100))
    photoSN3 = ImageTk.PhotoImage(SN3)
    button = Button(master=L1,image=photoSN3,command=lambda: Show_Product(3,inp1,app))
    button.place(relx=0.783,rely=0.05)
    #----------------------------------------------------------------------------
    
    #row 2
    #----------------------------------------------------------------------------
    #button 2,1
    SN4 = Image.open('BG Sneakers/Chaussure_OZWEEGO_Bleu_HQ8863_04-removebg-preview.png')
    SN4 =SN4.resize((130,100))
    photoSN4 = ImageTk.PhotoImage(SN4)
    button = Button(master=L1,image=photoSN4,command=lambda: Show_Product(4,inp1,app))
    button.place(relx=0.35,rely=0.37)
    #----------------------------------------------------------------------------
    #button 2,2
    SN5 = Image.open('BG Sneakers/Chaussure_VS_Pace_2.0_3-Stripes_-removebg-preview.png')
    SN5 =SN5.resize((130,100))
    photoSN5 = ImageTk.PhotoImage(SN5)
    button = Button(master=L1,image=photoSN5,command=lambda: Show_Product(5,inp1,app))
    button.place(relx=0.56,rely=0.37)
    #----------------------------------------------------------------------------
    #button 2,3
    SN6 = Image.open('BG Sneakers/chaussure-air-max-90-pour-p2gZgN-removebg-preview.png')
    SN6 =SN6.resize((130,100))
    photoSN6 = ImageTk.PhotoImage(SN6)
    button = Button(master=L1,image=photoSN6,command=lambda: Show_Product(6,inp1,app))
    button.place(relx=0.783,rely=0.37)
    #----------------------------------------------------------------------------
    
    #row 3
    #----------------------------------------------------------------------------
    #----------------------------------------------------------------------------
    #button 3,1
    SN7 = Image.open('BG Sneakers/chaussure-dunk-low-pour-hQBFRp-removebg-preview.png')
    SN7 =SN7.resize((130,100))
    photoSN7 = ImageTk.PhotoImage(SN7)
    button = Button(master=L1,image=photoSN7,command=lambda: Show_Product(7,inp1,app))
    button.place(relx=0.35,rely=0.665)
    #----------------------------------------------------------------------------
    #button 2,2
    SN8 = Image.open('BG Sneakers/custom-nike-dunk-low-by-you-removebg-preview.png')
    SN8 =SN8.resize((130,100))
    photoSN8 = ImageTk.PhotoImage(SN8)
    button = Button(master=L1,image=photoSN8,command=lambda: Show_Product(8,inp1,app))
    button.place(relx=0.56,rely=0.665)
    #----------------------------------------------------------------------------
    #button 2,3
    SN9 = Image.open('BG Sneakers/Dame_Extply_2.0_Shoes_Green_ID18-removebg-preview.png')
    SN9 =SN9.resize((130,100))
    photoSN9 = ImageTk.PhotoImage(SN9)
    button = Button(master=L1,image=photoSN9,command=lambda: Show_Product(9,inp1,app))
    button.place(relx=0.783,rely=0.665)
    #----------------------------------------------------------------------------
    #creating and appending input 

    inp1=customtkinter.CTkEntry(master=L1 ,width=180  , placeholder_text="Enter Product name")
    inp1.insert(0, "This is the default text")
    inp1.place(relx=0.01,rely=0.2)
    #loop

    app.mainloop()
    return 0


