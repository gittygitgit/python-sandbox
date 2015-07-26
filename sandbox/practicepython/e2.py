#!/usr/bin/python
'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
'''
n=input("Enter a number:")
isOdd=n % 2
if isOdd:
  print "Number is odd."
else:
  print "Number is even."
