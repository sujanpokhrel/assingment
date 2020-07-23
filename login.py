from tkinter import *
from Registration12 import Register  ##############importing registraiton window
#import Student_Mangement_DETAILS
from tkinter import messagebox
from stundent_using_data import Student    ############import wanted to open window

from PIL import Image,ImageTk

# import Registration12

class Students:
    def __init__(self,window):
        self.window = window
        #self.regi = Student
        self.window.title("Student Database Management System")
        self.window.geometry("700x700+200+50")
        self.window.resizable(0,0)
        self.photo = PhotoImage(file="butterfly.png")

        self.window.iconbitmap("skull.ico")
        global w
        w = Label(self.window, image=self.photo)
        w.place(x=0, y=0, relwidth=1, relheight=1)
        w.photo = self.photo
        w.pack()

 ###########variables sauve user and password-------------------
        self.uname=StringVar()
        self.pass_=StringVar()

        #btn_log=Button(login_Frame,text="Login", width=15,font("arial", 14, "bold"), bg="yellow", fg="red").grid(row=3,column=1)

        self.entry_username=Entry(self.window, font=("Calibri(Body)", 18), fg="#4debe7", textvariable=self.uname)
        self.entry_username.place(x=230, y=340)

        self.entry_password = Entry(self.window, font=("Calibri(Body)", 18), fg="#4debe7", show="*", textvariable=self.pass_)
        self.entry_password.place(x=230, y=455)

        #############login##########
        #########################################################################################
        self.bttn_login = Button(self.window, text="L O G I N", font=("Azonix", 15), cursor="man" ,bg="#261a39", fg="#261a39",  activebackground="white", activeforeground="#261a39",
                                 command=self.bttn_login_clk)
        self.bttn_login.place(x=300, y=550)

###################################---registration--------------------


        self.bttn_regis = Button(self.window, text="R e g i s t r a t i o n",command=self.regis, font=("Azonix", 7), cursor="man", bg="#ff3510",
                                 fg="white", activebackground="white", activeforeground="#93c1cb")
        self.bttn_regis.place(x=570, y=30)





 ######login function-------------------

    def bttn_login_clk(self):
        if self.uname.get()=="" or self.pass_.get=="":
            messagebox.showerror("Error", "Please fill the Entry !!")

        elif self.uname.get()=="Administrator" and self.pass_.get()=="986043":
            messagebox.showinfo("Successfull", f"welcome {self.uname.get()}")
            self.new_window= Toplevel(self.window)   ##############
            Student(self.new_window)            ########calling another window class student
        else:
            messagebox.showerror("Error", "Your Detail are incorrect.Please try again")


    #######################################registration function##############
    def regis(self):
        self.window.withdraw()
        self.new_window = Toplevel(self.window)   ##############to open another window
        Register(self.new_window)   #################opens another page of resgistraiton



wn=Tk()
Students(wn)
wn.mainloop()


