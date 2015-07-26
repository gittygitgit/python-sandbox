#!/usr/bin/python
"""
hash

numeric types that compare equal must have the same hash
"""
s="testing"
s1="testing"

print s == s1 # prints True
print hash(s) == hash(s1) # prints True

