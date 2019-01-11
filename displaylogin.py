import sqlite3;
conn = sqlite3.connect('login.db');
cursor = conn.execute("select * from logintab1");
for row in cursor:
	print "username = ",row[0];
	print "password = ",row[1];
conn.commit()
conn.close()