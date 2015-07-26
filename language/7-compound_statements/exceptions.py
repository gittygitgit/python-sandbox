#!/usr/bin/python
f="test"
try:
  print f
  del f
  print f
except NameError as e:
  try:
    print "caught an exception: " + e
  except TypeError as te:
    print te
    print "caught an exception: " + str(e)
else:
  print "no errors"



try:
  raise Exception('spam', 'eggs')
except Exception as e:
  print type(e)
  print e.args
  print e
  x,y = e.args
  print 'x =', x
  print 'y =', y
