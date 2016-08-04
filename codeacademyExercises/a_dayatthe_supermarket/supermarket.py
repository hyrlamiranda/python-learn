#A Day at the Supermarket

names = ["Adam","Alex","Mariah","Martine","Columbus"]
#loop to print out all of the elements in the list names.
for names in names: 
    print names

#loop to go through the webster dictionary and print out all of the definitions.
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

for key in webster:
    print webster[key]

#Control Flow and Looping
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for entry in a:
   if entry % 2 == 0:
        print entry
   else:
        pass

#function that counts how many times the string "fizz" appears in a list.

#mycode

def fizz_count(x):
    count = 0
    for fizz in x:
        if fizz == "fizz":
            count+=1
    return count

print fizz_count(["fizz","cat","fizz"])

# new dictionary called prices using {}
#mycode
prices = { "banana": 4,"apple": 2,"orange": 1.5,"pear": 3}
#stock dictionary
stock = {"banana": 6, "apple": 0,"orange": 32,"pear": 15}

#Keeping Track of the Produce
for fruits in prices:
    print fruits
    print "price: %s" % prices[fruits]
    print "stock: %s" % stock[fruits]

#Something of Value
total = 0
for fruits in prices:
   total += (stock[fruits] * prices[fruits])
   print total

#list called groceries

groceries = ["banana","orange","apple"]

#mycode, paying for all of the items on your grocery list.
#Making a Purchase
def compute_bill(food):
    total = 0
    for item in food:
        total += prices[item]
    return total

print compute_bill(groceries)

#Stocking Out

#mycode
#groceries = ["banana", "orange","apple"]
#stock = {"banana": 6,"apple": 0,"orange": 32,"pear": 15}
#prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}

def compute_bill(food):
    total = 0
    for item in food:  
        if stock[item] > 0: 
            total += prices[item] 
            stock[item] -= 1
    return total

