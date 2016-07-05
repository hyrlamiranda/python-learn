#Write a guessing game where the user has to guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed. I counts only as one 
#try if they input the same number multiple times consecutively.

import random


N = int(input("The computer, please input N:\n"))
print("The computer has produced a number, please guess:\n")
number = random.randint(1, N)
total = 0
last_guess = 0

while True:
    guess = int(input())
    if last_guess != guess:
        last_guess = guess
        total += 1
    if guess < number:
        print("Small, please guess again.")
    elif guess > number:
        print("Big, please guess again.")
    else:
        print("After {0} guesses, Congratulations, you are right!!Finally!!".format(total))
        break
