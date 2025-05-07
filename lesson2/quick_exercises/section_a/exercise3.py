"""
Create a Python while loop that rolls two dice. The script should keep rolling the dice
until "snake eyes" are rolled (both dice have a value of 1). Keep track of how many dice
rolls are required. Additionally print out each dice roll. Once you have rolled "snake eyes"
your program should break out of the while loop. You can create two dice using the following
code:
"""

import random

print()
rolls = 0
while True:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    rolls += 1

    print(f"Dice roll{rolls}: {dice1} {dice2}")
    if dice1 == 1 and dice2 == 1:
        print(f"\n\nFinally 'snake eyes', total rolls: {rolls}\n")
        break
