#Change the loop so it counts up to 9 (inclusive).
#Be careful not to change or remove the count += 1 bit—if Python has no way to increase count, your loop could go on forever and become an infinite loop
count = 0
if count < 5:
    print "Hello, I am an if statement and count is", count
    
while count <= 9:
    print "Hello, I am a while and count is", count
    count += 1
# loop checks its condition, and when it stops executing
loop_condition = True

while loop_condition:
    print "I am a loop"
    loop_condition = False

#Create a while loop that prints out all the numbers from 1 to 10 squared (1, 4, 9, 16, ... , 100), each on their own line.
#Fill in the blank space so that our while loop goes from 1 to 10 inclusive.
#Inside the loop, print the value of num squared. The syntax for squaring a number is num ** 2.
#Increment num
num = 1

while num <= 10:  # Fill in the condition
    # Print num squared
    print num ** 2
    # Increment num (make sure to do this!)
    num += 1

#Fill in the loop condition so the user will be prompted for a choice over and over while choice does not equal 'y' and choice does not equal 'n'

choice = raw_input('Enjoying the course? (y/n)')

while choice != "y" and choice != "n":  # Fill in the condition 
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")

#Infinite loops
count = 0

while count < 10: # Add a colon
    print count
    # Increment count
    count += 1

#While / else
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"    

#Use a while loop to let the user keep guessing so long as guesses_left is greater than zero.
#Ask the user for their guess, just like the second example above.
#If they guess correctly, print 'You win!' and break.
#Decrement guesses_left by one.
#Use an else: case after your while loop to print You lose..
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    if guess == random_number:
        print "You win!"
        break
    guesses_left = guesses_left - 1
else:
    print "You lose!"

#Make sure to change the number inside of range
print "Counting..."

for i in range(20):
    print i
    
#Create a for loop that prompts the user for a hobby 3 times, then appends each one to hobbies.
hobbies = []

# my code below!
for i in range(3): 
    hobby = raw_input("What's your hobby?")
    hobbies.append(hobby)
print hobbies    


#Add a second for loop so that each character in word is printed one at a time.
thing = "spam!"

for c in thing:
    print c

word = "eggs!"

# my code here!
for d in word:
    print d

#Do the following for each character in the phrase.
#If char is an 'A' or char is an 'a', print 'X', instead of char. Make sure to include the trailing comma.
#Otherwise (else:), please print char, with the trailing comma.

phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
    if char == "A" or char == "a":
        print "X",
    else: print char,
#Don't delete this print statement!
print 