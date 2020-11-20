import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("CREATE TABLE if not exists Roster (\
            Name TEXT, \
            Species TEXT, \
            IQ INT \
            );")

#Insert values into table, creating tuple to do so
peopleValues = (('Jean-Baptiste Zorg', 'Human', 122),('Korben Dallas', 'Meat Popsicle', 100),('Ak\'not', 'Mangalore', -5))

c.executemany("INSERT INTO Roster VALUES(?, ?, ?)", peopleValues)

#update value in table
c.execute("UPDATE Roster SET Species=? WHERE Name=?",
          ('Human', 'Korben Dallas'))

conn.commit()
#Display names and IQs of everyone in the table who is classified as human
c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
while True:
    row = c.fetchone()
    if row is None:
        break
    print(row)
conn.close()
