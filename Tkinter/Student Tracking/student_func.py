

import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3

import student_main
import student_gui

def ask_quit(self):
    if messagebox.askokcancel("Exit Program", "OK to exit?"):
        self.master.destroy()
        os._exit(0)

def create_db(self):
    conn = sqlite3.connect('student.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_students( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_fullname TEXT, \
        col_phone TEXT, \
        col_email TEXT, \
        col_course TEXT \
        );")
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    conn = sqlite3.connect('student.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_students (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""", ('Carly','Scanlan','Carly Scanlan','444-444-4444','carlyscanlan@gmail.com','Python'))
            conn.commit()
    conn.close()

def count_records(cur):
    count=""
    cur.execute("""SELECT COUNT(*) FROM tbl_students""")
    count = cur.fetchone()[0]
    return cur,count


# Selecting item in Listbox
def onSelect(self,event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('student.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT col_fname,col_lname,col_phone,col_email,col_course FROM tbl_students WHERE col_fullname = (?)""", [value])
        varBody = cur.fetchall()
        # returns tuple, slice into 5 parts using data[]
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_course.delete(0,END)
            self.txt_course.insert(0,data[4])
            


def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()

    #normalizing data
    var_fname = var_fname.strip()
    var_lname = var_lname.strip()
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_course = self.txt_course.get().strip()
    var_course = var_course.title()
    if not "@" or not "." in var_email:
        print("Incorrect email format.")
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_course) > 0):
        conn = sqlite3.connect('student.db')
        with conn:
            cur = conn.cursor()
            cur.execute("""SELECT COUNT(col_fullname) FROM tbl_students WHERE col_fullname = '{}'""".format(var_fullname))
            count = cur.fetchone()[0]
            chkName = count
            if chkName == 0:
                cur.execute("""INSERT INTO tbl_students (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""", (var_fname,var_lname,var_fullname,var_phone,var_email,var_course))
                self.lstList1.insert(END, var_fullname)
                onClear(self)
            else:
                messagebox.showerror("Name Error","{} already exists in the database.".format(var_fullname))
                onClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that all forms are filled out.")


def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection())
    conn = sqlite3.connect('student.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "The information asscociated with \n{} will be deleted.\nProceed with the request?.".format(var_select))
            if confirm:
                conn = sqlite3.connect('student.db')
                with conn:
                    cur = conn.cursor()
                    cur.execute("""DELETE FROM tbl_students WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self)
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "{} is the last record in the database and cannot be deleted.".format(var_select))
    conn.close()


def onDeleted(self):
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)


def onRefresh(self):
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('student.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cur.fetchone()[0]
        i = 0
        while i < count:
            cur.execute("""SELECT col_fullname FROM tbl_students""")
            varList = cur.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i = i + 1
    conn.close()



if __name__ =="__main__":
    pass
