
from tkinter import *

root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
c1 = Checkbutton(root, text="Music", onvalue=1, offvalue=0)
c1.pack()
c2 = Checkbutton(root, text="VIdeo")
c2.pack()
root.mainloop()
