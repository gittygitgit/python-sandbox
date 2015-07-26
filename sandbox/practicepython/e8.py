#!/usr/bin/python
'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''
def newGame():
  another=raw_input("Play again? (Y)es/(N)o")
  return another == 'Y' 

while True:
  p1move=raw_input("Your move (rock, paper, or scissors)?")
  p2move=raw_input("And yours (rock, paper, or scissors)?")
  
  if p1move == "rock":
    if p2move == "rock":
      print "Tie game."
      if not newGame():
        break; 
    elif p2move == "paper":
      print "Paper beats rock.  Player 2 wins!"
      if not newGame():
        break; 
    elif p2move == "scissors":
      print "Rock beats scissors.  Player 1 wins!"
      if not newGame():
        break; 
    else: 
      print "Bad move entered.  Please enter a valid move (rock, paper, or scissors)."
  elif p1move == "paper":
    if p2move == "rock":
      print "Paper beats rock.  Player 2 wins!"
      if not newGame():
        break; 
    elif p2move == "paper":
      print "Tie game.  Try again..."
      if not newGame():
        break; 
    elif p2move == "scissors":
      print "Scissors beats paper.  Player 2 wins!"
      if not newGame():
        break; 
    else: 
      print "Bad move entered.  Please enter a valid move (rock, paper, or scissors)."
  elif p1move == "scissors":
    if p2move == "rock":
      print "Rock beats scissors.  Player 1 wins!"
      if not newGame():
        break; 
    elif p2move == "paper":
      print "Scissors beats paper.  Player 2 wins!"
      if not newGame():
        break; 
    elif p2move == "scissors":
      print "Tie game.  Try again..."
      if not newGame():
        break; 
    else: 
      print "Bad move entered.  Please enter a valid move (rock, paper, or scissors)."
  else:
    print "Bad move entered.  Please enter a valid move (rock, paper, or scissors)."


