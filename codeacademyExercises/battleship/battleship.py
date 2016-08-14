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