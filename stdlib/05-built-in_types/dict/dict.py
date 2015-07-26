#!/usr/bin/python
'''
'''
d={} # create empty dictionary
e={"cakes":5,"pets":34} # create initialized dictionary

del e["cakes"] # delete dict entry
print "cakes" in e # False
print "pets" in e # True

''' 
dict comprehensions
'''
{x:x+2 for x in [1,2,3]}

'''
ctors
'''

