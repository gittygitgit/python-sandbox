#!/usr/bin/python

"""
What sequence types are mutable?
bytearray and List
"""
ba=bytearray(10) # new bytearray having size 10, each position initialized to null
l=range(0,10) # new list initialized with ints 1 through 10

"""
all the following operations are valid for both bytearray and list
"""

print len(l) # prints 10
l[0]=100
l[0:3]='s' # replace the first 3 el's with a single 's'
print len(l) # prints 8
del l[4:5]
print len(l) # prints 7
l[0:10:2]=('x','y','z','s')
print len(l) # prints 7
l.append("hello")
print len(l) # prints 8
l.extend(range(1,5))
print len(l) # prints 12
l.extend(("one","two"))
print len(l) # prints 14
l.count('s') # 1
l.append('s')
print l.index('s',1) # 6
print l.index('s',1,8) # 6
print l.index('s',7,20) # 14
l.insert(3,"idx3")
print len(l) # 16
print l.pop(3) # 'idx3'
print len(l) # 15 
print l.index('s') # 6
print l.index('s', 7) # 14
print l.index('s') # 6
print l.index('s', 7) # 14
l.remove('s') # removes 's' at index 6
print l.index('s') # 13
l.remove('s') # removes 's' at index 13
print len(l) # 13

l=range(0,10) # doesn't include 10
print l[0] # 0
l.reverse()
print l[0] # 9
l=[1,2,7,4,5]
print l.sort() # [1,2,4,5,7]



