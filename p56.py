import tkinter as tk

root = tk.Tk()
root.title("Python Menus")

m1 = tk.Menu(root)

menu = tk.Menu(m1, tearoff=0)

menu.add_command(label="Open")
menu.add_command(label="Save")
menu.add_command(label="Save As")
menu.add_command(label="Close")
menu.add_separator()
menu.add_command(label="Exit", command=root.quit)

root.config(menu=m1)
m1.add_cascade(label="File", menu=menu)

t = tk.Entry(root)
t.insert(tk.END, "Some Default Text Here TO view New Text")
t.configure(font=("Arial", 12))
t.pack()

s1 = tk.Scrollbar(root, orient=tk.HORIZONTAL)
s1.config(command=t.xview())

t.configure(xscrollcommand=s1.set)
s1.pack(side=tk.BOTTOM, fill=tk.X)
tk.mainloop()
