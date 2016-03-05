import sqlite3 as lite
import pandas as pd

con= lite.connect('getting_started.db')

with con:
	cur = con.cursor()
	cur.execute("SELECT city, state, warm_month FROM weather12 INNER JOIN cities12 ON name = city ORDER BY 'state' HAVING warm_month = 'July'; ")

	rows=cur.fetchall()
	cols =(desc[0] for desc in cur.description)
	df = pd.DataFrame(rows, columns=cols)

	print(df)

