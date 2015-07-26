#!/usr/bin/python
"""
import the math module
"""
import math

# modules, like a number of other types, have a __doc__ attribute
print math.__doc__

# Must precede imported functions with module name
print math.sqrt(18.7) 

# Create an alias for math.sqrt
foo=math.sqrt

# Use alias
print foo(14)
