#!/usr/bin/python
'''
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
'''

v=range(2000,3201)

l=[]  

for i in v:
  if i % 7 == 0 && i % 5 != 0:
    result.append(str(i));

print ",".join(l)  

