#!/usr/bin/python

# returns true if all elements of an iterable are True, or if the iterable is empty
print all([]) # false
print all([1, True]) # True
print all([0, True]) # False
print all([1, True, None]) # False

