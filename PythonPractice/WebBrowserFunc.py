import tkinter as tk
from tkinter import filedialog
import webbrowser

import WebBrowserApp


fileName = filedialog.askopenfilename(initialdir = "/",title= "Select file",filetypes=([("Html files","*.html")]))
def openFile(self):
    f = open(fileName)
    txt = f.read()
    f.close()
    self.txt_box.insert(tk.END,txt)

def update(self,fileName):
    f = open(fileName,"a")  #'w' for overwrite, 'x' for create new, 'a' for append
    updateTxt = self.txt_box.get()
    f.write(updateTxt)
    f.close()

def launch(self,fileName):
    url = fileName
    webbrowser.open_new_tab(url)   #opens html file in new tab on browser
