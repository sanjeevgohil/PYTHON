from tkinter import *
root = Tk()
root.geometry("400x400")

l1 = Label(root, text="IMAGE", justify=LEFT, padx=10)
l1.pack(side=LEFT)

P1 = PhotoImage(file="D:/v1.png")

l2 = Label(root, image=P1)
l2.pack(side=RIGHT)
mainloop()
