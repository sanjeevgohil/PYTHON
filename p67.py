from tkinter import *
m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)
left = Entry(m1, bd=5)
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

e2 = Entry(m2)
e2.pack()
mainloop()