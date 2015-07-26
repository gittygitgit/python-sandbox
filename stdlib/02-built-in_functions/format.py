#!/usr/bin/python
"""
format
"""

format("left", "-<20") # right fill with -'s
format("right", "+>20") # left fill with +'s
format("center", "=^20") # fill with ='s

format(1000000, ',') # comma separator
format(23432, '+') # prefix positive numbers with + sign
format(2324234, ' ') # prefix positive numbers with space, negatives with a minus sign

