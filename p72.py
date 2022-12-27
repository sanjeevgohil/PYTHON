from tkinter import *
root = Tk()
root.geometry("400x400")
root.resizable(False, False)
lf1 = LabelFrame(root, text="Positive Comments")
lf1.pack(fill=BOTH, expand=YES)
l1 = Label(lf1, text="Place To Put The Positive Comment")
l1.pack()

lf2 = LabelFrame(root, text="Negative Comments")
lf2.pack(fill=BOTH, expand=YES)
l2 = Label(lf2, text="Place To Put The Negative Comment")
l2.pack()
mainloop()