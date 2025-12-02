from tkinter import*
import tkinter.messagebox


class Libary:

    def __init_(self,root):
        self.root = root
        self.root.title("Libary Database Mnagement System")
        self.root.geometry("1350x750+0+0")


        MTy = StringVar()
        Ref = StringVar()
        Tit = StringVar()
        fna = StringVar()
        sna= StringVar()
        Adr1= StringVar()
        Adr2 = StringVar()
        pcd = StringVar()
        MNo= StringVar()
        BkID = StringVar()
        BkT = StringVar()
        Bkt = StringVar()
        Atr = StringVar()
        DBo = StringVar()
        Ddu = StringVar()
        sPr = StringVar()
        LrF = StringVar()
        DoD = StringVar()
        DonL = StringVar()

        ############################################################################################################################################
        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2,padx=40, pady=8, bg="Cadet blue", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial', 46, 'bold'), text="Libary Database Mnagement System")
        self.lblTit.grid(sticky=W)

        ButtonFrame =Frame(MainFrame, bd=2, width=1350, height=100, padx=2,pady=20, bg="Cadet Blue", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail =Frame(MainFrame, bd=0, width=1350, height=50, padx=20,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame =Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT =LabelFrame(DataFrame, bd=1, width=800, height=300, padx=20, relief=RIDGE
                            ,  font=('arial', 12,'bold'), text="Libary Membership Info:",bg="Cadet Blue")
        DataFrameLEFT.pack(side=LEFT)


        DataFrameRIGHT =LabelFrame(DataFrame, bd=1, width=450, height=300, padx=20,pady=3, relief=RIDGE
                                   , font=('arial', 12,'bold'),bg="Cadet Blue", text="Book Details:",)
        DataFrameRIGHT.pack(side=RIGHT)



        

        


        
        




