from tkinter import *
root = Tk()

for i in ['blue', 'red', 'yellow', 'white', 'black']:

    Frame(width=440, height=20, bg=i).pack()
mainloop()