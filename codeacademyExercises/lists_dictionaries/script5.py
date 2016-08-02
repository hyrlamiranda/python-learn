#The list zoo_animals has three items (check them out on line 1). Go ahead and add a fourth! Just enter the name of your favorite 
#animal (as a "string") on line 1, after the final comma but before the closing ].


zoo_animals = ["pangolin", "cassowary", "sloth","turtle" ];
# One animal is missing!#Mycode
if len(zoo_animals) > 3:
	print "The first animal at the zoo is the " + zoo_animals[0]
	print "The second animal at the zoo is the " + zoo_animals[1]
	print "The third animal at the zoo is the " + zoo_animals[2]
	print "The fourth animal at the zoo is the " + zoo_animals[3]

#Write a statement that prints the result of adding the second and fourth items of the list. Make sure to access the list by index!
numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
print numbers[1] + numbers[3]

#Write an assignment statement that will replace the item that currently holds the value "tiger" with another animal (as a string). It can be any animal you like.
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked 
#the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"
# What shall fill the void left by our dear departed tiger?
zoo_animals[3] = "Cat"

#On lines 5, 6, and 7, append three more items to the suitcase list, just like the second line of the example above. (Maybe bring a bathing suit?)
#Then, set list_length equal to the length of the suitcase list.

suitcase = [] 
suitcase.append("sunglasses")

#Mycode
suitcase = [] 
suitcase.append("Dresses")
suitcase.append("underwear")
suitcase.append("Boots")
suitcase.append("Shoes")

list_length = len(suitcase)

print "There are " + str(list_length) + " items in the suitcase."
print suitcase

#On line 4, create a list called middle containing only the two middle items from suitcase.
#On line 5, create a list called last made up only of the last two items from suitcase.

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]              # Third and fourth items (index two and three)
last   = suitcase[4:6]          # The last two items (index four and five)

#Assign to dog a slice of animals from index 3 up until but not including index 6.
#Assign to frog a slice of animals from index 6 until the end of the string.
animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]             # The fourth through sixth characters
frog = animals[6:10]    # From the seventh character to the end

#Use the .index(item) function to find the index of "duck". Assign that result to a variable called duck_index.
#Then .insert(index, item) the string "cobra" at that index.

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")   # Use index() to find "duck"

animals.insert(duck_index,"cobra")
print animals # Observe what prints after the insert operation

#Write a statement in the indented part of the for-loop that prints a number equal to 2 * number for every list item.

my_list = [1,9,3,8,5,7]

for number in my_list:
    #Mycode
    print 2 * number
  
#Write a for-loop that iterates over start_list and .append()s each number squared (x ** 2) to square_list.
#Then sort square_list!
start_list = [5, 3, 1, 2, 4]
square_list = []

#Mycode
for start in start_list:
    square_list.append(start ** 2)
    
square_list.sort()
print square_list

#Print the values stored under the 'Sloth' and 'Burmese Python' keys. Accessing dictionary values by key is just like accessing list values by index:
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

#Mycode
print residents ['Sloth']
print residents['Burmese Python']

#Add at least three more key-value pairs to the menu variable, with the dish name (as a "string") for the key and the price (a float or integer) as the value.

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
#mycode
menu['Spam'] = 2.50
menu['Eggs'] = 4.00
menu['Bananas'] = 5.00

print "There are " + str(len(menu)) + " items on the menu."
print menu


#Delete the 'Sloth' and 'Bengal Tiger' items from zoo_animals using del.
#Set the value associated with 'Rockhopper Penguin' to anything other than 'Arctic Exhibit'.

# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

#Mycode!
del zoo_animals["Sloth"]
del zoo_animals["Bengal Tiger"]
zoo_animals["Rockhopper Penguin"] = 'Other place'

print zoo_animals

#Remove 'dagger' from the list of items stored in the backpack variable.

backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove("dagger")

#1.Add a key to inventory called 'pocket'
#2.Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'
#3.sort() the items in the list stored under the 'backpack' key
#4.Then .remove('dagger') from the list of items stored under the 'backpack' key
#5.Add 50 to the number stored under the 'gold' key

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

#mycode 
#Steps 1 and 2
inventory["pocket"] = ["seashell","strange berry", "lint"]
#Step 3
inventory["backpack"].sort()
#Steps 4 and 5
inventory['backpack'].remove('dagger')
inventory['gold'] += 50
print inventory

