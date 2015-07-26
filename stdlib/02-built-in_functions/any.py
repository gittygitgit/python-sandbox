#!/usr/bin/python

""
any
Returns true if any items in an iterable are true, or false if the iterable is empty
"""

print any('') # False
print any([0,0,0]) # False
print any({'':"hello"}) # False
print any([0,2,0]) # True
print any({}) # False
print any({1:None}) # True

