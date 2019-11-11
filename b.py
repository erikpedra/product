from tkinter import *
import login

class WelcomeWindow:

    def __init__(self):
        self.root = Tk()

        self.canvas = Canvas(self.root, width=600, height=400, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)


        width  = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)
        stri = "600x400+"+ str(x) + "+" + str(y)
        self.root.geometry(stri)

        self.root.resizable(width=False, height=False)

        self.root.title("GX40 Product Sell")

    def add_frame(self):
        self.frame = Frame(self.root, height=300, width=450)
        self.frame.place(x=80, y=50)

        x, y =70, 20

        
        self.labeltitle = Label(self.frame, text=" Welcome to GX40 Product")
        self.labeltitle.config(font=("Courier", 20, 'bold'))
        self.labeltitle.place(x=10, y=y+110)

        self.button = Button(self.frame, text="Continue", font=('helvetica', 20, 'underline italic'), bg='dark red', fg='white', command=self.login)
        self.button.place(x=x+80, y=y+150)


        self.root.mainloop()

    def login(self):
        self.root.destroy()
        log = login.LoginWindow()
        log.add_frame()


if __name__ == "__main__":
    x = WelcomeWindow()
    x.add_frame()