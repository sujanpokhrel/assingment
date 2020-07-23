from tkinter import *

from tkinter import ttk
import pymysql
import tkinter
from tkinter import messagebox
import tempfile
import os
class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x790+0+0")
        self.root.resizable(0, 0)
        self.root.iconbitmap("skull.ico")
        # title = Label(self.root, text="S T U D E N T   M A N A G E M E N T   S Y S T E M",
        #               font=("Calibri(Body)", 20, "bold"), bg="#ffead7",
        #               fg="black")
        # title.pack(side=TOP)

        #########################--------------IMAGE----------
        photo = PhotoImage(file="whitedude.png")

        w = Label(root, image=photo)
        w.place(x=0, y=0, relwidth=1, relheight=1)
        w.photo = photo
        w.pack()
        #######################ALL variable#################
        self.Roll_No_var=StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.txt_add = StringVar()
        self.address_var = StringVar()
        self.search_by= StringVar()
        self.search_txt= StringVar()
        #self.search_by_name=StringVar()




        #################################forward button------------------------------------------------




    #################################menubar>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        menubar = Menu(root, bg="red")
        filemenu = Menu(menubar, tearoff=0)

        filemenu.add_command(label="New", activebackground="#c00e0e", command=self.clear)
        filemenu.add_command(label="Save", state=DISABLED)
        filemenu.add_separator()
        filemenu.add_command(label="Insert")
        submenu = Menu(filemenu)

        #######menuuuuuuuuuuuuuuuuuuuuu>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Copy", state=DISABLED)
        editmenu.add_command(label="Cut", state=DISABLED)
        editmenu.add_command(label="Paste", state=DISABLED)
        editmenu.add_command(label="Search", state=DISABLED)
        editmenu.add_command(label="Delete", activebackground="#c00e0e", command=self.delete_data)

        ################################helpmenu>>>>>>>>>>>>>>>>>>>
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About")
        #
        menubar.add_cascade(label="Files", menu=filemenu)
        menubar.add_cascade(label="Edit", menu=editmenu)
        menubar.add_cascade(label="Help", menu=helpmenu)
        #
        root.config(menu=menubar)
        ########################### Manage Frame---------------------------------------------
        Manage_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="#ffffff")
        Manage_Frame.place(x=20, y=100, width=470, height=580)


        m_title = Label(Manage_Frame, text="Manage Students", bg="WHITE", fg="BLACK",
                        font=("Californian FB", 15, "bold"))
        m_title.grid(row=0, columnspan=2, padx=20)

        lbl_roll = Label(Manage_Frame, text="R O O L L  N O .", bg="#ffffff", fg="black", font=("Californian FB", 15))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_roll = Entry(Manage_Frame, textvariable=self.Roll_No_var ,font=("Calibri(Body)", 15), bd=5, relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(Manage_Frame, text="N A M E ", bg="white", fg="black", font=("Californian FB", 15))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_Frame,textvariable=self.name_var,font=("Calibri(Body)", 15), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        ##################frame right----------------------------

        Detail_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Detail_Frame.place(x=500, y=100, width=800, height=580)
        #######################################################################

        lbl_email = Label(Manage_Frame, text="E - M A I L ", bg="white", fg="black", font=("Californian FB", 15))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_email = Entry(Manage_Frame, textvariable=self.email_var, font=("Calibri(Body)", 15), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_Frame, text="G E N D E R ", bg="white", fg="black", font=("Californian FB", 15, ))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        #############combobox----------------of---gender
        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var,  font=("Californian FB", 15), state="readonly")
        combo_gender['values'] = ("S E L E C T", "M A L E ", "F E M A L E ", "O T H E R ")
        combo_gender.grid(row=4, column=1, pady=20, padx=10, sticky="w")
        combo_gender.current(0)


        # txt_gend = Entry(Manage_Frame, font=("Calibri(Body)", 15, "bold"), bd=5, relief=GROOVE)
        # txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_contact = Label(Manage_Frame, text="C O N T A C T S ", bg="white", fg="black",
                            font=("Californian FB", 15))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("Californian FB", 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_DOB = Label(Manage_Frame, text="D O B", bg="white", fg="black",
                        font=("Californian FB", 15))
        lbl_DOB.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_DOB = Entry(Manage_Frame,textvariable=self.dob_var,  font=("Californian FB", 15), bd=5, relief=GROOVE)
        txt_DOB.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(Manage_Frame, text="A D D R E S S ", bg="white", fg="black",
                            font=("Californian FB", 15))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_address = Entry(Manage_Frame, textvariable=self.address_var , width=32, font=("Californian FB", 10),relief=GROOVE)
        txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")
        #########################BUTTONS----------------------
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="white", )
        btn_Frame.place(x=15, y=500, width=420, )

        Addbtn=Button(btn_Frame, command=self.add_students, text="Add", width=10,  activebackground="#0c141b", activeforeground="white", cursor="hand2").grid(row=0, column=0, padx=10, pady=10, )
        updatebtn=Button(btn_Frame, text="Update", width=10,command=self.update_data,activebackground="#182937", activeforeground="white", cursor="hand2").grid(row=0, column=1, padx=10, pady=10)
        deletebtn=Button(btn_Frame, text="Delete",command=self.delete_data, width=10, activebackground="#d0001d", activeforeground="white", cursor="hand2").grid(row=0, column=2, padx=10, pady=10)
        Clearbtn=Button(btn_Frame, text="Clear", width=10,command=self.clear, activebackground="#406c93", activeforeground="white", cursor="hand2").grid(row=0, column=3, padx=10, pady=10)


        ####################################################SERACH----------------

        lbl_search = Label(Detail_Frame, text="Search_By", bg="white", fg="black",
                           font=("Californian FB", 15, ))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")




        combo_searach = ttk.Combobox(Detail_Frame,textvariable=self.search_by, width=10, font=("Californian FB", 14, "bold"), state="readonly")
        combo_searach['values'] = ("Roll_no", "Name", "Contact")
        combo_searach.grid(row=0, column=1, pady=20, padx=10)
        combo_searach.current(0)

        txt_search=Entry(Detail_Frame, textvariable=self.search_txt, font=("Californian FB", 13, "bold"), width=15, bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn=Button(Detail_Frame, text="Search", width=10,command=self.search_data, activebackground="#0c141b", activeforeground="white", cursor="hand2").grid(row=0, column=3, padx=10, pady=10)
        exitbtn=Button(Detail_Frame,command=self.iExit ,text="Exit", width=10, activebackground="#0c141b", activeforeground="white", cursor="hand2").grid(row=0, column=5, padx=10, pady=10)
        printbtn =Button(Detail_Frame,  text="Print", width=10,
                            activebackground="#0c141b", activeforeground="white", cursor="hand2").grid(row=0, column=4,
                                                                                                       padx=10, pady=10)

        ##########################################_Table Frame---frame#################################

        Table_Frame = Frame(Detail_Frame, bd=2, relief=RIDGE, bg="#2b2b2b")
        Table_Frame.place(x=10, y=70, width=760, height=480)

        scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("roll", "name", "email", "gender", "contact", "dob", "Address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll", text="Roll No.")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("Address", text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=100)
        self.Student_table.column("name", width=120)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("Address", width=150)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error", "There are items that requires your attention!!")
        else:

            con=pymysql.connect(host="localhost", user="root",password="", database="stm")
            cur=con.cursor()
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
####>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>fetch>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()
 #########################################cleardata------------------
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.address_var.set("")
########################fetch data------------

##############update and fetchhhh--------------------

    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        print(row)
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.address_var.set(row[6])
        # self.txt_address.insert( row[7])
  ############################updatedata-----------------

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
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


    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("delete  from students where roll_no=%s", self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

####################searchby function--------------
    def search_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur=con.cursor()

################search is not working#######
        cur.execute("select * from students where " + str(self.search_by.get())+"=" +str(self.search_txt.get()))
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()

        ###############################################
########################################exit  function###############
    def iExit(self):
        iExit =tkinter.messagebox.askyesno("Student record system", "confirm if you want to exit?")
        if iExit >0:
            self.root.destroy()
            return


#############################################print function################################################

    # def iPrint():
    #     q = .get("1.0", "end-1c")
    #     filename = tempfile.mktemp(".txt")
    #     open (filename, "w"). write(q)
    #     os.startfile(filename, "print")






#
# wn=Tk()
# Student(wn)
# wn.mainloop()
#






