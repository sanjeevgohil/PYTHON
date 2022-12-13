from tkinter import *
from tkinter.filedialog import *
root = Tk()
root.title("Untitled-Notepad")


def newFile():
    ta.delete(1.0, END)


def Openfile():
    askopenfilename()


def Savefile():
    name = asksaveasfile()


def Saveas():
    name = asksaveasfilename()


m1 = Menu(root)
file = Menu(m1, tearoff=0)
file.add_command(label="New", accelerator="Ctrl+N", command=newFile)
file.add_command(label="New Window", accelerator="Ctrl+Shift+N")
file.add_command(label="Open", accelerator="Ctrl+O", command=Openfile)
file.add_command(label="Save", accelerator="Ctrl+S", command=Savefile)
file.add_command(label="Save As...", accelerator="Ctrl+Shift+S", command=Saveas)
file.add_separator()
file.add_command(label="Page Setup")
file.add_command(label="Print...", accelerator="Ctrl+P")
file.add_separator()
file.add_command(label="Exit", command=root.quit)
m1.add_cascade(label="File", menu=file)

edit = Menu(m1, tearoff=0)
edit.add_command(label="Undo", accelerator="Ctrl+Z")
edit.add_separator()
edit.add_command(label="Cut", accelerator="Ctrl+X")
edit.add_command(label="Copy", accelerator="Ctrl+C")
edit.add_command(label="Paste", accelerator="Ctrl+V")
edit.add_command(label="Delete", accelerator="Del")
edit.add_separator()
edit.add_command(label="Find...", accelerator="Ctrl+F")
edit.add_command(label="Find Next", accelerator="F3")
edit.add_command(label="Find Previous", accelerator="Shift+F3")
edit.add_command(label="Replace...", accelerator="Ctrl+H")
edit.add_command(label="Go To...", accelerator="Ctrl+G")
edit.add_separator()
edit.add_command(label="Select All", accelerator="Ctrl+A")
edit.add_command(label="Time/Date", accelerator="F5")
edit.add_command(label="Font")
m1.add_cascade(label="Edit", menu=edit)

view = Menu(m1, tearoff=0)
view.add_command(label="Zoom")
view.add_command(label="Status Bar")
view.add_command(label="Word wrap")
m1.add_cascade(label="View", menu=view)

ta = Text(root)
ta.pack(expand=True, fill=BOTH)
root.config(menu=m1)
root.mainloop()
