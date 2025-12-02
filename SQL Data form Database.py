from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import random
import time





class DataEntryForm:

    def __init__(self,root):
        self.root = root
        self.root.title = ("Data Entry Form")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background ="gainsboro")

        MainFrame = Frame(self.root, bd =10, width=1250, height =700 , relief=RIDGE)
        MainFrame.grid()



        TopFrame1 = Frame(MainFrame, bd =10, width=1250, height =200 , relief=RIDGE, bg= 'cadet blue')
        TopFrame1.grid(row=0, column=0)
        TopFrame2 = Frame(MainFrame, bd =10, width=1250, height =50 , relief=RIDGE, bg= 'cadet blue')
        TopFrame2.grid(row=1, column=0)
        TopFrame3 = Frame(MainFrame, bd =10, width=1250, height =300 , relief=RIDGE, bg= 'cadet blue')
        TopFrame3.grid(row=2, column=0)



        InnerTopFrame1 = Frame(TopFrame1, bd =10, width=1240, height =190 , relief=RIDGE)
        InnerTopFrame1.grid()
        InnerTopFrame2 = Frame(TopFrame2, bd =10, width=1240, height =48 , relief=RIDGE)
        InnerTopFrame2.grid()
        InnerTopFrame3 = Frame(TopFrame3, bd =10, width=1240, height =280 , relief=RIDGE)
        InnerTopFrame3.grid()



        ##########################=]============================================================================================================

        lblReference = Label(InnerTopFrame1, font =('arial',12,'bold'),text="Reference No", bd=10)
        lblReference.grid(row=0, column=0, sticky=W)
        txtReference = Entry(InnerTopFrame1, font =('arial',12,'bold'), bd=5, width=32, justify='left')
        txtReference.grid(row=0, column=1)

        lblFirstname = Label(InnerTopFrame1, font =('arial',12,'bold'),text="Firstname ", bd=10)
        lblFirstname .grid(row=1, column=0, sticky=W)
        txtFirstname = Entry(InnerTopFrame1, font =('arial',12,'bold'), bd=5, width=32, justify='left')
        txtFirstname .grid(row=1, column=1)

        lblSurname = Label(InnerTopFrame1, font =('arial',12,'bold'),text="Surname", bd=10)
        lblSurname.grid(row=2, column=0, sticky=W)
        txtSurname = Entry(InnerTopFrame1, font =('arial',12,'bold'), bd=5, width=32, justify='left')
        txtSurname.grid(row=2, column=1)


        lblReference = Label(InnerTopFrame1, font =('arial',12,'bold'),text="Reference No", bd=10)
        lblReference.grid(row=0, column=0, sticky=W)
        txtReference = Entry(InnerTopFrame1, font =('arial',12,'bold'), bd=5, width=32, justify='left')
        txtReference.grid(row=0, column=1)

        lblFirstname = Label(InnerTopFrame1, font =('arial',12,'bold'),text="Firstname ", bd=10)
        lblFirstname .grid(row=1, column=0, sticky=W)
        txtFirstname = Entry(InnerTopFrame1, font =('arial',12,'bold'), bd=5, width=32, justify='left')
        txtFirstname .grid(row=1, column=1)

        lblSurname = Label(InnerTopFrame1, font =('arial',12,'bold'),text="Surname", bd=10)
        lblSurname.grid(row=2, column=0, sticky=W)
        txtSurname = Entry(InnerTopFrame1, font =('arial',12,'bold'), bd=5, width=32, justify='left')
        txtSurname.grid(row=2, column=1)
        
        
        

        
        

        


if __name__=='__main__':
    root = Tk()
    application = DataEntryForm(root)
    root.mainloop()
