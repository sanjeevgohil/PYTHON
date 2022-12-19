from tkinter import *

root = Tk()
root.geometry("400x400")


def show():
    root.configure(background=a.get())


a = StringVar()
sb = Spinbox(values=["red", "green", "pink"], textvariable=a)
b1 = Button(root, text="Click", command=show)
sb.pack()
b1.pack()
mainloop()
