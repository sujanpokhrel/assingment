from tkinter import*
from tkinter import ttk, messagebox   ##########combo box

from PIL import Image, ImageTk
import pymysql
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registraiton Window")
        self.root.geometry("1350x700+0+0")
        self.root.iconbitmap("skull.ico")
        self.root.resizable(0, 0)

        photo = PhotoImage(file="glass.png")

        w = Label(root, image=photo)
        w.place(x=0, y=0, relwidth=1, relheight=1)
        w.photo = photo
        w.pack()

###############>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.name_var = StringVar()
        self.contact_var = StringVar()
        self.email_var = StringVar()
        self.pass_var = StringVar()
        self.conpass_var = StringVar()
        self.cmb_gender_var =StringVar()







########################left image..........
        self.left=ImageTk.PhotoImage(file="leftis.png")
        left=Label(self.root, image=self.left).place(x=75, y=100)


############REGISTERframe>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        frame1=Frame(self.root, bg="#f0f0f0")
        frame1.place(x=480, y=100 ,width=700, height=500)


#######################title......................
        title=Label(frame1,text="REGISTER HERE", font=("Work Sans", 20),bg="#f0f0f0", fg="black")
        title.place(x=50, y=30)

#############################text and label
        title = Label(frame1, text="N a m e ", font=("Work Sans", 15), bg="#f0f0f0", fg="black")
        title.place(x=50, y=100)

        self.txt_name=Entry(frame1, font=("Work Sans", 15),bg="#dedede", textvariable=self.name_var)
        self.txt_name.place(x=50, y=130)


        # title = Label(frame1, text="Last Name", font=("Work Sans", 15), bg="#f0f0f0", fg="black")
        # title.place(x=370, y=100)
        #
        # txt_lname = Entry(frame1, font=("Work Sans", 15), bg="#dedede")
        # txt_lname.place(x=370, y=130)


##################################################
        title = Label(frame1, text="Contact", font=("Work Sans", 15), bg="#f0f0f0", fg="black")
        title.place(x=370, y=100)

        self.txt_contact = Entry(frame1, font=("Work Sans", 15), bg="#dedede", textvariable=self.contact_var)
        self.txt_contact.place(x=370, y=130)

        title = Label(frame1, text="E-mail", font=("Work Sans", 15), bg="#f0f0f0", fg="black")
        title.place(x=50, y=200)

        self.txt_email = Entry(frame1, font=("Work Sans", 15), bg="#dedede", textvariable=self.email_var)
        self.txt_email.place(x=50, y=230)

#####################question.........................................................
        title = Label(frame1, text="Gender", font=("Work Sans", 15), bg="#f0f0f0", fg="black")
        title.place(x=50, y=300)

        self.cmb_gender = ttk.Combobox(frame1, font=("Work Sans", 15),state="readonly", justify=CENTER)
        self.cmb_gender['values']=("SELECT", "Male", "Female", "Rather Not to say")
        self.cmb_gender.place(x=50, y=330, width=250 )
        self.cmb_gender.current(0)

        title = Label(frame1, text="Password", font=("Work Sans", 15), bg="#f0f0f0", fg="black")
        title.place(x=370, y=200)

        self.txt_pass = Entry(frame1, font=("Work Sans", 15), bg="#dedede", show="*", textvariable=self.pass_var)
        self.txt_pass.place(x=370, y=230)

        title = Label(frame1, text="Confirm Password", font=("Work Sans", 15), bg="#f0f0f0", fg="black")
        title.place(x=370, y=300)

        self.txt_conpass = Entry(frame1, font=("Work Sans", 15), bg="#dedede", show="*", textvariable=self.conpass_var)
        self.txt_conpass.place(x=370, y=330)


##################terms.........................
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="#f0f0f0").place(x=50,y=380) #,bg="white", font=("Work Sans", 15))

        self.btn_img=ImageTk.PhotoImage(file="register.png")
        btn_register=Button(frame1,image=self.btn_img, bd=0, cursor="hand2",command=self.register_data).place(x=50,y=420)

#####################file menu>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        menubar = Menu(root, bg="red")
        filemenu = Menu(menubar, tearoff=0)

        filemenu.add_command(label="New", activebackground="#c00e0e", command=self.clear)
        filemenu.add_command(label="Save", state=DISABLED)
        filemenu.add_separator()
        filemenu.add_command(label="Insert")
        submenu = Menu(filemenu)

        #######edit>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Copy")
        editmenu.add_command(label="Cut")
        editmenu.add_command(label="Paste")
        #editmenu.add_command(label="Delete", activebackground="#c00e0e", command=self.delete_data)

        ################################helpmenu>>>>>>>>>>>>>>>>>>>
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About")

        menubar.add_cascade(label="Files", menu=filemenu)
        menubar.add_cascade(label="Edit", menu=editmenu)
        menubar.add_cascade(label="Help", menu=helpmenu)

        root.config(menu=menubar)

    ################################################
    def register_data(self):
        if self.txt_name.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_gender.get()=="Select" or self.pass_var.get()=="" or self.conpass_var.get()=="":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        elif self.pass_var.get()!=self.conpass_var.get():
            messagebox.showerror("Error", "Password do not Match", parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error", "Please Agree on Terms and Conditions", parent=self.root)
        else:
            messagebox.showinfo("Success", "Register Successful", parent=self.root)
            try:
                con=pymysql.connect(host="localhost", user="root", passwor="", database="stm")
                cur=con.cursor()
                cur.execute("insert into employee (name, contact, email, password,gender) values(%s,%s,%s,%s,%s,%s,%s)",
                            (self.txt_name.get(),
                             self.txt_contact.get(),
                             self.txt_email.get(),
                             self.pass_var.get(),
                             self.conpass_var.get(),
                             self.cmb_gender_var.get()


                            ))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Register Successful", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)















##################clear all files>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def clear(self):
        self.name_var.set("")
        self.contact_var.set("")
        self.email_var.set("")
        self.pass_var.set("")
        self.conpass_var.set("")
        self.cmb_gender_var.set("")












































###################################leftimage.......................










#
# root=Tk()
# obj=Register(root)
# root.mainloop()