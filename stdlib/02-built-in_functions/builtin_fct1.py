#!/usr/bin/python

print abs(-123) # 123

# args to all and any are iterables
l=[1,2,3,4,5]
print all(l) # True
l=[0,2,3]
print all(l) # False

l=[0,0,None]
print any(l) # False

l=[0,None,1]
print any(l) # True


print globals() # print current global symbol table
