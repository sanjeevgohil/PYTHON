from tkinter import *

root = Tk()
root.geometry("400x400")

mb = Menubutton(root, text="Programming Language")

op = Menu(mb)

mb.config(menu=op)

op.add_command(label="DWDM")
op.add_command(label="Python")
op.add_separator()
op.add_command(label="Android")

mb.pack()
root.mainloop()