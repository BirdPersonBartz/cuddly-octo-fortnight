import sqlite3 as sql
import pandas as pd 


city_table = 'cities12'
weather_table = 'weather12'

city_col = 'city'
state_col = 'state'
year_col = 'year'
w_month = 'warm_month'
c_month = 'cold_month'
avg_high = 'avg_high'
text_type = 'text'
integer_type = 'integer'

citiesinput = ('NYC','NY'),('Boston', 'MA'),('Chicago','IL'),('Miami','FL'),('Dallas','TX'),('Seattle','WA)')
weatherinput = (('NYC',2013,'July','Jan',62),('Boston',2013,'July','Jan',59),('Chicago',2013,'July','Jan',59),('Miami',2013,'Aug','Jan',84),('Dallas',2013,'July','Jan',77),('Seattle',2013,'July','Jan',61))


con = sql.connect('getting_started.db')

with con:
	cur = con.cursor()
	cur.execute('CREATE TABLE {tn} ({fn1} {ft1}, {fn2} {ft1})'\
		.format(tn=city_table, fn1=city_col, ft1=text_type, fn2=state_col))
	cur.execute('CREATE TABLE {tn} ({fn1} {ft1}, {fn2} {ft2}, {fn3} {ft1}, {fn4} {ft1}, {fn5} {ft1})'\
		.format(tn=weather_table, fn1=city_col, ft1=text_type, fn2=year_col,ft2=integer_type,fn3=w_month,fn4=c_month,fn5=avg_high))
	cur.executemany("INSERT INTO cities8 VALUES (?,?)", citiesinput)
	cur.executemany("INSERT INTO weather8 VALUES (?,?,?,?,?)", weatherinput)
	cur.execute("SELECT city, state, warm_month FROM weather12 INNER JOIN cities12 ON name = city ORDER BY state HAVING warm_month = 'July' ")

	rows=cur.fetchall()
	cols =(desc[0] for desc in cur.description)
	df = pd.DataFrame(rows, columns=cols)

	print(df)



