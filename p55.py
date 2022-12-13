from tkinter import *
import tkinter as tk

root = Tk()
root.resizable(False, False)
root.title("Scroll Widget Example")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
text = tk.Text(root, height=10)
text.grid(row=0, column=0)
sb1 = Scrollbar(root, orient=VERTICAL, command=text.xview())
sb1.grid(row=0, column=1)
text['yscrollcommand'] = sb1.set
root.mainloop()
