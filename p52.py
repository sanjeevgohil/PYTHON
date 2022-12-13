from tkinter import *

root = Tk()


def sl1():
    selection = "Value " + str(var.get())
    l1.config(text=selection)


var = DoubleVar()
s1 = Scale(root, variable=var)
s1.pack()

b1 = Button(root, text="Get Scale Value", command=sl1)
b1.pack()

l1 = Label(root)
l1.pack()

root.mainloop()
