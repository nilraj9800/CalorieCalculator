from tkinter import *
from tkinter import messagebox, ttk
import login_backend
import sqlite3


class login:
    # creating login page along with the register page.
    def __init__(self, window):
        self.window = window
        self.frame = Frame(self.window, bg='Gray89', width=1000, height=600)  # creating frame

    def loginfn(self):
        # login window design codes
        self.label = Label(self.frame, text='Welcome to LOGIN', bg='Gray89', font=('Georgia', 28, 'bold'))

        self.name = Label(self.frame, text='UserName: ', bg='Gray89', font=('Arial', 16, 'bold'))

        self.namee_text = StringVar()
        self.namee = Entry(self.frame, textvariable=self.namee_text, fg='black', width=25, font=('Arial', 16))

        self.password1 = Label(self.frame, text=' Password : ', bg='Gray89', fg='black', font=('Arial', 16, 'bold'))

        self.password1e_text = StringVar()
        self.password1e = Entry(self.frame, textvariable=self.password1e_text, bg='White', fg='black', width=25,
                                font=('Arial', 16), show='*')

        self.buttonlogin = Button(self.frame, text='LOG IN', bg='Orange', fg='gray12', font=('Georgia', 18),
                                  cursor='hand2', command=self.login_user)
        self.buttonr = Button(self.frame, text='Register', bg='Orange', fg='gray12', font=('Georgia', 18),
                              cursor='hand2', command=self.register)
        self.label.place(x=40, y=40, width=370, height=30)

        self.name.place(x=100, y=140, width=240, height=60)

        self.namee.place(x=320, y=150, width=200, height=30)

        self.password1.place(x=85, y=220, width=240, height=30)

        self.password1e.place(x=320, y=215, width=200, height=30)

        self.buttonlogin.place(x=180, y=300, width=140, height=50)

        self.buttonr.place(x=350, y=300, width=140, height=50)

        self.frame.pack()

    def register(self):
        # Registration page designing part
        self.label.destroy()
        self.name.destroy()
        self.namee.destroy()
        self.password1.destroy()
        self.password1e.destroy()
        self.buttonlogin.destroy()
        self.buttonr.destroy()
        self.labelr = Label(self.frame, text='Register', bg='Gray89', font=('Georgia', 32, 'bold'))
        self.namer = Label(self.frame, text='Name : ', bg='Gray89', font=('Arial', 14, 'bold'))
        self.namere_text = StringVar()
        self.namere = Entry(self.frame, textvariable=self.namere_text, fg='black')
        self.passwordr1 = Label(self.frame, text='Create Password : ', bg='Gray89', fg='black',
                                font=('Georgia', 14, 'bold'))
        self.passwordr1e_text = StringVar()
        self.passwordr1e = Entry(self.frame, textvariable=self.passwordr1e_text, bg='White', fg='black', width=25,
                                 font=('Georgia', 12, 'bold'), show='*')
        self.passwordr2 = Label(self.frame, text='Confirm Password: ', bg='Gray89', fg='black',
                                font=('Georgia', 14, 'bold'))
        self.passwordr2e_text = StringVar()
        self.passwordr2e = Entry(self.frame, textvariable=self.passwordr2e_text, bg='White', fg='black', width=25,
                                 font=('Georgia', 12, 'bold'), show='*')
        self.buttonr = Button(self.frame, text='Register', bg='Turquoise1', fg='gray12', font=('Georgia', 14, 'bold'),
                              cursor='hand2', command=self.create)
        self.buttonr2 = Button(self.frame, text='Back', bg='Turquoise1', fg='gray12', font=('Georgia', 14, 'bold'),
                               cursor='hand2', command=self.destroy)

        # placing of the label ana textbox in the frame
        self.labelr.place(x=40, y=10, width=200, height=80)
        self.namer.place(x=80, y=100, width=240, height=60)
        self.namere.place(x=300, y=115, width=200, height=30)
        self.passwordr1.place(x=28, y=180, width=240, height=30)
        self.passwordr1e.place(x=300, y=180, width=200, height=30)
        self.passwordr2.place(x=23, y=233, width=240, height=30)
        self.passwordr2e.place(x=300, y=233, width=200, height=30)
        self.buttonr.place(x=160, y=330, width=140, height=50)
        self.buttonr2.place(x=320, y=330, width=140, height=50)

    def create(self):
        # validation codes for the Registration
        if len(self.namere.get()) == 0:
            messagebox.showinfo('error', 'Name field is empty')
        elif len(self.passwordr1e.get()) == 0:
            messagebox.showinfo('error', 'PASSWORD field is empty')
        elif len(self.passwordr2e.get()) == 0:
            messagebox.showinfo('error', 'Confirm PASSWORD field is empty')
        elif len(self.namere.get()) < 5:
            messagebox.showinfo('Error','Name should be greater than five character')
        elif len( self.passwordr1e.get()) < 5:
            messagebox.showinfo("Error",'Password should be greater than five character')
        elif self.passwordr1e.get() != self.passwordr2e.get():
            messagebox.showinfo('error', 'Passwords do not match')

        else:
            # inserting the data into the database
            login_backend.insert(self.namere_text.get(), self.passwordr1e_text.get())
            # reseting the textbox after successfully registration
            self.namere_text.set("")
            self.passwordr1e_text.set("")
            self.passwordr2e_text.set("")

    def login_user(self):
        # Validation points for checking if the textbox are empty
        # if needed name and password can be checked individually
        if len(self.namee.get()) == 0 or len(self.password1e.get()) == 0:
            messagebox.showinfo("ERROR", "Fields are empty")
        else:
            # checking whether the user name exists or not
            data.checks(self.namee_text.get(), self.password1e_text.get())

    def destroy(self):
        self.labelr.destroy()
        self.namer.destroy()
        self.namere.destroy()
        self.passwordr1.destroy()
        self.passwordr1e.destroy()
        self.passwordr2.destroy()
        self.passwordr2e.destroy()
        self.buttonr.destroy()
        self.buttonr2.destroy()
        self.buttonlogin.destroy()

        self.loginfn()  # calling the loginfn function


class data:
    def checks(name, password):
        conn = sqlite3.connect('login.db')
        cur = conn.cursor()
        if cur.execute('SELECT * FROM user WHERE name = ? AND password = ?', (name, password)):
            if cur.fetchone():
                window.destroy()
                login_backend.back()
            else:
                messagebox.showinfo('error', 'Username and password is wrong')


# creating the window
window = Tk()
window.title('Login')
window.geometry('700x400')
# creating object to login class
obj = login(window)
obj.loginfn()
window.mainloop()
