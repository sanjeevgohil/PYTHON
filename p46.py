from tkinter import *

root = Tk()
root.geometry("400x400")
mb = Menubutton(root, text="Check Button")
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu
ch1 = IntVar()
ch2 = IntVar()
mb.menu.add_checkbutton(label="Python", variable=ch1)
mb.menu.add_checkbutton(label="DWDM", variable=ch2)
mb.pack()
mainloop()
