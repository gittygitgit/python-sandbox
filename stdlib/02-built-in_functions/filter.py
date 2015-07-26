#!/usr/bin/python
"""
filter
filters an iterable

What's an iterable?
a sequence, a container that supports iteration, or an iterator.

return type?
If filtering a string or tuple, the result is the same type, otherwise, always a list
"""
l=[300,500,900]
print filter(lambda x: x < 600, l) # prints [300, 500]

s="testing"
print filter(lambda a: a != 't', s) # "esing"

t=(1,"abc",55)
print filter(lambda a: a == 55, t) # (55,)

t=(0,244,False,True)
print filter(None, t) # (244, True) // False items are filtered out


