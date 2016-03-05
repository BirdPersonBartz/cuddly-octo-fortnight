import sqlite3 as lite

cities2 = (('Las Vegas', 'NV'),
                    ('Atlanta', 'GA'))

weather2 = (('Las Vegas', 2013, 'July', 'December',90),
                     ('Atlanta', 2013, 'July', 'January',85))

con = lite.connect('getting_started.db')

# Inserting rows by passing tuples to `execute()`
with con:

    cur = con.cursor()
    cur.executemany("INSERT INTO cities2 VALUES(?,?)", cities2)
    cur.executemany("INSERT INTO weather2 VALUES(?,?,?,?,?)", weather2)