#Lists:
#Lists are a datatype(tipos de variaveis ou dados) you can use to store a collection of different pieces of information as a sequence under a single variable name. (Datatypes you've already learned about include strings, numbers, and booleans.)

#Dictionary:
#A dictionary is similar to a list, but you access values by looking up a key instead of an index. A key can be any string or number. 

#What is python?
#Flexible language.
#
#Variables
#Containers for data
Var = 5
#(name) (value)
#
#Naming
bigFoot = 4
#(Lowercase) (Uppercase,no spaces)
#
#Math
# +add
# -subtract
# * multiply
# /Divide
# ()parenthesis
# **power
# %remainder

#Other functions

# abs() absolute value
# sin() Sin of
# cos()Cosine of
# floor() = round down
#ceil() round up
# pow() power(aka **)
# and more…
#
#Strings = Bunch of characters and they could be letters of the alphabet numbers that could be characters like! or ampersand sign.
#“Pe or % “Payne”

#Example:
x = ‘ham’
y= x+” book”
y
'ham' book

#
#Strings: SPECIAL CHARACTERS
#Placing number values within strings

“%d” %NUM = substitute INTEGER
z=10
y = "something %d” %z
“%f" %NUM = Substitute FLOAT
z=10
y = "something %f” %z
“%.3.f” %NUM = substitute CUT OFF FLOAT

z=10
y = "something %3.f” %z

#
#MORE SPECIAL CHARACTERS
“\n” = newline character ( Enter key)
print(“test\n\ntest”)

“\t” = TAB character(tab key)
print(“test\t\t test”)

#
#Keyword ‘IN’
#Used to check if a value is within another value
#example: “Ham” in “hamsandwich”
#

#Lists
#Data Structure used for storing all data TYPES; INT FLOAT, STRING ETC

x = [“ham,4,2.2]

#LISTS: FUNCTIONS
#append(VALUE)
#Adds value to end of list

x = [“ham,4,2.2]
x.append(5)
Resultado : [‘ham’, 4,2.2,5]

insert(Location, VALUE):
insert value at a location
x= [“ham”, 4, 2.2,5 ]
x.insert(1,3.1415

pop(location):
Remove and return the value at the location

x = [“ham”,3.1425,4,2.2,5]
x.pop(1)

OTHER FUNCTIONS

len(string or list):
returns the total number of items within a string or list, short for length

x =[ “ham, 4, 2.2,5 ]
len(x)

list(item):
Converts item to a list

list(“ham”)

MORE ‘IN’ STUFFS
is it ‘in’ there?

y = [“ham”]
“s” in y

#
#TUPLES
#Just like lists but 
#UNADJUSTABLE

x= ()
x = (“ham”,4,5)

#Its grocery lists but they have a no-return policy in other words they cannot be adjusted once they are created. They’re pretty fixed. 
#How do you declare them just like you would create list x equals but instead of using brackets use parentheses.

#TUPLES VS. LISTS
#TUPLES: More memory, efficient, cannot be adjusted
#LISTS: Takes more memory, adjustable

#
#DICTIONARIES
#(Aka Hashtable,map)
#used for binding KEYS TO VALUES

#Just like a phone book! or Address book

#Dictionary example
sam ={}
sam[“weapon”] = “chainsaw" 
sam [“health" ] = 10

dictionary[key]: GET and SET the value
del dict[Key]: DELETE a value/key pair

sam[“weapon"]
del sam[“health”]

##
#CONDITIONALS
#A WAY TO CHECK FOR Some something:

#hero enters new area
#health below zero
#food visible(eat!)

#“IF”
if(condition is true):
	do this!

#Example: Mail
if( we have mail):
	grab mail
else:
cry… :,(

“ELSE” :  Catches everything that does NOT meet prior conditionals

if(…):
…
else:
…….

#“ELIF” = ELSE IF
#Comes AFTER “IF” statement 
#Sets up another conditional

if(…):
…..
elif(…):
else:
…..

#“ELIF”
if(breathing):
	He’s alive!!!
elif(walking):
	He’s a Zombie!!
else:
	He’s dead…
TAB = IMPORTANT!!

#Python super sensitive to spacing
#Maintain consistent spacing in script or program, otherwise you will have problems

#“IF” EXAMPLE

mail =5
if mail:
	print”mail time!”

#“IF””ELSE”
mail = 0
if mail:
	print”mail time!”
else:
	print”no mail :(“

#
#Comparison OPERATORS

#Ways to compare two values:
#is the value..
# < LESS THAN?
# <= LESS THAN OR EQUAL TO?
# > GREATER THAN?
# >= GREATER THAN OR EQUAL TO?
# == EQUAL TO?
# != NOT EQUAL TO?

#
#PARENTHESES()
#Keeps your code clean!!!
#Use them to ENCLOSE conditionals

if(5<4):

#example
if (4<6):
	print “ham sandwich”
#
#“AND”
#Combines two conditionals
#only true if BOTH conditions are met!
#Example
if(7) and (6):
	print “yep”
#“OR”
#Combines two conditionals
#True if EITHER conditions are met!
#“AND” EXAMPLE #2

if(0) and (4)
	print “wahaaa"

#
#LOOPS
#Way to read actions over and over!

#4+4+4+…
#with less code!

#FUNCTIONS
#Combine many actions in a single process

#“WHILE” LOOP
#while(condition is true):
#	do this over and over

#example
x= 0 
while( x < 10):
	x+= 1

#“BREAK LOOP
#Used to stop loop

while(true):
	if (something):
break

example:
x,y=0,0
while(True):
	x+=1
	y+=2
	if(x+y>10):
		break

#“FOR” LOOPS
#For each item in list/range,loop!

X= [1,2,7]
for i in x:
	print i
#
#RANGE
#Creates a list of sequencial numbers

for i in range(30):
	print i

for i in range(10,30,2):
	print i

#start loop over(on next value, if in for loo)

for i in range(3):
	if not (i % 3):
		continue
	print i

#
#EXCEPTION HANDLING

#Prevents codes and scripts from Breaking!
#Can be used for handling user inputs

#TRY
#"try" to execute the code below...
#May be used anywhere that keyboarduser input is required

#EXCEPT
#catches all errors or can just catch a specific error
#May be used anywhere that keyboarduser input required

#BREAK THE CODE! X = 5 "ham"

#try example

try:
	x = 5 + "ham"
except:
	print "darn it"

#PASS
#SAYS to IGNORE and move on
#may be used in FOR,While, Try/Except instances

try:
	x = 5 + "ham"
except:
	pass

#RAISE

#force and error to occur
#raise TypeError("haha")

#FINALLY

#LAST ACTIONS to perform following "try" and "except"
#Occurs before any real errors are returned

try:
	x= 5 + "ham"
except ZeroDivision:
	print "will not see this"
finally:
	print "the final word"

#
#FUNCTIONS way to combine may ations into a single process, for reuse later.
#'define' = def /or declare a function
#() INPUT:arguments passed in here
#pass is your main code here

def doesNothing():
	pass 

doesNothing() #call your function

#RETURN a way to OUTPUT or return data from a function

def makeOne():
	return 1

x = makeOne()
print x

#ARGUMENTS A way to INPUT or pass in data to a function
#INPUT(ARGUMENTS)GAS OUTPUT(RETURN)DRIVE

#argument types

def myFunc(var1, var2 = 3):

	#Regular Argument var 1
	#Keyword Argument var 2
	# = Keyword args set DEFAULT value that MAY be overridden

#ARGUMENT EXAMPLE

def addTen(myInt):
	myInt += 10
	return myInt
x = 12
dir()
y= addTen(x)
print x,y
#12 22

#LOCAL VS GLOBAL VARIABLES. LOCAL: Variables created and stored WITHIN a function that will be deleted from memory when the function COMPLETES

def myFunc():
	localVar = 5
#GLOBAL variable that accessable ANYWHERE within program
#USES keyword 'global'

glVar = 5
def myFunc():
	global glVar


#COMMENTS AND DOCUMENTING

#Not necessary for code to run.
#Primarily used for debugging, and breaking down code for other programmers

#DOCUMENT STRING - Text DESCRIBING the function
# Comes immediately after function creation
#USE triple quotes to enclose

#def myfunc():
#	'"My description"'

#COMMENTS
#Tell program to IGNORE everything afterward in line
#declared with '#' pund/sharp symbol
#Frequently used to write notes or 'ignore' bits of code

#comment1
#x = 5 #2
#3

#COMMENT EXAMPLE

#def myFunc():
#	'"I documented something"' #document string
	#Only seen in code view, ignored #comment
	#pass
print myFunc._doc_