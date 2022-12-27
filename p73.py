import tkinter as tk
from tkinter import messagebox as mb


def ans():
    mb.showerror("Answer", "Sorry No Answer Available")


def callback():
    if mb.askyesno("Verify", "Really Quit?"):
        mb.showwarning("Yes", "Not Yet Implemented")
    else:
        mb.showinfo("No", "Quit Has Been Cancelled")


tk.Button(text="Answer", command=ans).pack()
tk.Button(text="Quit", command=callback).pack()

tk.mainloop()
