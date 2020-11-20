import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.title("Check files")
        self.master.minsize(500,180)
        self.master.maxsize(5000,180)

        self.btn_browse = tk.Button(self.master, width=12,height=1, text='Browse...', command=lambda: openDir(self))
        self.btn_browse.grid(row=1,column=0,padx=(10,10),pady=(40,5))
        self.btn_browse2 = tk.Button(self.master, width=12,height=1, text='Browse...', command=lambda: openDir2(self))
        self.btn_browse2.grid(row=2,column=0,padx=(10,10),pady=(5,5))
        self.btn_check = tk.Button(self.master, width=12,height=2, text='Check for files...')
        self.btn_check.grid(row=3,column=0,padx=(5,5),pady=(5,10))
        self.btn_close = tk.Button(self.master, width=12,height=2, text='Close Program')
        self.btn_close.grid(row=3,column=2,padx=(5,15),pady=(5,10), sticky=E)

        self.txt_browse = tk.Entry(self.master, text='')
        self.txt_browse.grid(row=1, column=1,rowspan=1, columnspan=2, padx=(10,15),pady=(40,5),sticky=E+W)
        self.txt_browse2 = tk.Entry(self.master, text='')
        self.txt_browse2.grid(row=2, column=1,rowspan=1,columnspan=2, padx=(10,15),pady=(5,5),sticky=E+W)       

        self.master.columnconfigure(1,weight=1)






def openDir(self):
    folderPath = filedialog.askdirectory()
    self.txt_browse.insert(0,folderPath)

def openDir2(self):
    folderPath = filedialog.askdirectory()
    self.txt_browse2.insert(0,folderPath)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
