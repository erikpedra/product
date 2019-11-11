from tkinter import *
import product.add_income

class DashBoardWindow:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=600, height=500, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)


        width  = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        x = int(width / 2 - 1000 / 2)
        y = int(height / 2 - 500 / 2)
        stri = "1000x500+"+ str(x) + "+" + str(y)
        self.root.geometry(stri)

        self.root.resizable(width=False, height=False)

        self.root.title("Welcome | Dashboard ")

    def add_menu(self):
        self.mainmenu = Menu(self.root)
        self.root.config(menu=self.mainmenu)

        self.income = Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="Product", menu=self.income)

        #Menu Pertama
        self.income.add_command(label="Apple Email Checker", command=self.add_income)
        self.income.add_command(label="Office Email Checker")
        self.income.add_command(label="Sender XMailer")
        self.income.add_command(label="Sender GX40")

        #Menu Kedua
        self.expense = Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="Manage Token", menu=self.expense)

        self.expense.add_command(label="Add Token")
        self.expense.add_separator()
        self.expense.add_command(label="Quit")

    def add_frame(self):
        self.img = PhotoImage(file='images/store.png')
        self.label = Label(self.root, image=self.img)
        self.label.place(x=0, y =0)
        self.root.mainloop()
        
    def add_income(self):
        x = product.add_income.IncomeWindow()


if __name__ == "__main__":
    x = DashBoardWindow()
    x.add_menu()
    x.add_frame()