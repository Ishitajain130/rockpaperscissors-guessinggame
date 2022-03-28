import random


a = int(input("What do u want to play?(1, guessing game or 2, rock paper scissors: "))

if(a == 1):

  print("Lets Play Guessing Game!")
  x = random.randint(1,10)
  z = int(input("Guess a number 1-10: "))
  if(z == x):
    print("GREAT JOB!!!")
  else:
    print("too bad")

if(a == 2):
  print("Lets Play Rock, Paper, Scissors!")
  
  d = int(input("What do u pick? 1, Rock, 2, paper, or 3, scissors: "))
  g = random.randint(1,3)
  if(g == 1):
    print("rock")
  if(g == 2):
    print("paper")
  if(g == 3):
    print("scissors")
  if(d == g):
    print("Its a tie")
  if(d == 1):
    if(g == 2):
      print("You lose")
    else:
      print("you win")
  if(d == 2):
    if(g == 3):
      print("You lost")
    else:
      print("you win")
  if(d == 3):
    if(g == 1):
      print("you lost")
    else:
      print("you won")
