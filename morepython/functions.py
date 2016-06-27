## Python tutorial by Derek Banas 
#Code
#Learn-program(Python)
#####

# FUNCTIONS
# Functions allow you to reuse and write readable code
# Type def (define), function name and parameters it receives
# return is used to return something to the caller of the function

import random
import os
import sys

def addNumbers(fNum,sNum):
    sumNum = fNum + sNum
    return sumNum

print(addNumbers(1,4))

# Can't get the value of rNum because it was created in a function
# It is said to be out of scope
# print(sumNum)

# If you define a variable outside of the function it works every place
newNum = 0;
def subNumbers(fNum, sNum):
    newNum = fNum - sNum
    return newNum

print(subNumbers(1,4))

#USER INPUT
print('What is your name?')

#Stores everything typed up until ENTER
name = sys.stdin.readline()

print('Hello', name)

#STRINGS
# A STRING is a series of characters surrounded by ' or "
long_string = "I'll catch you if you fall - The Floor"

#Retrieve the first 4 characters
print(long_string[0:4])

#Get the last 5 characters
print(long_string[-5:])

# Everything up to the last 5 characters
print(long_string[:-5])

# Concatenate part of a string to another
print(long_string[:4] + " be there")

# String formatting
print("%c is my %s letter and my number %d number is %.5f" % ('X', 'favorite', 1, .14))

# Capitalizes the first letter
print(long_string.capitalize())

# Returns the index of the start of the string
# case sensitive
print(long_string.find("Floor"))

# Returns true if all characters are letters ' isn't a letter
print(long_string.isalpha())

# Returns true if all characters are numbers
print(long_string.isalnum())

# Returns the string length
print(len(long_string))

# Replace the first word with the second (Add a number to replace more)
print(long_string.replace("Floor", "Ground"))

# Remove white space from front and end
print(long_string.strip())

# Split a string into a list based on the delimiter you provide
quote_list = long_string.split(" ")
print(quote_list)
