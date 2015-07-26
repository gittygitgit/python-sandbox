#!/usr/bin/python
"""
global
"""

foo="bar" # a global variable

print "foo" in globals() # True

# A function's global namespace is the global namespace of the module in which it is defind.
def test():
  print "foo" in globals() # True

# If a global variable is referred to in a function, a local variable of the same name cannot be created.
def test2():
  try:
    print foo # foo is found in the global namespace
    foo="hello" # Can't
  except UnboundLocalError as e:
    print "Can\'t create / assign a local variable if a global var of the same name is referenced already"

test2() # exception caught

def test3():
  foo="local" # this is a local variable and shadows the global foo
  print foo # prints local, but will be forgotten when the function exits

test3() # prints local
print foo # prints "bar"

def test4():
  global foo
  foo="global"
  print foo # global

test4() # prints global
print foo # prints global

def test5():
  global foo
  print foo # prints global
  del foo # deletes foo
  try:
    print foo # error
  except NameError as ne:
    print "foo doesn't exist anymore"

test5()
try:
  print foo # error
except NameError as ne:
  print" foo doesn't exist anymore"
