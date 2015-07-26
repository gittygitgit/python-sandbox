#!/usr/bin/python
"""
getattr
retrieves the value of a given attribute
"""
class Test:
  f="foo"
t=Test()

print getattr(t, "f") # foo


