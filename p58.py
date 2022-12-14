from tkinter import *

root = Tk()
root.geometry("250x250")

t = Text(root, height=5, width=50)

l = Label(root, text="Python Tkinter Example")
l.config(font=("Arial", 14))

s1 = "different type of text"

b1 = Button(root, text="Edit", command=root.destroy)
b1.pack()

t.insert(END, s1)
l.pack()
t.pack()

mainloop()