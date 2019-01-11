import sqlite3;
conn = sqlite3.connect('login.db');
conn.execute("create table logintab1 (username char(20) primary key NOT NULL,pass char(20) NOT NULL);")
conn.execute("insert into logintab1(username,pass) values('aditya','ag16')")
conn.execute("insert into logintab1(username,pass) values('aditya1','ag16')")
conn.execute("insert into logintab1(username,pass) values('aditya2','ag16')")
conn.execute("insert into logintab1(username,pass) values('aditya3','ag16')")
conn.commit()
conn.close()