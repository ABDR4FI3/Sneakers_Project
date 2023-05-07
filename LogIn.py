from tkinter import  *
from tkinter import  messagebox
import customtkinter
from PIL import ImageTk, Image
import SignIn as S
import Code as C
from ProductsCopy  import create_Products 



#function part

app = customtkinter.CTkToplevel() #creating tkinter window
app.geometry("1500x470") #window dimension
app.title('Login') #window title 
def CreateLogin():
    #codes:




    #_________________________________________________________________

  


    LoginBg = ImageTk.PhotoImage(Image.open('login.png')) #open the image 
    L1 = customtkinter.CTkLabel(master=app, image=LoginBg,text="") #append img as Label
    L1.pack()

    frame = customtkinter.CTkFrame(master=L1, width=400, height=365 , corner_radius=30)
    frame.place(relx=0.9, rely=0.5, anchor=E) # updated relx value and anchor


    l2=customtkinter.CTkLabel(master=frame , text= "Login into Your  Accout" , font= ('Lato',20))
    l2.place(x=50,y=25)

    user=customtkinter.CTkEntry(master=frame ,width=280  , placeholder_text="Username")
    user.place(x=50,y=105)


    password=customtkinter.CTkEntry(master=frame ,width=280  , placeholder_text="Password")
    password.place(x=50,y=175)




    btn1=Button(master=frame,width=30, text='Login ',  fg="#931A25", font="bold",command=lambda : Login(user, password))
    btn1.place(relx=0.14 , rely=0.7 )
    signup=Button(master=frame , text= "Create account" , font= ('Lato',14),command=click_signup,background="black" ,fg="white")
    signup.place(x=265,y=265)
    app.mainloop()
    #--------------------------------------------------------------------
    #data base connection

    #----------------------------------------------------------------------
    return 0

def Login(entry_widget1 ,entry_widget2 ):

    User = entry_widget1.get()
    password= entry_widget2.get()
    #messagebox.showinfo("Success", f"Username: {User}\nPassword: {password}") 
    x=C.Entry_check(User,password)
    if x is True :
        app.destroy()
        create_Products()
    #code log in
    #Entry_check()
    

def click_signup():
    app.destroy()
    S.creat_account()
