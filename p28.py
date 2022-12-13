
from tkinter import *

root = Tk()
root.geometry("400x400")
root.resizable(0,0)
c = Canvas(root, height=250, width=300)
Line = c.create_line(150,50,100,200)
Line = c.create_line(150,50,220,200)
Line = c.create_line(220,200,80,80)
Line = c.create_line(80,80,230,80)
Line = c.create_line(230,80,100,200)
c.pack()
root.mainloop()
