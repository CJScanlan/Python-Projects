import webbrowser
from tkinter import *
from tkinter import filedialog
import tkinter as tk





class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        #master framme configuration
        self.master = master
        self.master.title("Web Page Generator")
        self.master.minsize(600,600)
       
        #configure column and rows to determine weight
        self.master.columnconfigure(1,weight=1)
        self.master.rowconfigure(2, weight=1)

        #labels
        self.lbl_main = tk.Label(self.master,text='HTML Body')
        self.lbl_main.grid(row=0,column=1,padx=(15,0),pady=(20,10), sticky=N+W)

        #buttons
        self.btn_update = tk.Button(self.master,width=12,height=2,text='Update', command=lambda: update(self,fileName))
        self.btn_update.grid(row=4,column=1,padx=(5,5),pady=(10,30),sticky=E)
        self.btn_launch = tk.Button(self.master,width=12,height=2,text='Launch', command=lambda: launch(self,fileName))
        self.btn_launch.grid(row=4,column=2, padx=(5,5),pady=(10,30),sticky=E)
        self.btn_create = tk.Button(self.master,width=12,height=2,text='Save As...', command=lambda: createFile(self))
        self.btn_create.grid(row=4,column=1,padx=(125,5),pady=(10,30),sticky=W)
        self.btn_openFile = tk.Button(self.master,width=12,height=2,text='Open File', command=lambda: openFile(self))
        self.btn_openFile.grid(row=4,column=1,padx=(20,0),pady=(10,30),sticky=W)

        #text box with scrollbar
        self.scrollbar = tk.Scrollbar(self.master,orient=VERTICAL)
        self.txt_box = Text(self.master, height=20, width=40, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.txt_box.yview)
        self.scrollbar.grid(row=1,column=4,rowspan=2,columnspan=1,padx=(0,20),pady=(0,10),sticky=N+E+S)

        self.txt_box.grid(row=1,column=1, rowspan=2,columnspan=3, padx=(20,0),pady=(5,10),sticky=N+S+E+W)
        self.txt_box.config(yscrollcommand=self.scrollbar.set)


        #functions
        def createFile(self):   #prompts user to save file, creating a new one to edit
            text = self.txt_box.get("1.0",END)
            files = [('All Files', '*.*'),
                     ('HTML Files', '*.html')]
            global fileName
            fileName = filedialog.asksaveasfilename(filetypes = files, defaultextension = files)
            with open(fileName, "a") as outf:
                outf.write(text)

        def openFile(self):
            global fileName  #make global so other functions can pass in parameter
            fileName = filedialog.askopenfilename(initialdir = "/",title= "Select file",filetypes=([("Html files","*.html")]))
            f = open(fileName)
            txt = f.read()
            f.close()
            self.txt_box.insert(tk.END,txt)

            
        def update(self,fileName):
            f = open(fileName,"w")  #'w' for overwrite, 'x' for create new, 'a' for append
            updateTxt = self.txt_box.get("1.0",END)
            f.write(updateTxt)
            f.close()

        def launch(self,fileName):
            url = fileName
            webbrowser.open_new_tab(url)   #opens html file in new tab on browser
        
                









if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
