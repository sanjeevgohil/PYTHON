from tkinter import *

root = Tk()

root.geometry("400x400")
root.title("Text Example")


def inp():
    i1 = t1.get("1.0", "end-1c")
    if i1 == "120":
        outtxt.delete("1.0", "end")
        outtxt.insert(END, "Correct")
    else:
        outtxt.delete("1.0", "end")
        outtxt.insert(INSERT, "Wrong Answer")


l = Label(text="What is Answer Of 24 x 47")
t1 = Text(root, height=10, width=25, bg="light yellow")
outtxt = Text(root, height=10, width=25, bg="light cyan")
b1 = Button(root, height=2, width=20, text="Show", command=lambda: inp())

l.pack()
t1.pack()
outtxt.pack()
b1.pack()
mainloop()
