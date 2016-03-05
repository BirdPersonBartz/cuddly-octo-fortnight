import sqlite3 as sql
import pandas as pd 


city_table = 'cities9'
weather_table = 'weather9'

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
	cur.execute('CREATE TABLE {tn} (city text, state text)'\
		.format(tn=city_table))
	cur.execute('CREATE TABLE {tn} (city text, year integer, warm_month text, cold_month text, avgerage_high integer)'\
		.format(tn=weather_table))