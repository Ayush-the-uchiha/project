# game 0rock 1paper and 2scissor

import random

while True:
  
  # User input
  
  print("\n Press 0 for Rock, Press 1 for Paper and Press 2 for Scissor and Press any number greater than 3 for exit: \n")
  comp = random.randint(0, 2)
  user = int(input("Your choice : "))
  
  def check(comp, user):
    if comp ==user:
      return 0
      
    if(comp == 0 and user ==1):
      return -1
      
    if(comp == 1 and user ==2):
      return -1
      
    if(comp == 2 and user == 0):
      return -1
    return 1

  

  # Assigning return value of check in "score" variable
  score = check(comp, user)

  # Convert user's choice into words.
  def userChoice(user):
      if(user == 0):
          print("Your choice is: Rock")
      if(user == 1):
          print("Your choice is: Paper")
      if(user == 2):
          print("Your choice is: Scissor")
          
      if(user > 2):
          exit()

  # Convert computer's choice into words        
  def computerChoice(comp):
      if(comp == 0):
          print("Computer choice is: Rock")
      if(comp == 1):
          print("Computer choice is: Paper")
      if(comp == 2):
          print("Computer choice is: Scissor")

          
  # Printing both (user and computer) choices
  userChoice(user)
  computerChoice(comp)


  # Score message
  if(score == 0):
    print("Its a draw")
  elif (score == -1):
    print("You Won")
  else:
    print("You Lose")


  # Wons count

  userWon = 0
  compWon = 0

  if(score == -1):
    userWon = userWon + 1
  if(score == 1):
    compWon = compWon + 1
      
  print("userwon = ",userWon)
  print("compwon = ",compWon)


