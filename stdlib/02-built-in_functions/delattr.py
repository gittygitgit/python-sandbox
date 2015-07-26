#!/usr/bin/python

"""
delattr

attribute?
anything following a dot is an attribute of the thing preceding the dot


"""

class Test:
  fld="foo"

t=Test()
print t.fld # foo
delattr(Test,"fld")
print t.fld # no attribute fld
