#!/usr/bin/python

import pyodbc


conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=dbFbms;UID=appusr;PWD=F@ll2012__')
cursor=conn.cursor()

cursor.execute("select count(*) from tUser")
row=cursor.fetchone()
print 'Number of records in tUser: {0}'.format(row[0])

# load sql
f=open('../out/insert_tUsers.sql', 'r')
print 'Number of insert statements: {0}'.format(sum(1 for l in f))
for insert in f:
  print insert

f.seek(0)
for insert in f:
  cursor.execute(insert)
  conn.commit()

cursor.execute("select count(*) from tUser")
row=cursor.fetchone()
print 'Number of records in tUser: {0}'.format(row[0])

