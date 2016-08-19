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

while choice != "y" and choice != "n":  # Fill in the condition (before the colon)
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")