#!/usr/bin/python
"""
max
"""
print max(1,2,3) # 3
print max([1,2,3]) # 3
print max({"one":1,"two":2, "three":3}) # two

print max(1,2,3,key=lambda w: -w) # sorting function provided

