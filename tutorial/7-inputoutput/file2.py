#!/usr/bin/python

with open("entries.txt") as f:
  a=f.readlines()
  for l in a:
    print l.rstrip('\n')
