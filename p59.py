from tkinter import *

root = Tk()
root.title("Main Window")
root.geometry("400x400")

l1 = Label(root, text="This is Main Window")


def open_w1():
    root1 = Toplevel()
    root1.title("Top Level 1")
    root1.geometry("250x250")
    l = Label(root1, text="This is a Top Level 1 Window")
    b1 = Button(root1, text="Exit", command=root1.destroy)
    b2 = Button(root1, text="Open Top Level 2", command=open_w2)
    l.pack()
    b1.pack()
    b2.pack()
    root1.mainloop()


def open_w2():
    root2 = Toplevel()
    root2.title("Top Level 1")
    root2.geometry("250x250")
    l = Label(root2, text="This is a Top Level 2 Window")
    b1 = Button(root2, text="Exit", command=root2.destroy)
    l.pack()
    b1.pack()
    root2.mainloop()


b = Button(root, text="Open Top Level", command=open_w1)
l1.pack()
b.place(x=155, y=55)
root.mainloop()