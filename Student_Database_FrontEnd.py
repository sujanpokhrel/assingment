from tkinter import *
import tkinter.messagebox
# import stdDatabase

class Student:
    def __init__(self,window):
        self.window= window
        self.window.title("student managment")
        self.window.geometry("1551x700+30+50")
        self.window.config(bg="cadet blue")
        #
        # photo = PhotoImage(file="world.png")
        #
        # w = Label(window, image=photo)
        # w.place(x=0, y=0, relwidth=1, relheight=1)
        # w.photo = photo
        # w.pack()

        StdID = StringVar()
        Firstname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        #####################Frame#####################-----------------------------------
        self.MainFrame = Frame(self.window, bg="cadet blue")
        self.MainFrame.grid()

        self.TitFrame = Frame(self.window, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        self.TitFrame.grid(side=TOP)


        self.lblTit = Label(TitFrame, font=("arial", 47, "bold"), text="Student Database Management System", bg="Ghost White")
        self.lblTit.pack()

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=2, width=1300, height=400, padx=20, pady=10, bg="Ghost White", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, bd=2, width=1000, height=600, padx=20, relief=RIDGE, font=("arial", 47, "bold"), text="Student Info\n")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, bg="Ghost White", relief=RIDGE, font=("arial", 47, "bold"), text="Student Detail\n")
        DataFrameRIGHT.pack(side=RIGHT)


################################labeles and entry widget------------------------

        self.lblStdID = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Stundet ID:", padx=2, pady=2, bg="Ghost White")
        self.lblStdID.grid(row=0, column=0, sticky=W)
        self.txtStdID = Entry(DataFrameLeft, font=("arial", 10, "bold"), textvariable=StdID, width=39)
        self.txtStdID.grid(row=0, column=1)

        self.lblfna = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Firstname :", padx=2, pady=2,bg="Ghost White")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtlfna = Entry(DataFrameLeft, font=("arial", 10, "bold"), textvariable=StdID, width=39)
        self.txtlfna.grid(row=1, column=1)

        self.lblSna = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Surname:", padx=2, pady=2,bg="Ghost White")
        self.lblSna.grid(row=2, column=0, sticky=W)
        self.txtSna = Entry(DataFrameLeft, font=("arial", 10, "bold"), textvariable=StdID, width=39)
        self.txtSna.grid(row=2, column=1)

        self.lblDoB = Label(DataFrameLeft, font=("arial", 10, "bold"), text="DOB:", padx=2, pady=2,bg="Ghost White")
        self.lblDoB.grid(row=3, column=0, sticky=W)
        self.txtDoB = Entry(DataFrameLeft, font=("arial", 10, "bold"), textvariable=DoB, width=39)
        self.txtDoB.grid(row=3, column=1)

        self.lblAge = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Age:", padx=2, pady=2, bg="Ghost White")
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLeft, font=("arial", 10, "bold"), textvariable=Age, width=39)
        self.txtAge.grid(row=4, column=1)

        self.lblGender = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Gender:", padx=2, pady=2, bg="Ghost White")
        self.lblGender.grid(row=5, column=0, sticky=W)
        self.txtGender = Entry(DataFrameLeft, font=("arial", 10, "bold"), textvariable=Gender, width=39)
        self.txtGender.grid(row=5, column=1)

        self.lblAdr = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Address:", padx=2, pady=2, bg="Ghost White")
        self.lblAdr.grid(row=6, column=0, sticky=W)
        self.txtAdr = Entry(DataFrameLeft, font=("arial", 10, "bold"), textvariable=Address, width=39)
        self.txtAdr.grid(row=6, column=1)

        self.lblMobile = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Mobile:", padx=2, pady=2, bg="Ghost White")
        self.lblMobile.grid(row=7, column=0, sticky=W)
        self.txtMobile = Entry(DataFrameLeft, font=("arial", 10, "bold"), textvariable=Mobile, width=39)
        self.txtMobile.grid(row=7, column=1)


        ##############listbox and ScrollBox Widget##############################################
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=5, column=1, sticky="ns")

        studentlist = Listbox(DataFrameRIGHT, width=41, height=16, font=("arial", 12, "bold"),  yscrollcommand=scrollbar.set)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command= studentlist.yview)



############################################button and widgets#########################################

        self.btnAddData = Button(ButtonFrame, text ="Add New", font=("arial", 10, "bold"), height=1, width=10, bd=4)
        self.btnAddData.grid(row=0, column=0)
        self.btnAddData = Button(ButtonFrame, text="Add New", font=("arial", 10, "bold"), height=1, width=10, bd=4)
        self.btnAddData.grid(row=0, column=1)
        self.btnAddData = Button(ButtonFrame, text="Add New", font=("arial", 10, "bold"), height=1, width=10, bd=4)
        self.btnAddData.grid(row=0, column=2)
        self.btnAddData = Button(ButtonFrame, text="Add New", font=("arial", 10, "bold"), height=1, width=10, bd=4)
        self.btnAddData.grid(row=0, column=3)
        self.btnAddData = Button(ButtonFrame, text="Add New", font=("arial", 10, "bold"), height=1, width=10, bd=4)
        self.btnAddData.grid(row=0, column=4)
        self.btnAddData = Button(ButtonFrame, text="Add New", font=("arial", 10, "bold"), height=1, width=10, bd=4)
        self.btnAddData.grid(row=0, column=5)











if __name__=='__main__':
    window =Tk()
    application = Student(window)
    window.mainloop()







