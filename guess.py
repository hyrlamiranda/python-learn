import random


N = int(input("The computer, please input N:\n"))
print("The computer has produced a number, please guess:\n")
number = random.randint(1, 5)
guess = int(input())
if guess > number:
    print("{0} is Big number.".format(guess))
elif guess < number:
    print("{0} is Small number.".format(guess))