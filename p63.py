from tkinter import *

root = Tk()
root.geometry("400x400")


def show():
    l1.config(text=f'You Selected::{a.get()}', font=("Arial", 14), bg="red")


a = StringVar()
sb = Spinbox(values=["Android", "DWDM", "Python", "Project"], textvariable=a, command=show)
l1 = Label(root, text="", bg="yellow")
sb.pack()
l1.pack()
root.mainloop()