import sqlite3 as sql
import pandas as pd 


city_table = 'cities8'
weather_table = 'weather8'

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
		.format(tn=city_table, fn1= 'city', ft1= 'text', fn2= 'state'))

	rows=cur.fetchall()
	cols =(desc[0] for desc in cur.description)
	df = pd.DataFrame(rows, columns=cols)

	print(df)



