#Use range() to loop 5 times.
#Inside the loop, .append() a list containing 5 "O"s to board, just like in the example above.
#Note that these are capital letter "O" and not zeros.
board = []
for i in range(5):
    board.append(["O"] * 5) 
print board