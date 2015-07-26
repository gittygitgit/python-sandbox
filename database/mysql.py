#!/usr/bin/python
import MySQLdb

types={}

for i in MySQLdb.STRING:
  types[i]="String"

for i in MySQLdb.NUMBER:
  types[i]="Number"
  

db=MySQLdb.connect(passwd="rubberband", host="127.0.0.1", user="root")
c=db.cursor()
result=c.execute("show databases")
print """There are {0!s} databases
  """, result

print "Result has {:d} columns".format(len(c.description))

for col in c.description:
  print "Column..."
  print "  Name={:s}".format(col[0])
  print "  Type={:s}".format(types[col[1]])



