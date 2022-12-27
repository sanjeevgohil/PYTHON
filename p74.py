from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Registration From")
root.resizable(False, False)

l1 = Label(root, text="Registration Form", width=24, font=("bold", 20))
l1.place(x=55, y=60)

l2 = Label(root, text="Full Name", width=20, font=("bold", 10))
l2.place(x=80, y=130)

e1 = Entry(root)
e1.place(x=240, y=130)

l3 = Label(root, text="Email", width=20, font=("bold", 10))
l3.place(x=68, y=180)

e2 = Entry(root)
e2.place(x=240, y=180)

l4 = Label(root, text="Hobby", width=20, font=("bold", 10))
l4.place(x=70, y=230)

var = IntVar()
Checkbutton(root, text="Cricket", variable=var).place(x=235, y=230)
Checkbutton(root, text="Football", variable=var).place(x=290, y=230)
Checkbutton(root, text="Reading", variable=var).place(x=360, y=230)

l5 = Label(root, text="Country", width=20, font=("bold", 10))
l5.place(x=72, y=280)
ls = ["India", "US", "UK", "Germany"]
c = StringVar()
dl = OptionMenu(root, c, *ls)
dl.config(width=20)
c.set("Select Your Country")
dl.place(x=240, y=280)

l6 = Label(root, text="Gender", width=20, font=("bold", 10))
l6.place(x=70, y=330)

var1 = IntVar()
Radiobutton(root, text="Male", variable=var1).place(x=230, y=330)
Radiobutton(root, text="Female", variable=var1).place(x=290, y=330)

Button(root, text="Submit", width=20, bg="brown", fg="cyan").place(x=180, y=380)
root.mainloop()
