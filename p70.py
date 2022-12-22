from tkinter import *

root = Tk()
pw = PanedWindow(orient=VERTICAL)
b1 = Button(pw, text="Click")
b1.pack(side=TOP)
cb = Checkbutton(pw, text="Select...")
cb.pack(side=BOTTOM)
pw.pack(fill=BOTH, expand=True)
mainloop()
