import sqlite3 as lite

con=lite.connect('getting_started.db')

with con:
	cur = con.cursor()
	cur.execute('INSERT INTO cities2 VALUES ('Washington','DC')')
	cur.execute('INSERT INTO cities2 VALUES ('HOUSTON','TX')')
	cur.execute('INSERT INTO weather2 VALUES ('Washington',2013,'July','Jan')')
	cur.execute('INSERT INTO weather2 VALUES ('HOUSTON',2013,'July','Jan')')
