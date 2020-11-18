#
# Python Ver:   3.8.5
#
# Author:       Carly J. Scanlan
#
# Purpose:      Demo using OOP, Tkinter GUI module, and SQLite3.
#
# Tested OS:    This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk
from tkinter import messagebox

import student_func
import student_gui

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,350)
        self.master.maxsize(500,350)
        self.master.title("Student Tracking")
        self.master.configure(bg="lightblue")
        self.master.protocol("WM_DELETE_WINDOW", lambda: student_func.ask_quit(self))
        arg = self.master

        #loading GUI widgets from separate module
        student_gui.load_gui(self)

        #Tkinter menu dropdown object
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q", command=lambda: student_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.master.config(menu=menubar, borderwidth='1')



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
                             

        
        
