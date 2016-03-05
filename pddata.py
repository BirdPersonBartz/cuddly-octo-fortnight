import sqlite3 as lite
import pandas as pd 

con= lite.connect('getting_started.db')

with con:
	cur = con.cursor()
	cur.execute("SELECT * from weather2")

	rows = cur.fetchall()

	df = pd.DataFrame(rows)