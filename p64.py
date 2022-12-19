from tkinter import *

root = Tk()
root.geometry("400x400")


def show():
    root.configure(background=a.get())


a = StringVar()
sb = Spinbox(values=["black", "blue", "green", "pink"], textvariable=a, command=show)
sb.pack()
root.mainloop()
