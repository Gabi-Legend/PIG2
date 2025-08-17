# Choose the number of players (2 to 4) and roll the dice.
# If a player rolls 1, they lose automatically and their score resets to 0.
# The player with the highest score can choose to stay or roll again.
# The last player who has not rolled a 1 wins.

import random
import time

playersCount = int(input("How many players do you want to play?(2-4): "))

if playersCount < 2 or playersCount > 4:
    playersCount = int(input("Chosee a number between 2 and 4, 2 and 4 included! "))

player1 = 0
player2 = 0
if playersCount == 3:
    player3 = 0
elif playersCount == 4:
    player4=0

while playersCount>1:
    pass
