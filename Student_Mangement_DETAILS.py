from tkinter import *
import tkinter as ttk





import pymysql
from PIL import Image,ImageTk
import http.client
from tkinter import ttk


from tkinter import messagebox

class Students:
    def __init__(self,window):
        self.window = window
        self.window.title("Student  Management Detail")
        self.window.geometry("1551x700+30+50")
        self.window.iconbitmap("skull.ico")
        self.window.resizable(0,0)
        #self.window.iconbitmap(r'C:\Users\Lenovo\Desktop\army.png')
        #self.window.config(bg="cadet blue")
        ######### Using image in background
        photo = PhotoImage(file="ericaa.png")

        w = Label(window, image=photo)
        w.place(x=0, y=0, relwidth=1, relheight=1)
        w.photo = photo
        w.pack()

        #######################ALL variable#################
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.txt_add = StringVar()
        # self.txt_address = StringVar()
        self.address_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

################text---------------------------------------
        self.roll = Label(self.window, text="R O O L L  N O ", bg="#eeeeee", fg="black", font=("Californian FB", 15))
        self.roll.place(x=10, y=100)

        self.name = Label(self.window, text="N A M E  ", bg="#eeeeee", fg="black", font=("Californian FB", 15))
        self.name.place(x=10, y=170)

        self.email = Label(self.window, text="E - M A I L ", bg="#eeeeee", fg="black", font=("Californian FB", 15))
        self.email.place(x=10, y=240)

        self.gender = Label(self.window, text="G E N D E R ", bg="#eeeeee", fg="black", font=("Californian FB", 15))
        self.gender.place(x=10, y=315)

        self.contact = Label(self.window, text="C O N T A C T ", bg="#eeeeee", fg="black", font=("Californian FB", 15))
        self.contact.place(x=10, y=390)

        self.dob = Label(self.window, text="D . O . B ", bg="#eeeeee", fg="black", font=("Californian FB", 15))
        self.dob.place(x=10, y=470)

        self.address = Label(self.window, text="A D D R E S S ", bg="#eeeeee", fg="black", font=("Californian FB", 15))
        self.address.place(x=10, y=550)
####################################################SERACH----------------


        self.search = Label(self.window, text="Search_by ", bg="#eeeeee", fg="black", font=("Californian FB", 15))
        self.search.place(x=500, y=60)

        self.entry_roll = Entry(self.window, font=("Calibri(Body)", 14), cursor="hand2", fg="black")
        self.entry_roll.place(x=900, y=60)

        self.combo_box_search = ttk.Combobox(self.window, font=("Calibri(Body 10"), cursor="hand2", state="readonly",
                                             justify=CENTER, textvariable=self.search)  # textvariable=self.room)
        self.combo_box_search.place(x=600, y=65, width=220)
        self.combo_box_search["values"] = ("Select", "Roll", "Name", "Contact")
        self.combo_box_search.current(0)

#################entrybox###############

        self.entry_roll = Entry(self.window,textvariable=self.Roll_No_var,  font=("Calibri(Body)", 15),cursor="hand2",  fg="black")
        self.entry_roll.place(x=200, y=105)

        self.entry_name = Entry(self.window,textvariable=self.name_var, font=("Calibri(Body)", 15), cursor="hand2", fg="black",)
        self.entry_name.place(x=200, y=175)

        self.entry_email = Entry(self.window,textvariable=self.email_var, font=("Calibri(Body)", 15), cursor="gobbler", fg="black", )
        self.entry_email.place(x=200, y=240)

        self.combo_box_gender = ttk.Combobox(self.window,textvariable=self.gender_var, font=("Calibri(Body 13"), cursor="hand2", state="readonly", justify=CENTER,)#textvariable=self.room)
        self.combo_box_gender.place(x=200, y=315, width=220)
        self.combo_box_gender["values"] = ("Select", "Male", "Female", "Rather Not to Say")
        self.combo_box_gender.current(0)

        self.entry_contact = Entry(self.window, textvariable=self.contact_var, font=("Calibri(Body)", 15),cursor="hand2",  fg="black")
        self.entry_contact.place(x=200, y=390)


        self.entry_dob = Entry(self.window,textvariable=self.dob_var, font=("Calibri(Body)", 15),cursor="hand2",  fg="black") #textvariable=self.repassword)
        self.entry_dob.place(x=200, y=470)

        self.entry_address = Entry(self.window, textvariable=self.address_var , font=("Calibri(Body)", 15), cursor="hand2", fg="black"
                              )  # textvariable=self.repassword)
        self.entry_address.place(x=200, y=520, height=50)

        ###########checkbox###########
        # -----------------termcheckbox-----------
        self.chk = Checkbutton(self.window, text="I Agree the Terms and Conditions",font=("Calibri(Body 8"), cursor="gobbler",  fg="#1d1227")
        self.chk.place(x=30, y=620)



        #__________________________frameright---------------
        self.frame = Frame(self.window, bd=2, relief=RIDGE, bg="white")
        self.frame.place(x=467, y=92, width=1000, height=600)


    ######################################button for upright-------------------------------
        self.bttn_search = Button(self.window, text="S E A R C H ", font=("ADAM.CG PRO", 11), cursor="hand2", fg="#f7da51",
                               bg="#261a39",
                               activebackground="#f7da51", activeforeground="white")
        self.bttn_search.place(x=1150, y=60)

        self.bttn_showall = Button(self.window, text="S H O W  A L L", font=("ADAM.CG PRO", 11), cursor="hand2", fg="#f7da51",
                                  bg="#261a39",
                                  activebackground="#f7da51", activeforeground="white")
        self.bttn_showall.place(x=1300, y=60)






        ##################box################

        self.bttn_add = Button(self.window, text="A D D",  font=("ADAM.CG PRO", 11), cursor="hand2", fg="#f7da51", bg="#261a39",
                                  activebackground="#f7da51", activeforeground="white", command=self.add_students)
        self.bttn_add.place(x=30, y=650)

        self.bttn_update = Button(self.window, text="U P D A T E", font=("ADAM.CG PRO", 11), cursor="hand2",fg="#f7da51", bg="#261a39",
                                  activebackground="#f7da51", activeforeground="white", command=self.update_data)
        self.bttn_update.place(x=110, y=650)

        self.bttn_delete = Button(self.window, text="D E L E T E", font=("ADAM.CG PRO", 11),cursor="hand2",  fg="#f7da51", bg="#261a39",
                                  activebackground="#f7da51", activeforeground="white", command=self.delete_data)
        self.bttn_delete.place(x=230, y=650,)

        self.bttn_clear = Button(self.window, text="C L E A R ", font=("ADAM.CG PRO", 11), cursor="hand2",  fg="#f7da51", bg="#261a39",
                                  activebackground="#d0001d", activeforeground="White", command=self.clear)
        self.bttn_clear.place(x=350, y=650)

######----menues---------------

        menubar = Menu(window, bg="red")
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
        editmenu.add_command(label="Delete", activebackground="#c00e0e", command=self.delete_data)


        ################################helpmenu>>>>>>>>>>>>>>>>>>>
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About")

        menubar.add_cascade(label="Files", menu=filemenu)
        menubar.add_cascade(label="Edit", menu=editmenu)
        menubar.add_cascade(label="Help", menu=helpmenu)

        window.config(menu=menubar)

        ######---------treeview----------------------------------------
        self.frame = Frame(self.frame, bd=2, relief=RIDGE, bg="#2b2b2b")
        self.frame.place(x=0, y=0, width=1000, height=480)

        scroll_x = Scrollbar(self.frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.frame, orient=VERTICAL)
        self.Students_table = ttk.Treeview(self.frame,columns=("roll", "name", "email", "gender", "contact", "dob", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Students_table.xview)
        scroll_y.config(command=self.Students_table.yview)
        self.Students_table.heading("roll", text="Roll No.")
        self.Students_table.heading("name", text="Name")
        self.Students_table.heading("email", text="Email")
        self.Students_table.heading("gender", text="Gender")
        self.Students_table.heading("contact", text="Contact")
        self.Students_table.heading("dob", text="D.O.B")
        self.Students_table.heading("Address", text="Address")
        self.Students_table['show'] = 'headings'
        self.Students_table.column("roll", width=100)
        self.Students_table.column("name", width=120)
        self.Students_table.column("email", width=100)
        self.Students_table.column("gender", width=100)
        self.Students_table.column("contact", width=100)
        self.Students_table.column("dob", width=100)
        self.Students_table.column("Address", width=150)
        self.Students_table.pack(fill=BOTH, expand=1)
        self.Students_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if self.Roll_No_var.get() == "" or self.name_var.get() == "":
            messagebox.showerror("Error", "There are items that requires your attention!!")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="paper")
            cur = con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)", (self.Roll_No_var.get(),
                                                                              self.name_var.get(),
                                                                              self.email_var.get(),
                                                                              self.gender_var.get(),
                                                                              self.contact_var.get(),
                                                                              self.dob_var.get(),
                                                                              self.address_var.get()
                                                                              ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo(("Success", "Record has been added"))



#####################################################fetch-allll-----------------------------------------

    def fetch_data(self):

        con = pymysql.connect(host="localhost", user="root", password="", database="paper")
        cur = con.cursor()
        cur.execute("select * from Students")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Students_table.delete(*self.Students_table.get_children())
            for row in rows:
                    self.Students_table.insert('', END, values=row)
            con.commit()
        con.close()


##################################clear
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.address_var.set("")


##############update and fetchhhh--------------------
    def get_cursor(self, ev):
        cursor_row = self.Students_table.focus()
        contents = self.Students_table.item(cursor_row)
        row = contents['values']
        print(row)
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.address_var.set(row[6])
############################updatedata-----------------
    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="paper")
        cur = con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s", (
                                                                                                self.name_var.get(),
                                                                                                self.email_var.get(),
                                                                                                self.gender_var.get(),
                                                                                                self.contact_var.get(),
                                                                                                self.dob_var.get(),
                                                                                                self.address_var.get(),
                                                                                                self.Roll_No_var.get()
                                                                                                ))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
###############################delete data---------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="paper")
        cur = con.cursor()
        cur.execute("delete  from students where roll_no=%s", self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()


####################searchby function--------------
    def search_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="paper")
        cur=con.cursor()

################search is not working#######
        cur.execute("select * from students where "+ str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Students_table.delete(*self.Students_table.get_children())
            for row in rows:
                    self.Students_table.insert('', END, values=row)
            con.commit()
        con.close()



wn=Tk()
Students(wn)
wn.mainloop()
