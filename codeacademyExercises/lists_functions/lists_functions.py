#Add the code to print out the second element in the list

n = [1, 3, 5]

#myCode
print  n[1]


#On line 3, multiply the second element of the n list by 5
#Overwrite the second element with that result.
#Make sure to print the list when you are done!
# Code
n[1] = 3 * 5
print n

#Append the number 4 to the end of the list n.
n = [1, 3, 5]
# Append the number 4 here
n.append(4)
print n


# Remove the first item in the list here
n = [1, 3, 5]
#myCode
#n.pop(0) #Another way
#n.remove(0)  #Another way
del(n[0])

print n

#Change the function so the given argument is multiplied by 3 and returned.

number = 5

def my_function(x):
    return x * 3

print my_function(number)

#Define a function called add_function that has 2 parameters x and y and adds them together.

m = 5
n = 13
# Add add_function here!
def add_function(x, y):
    return x + y

print add_function(m, n)

#Write a function called string_function that takes in a string argument (s) 
#and then returns that argument concatenated with the word 'world'.

n = "Hello"
# Your function here! MyCode
def string_function(s):
    return s + "world"

print string_function(n)

#Passing a list to a function

def list_function(x):
    return x

n = [3, 5, 7]
print list_function(n)

#Change line 2 so that list_function returns only the item stored in index one of x, rather than the entire x list.

def list_function(x):
    return x[1]

n = [3, 5, 7]
print list_function(n)