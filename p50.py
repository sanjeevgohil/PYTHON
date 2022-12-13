from tkinter import *

root = Tk()
root.geometry("400x400")


def sel1():
    s1 = "You Select The Option " + var.get()
    l1.config(text=s1)


var = StringVar()

r1 = Radiobutton(root, text="Python", variable=var, value="Python", command=sel1)
r1.select()
r1.pack()
r2 = Radiobutton(root, text="Android", variable=var, value="Android", command=sel1)
r2.deselect()
r2.pack()
r3 = Radiobutton(root, text="DWDM", variable=var, value="DWDM", command=sel1)
r3.deselect()
r3.pack()

l1 = Label(root)
l1.pack()
mainloop()
