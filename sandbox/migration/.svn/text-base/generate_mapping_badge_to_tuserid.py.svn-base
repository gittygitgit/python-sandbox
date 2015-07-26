#!/usr/bin/python

import pyodbc


# connect
#conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=dbFbms;UID=appusr;PWD=F@ll2012__')
#conn = pyodbc.connect('DRIVER={SQL Server};SERVER=secpapbodbqa03,2198;DATABASE=dbFbms;UID=FBMS_AppUser;PWD=efbE$12sMP')
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.96.128.15,1198;DATABASE=dbFbms;UID=FBMS_AppUser;PWD=noT02Br@cH')
cursor=conn.cursor()

sql="select Badge, UserId from tUser where Badge is not null"
cursor.execute(sql)

rows=cursor.fetchall()
print "Found {0} users".format(len(rows))

f=open('../out/badge_to_uid.txt', 'w')

for row in rows:
  f.write(row.Badge + "," + str(row.UserId) + "\n")

#print "Wrote {0} rows".format(f.tell())
f.close()
