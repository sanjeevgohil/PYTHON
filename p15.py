from tkinter import *

root = Tk()
root.geometry("400x400")
root.resizable(0,0)
def show1(e):
    root.configure(background="red")
def show2(e):
        root.configure(background="pink")
def show3(e):
        root.configure(background="green")

b1 = Button(root, text="Login", font=("Arial",20))
b1.bind("<Button-1>",show1)#left
b1.bind("<Button-2>",show2)#scroll
b1.bind("<Button-3>",show3)#right
b1.pack()
root.mainloop()
