from tkinter import *
from tkinter import ttk, messagebox


class user:
    def __init__(self, window):
        self.window = window
        self.frame = Frame(self.window, bg='Gray89', width=700, height=500)
        self.option = StringVar()
        self.dblcalorie = float()
        self.activity_level = float()
        self.age = Label(self.frame, text='AGE :', fg='black', font=('Georgia', 14, 'bold'))
        self.age_text = StringVar()
        self.agee = Entry(self.frame, textvariable=self.age_text, fg='black', width=250)
        self.notice = Label(self.frame, text='* Between 10 to 80 years old', fg='RED', font=('Georgia', 12))
        self.height = Label(self.frame, text='Height :', fg='black', font=('Georgia', 14, 'bold'))
        self.height_text = StringVar()
        self.height1 = Entry(self.frame, textvariable=self.height_text, fg='black', width=250)
        self.notice1 = Label(self.frame, text='cm *(2 to 1000 cm) :', fg='RED', font=('Georgia', 12))
        self.weight = Label(self.frame, text='Weight :', fg='black', font=('Georgia', 14, 'bold'))
        self.weight_text = StringVar()
        self.weight1 = Entry(self.frame, textvariable=self.weight_text, fg='black', width=250)
        self.notice2 = Label(self.frame, text='*kg (20 to 200 kg) :', fg='RED', font=('Georgia', 12))
        # Setting the radio button to option 'men' in order not to write validation code later
        self.option.set("men")
        self.radio = Label(self.frame, text='Gender', width=25, font=('Georgia', 14, 'bold'))
        self.male = Radiobutton(self.frame, text='Male', variable=self.option, value="men")
        self.female = Radiobutton(self.frame, text='female', variable=self.option, value="women")
        self.activity = Label(self.frame, text="Activity:", fg='black', font=('Georgia', 14, 'bold'))
        self.combo = ttk.Combobox(self.frame, values=["light", "normal", "heavy", "extreme"])
        self.result = Label (self.frame,text = 'Calories/day',fg= 'black',font=('Georgia', 12))
        self.gainl = Label(self.frame, text='Calorie:', fg='black', font=('Georgia', 14, 'bold'))
        self.gain = Text(self.frame, width=250, font=('Arial', 14))

        self.buttoncal = Button(self.frame, text='Calculate', bg='Royal blue', fg='gray12', font=('Georgia', 14),
                                cursor='hand2', command=self.calculate)
        self.buttonreset = Button(self.frame, text='Reset', bg='Royal blue',fg='gray12', font=('Georgia', 14),command=self.reset)

        self.age.place(x=20, y=40, width=100, height=20)
        self.agee.place(x=150, y=40, width=180, height=30)
        self.notice.place(x=350, y=40, width=210, height=25)
        self.height.place(x=20, y=120, width=100, height=30)
        self.height1.place(x=150, y=120, width=180, height=30)
        self.notice1.place(x=350, y=120, width=280, height=25)
        self.weight.place(x=20, y=200, width=100, height=30)
        self.weight1.place(x=150, y=200, width=180, height=30)
        self.notice2.place(x=350, y=200, width=200, height=30)
        self.radio.place(x=20, y=260, width=100, height=20)
        self.male.place(x=150, y=260, width=100, height=20)
        self.female.place(x=340, y=260, width=100, height=20)
        self.activity.place(x=20, y=310, width=100, height=25)
        self.combo.place(x=150, y=310, width=100, height=20)
        self.gainl.place(x=20, y=360, width=100, height=30)
        self.gain.place(x=150, y=360, width=160, height=30)
        self.result.place(x=350,y=360,width=200,height=30)
        self.buttonreset.place(x=250, y=410, width=200, height=50)
        self.buttoncal.place(x=20, y=410, width=200, height=50)
        self.frame.pack()

    # Creating the function for the calculation of the calorie.
    def gender(self):
        # first all the validation are checked before the calculation takes places.
        if int(self.age_text.get()) < 10 or int(self.age_text.get()) > 80:
            messagebox.showinfo("Error", "Please check your age")
        elif int(self.height_text.get()) < 2 or int(self.height_text.get()) > 1000:
            messagebox.showinfo("Error", "Please check your height")
        elif int(self.weight_text.get()) < 20 or int(self.weight_text.get()) > 200:
            messagebox.showinfo("Error", "Please check your weight")
        else:
             if self.age_text.get().isnumeric() and self.weight_text.get().isnumeric() and self.height_text.get().isnumeric():
                 if self.option.get() == "men":
                     self.dblcalorie = (13.3 * int(self.weight_text.get())) + (4.7 * int(self.height_text.get())) - (5.6 * int(self.age_text.get())) + 88.3
                 else:
                    self.dblcalorie = (9.2 * int(self.weight_text.get())) + (3.0 * int(self.height_text.get())) - (4.3 * int(self.age_text.get())) + 447.5
             else:
                messagebox.showinfo("ERROR", "The fields must be numeric")

            # return self.dblcalorie

    def act(self):
        if len(self.combo.get()) == '0':
            messagebox.showinfo("ERROR", "please choose one activity level ")
        elif self.combo.get() == 'light':
            self.activity_level = 1.24 * self.dblcalorie
        elif self.combo.get() == 'normal':
            self.activity_level = 1.55 * self.dblcalorie
        elif self.combo.get() == 'heavy':
            self.activity_level = 1.725 * self.dblcalorie
        elif self.combo.get() == 'extreme':
            self.activity_level = 1.9 * self.dblcalorie
        # Giving the precision of 0.00 to the total
        self.activity_level = "{:.2f}".format(self.activity_level)
        #  return self.activity_level

    def calculate(self):
        # Python gives direct error when the fields are null so try and
        # except must be implemented in order to prevent the error
        try:
            self.gender()
            self.act()
            self.gain.delete(1.0, END)
            self.gain.insert(END, str(self.activity_level))

        except Exception:
            messagebox.showinfo(" Error", "The fields should not be empty.")
            return self

    def reset(self):
        self.age_text.set("")
        self.weight_text.set("")
        self.height_text.set("")
        self.combo.set("")
        self.gain.delete("1.0", END)


'''
window = Tk()
window.title('Calculator')
window.geometry('700x700')
obj = student(window)
window.mainloop()'''
