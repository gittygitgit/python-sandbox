#!/usr/bin/python
'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types "exit"
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''
import sys
import random

a=range(1,10)
r=random.choice(a)
tries=0

def playAgain():
  if raw_input("Play again? (Y)es / (N)o").lower() == "y":
    r=random.choice(a)
    global tries
    tries = 0
    return True
  else:
    return False

while True:
  print tries
  guess=input("Guess a number between 1 and 9.")
  tries += 1
  if guess == r:
    print "You guessed correctly.  Number of tries={0}".format(tries)
    if not playAgain():
      sys.exit(1)
  elif guess < r:
    print "Too low."
  else: 
    print "Too high."

