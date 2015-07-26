#!/usr/bin/python
"""
map

Applies a function to every item in an iterable, returning a list

"""

print map(lambda x: x+2, [1,2,3]) # [3,4,5]
print map(lambda x, y: x+y, [1,2,3], [5,6,7]) # [6, 8, 10]

