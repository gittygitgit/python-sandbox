#!/usr/bin/python
class Foo:
  pass

class Bar(Foo):
  pass


class Test(Bar):
  pass

t=Test()
isinstance(t,Foo) # True
isinstance(t,Bar) # True
issubclass(Test,Foo) # True
issubclass(Test,Bar) # True


