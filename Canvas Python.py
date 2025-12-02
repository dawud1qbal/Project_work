from tkinter import*
import tkinter.messagebox
from tkinter import ttk, colorchooser

class writer:

    def __init__(self,root):
        self.root = root
        self.root.geometry("1360x800+0+0")
        space = " "
        self.root.title(190 * space + "Display various Images on Canvas in Python")
        self.root.iconbitmap('Capt.ico')

        self.myCanvas = Canvas(self.root, bg='#ABCDEF')
        self.myCanvas.pack(fill = BOTH, expand = True)




if __name__=='__main__':
    root = Tk()
    root.option_add('*font',('verdana', 10, 'bold'))
    application = writer(root)
    root.mainloop()
