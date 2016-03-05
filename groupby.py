import sqlite3 as lite
import pandas as pd 

con = lite.connect('getting_started.db')


with con:
	cur = con.cursor()
	cur.execute("SELECT city, warm_month FROM weather2 GROUP BY warm_month")

	rows = cur.fetchall()
	cols = [desc[0] for desc in cur.description]
	df = pd.DataFrame(rows, columns=cols)
	print(df)