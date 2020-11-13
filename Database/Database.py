
import sqlite3
import os

conn = sqlite3.connect('files.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    data_type TEXT \
    )")
    conn.commit()
conn.close()

cwd = os.listdir()
print(cwd)

conn = sqlite3.connect('files.db')

for x in cwd:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            #The value for each row will be one name out of the tuple therefore (x,)
            #will denote a one element tuple for each name ending with .txt.
            cur.execute("INSERT INTO tbl_files (data_type) VALUES (?)", (x,))
            print(x)
conn.close()
