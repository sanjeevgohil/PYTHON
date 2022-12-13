
from tkinter import *

root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
c = Canvas(root, height=400, width=400)
filename = PhotoImage(file="d:/s1.gif")
i = c.create_image(100, 100, image=filename)
c.pack()
root.mainloop()
