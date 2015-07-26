#!/usr/bin/python
"""
int, float, long, complex

booleans are a subtype of int

int has max precision of 32 bits
long has unlimited max precision

integer literals
include binary, hex and octal numbers

binary literal
0b100 => 4

literal modifier
forces a number that would otherwise be considered an int to be treated as a different type
"""

type(0b100) # int
print 0b100 # 4

type(0xf) # int
print (15 == 0xf) # True

print sys.maxint # 2147483647
print type(sys.maxint) # int
print type(sys.maxint + 1) # long

print type(1L) # long
print type(long(1)) # long

# convert float to long
print long(1.1) # 1


