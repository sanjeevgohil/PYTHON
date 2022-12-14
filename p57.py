from tkinter import *


def onclick():
    pass


root = Tk()
t1 = Text(root)
t1.insert(INSERT, "Ruparel")
t1.insert(END, "Junagadh")

t1.pack()
t1.tag_add("Education", "1.0", "1.4")
t1.tag_add("Start", "1.8", "1.13")

t1.tag_config("Education", background="yellow", foreground="green")
t1.tag_config("Start", background="black", foreground="white")

root.mainloop()
