#!/usr/bin/python

# is there an Object class that everything extends from?
# yes

# how do you get a handle to the Object class?
print object

# object has no baseclasses
print object.__bases__ # returns empty tuple ()

# difference between a type and a base...
# each object has a single type...it's type
print type("test") # type string

# a base is like a superclass
print type("sdsdf").__bases__
print type(type("sdfsdf")).__bases__

# type returns an instance's __class__ attribute
print isinstance("sdfsdf",str)

# what's the difference between type and object?
# both are primitive objects
# every object has a __class__ attribute
# every type object has a __bases__ attribute

# test if str is a subclass of object
issubclass(str,object) # true if str extends object directly or one of it's baseclasses extends object

# identity operator
a="one"
b=a
print "id(a): " + id(a) + ", id(b):" + id(b)
print a is b # prints True

c="two"
print a is c # prints False





# 
# stuff provided by object



