import sqlite3
import cgi,cgitb
#!/usr/bin/python					
							
#conn = sqlite3.connect('login.db');
#cursor = conn.execute("select * from logintab1");
form = cgi.FieldStorage()
user = form.getValue('username')
pas = form.getValue('password')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>login</title>"
print "</head>"
print "<body>"
print "<h1>username %s password %s</h1>"%(user,pas)
print "</body>"
print "</html>"
#conn.commit()
#conn.close()