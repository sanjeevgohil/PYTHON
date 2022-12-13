from tkinter import *
root = Tk()
root.geometry("400x400")

Str = "Long Message"

msg = Message(root, text=Str)
msg.config(bg="lightgreen", font=("Arial", 24, "italic"))
msg.pack()
mainloop()

