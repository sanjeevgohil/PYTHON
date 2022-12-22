from tkinter import *

w1 = PanedWindow()


def add():
    a = int(e1.get())
    b = int(e2.get())
    ans = str(a + b)
    l1.insert(1, ans)


w1.pack(fill=BOTH, expand=1)
l1 = Entry(w1, bd=5)
w1.add(l1)

w2 = PanedWindow(w1, orient=VERTICAL)
w1.add(w2)
e1 = Entry(w2)
e2 = Entry(w2)
w2.add(e1)
w2.add(e2)

b1 = Button(w2, text="Add", command=add)
w2.add(b1)

mainloop()
