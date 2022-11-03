import sqlite3 as sql

con1 = sql.connect("Nail.db")

cho = con1.cursor()
cho1 = con1.cursor()

cho.execute('''
CREATE TABLE IF NOT EXISTS Shlak(
    color TEXT,
    price INTEGER
)
''')
cho1.execute('''
CREATE TABLE IF NOT EXISTS Tipsi(
    color TEXT,
    price INTEGER
)
''')