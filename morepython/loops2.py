## Python tutorial by Derek Banas 
#Code
#Learn-program(Python)
#####

import random
import os
import sys

# WHILE LOOPS -------------
# While loops are used when you don't know ahead of time how many
# times you'll have to loop
random_num = random.randrange(0, 100)

while (random_num != 15):
    print(random_num)
    random_num = random.randrange(0, 100)

# An iterator for a while loop is defined before the loop
i = 0;
while (i <= 20):
    if (i % 2 == 0):
        print(i)
    elif (i == 9):
        # Forces the loop to end all together
        break
    else:
        # Shorthand for i = i + 1
        i += 1
        # Skips to the next iteration of the loop
        continue

    i += 1