#Write a guessing game where the user has to guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed. I counts only as one 
#try if they input the same number multiple times consecutively.

import random


N = int(input("The computer, please input N:\n"))
print("The computer has produced a number, please guess:\n")
number = random.randint(1, 5)
guess = int(input())
if guess > number:
    print("{0} is Big number.".format(guess))
elif guess < number:
    print("{0} is Small number.".format(guess))