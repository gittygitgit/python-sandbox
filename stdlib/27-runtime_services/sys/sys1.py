#!/usr/bin/python
import sys

# print args to this script...returns a list, with first arg being the script name
print sys.argv
print sys.argv[0]
print len(sys.argv)

# print the python module search path...initialized using env var PYTHONPATH
print sys.path


