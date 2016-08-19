#Project I will build a simplified, one-player version of the classic board game Battleship
#Use range() to loop 5 times.
#Inside the loop, .append() a list containing 5 "O"s to board, just like in the example above.
#Note that these are capital letter "O" and not zeros.
board = []
for i in range(5):
    board.append(["O"] * 5) 
print board

#First, delete your existing print statement.
#Then, define a function named print_board with a single argument, board.
#Inside the function, write a for loop to iterates through each row in board and print it to the screen.
#Call your function with board to make sure it works.
board = []
# range(5) is a shortcut for range(0, 5)
for i in range(5):
    board.append(["O"] * 5) 
def print_board(board):
    for row in board:
        print row
print print_board(board)

#Inside your function, inside your for loop, use " " as the separator to .join the elements of each row.

board = []
# range(5) is a shortcut for range(0, 5)
for i in range(5):
    board.append(["O"] * 5) 
def print_board(board):
    for row in board:
        #mycode
        print " ".join(row)
print print_board(board)

#Define two new functions, random_row and random_col, that each take board as input.
#These functions should return a random row index and a random column index from your board, respectively. Use randint(0, len(board) - 1).
#Call each function on board.

from random import randint 

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

# Add your code below!My code
def random_row(board):
    return randint(0, len(board)-1)
def random_col(board):
    return randint(0, len(board[0])-1)
    
print random_row(board)
print random_col(board)

#Create a new variable called guess_row and set it to int(raw_input("Guess Row: ")).
#Create a new variable called guess_col and set it to int(raw_input("Guess Col: ")).
# Add your code below!my code
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))


#Here I am printing statement that displays the location of the hidden ship
print ship_col
print ship_row

#On line 29, add an if guess_row equals ship_row and guess_col equals ship_col.
#If that is the case, please print out "Congratulations! You sank my battleship!"
# Write your code below!My code
if  guess_row == ship_row and guess_col == ship_col:
    print " Congratulations! You sank my battleship!"
#Add an else under the if we wrote in the previous step.
#Print out "You missed my battleship!"
#Set the list element at guess_row, guess_col to "X".
#As the last line in your else statement, call print_board(board) again so you can see the "X".
#Make sure to enter a col and row that is on the board!
else: 
    print "You missed my battleship!"
    board[int(guess_row)][int(guess_col)] = "X"
    print_board(board

#Add a new if: statement that is nested under the else.
#Like the example above, it should check if guess_row is not in range(5) or guess_col is not in range(5).
#If that is the case, print out "Oops, that's not even in the ocean."
#After your new if: statement, add an else: that contains your existing handler for an incorrect guess. Don't forget to indent the code!

if guess_row not in range(5) or \
   guess_col not in range(5):
        print "Oops, that's not even in the ocean."
#Add an elif to see if the guessed location already has an 'X' in it.
#If it has, print "You guessed that one already."
elif guess_row == guess_col:
    print "You guessed that one already."
