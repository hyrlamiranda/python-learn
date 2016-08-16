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