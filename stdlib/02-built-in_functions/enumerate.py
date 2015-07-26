#!/usr/bin/python
"""
enumerate

enumerate object?
an object that supports iterating over a sequence using the next function.
"""

s="string"
e=enumerate(s)
list(e) # [(0,'s'),(1,'t'),(2,'r'),(3,'i'),(4,'n'),(5,'g')]
list(e) # [] // passing an enumerate obj to list has the side-effect of having next invoked for all items enumerable
e=enumerate(s)
print e.next() # (0,'s')
e=enumerate(s, 2)
print e.next # (2, 's')
