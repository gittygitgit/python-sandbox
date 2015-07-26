#!/usr/bin/python
import string
import re
f=open("C:\\dev\\tools\\cygwin\\etc\\passwd", 'r')
print f
#for line in f:
#  print line.split(':',1)[0]

for line in f:
  a=line.split(':')
  # print "username: {:<20}, uid: {}".format(a[0], a[2])
#  print "username: " + a[0] + "\t\tuid: " + a[2]
  if re.search("grud",a[0]): print "sfsfs"