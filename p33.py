
from tkinter import *

root = Tk()
root.geometry("400x400")
root.resizable(0,0)
c = Canvas(root, height=400, width=400)
c.create_arc(20, 20, 100, 100, start=0, extent=100)
c.pack()
root.mainloop()