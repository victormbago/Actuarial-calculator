from tkinter import *
import time
import am92

into = Tk()  # creates window
into.geometry('900x800')  # size of window
into.title('ACTUARIAL INTERFACE')
text = Label(into, text='ACTUARIAL  ', fg='black', bg='light blue', relief='solid', font='bold')
text.pack(fill=BOTH, pady=2, padx=2, expand=True)
text.pack()
into.mainloop()


def calculations():
    calc= Tk()
    calc.geometry('900x800')
    buton1 = Button(root, text='annuities', fg='blue', bg='red', relief=RIDGE, font='bold')
    buton1.place(x=400, y=100)
    buton1.pack()
    calc.mainloop()


root = Tk()  # creates window
root.geometry('900x800')  # size of window
root.title('ACTUARIAL INTERFACE')

text = Label(root, text='ACTUARIAL  ', fg='blue', bg='yellow', relief='solid', font='bold')
text.pack(fill=BOTH, pady=2, padx=2, expand=FALSE)
text.pack()
button1 = Button(root, text="CALCULATIONS", command=calculations)
button1.place(x=400, y=100)
button1.pack()
button2 = Button(root, text='BRAIN TEST', fg='blue', bg='white', relief=RIDGE, font='bold')
button2.place(x=400, y=400)
button2.pack()
button3 = Button(root, text='ABOUT', fg='blue', bg='light blue', relief=RIDGE, font='bold')
button3.place(x=400, y=600)
button3.pack()
button4 = Button(root, text='EXIT', fg='blue', bg='light green', relief=RIDGE, font='bold')
button4.place(x=400, y=600)
button4.pack()

root.mainloop()
today = Tk()
today.geometry('900x800')  # size of window
today.title('SECOND INTERFACE')
Label(today, text='First Name ').grid(row=0)
Label(today, text='Last Name ').grid(row=1)
e1 = Entry(today)
e2 = Entry(today)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

today.mainloop()

top = Tk()
top.title('TABLES')
Lb = Listbox(top)
Lb.insert(1, 'AM92')

Lb.insert(2, 'A1967-70')
Lb.pack()
top.mainloop()
