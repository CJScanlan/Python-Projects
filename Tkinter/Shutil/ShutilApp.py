import tkinter as tk
import datetime as dt
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #master frame configuration
        self.master = master
        self.master.title("Check files")
        self.master.minsize(500,215)
        self.master.maxsize(5000,215)

        #labels
        self.source_lbl = tk.Label(self.master, text="Source folder:")
        self.source_lbl.grid(row=0,column=1,padx=(5,5),pady=(15,5),sticky=W)
        self.destination_lbl = tk.Label(self.master, text="Destination folder:")
        self.destination_lbl.grid(row=2,column=1,padx=(5,5),pady=(15,5),sticky=W)
                            

        #buttons
        self.btn_browse = tk.Button(self.master, width=12,height=1, text='Browse...', command=lambda: openDir(self))
        self.btn_browse.grid(row=1,column=0,padx=(10,10),pady=(5,5))
        self.btn_browse2 = tk.Button(self.master, width=12,height=1, text='Browse...', command=lambda: openDir2(self))
        self.btn_browse2.grid(row=3,column=0,padx=(10,10),pady=(5,5))
        self.btn_check = tk.Button(self.master, width=12,height=2, text='Check for files...', command=lambda: checkFiles(self,source,destination))
        self.btn_check.grid(row=4,column=0,padx=(5,5),pady=(5,10))
        self.btn_close = tk.Button(self.master, width=12,height=2, text='Close Program', command=lambda: closeProgram(self))
        self.btn_close.grid(row=4,column=2,padx=(5,15),pady=(5,10), sticky=E)

        #text entries
        self.txt_browse = tk.Entry(self.master, text='')
        self.txt_browse.grid(row=1, column=1,rowspan=1, columnspan=2, padx=(10,15),pady=(5,5),sticky=N+S+E+W)
        self.txt_browse2 = tk.Entry(self.master, text='')
        self.txt_browse2.grid(row=3, column=1,rowspan=1,columnspan=2, padx=(10,15),pady=(5,5),sticky=N+S+E+W)       

        self.master.columnconfigure(1,weight=1)



def openDir(self):
    global source
    source = filedialog.askdirectory()+'/'
    self.txt_browse.insert(0,source)

def openDir2(self):
    global destination
    destination = filedialog.askdirectory()+'/'
    self.txt_browse2.insert(0,destination)

def closeProgram(self):
    if messagebox.askokcancel("Exit program", "Exit application?"):
        #closes app
        self.master.destroy()
        os._exit(0)


def checkFiles(self,source,destination):
    files = os.listdir(source)
    now = dt.datetime.now()
    Hour24 = now-dt.timedelta(hours=24)
    for i in files:   #create loop to find files modified within last 24 hours
        st = os.stat(source+i)
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > Hour24:   #if modified time less than 24 hrs, move to destination folder
            shutil.move(source+i, destination)
            messagebox.showinfo("Files transferred","Recently modified files have been transferred.")
        else:
            messagebox.showinfo("No Files to Transfer","There were no recently modified files.")





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
