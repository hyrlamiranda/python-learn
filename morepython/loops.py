## Python tutorial by Derek Banas 
#Code
#Learn-program(Python)
#####



# FOR LOOPS
# Allows you to perform an action a set number of times
# Range performs the action 10 times 0 - 9

import random
import os
import sys

for x in range(0, 10):
    print(x, ' ', end="")

print('\n')

grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']

for y in grocery_list:
    print(y)

for x in [2, 4, 6, 8, 10]:
    print(x)

print('\n')

num_list = [[1,2,3],[10,20,30],[100,200,300]]

for x in range(0,3):
    for y in range (0,3):
        print(num_list[x][y])
