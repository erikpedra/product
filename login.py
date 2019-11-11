from tkinter import *
from tkinter import messagebox
import db.db
import dashboard

class LoginWindow:
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

        self.root.title("Welcome | Login ")


    def add_frame(self):
        self.frame = Frame(self.root, height=400, width=450)
        self.frame.place(x=80, y=50)

        x, y = 70, 20

        self.img = PhotoImage(file='images/logins.png')
        self.label = Label(self.frame, image=self.img)
        self.label.place(x= x + 10, y = y + 0)

        self.label = Label(self.frame, text="User Login")
        self.label.config(font=("Courier", 20, 'bold'))
        self.label.place(x=110, y = y + 190)

        self.embel = Label(self.frame, text="Username")
        self.embel.config(font=("Courier", 12, 'bold'))
        self.embel.place(x=50, y= y + 230)

        self.username = Entry(self.frame, font="Courier 12")
        self.username.place(x=200, y= y + 230)

        self.pslabel = Label(self.frame, text="Password")
        self.pslabel.config(font=("Courier", 12, 'bold'))
        self.pslabel.place(x=50, y= y + 260)

        self.password = Entry(self.frame, font="Courier 12")
        self.password.place(x=200, y= y + 260)

        self.button = Button(self.frame, text="Login", font='Courier 15 bold', command=self.login)
        self.button.place(x=170, y=y+290)

        self.root.mainloop()

    def login(self):
        #Letek Data
        data = (
            self.username.get(),
            self.password.get()
        )
        #
        if self.username.get() =="":
            messagebox.showinfo("Waspada!", "Masuk Username Pertama")
        elif self.username.get() == "":
            messagebox.showinfo('Waspada!', "Masuk Password Pertama")
        else:
            res = db.db.user_login(data)
            if res:
                messagebox.showinfo("Succes", "Login Berhasil")
                self.root.destroy()
                x = dashboard.DashBoardWindow()
                x.add_menu()
                x.add_frame()
            else:
                messagebox.showinfo("Failed", "Username dan Password anda salah")