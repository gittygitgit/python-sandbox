#!/usr/bin/python
'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. If you dont know what a divisor is it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.
'''
n=input("Enter a number.")

l=[x for x in range(1,n + 1) if not n % x]
print l
