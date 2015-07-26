#!/usr/bin/python

from foo import Foo

class Bar(Foo): # Bar subclasses Foo
  xyz="sss"
  count=0
  # constructor
  def __init__(self, f1, f2):
    self.f1=f1
    self.f2=f2
    Bar.count+=1

  # method
  def getFields(self):
    # try-catch in case non-strings are passed in
    try:
      print "f1: " + self.f1 + ", f2: " + self.f2 
    except:
      print "error"

# create instance of Bar
b=Bar(123,"abc")

# display all b attributes
print b.f1
print b.f2

# print them another way...use a method
b.getFields() # oops, can't concatenate ints and strings

# this will work though...
b=Bar("aaa","bbb")
b.getFields()


  
