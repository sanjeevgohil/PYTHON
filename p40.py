from tkinter import *
import time


class App(Frame):

    def __init__(self, main=None):
        Frame.__init__(self, main)
        self.master = main
        self.l1 = Label(text=" ", fg="red", font=("Arial", 18))
        self.l1.place(x=50, y=100)
        self.upd_clock()

    def upd_clock(self):
        new = time.strftime("%H:%M:%S")
        self.l1.config(text=new)
        self.after(1000, self.upd_clock)


root = Tk()
a1 = App(root)
root.title("Tkinter Clock")
root.after(1000, a1.upd_clock())
root.mainloop()
