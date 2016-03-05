import sqlite3 as lite
import pandas as pd 

con = lite.connect('getting_started.db')


with con:
	cur = con.cursor()
	cur.execute("SELECT state, AVG(average_high)  FROM cities2 INNER JOIN weather2 GROUP BY state HAVING AVG(average_high) > 65;")

	rows = cur.fetchall()
	cols = [desc[0] for desc in cur.description]
	df = pd.DataFrame(rows, columns=cols)
	print(df)