"""
Tic Tac Toe Player
"""

import math
import copy 

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX, countO = 0, 0
    
    for i in range (len(board)):
        for j in range (len(board)):
            if board[i][j] == X:
                countX += 1
            else:
                countO += 1
    
    if countX <= countO:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleMove = set()
    for i in range (len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                possibleMove.add((i,j))
    return possibleMove

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = board.deepcopy(board)
    if newBoard[action[0]][action[1]] != EMPTY:
         raise Exception("Invalid action")
    
    newBoard[action[0]][action[1]] = player(board)
    
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontally
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board [i][2]:
            if board[i][0] == X:
                return X
            elif board[i][0] == O:
                return O
    
     # Vertically 
    for j in range(len(board)):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == X:
                return X
            elif board[0][j] == O:
                return O
            
    # Diagonally
    if board[0][0] == board[1][1] == board [2][2]:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
            
    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] == X:
            return X
        elif board[2][0] == O:
            return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    if winner(board) == None:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == EMPTY:
                    return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    utility = 0
    if winner(board) == X:
        utility = 1
    elif winner(board) == O:
        utility = -1
    return utility  


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise

