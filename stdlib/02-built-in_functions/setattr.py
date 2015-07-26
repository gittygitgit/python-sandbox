#!/usr/bin/python
""" 
setattr
used to set an attribute value on an object

useful mainly when the attribute name is obtained dynamically
"""
class Foo:
  val=3

f=Foo()
a="val"
setattr(f,a, "bar")
print f.val # prints "bar"


