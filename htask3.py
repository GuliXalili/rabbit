import sqlite3 as sql

bbb = sql.connect("Shop.db")

qwe = bbb.cursor()
qwe1 = bbb.cursor()

qwe.execute('''
CREATE TABLE IF NOT EXISTS Juse(
    taste TEXT,
    kind INTEGER
)
''')
qwe1.execute('''
CREATE TABLE IF NOT EXISTS Soda(
    taste TEXT,
    kind INTEGER
)
''')