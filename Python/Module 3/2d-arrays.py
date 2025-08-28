#creating a 4x4 board
board = []
EMPTY = "-"

for i in range(4):  #outer loop creates th rows
    rows = [EMPTY for i in range(4)]   #inner loop creates columns with the expression "-"
    board.append(rows)
print(board)
print()

#condensed version
board = []
board = [[EMPTY for i in range(4)] for i in range(4)]
print(board)