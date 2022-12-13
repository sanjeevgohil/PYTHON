from tkinter import *

root = Tk()

sb1 = Scrollbar(root)
sb1.pack(side=RIGHT, fill=Y)

lb = Listbox(root, yscrollcommand=sb1.set)
for i in range(100):
    lb.insert(END, 1)

lb.pack(side=LEFT, fill=BOTH)
sb1.config(command=lb.yview())


root.mainloop()
