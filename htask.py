import sqlite3 as sql

con = sql.connect("first.db")

inf = con.cursor()
inf1 = con.cursor()

inf.execute('''
CREATE TABLE IF NOT EXISTS Flowers(
    type TEXT,
    color TEXT
)
''')
inf1.execute('''
CREATE TABLE IF NOT EXISTS Fruits(
    type TEXT,
    taste TEXT
)
''')