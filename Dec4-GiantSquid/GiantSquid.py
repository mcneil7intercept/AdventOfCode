from os import makedirs
import numpy as np

file = open("input.txt", 'r')
numbers = [int(x) for x in file.readline().split(',')]

rowcount = 0
board = []
boards = []
MarkedBoards = []

# parse input.  first line is numbers, rest into a list of 5X5 2 dimensional arrays
while True:
    line = file.readline()

    if(rowcount == 5):
        boards.append(board)
        rowcount = 0
        board = []

    if line == '\n':
        continue

    if not line:
        break

    rowcount += 1
    row = [int(x) for x in line.split()]
    board.append(row)


# Create a second list of 5X5 arrays populated with Booleans to keep track of marking
for board in boards:
    MarkedBoards.append([[False for _ in range(5)]for _ in range(5)])


# Create a list of bools the length of the number of boards we have to keep track of winners.
BoardsWon = [False for _ in range(len(boards))]
num_won = 0

# loop through all numbers
for number in numbers:
    # loop through all boards and check every number
    for i, board in enumerate(boards):
        for row in range(5):
            for column in range(5):
                # if number matches mark the corresponding board in the boolean matrix list
                if board[row][column] == number:
                    MarkedBoards[i][row][column] = True
        # check each column and row to see if any are all True
        won = False
        for row in range(5):
            ok = True
            for column in range(5):
                if not MarkedBoards[i][row][column]:
                    ok = False
            if ok:
                won = True
        for column in range(5):
            ok = True
            for row in range(5):
                if not MarkedBoards[i][row][column]:
                    ok = False
            if ok:
                won = True

        # if a row or column is all true the board won.
        if won and not BoardsWon[i]:
            # mark that this particular board won
            BoardsWon[i] = True
            # keep track of how many boards have won
            num_won = len([j for j in range(len(boards)) if BoardsWon[j]])
            # if this is the first or last winner, calculate the score
            if num_won == 1 or num_won == len(boards):
                unmarked = 0
                for row in range(5):
                    for column in range(5):
                        if not MarkedBoards[i][row][column]:
                            unmarked += board[row][column]
                print(unmarked, number, unmarked*number)
