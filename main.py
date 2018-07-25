import numpy
# use numpy to generate, a 6 row / 7 columns matrix
board = numpy.zeros((6, 7))
# set the turn to 1
turn = 1
# boolean use to check if the game is over or not
over = False


def play(player, board):
    # tell the player to choose a column where to drop his piece
    choice = int(input("(Player " + str(player) + ") Select a column between 0 and 6 : "))
    # tell the player to choose again if he exceed the column limit
    while choice > 7:
        choice = int(input("(Player " + str(player) + ") Wrong column please, select a column between 0 and 6 : "))
    # tell the player to choose again if he's choosing a filled column
    while board[0][choice] != 0:
        choice = int(input("(Player " + str(player) + ") This column is already filled, select another one "))
    # drop the piece if the column choosed is not full
    if board[0][choice] == 0:
        drop_to_col(board, choice, player)

# looping into rows to set the piece to the highest row, then print the board
def drop_to_col(board, choice, player):
    for row in range(6):
        if board[row][choice] == 0:
            r = row
    board[r][choice] = player
    print(board)

# Play the game until a winning condition is met
while not over:
    if turn == 1:
        play(1, board)
    else:
        play(2, board)
    turn += 1
    turn = turn % 2