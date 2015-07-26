#!/usr/bin/python
"""
bytearray

What is a bytearray?
A mutable sequence of integers with each integer in the range 0 <= x < 256

How is source data encoded?
Using the indicated encoding, or the default one if none given
"""

ba = bytearray() # empty bytearray
ba = bytearray("abc") # three element bytearray, with each element being the encoded representation of each character in the given string.
ba = bytearray(5) # an array of len 5


