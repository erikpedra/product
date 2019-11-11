from tkinter import *

class IncomeWindow:

    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=600, height=500, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)


        width  = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 500 / 2)
        stri = "600x500+"+ str(x) + "+" + str(y)
        self.root.geometry(stri)
        self.root.resizable(width=False, height=False)

        self.root.title("Apple Email Checker")

    def add_frame(self):
        self.frame = Frame(self.root, height=350, width=450)
        self.frame.place(x=80, y=20)

        x, y =70, 20
        self.label = Label(self.frame, text="Apple Email Checker")
        self.label.config(font=(" Courier", 20, 'bold'))
        self.label.place(x = x + 30, y = y + 50)
        
        self.income = Label(self.frame, text="Enter Source")
        self.income.config(font=(" Courier", 20, 'bold'))
        self.income.place(x = x + 50, y = y + 100)

        self.inc = Entry(self.frame, font='Courier 12')
        self.inc.place(x=200, y= y + 100)
        self.root.mainloop()