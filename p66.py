from tkinter import *

m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="Left pane")
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

top = Label(m2, text="Top Pane")
m2.add(top)

bottom = Label(m2, text="Bottom Pane")
m2.add(bottom)

mainloop()