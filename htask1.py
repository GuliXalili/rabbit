import sqlite3 as sql

con = sql.connect("MobilePhone.db")

abc = con.cursor()
abc1 = con.cursor()

abc.execute('''
CREATE TABLE IF NOT EXISTS Apple(
    operating system TEXT,
    storage FLOAT
)
''')
abc1.execute('''
CREATE TABLE IF NOT EXISTS Artel(
    operating system TEXT,
    storage FLOAT
)
''')