import sqlite3
from tkinter import *
from tkinter import messagebox
from user import user


def connect():
    # To connect to the database
    conn=sqlite3.connect("login.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE if NOT exists user(name_id integer primary key AUTOINCREMENT,name text unique not null,password text not null)")
    conn.commit()
    conn.close()


def insert(name,password):
    conn=sqlite3.connect('login.db')
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO user(name,password) VALUES(?,?)', (name, password))
        messagebox.showinfo('Register', 'Entry success')

        # to check whether the user previously exists or not
    except sqlite3.IntegrityError as e:
        if re.match(r'UNIQUE constraint failed', e.args[0]):
            messagebox.showinfo('Error', 'User already exist')
        else:
            raise e

    conn.commit()
    conn.close()


def back():
            window = Tk()
            window.title('Calculator')
            window.geometry('700x500')
            obj = user(window)
            window.mainloop()


connect()
