'''The Snake Water Gun game is a popular simple game, often played in a similar style to Rock, Paper, Scissors. It's a hand-based game where each player has three choices: Snake, Water, and Gun. The game is typically played between two players, and the rules are as follows:

Rules:
Snake beats Water (Snake drinks the water).
Water beats Gun (Water douses the gun).
Gun beats Snake (Gun shoots the snake).
The players simultaneously choose one of the three options (Snake, Water, or Gun), and the winner is determined by the rules above.'''

# -1 for snake
# 1 for water
# 0 for Gun

import random
from typing import Dict 
computer = random.randint(-1,2)

youStr = input("Enter your choice :")
choice = {"s":-1 , "w":1 , "g":0}
reverseDict = {-1 :"Snake " ,1:"water",0:"Gun"}
you = choice[youStr]
print("Computer Chose {}".format(reverseDict[computer]))
print("You Chose {}".format(reverseDict[you]))

if computer== -1 and you == -1: 
    print("Its a tie")
elif computer== 1 and you == 1: 
    print("Its a tie")
elif computer== 0 and you == 0: 
    print("Its a tie")
elif computer== -1 and you ==  1:
    print("Computer wins")
elif computer== -1 and you ==  0:
    print("You won")
elif computer== 1 and you ==  -1:
    print("You won")
elif computer== 1 and you ==  0:
    print("Computer wins")
elif computer== 0 and you ==  -1:
    print("You win")
elif computer== 0 and you ==  1:
    print("You win")
else:
    print("Something went wrong")






