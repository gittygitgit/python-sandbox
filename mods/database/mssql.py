#!/usr/bin/python

import pyodbc


# connect
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=dbFbms;UID=appusr;PWD=F@ll2012__')
cursor=conn.cursor()

sql="select count(*) from tUser"
cursor.execute(sql)

row=cursor.fetchone()

if row:
  print row[0]
