from tkinter import *

win = Tk()
lb = Listbox(win, height=3)
lb.pack(side=LEFT)
lb.insert(END, "First entry")
lb.insert(END, "Second entry")
lb.insert(END, "Third entry")
lb.insert(END, "Fourth entry")

sb = Scrollbar(win, orient=VERTICAL)
sb.pack(side=LEFT, fill=Y)
sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)

lb.curselection()
