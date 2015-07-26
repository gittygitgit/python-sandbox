#!/usr/bin/python

class foo:

  def __init__(self, fname, lname):
    print "in __init__"
    self.firstname=fname
    self.lastname=lname
	
  def __enter__(self):
    print "in __enter__"
	
  def __exit__(self, type, value, traceback):
    print "in _exit__"
	
  def printname(self):
    print "here"
    print "[firstname=" + self.firstname + ", lastname=" + self.lastname + "]"
	
bar=foo("mike", "grudkowski")

bar.printname()
