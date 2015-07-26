#!/usr/bin/python
'''
Question
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

sentences=[]
while True:
  s=raw_input()

  if s:
    sentences.append(s.upper())
  else:
    break;

for s in sentences:
  print s


