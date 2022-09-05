# nim.py
# Michael Randazzo
# CSCI 77800 Fall 2022
# collaborators: None
# consulted: ThinkJava

import random

stones = 12
print("Lets Play the Game of Nim!")
print( "There are", stones, "stones.")

while stones >=0:
  #user turn
  user_num = input("Pick a number from 1 to 3: ")
  #convert input to an int
  user_num_int = int(user_num)
  stones = stones - user_num_int
  print("There are", stones, "stones left")
  #check for win
  if stones <= 0:
    print("You Won!!")
    break

  #computer turn
  com_num = random.randrange(1,4)
  if stones < 4:
    com_num = stones
  print("The computer took", com_num)
  stones = stones - com_num
  print("There are", stones, "stones left")
  if stones <= 0:
    print("The Computer Won")
    break
  