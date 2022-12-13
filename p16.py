from tkinter import *

root = Tk()
root.geometry("400x400")
root.resizable(0,0)
def show1(e):
    root.configure(background="red")
def show2(e):
        root.configure(background="pink")

b1 = Button(root, text="Login", font=("Arial",20))
b1.bind("<Enter>",show1)
b1.bind("<Leave>",show2)
b1.pack()
root.mainloop()
