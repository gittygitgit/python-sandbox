#!/usr/bin/python

"""
What is a lambda?
An expression used to create anonymous functions

Why anonymous functions?
To create an invokable piece of logic without the need for reuse

Can anonymous functions contain statements?
No

What is the difference between a statement and an expression?
Expresssions are a subset of statements
A statement includes everything that can make up a line(s) of code
An expression can only contain identifiers, literals and operators

"""

f=lambda x, y: x + y
print type(f) # function
print f(1,2) # 3
print f("abc","def") # abcdef
