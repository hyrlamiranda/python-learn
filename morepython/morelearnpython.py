#Learning Python

#More exercises Python

#Basics1 - Integers, Floats and maths

x = 5
x = x**x
x #= 3125

g = 5
h = 7
h = g + h
h #= 12

w = 7 % 3
w #= 1

z = 5
z += 2
z #= 7

a = 45
a *= 3
a #= 135

#Basics2 - Strings,Lists, Tuples and Dictionaries

a = str(int(2.23) + float(14)) + "tomatoes"
a #= '16.0 tomatoes'

"ham Ham".upper()
#HAM HAM"

"SUPER Baby".lower()
#'super baby'

b = "I am ham"
b.split()
#['I', 'am', 'ham']

b.split("m")
#['I a', ' ha', '']

b.join(a)
#'1I am ham6I am ham.I am ham0I am hamtI am hamoI am hammI am hamaI am hamtI am hamoI am hameI am hams'

s ="-";
seq = ("a","b","c");
print s.join(seq)
#a-b-c

"int: %d, float %5f" % (14.44, 55.2)
#'int: 14, float 55.200000'

L =[1,6,7,26,8,3,4,5]
L[:]
#[1, 6, 7, 26, 8, 3, 4, 5]
L[:2]
#[1, 6]
L[2:]
#[7, 26, 8, 3, 4, 5]
L[::2]
#[1, 7, 8, 4]
L[1::2]
#[6, 26, 3, 5]

L = [1,2,3]
x = [5,6,L]
x #=[5,6[1,2,3]]

myDict = {14:"Ham", 20: "sandwich"}
myDict.keys() #[20, 14]
myDict.values()#['sandwich', 'Ham']
len(myDict) #2

#Basics3 - Conditionals,if,else,elif

if(7<6) and (4>3):
	print "if"
elif(7>6):
	print "elif"
else:
	print "else"
#elif

if not(6):
	print"yep"
else:
	print "nope"
#nope

if(7)or(3>5):
	print"yep"
else:
	print"nope"
#yep

#Basics4 - Loops

fiboSeq = []
a,b = 0,1
while(b<1000):
	fiboSeq.append(a)
	a,b = b,a +b
print(fiboSeq)
#[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610]

primes = []
for i in range(2,100):
	for x in range(2,i):
        if(i%x ==0):
			 break
	else:
     	primes.append(i)
print(primes)
#[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

factorial = 0
for i in range(30):
	factorial += i 
print factorial
#435 

#Basics5 - Exception Handling

try:
	x = 1.0/0.0
except ZeroDivisionError:
	print("Got it! I'm awesome!")
finally:
	raise TypeError("Just kidding!")
#Got it! I'm awesome!
#Traceback (most recent call last):
#  File "/...", line 6, in <module>
#    raise TypeError("Just kidding!")
#TypeError: Just kidding!

for i in [[1,2,3],[4,5],[6,7]]:
	for j in i:
		if(4<j <=6):
			print(j)
#5
#6

#Basics6

def returnTwo():
	return 20,30
x,y = returnTwo()
print(x,y)
#(20, 30)

def mul(x,y):
	return x*y
##FACTORIAL
print reduce(mul,range(1,11))
#3628800

def cubeFunc(x):
	'''Returns the cube of value passed in.'''
	return x*x*x
print list(map(cubeFunc,range(1,11)))
#[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

def myAdd(var1,var2 = 10):
	return var1 + var2
print(myAdd(7))
print(myAdd(8,5))
#17
#13


