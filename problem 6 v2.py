import numpy as np
def create_board(m,n):
    return np.zeros((m,n))

def coordinates(board, player):
    i, j, cn = (-1, -1, 0)
    try:
        while (i > n or i < 0 or j < 0 or j > m) or (board[i][j] != 0):
            if cn > 0:  # makes sure user doesn't hit the same spot already inputted
                print("Wrong Input. Try Again")
            print("Player {}'s turn".format(player))
            i = int(input("your X coordinates?: "))
            j = int(input("your Y coordinates?: "))
            i -=  1
            j -=  1
            cn = cn + 1
        board[i][j] = str(player)
        return board
    except:
        print("you must follow coordinates,Wrong Input!")






def row_win(board, player):
    win = False
    for row in board:
        if all([cell == player for cell in row]):
            win = True
    return win

def col_win(board,player):
    win = False
    newB= np.transpose(board)
    for row in newB:
        if all([cell == player for cell in row]):
            win = True
    return win


def diag_win(board, player):
    win = True
    y = 0
    for x in range(len(board)):
        if board[x][x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x][y] != player:
                win = False
    return win


def evaluate(board):
    winner = 0

    for player in [1,2]:
        if (row_win(board, player) or
                col_win(board, player) or
                diag_win(board, player)):
            winner = player

    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner


def play_game():
    board, winner, counter = create_board(m,n), 0, 1
    print(board)
    while winner == 0:
        for player in [1, 2]:
            board = coordinates(board, player)
            print("Move number: " + str(counter))
            print(board)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break
    return winner
n=m=int(input("please enter your desired board size:"))
print("Winner is Player " + str(play_game()))