## Python tutorial by Derek Banas 
#Code
#Learn-program(Python)
#####

## import is used to make specialty functions available
# These are called modules
import random
import sys
import os

# Hello world is just one line of code
# print() outputs data to the screen
print("Hello world")

# A variable is a place to store values
# Its name is like a label for that value
name = "Hyrla"
print(name)

# A variable name can contain letters, numbers, or _
# but can't start with a number

# There are 5 data types Numbers, Strings, List, Tuple, Dictionary
# You can store any of them in the same variable
name = 15
print(name)

# The arithmetic operators +, -, *, /, %, **, //
# ** Exponential calculation
# // Floor Division

print("5 + 2 =", 5+2)
print("5 - 2 =", 5-2)
print("5 * 2 =", 5*2)
print("5 / 2 =", 5/2)
print("5 % 2 =", 5%2)
print("5 ** 2 =", 5**2)
print("5 // 2 =", 5//2)

# Order of Operation states * and / is performed before + and -
print("1+2-3*2 =", 1+2-3*2)
print("(1+2-3)*2 =", (1+2-3)*2)

# You can print a string multiple times with *
print('\n' * 2)

# Making quotes: A string is a string of characters surrounded by " or '
# If you must use a " or ' between the same quote escape it with \

quote = "\"Always remember you are unique"

# A multi-line quote
multi_line_quote = '''just like everyone else'''

# To embed a string in output use %s
print("%s %s %s" % ('I like the quote', quote, multi_line_quote))

print('\n' * 2)

# To keep from printing newlines use end=""
print("I don't like ", end="")
print("Beer :p")


# I learned watching video by Derek Banas
