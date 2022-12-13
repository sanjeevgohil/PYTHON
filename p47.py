from tkinter import *
root = Tk()
root.geometry("400x400")
mb = Menubutton(root, text="Radio Button")
mb.menu = Menu(mb)
mb["menu"] = mb.menu
ch1 = IntVar()

mb.menu.add_radiobutton(label="Python", variable=ch1)
mb.menu.add_radiobutton(label="DWDM", variable=ch1)
mb.pack()
mainloop()
