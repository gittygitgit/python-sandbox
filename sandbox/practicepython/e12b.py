#!/usr/bin/python
'''
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
'''
l = [5,10,15,20,25]

r=[v for i,v in enumerate(l) if i == 0 or i == len(l) - 1]

print r

