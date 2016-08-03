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
