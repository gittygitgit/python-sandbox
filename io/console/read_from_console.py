#!/usr/bin/python
import sys

'''
read a single character from the console and echo it back

Note: this won't print until user enters enter, which will trigger the subsequent readline() to return.

'''
char=sys.stdin.read(1)
print char

# read a line from console and print it
line=sys.stdin.readline()
print line
