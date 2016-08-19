#Play It, Sam
#Add a for loop that repeats the guessing and checking part of your game for 4 turns, like the example above.
#At the beginning of each iteration, print "Turn", turn + 1 to let the player know what turn they are on.
#Indent everything that should be repeated.
from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

for turn in range(4):
    print_board(board)
    print "Turn", turn + 1
    guess_row = int(raw_input("Guess Row:"))    
    guess_col = int(raw_input("Guess Col:"))
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
#Game Over
#Add an if statement that checks to see if the user is out of guesses.
#Put it under the else that accounts for misses.
#Put it after the if/elif/else statements that check for the reason the player missed. We want "Game Over" to print regardless of the reason.
#If turn equals 3, print "Game Over".
        elif turn == 3:
            print "Game Over"
            #break to get out of a for loop.
            break


