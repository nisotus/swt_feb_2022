# To create a basic dice game where two users will row a pair of dice to see who wins.

import random                                           #step2

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total
    
#main program

player1 = input("Enter player 1's name: ")              #step1
player2 = input("Enter player2's name: ")

#Time for the player to row the dice

roll1 = roll_dice()                                     #step3
roll2 = roll_dice()

print(player1, "rolled", roll1 )                        #step4
print(player2, "rolled", roll2)

if roll1 > roll2:                                       #step5
    print(player1, "wins")
elif roll2 > roll1:
    print(player2, "wins")
else:
    print("You tie!")
    

    



