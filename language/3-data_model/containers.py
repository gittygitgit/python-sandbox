#!/usr/bin/python

# Contain references to other objects
# tuples, lists, dictionaries, string

# A container's value is defined by it's contained values

# Containers have certain behaviors in common.
# To implement a container-type, one should implement certain well-known methods such as:
#   __len__(self) 		- called by built-in len() fct
#   __getitem__(self,key)       - called to resolve self[ley] expressions
#   ...many more
#   ...

s=set([1,2,3,4])
for i in s:
  print i

if 4 in s:
  print "4 is here"

if 8 in s:
  print "8 is here"

if 8 not in s:
  print "8 is missing"

print len(s)

# brace syntax
s={1,2,3,5}

t={2,55,6}


