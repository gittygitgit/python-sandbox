#!/usr/bin/python
 
# A set is an unordered list of immutable items containing no duplicates
# Sets are created from lists
s=set([1,2,2,3,3,3,4])
print "Set {} contains {} elements.".format(s, len(s))

# Test if set contains item
print "Does set contain 5? {}".format(5 in s)

# Test if set contains item
print "Does set contain 3? {}".format(3 in s)

# contains common container operations
for i in s:
  print i

s1={1,2,3,4}
s2={3,4,5}
s3={2,3}
s4={1,2,3,4,5}
print s1.isdisjoint(s2) # False
print s1.issubset(s2) # False
print s1.issubset(s4) # True
print "Is every element in s1 in s4? " + str(s1 <= s4) # True
print "Is s1 a proper subset of s4? " + str(s1 < s4) # True
print "Is s1 a proper subset of s1? " + str(s1 < s1) # False
print "Is s4 a superset of s1?" + str(s4.issuperset(s1)) # True
print "s1 union s2: " + str(s1.union(s2))
print "s1 intersection s2: " + str(s1.intersection(s2))
print "s1.difference(s2): " + str(s1.difference(s2))


