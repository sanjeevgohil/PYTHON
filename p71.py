from tkinter import *
root = Tk()

lf = LabelFrame(root, text="This is a Label Frame")
lf.pack(fill=BOTH, expand=YES)

l1 = Label(lf, text="Inside The Label Frame")
l1.pack()
mainloop()