import tkinter.messagebox
from tkinter import *

root = Tk()
root.geometry("400x400")
root.resizable(0,0)
def show():
    tkinter.messagebox.showinfo("Bca 6", "Sanjeev")

b1 = Button(root, text="Login", font=("Arial",20), command=show)

b1.pack()
root.mainloop()
