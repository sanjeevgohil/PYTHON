from tkinter import *

root = Tk()
root.geometry("400x400")
root.resizable(0, 0)

ch1 = IntVar()
ch2 = IntVar()
ch3 = IntVar()


def sel():
    if ch1.get() == 1:
        l.config(text="Python")
    elif ch2.get() == 1:
        l.config(text="Android")
    elif ch3.get() == 1:
        l.config(text="DWDM")
    else:
        l.config(text="Not Selected")


l = Label(root, bg="green", width=20, text="Empty")
l.pack()
c1 = Checkbutton(root, text="Python", onvalue=1, offvalue=0, variable=ch1, command=sel)
c1.pack()
c2 = Checkbutton(root, text="Android", onvalue=1, offvalue=0, variable=ch2, command=sel)
c2.pack()
c3 = Checkbutton(root, text="DWDM", onvalue=1, offvalue=0, variable=ch3, command=sel)
c3.pack()
mainloop()