#!/usr/bin/python
"""
isinstance
"""
class Foo:
  pass

class Bar(Foo):
  pass

class Test(Bar):
  pass

print isinstance(Test(), Foo) # True
print isinstance(Test(), Bar) # True
print isinstance(Test(), object) # True

print isinstance("dsfsdf", Bar) # False
