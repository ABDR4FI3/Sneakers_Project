import tkinter 
from tkinter import  *
from tkinter import  messagebox
import customtkinter
from PIL import ImageTk, Image
import Code as c
import ProductsCopy as cp


#function part

def creat_account():
    app = customtkinter.CTkToplevel() #creating tkinter window
    app.geometry("1500x470") #window dimension
    app.title('Login') #window title 


    LoginBg = ImageTk.PhotoImage(Image.open('LoginBg.png')) #open the image 
    L5 = customtkinter.CTkLabel(master=app, image=LoginBg,text="") #append img as Label
    L5.pack()

    frame_width = 400 # updated frame width
    frame = customtkinter.CTkFrame(master=L5, width=frame_width, height=365 , corner_radius=30)
    frame.place(relx=0.9, rely=0.5, anchor=tkinter.E) # updated relx value and anchor


    l2=customtkinter.CTkLabel(master=frame , text= "Creat Your Account" , font= ('Lato',20),corner_radius=30)
    l2.place(x=50,y=25)

    user=customtkinter.CTkEntry(master=frame ,width=280  , placeholder_text="Username")
    user.place(x=50,y=100)


    email=customtkinter.CTkEntry(master=frame ,width=280  , placeholder_text="email")
    email.place(x=50,y=160)

    passwd=customtkinter.CTkEntry(master=frame ,width=280  , placeholder_text="Password")
    passwd.place(x=50,y=220)




    btn1=customtkinter.CTkButton(master=frame,width=240, text='Singup ', corner_radius=6, fg_color="#931A25",command=lambda: Acuiring_Values(user,passwd,app))
    btn1.place(x=50 , y=300 )
    app.mainloop()



def Acuiring_Values(entry_widget,entry_widget2,app):
    User = entry_widget.get()
    password= entry_widget2.get()
    if(User!="" and password!=""):
        test=c.insert_user(User,password)
        if(test):
            app.destroy()
            cp.create_Products()

            
    else:
        messagebox.showwarning("Warning","feilds are required")






