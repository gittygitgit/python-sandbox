#!/usr/bin/python
import sys
'''
This will only work if input is being piped.
To print lines from terminal input, use raw_input
'''
def foo(l):
  print l

for line in sys.stdin:
  foo(line)


