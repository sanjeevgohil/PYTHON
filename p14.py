from tkinter import *

root = Tk()
root.geometry("400x400")
root.resizable(0,0)
def show(e):
    root.configure(background="red")

b1 = Button(root, text="Login", font=("Arial",20))
b1.bind("<Button>",show)
b1.pack()
root.mainloop()
