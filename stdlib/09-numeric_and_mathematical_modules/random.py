#!/usr/bin/python
import random

print random.randint(1,10) # random int between 1 and 10
print random.choice([1,4,6,8,10,22]) # choose random one of given sequence
a=[1,2,3,4,5]
random.shuffle(a) # shuffles given sequence
print a


