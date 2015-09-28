"""
multiplication-table.py
Author: James Napier
Credit: http://code.runnable.com/U93SdCQWCF5gU8cz/generating-a-3x3-grid-for-python
Assignment:

Write and submit a Python program that prints a multiplication table. The user 
must be able to determine the width and height of the table before it is printed.

The final multiplication table should look like this:

Width of multiplication table: 10
Height of multiplication table: 8

  1   2   3   4   5   6   7   8   9  10
  2   4   6   8  10  12  14  16  18  20
  3   6   9  12  15  18  21  24  27  30
  4   8  12  16  20  24  28  32  36  40
  5  10  15  20  25  30  35  40  45  50
  6  12  18  24  30  36  42  48  54  60
  7  14  21  28  35  42  49  56  63  70
  8  16  24  32  40  48  56  64  72  80
"""
 Width=input("Width of multiplication table: ")
 Height=input("Height of multipication table: ")
 
 # Define blank list
board = []

#Generate rows with length of 3
for row in range(3):
  # Appen a blank list to each row cell
  board.append([])
  for column in range(3):
    # Assign x to each row
    board[row].append('x')

# Function will print board like an actual board
def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)