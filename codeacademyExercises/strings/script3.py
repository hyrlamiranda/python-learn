#Create a new variable brian and assign it the string "Hello life!".
brian = "Hello life!"

# Assign your variables below, each on its own line!
caesar = "Graham"
praline = "John"
viking = "Teresa"

# Put your variables above this line
print caesar
print praline
print viking

# The string below is broken. Fix it using the escape backslash!
print 'This isn\'t flying, this is falling with style!'

"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = "MONTY"[4]
print fifth_letter

#On line 1, create a variable named parrot and set it to the string "Norwegian Blue". On line 2, type len(parrot) after the word print, like so: print len(parrot).
#The output will be the number of letters in "Norwegian Blue"!
parrot = "Norwegian Blue"
len(parrot)
print 
print len(parrot)


#Call lower() on parrot (after print) on line 3 in the editor.
parrot = "Norwegian Blue"

print parrot.lower()

#Call upper() on parrot (after print on line 3) in order to capitalize all the characters in the string!
parrot = "norwegian blue"
print parrot.upper()

#Create a variable pi and set it to 3.14 on line 4. Call str(pi) on line 5, after print.
"""Declare and assign your variable on line 4,
then call your method on line 5!"""

pi = 3.14
print str(pi)

#On line 3, call the len() function with the argument ministry. On line 4, invoke the ministry's .upper() function.
ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()

#Print "Monty Python" to the console.
"""Tell Python to print "Monty Python"
to the console on line 4!"""

print "Monty Python"

#Declare a variable called the_machine_goes and assign it the string value "Ping!" on line 5.
#Go ahead and print the_machine_goes in line 6.
"""Assign the string "Ping!" to
the variable the_machine_goes on
line 5, then print it out on line 6!"""

the_machine_goes = "Ping!"
print the_machine_goes

#Let's give it a try. Print the concatenated strings "Spam ", "and ", "eggs" on line 3, just like the example above.
#Make sure you include the spaces after "Spam " and "and ".
print "Spam " + "and " + "eggs"

#Run the code as-is. You get an error!
#Use str() to turn 3.14 into a string. Then run the code again.
print "The value of pi is around " + str(3.14) 

#String Formatting with %, Part 1
string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

#String Formatting with %, Part 2
name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

#create the variable my_string and set it to any string you'd like.
#print the length of my_string.
#print the .upper() case version of my_string.
my_string = "Hyrla"
print len(my_string)
print "Hyrla".upper()