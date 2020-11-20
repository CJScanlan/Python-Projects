import tkinter as tk
import datetime as dt
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil


import ShutilApp



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

