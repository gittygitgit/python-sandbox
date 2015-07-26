#!/usr/bin/python
'''
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''
def factorial(x):
  if x == 0:
    return 1;
  return x * factorial(x - 1);
 
input=raw_input("input: ")

try:
  print factorial(int(input))
except ValueError as ve:
  print "Invalid number provided {0}".format(ve)


