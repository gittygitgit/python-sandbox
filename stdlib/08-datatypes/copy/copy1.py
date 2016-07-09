#!/usr/bin/python

import copy

'''
Copy is useful for creating copies of mutable objs.
'''

# given a dict
d={1:[1,2,3], 2:[5,6,7]}

# shallow copy
d2=copy.copy(d)
d[1].append(5)
isShallow=len(d2[1]) == 4
if isShallow:
  print "copy results in a new object that still references objects in the original"


d3=copy.deepcopy(d)
d[1].append(23)
isDeep=len(d3[1]) == 4
if isDeep:
  print "deepcopy results in a new object completely separate from the original"

