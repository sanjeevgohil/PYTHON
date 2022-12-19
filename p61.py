import tkinter as tk

t = tk.Tk()

t1 = tk.DoubleVar
sb = tk.Spinbox(t, from_=0.6, to=50.0, increment=.01)
sb.pack()
t.mainloop()