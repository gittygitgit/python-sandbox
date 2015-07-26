#!/usr/bin/python
"""
super

Only valid for new-style classes

Why super?
To delegate method calls to a class in the instance's ancestor tree.
"""
class A(object): # extend object so it's new-style class
  def foo(self):
    print "goo"

class B(A):
  def foo(self):
    print "foo"

class C(B):
  def foo(self):
    print "bar"

c=C()
c.foo() # bar
super(type(c), c) # foo

