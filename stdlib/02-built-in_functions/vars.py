#!/usr/bin/python
"""
vars

What is the __dict__ attribute?
Holds the namespace for a module, class, instance, or other object with a __dict__ attribute.

Equivilent to locals() in the absence of an argument.

Can local dictionary be updated?
No.  Local dictionaries are read-only.

"""

class Foo(object):
  a="test"

f=Foo()
print vars(f) # {}
f.test="test"
print vars(f) # {'test':'test'}

