#!/usr/bin/python
"""
issubclass
"""
class Foo:
  pass

class Bar(Foo):
  pass

class Bar2(Foo):
  pass

class Test(Bar):
  pass

print issubclass(Foo, Foo) # True
print issubclass(Bar, Foo) # True
print issubclass(Bar2, Foo) # True
print issubclass(Bar, Bar2) # False
print issubclass(Test, Foo) # True
