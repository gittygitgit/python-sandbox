#!/usr/bin/python
from foo import Foo
from bar import Bar

class Cat(Bar):
   test="sdfsdf"

 
class Dog(Foo,Bar):
  xyz="aaaaa"

# we can refer to Foo without the prefix since we imported it explicitly
print Foo

# prints all class variables
print Foo.__dict__

# print the module the class is defined in
print Foo.__module__

# print parent classes... only prints immediate parents
print Foo.__bases__

# print parent classes
print Cat.__bases__
print Dog.__bases__






