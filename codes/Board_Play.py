import sys
import numpy as np
from collections import defaultdict
from colorama import init, Fore, Back, Style
import random
import copy

###  Define board, black&white pieces (disk) using array and numbers
"""
Class Bloard
* black disk: 1, white disk: -1
* board: 8X8 array
* score: dictionary 
* isOnBoard: check if (x,y) is on the 8X8 board  
* resetBoard: reset board and return the initial state of the board
* printBoard: print current state of the board (using colorama)
* isValidMove: check if (x,y) place is a valid move for a specific player(black or white). return a list of all coordinates of places will be flipped to a player's color 
* makeMove: excute board updates based on a player's move + isValidMove
* allLegalMoves: find all the possible moves to specific player(black or white). return a list of all coordinates


"""


class Board(object):
    BLACK = 1
    WHITE = -1

    def __init__(self, n):
        self.n = n
        self.board = np.zeros((n,n), int)
        self.board[n//2-1][n//2-1] = Board.BLACK
        self.board[n//2][n//2] = Board.BLACK 
        self.board[n//2-1][n//2] = Board.WHITE
        self.board[n//2][n//2-1] = Board.WHITE
        self.score = {Board.BLACK: 2, Board.WHITE: 2}
        
    def returnScore(self):
        return self.score
    
    
    def isOnBoard(self, x, y):
        """List all the valid squares on the board."""
        return (x >= 0) and (x <= n-1) and (y >= 0) and (y <= n-1) 
        
    def resetBoard(self):
        self.board = np.zeros((n,n), int)
        self.board[n//2-1][n//2-1] = Board.BLACK
        self.board[n//2][n//2] = Board.BLACK 
        self.board[n//2-1][n//2] = Board.WHITE
        self.board[n//2][n//2-1] = Board.WHITE
        self.score = {Board.BLACK: 2, Board.WHITE: 2}
        
    def printBoard(self):
        def color(piece):
            if piece == 0: return Back.BLUE + Fore.BLACK + ' '
            elif piece == Board.BLACK: return Back.BLUE + Fore.BLACK + 'O'
            elif piece == Board.WHITE: return Back.BLUE + Fore.WHITE + 'O'   
        
        output = Back.YELLOW + Fore.BLACK + '  |'+ '|'.join([str(i) for i in range(n)]) + '|'+ '\n'
        for i in range(n):
            row = Back.YELLOW + Fore.BLACK + ' ' + str(i) + Back.BLUE + '|'
            row += '\x1b[44m\x1b[30m|'.join([color(p) for p in self.board[i]])
            row += '|\n'
            output += row

    
    def isValidMove(self, disk, xstart, ystart):
        if (~self.isOnBoard(xstart, ystart)) or self.board[xstart][ystart] != 0:
            return False
        
        flippable_disks = []
        self.board[xstart][ystart] = disk
        opponentDisk = disk * -1
        
        for xdir,ydir in ((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)):
            x, y = xstart, ystart
            x += xdir
            y += ydir
            if self.isOnBoard(x,y) and self.board[x][y] == opponentDisk:
                x += xdir
                y += ydir
                if not self.isOnBoard(x, y):
                    continue
                while self.board[x][y] == opponentDisk:
                    x += xdir
                    y += ydir
                    if not self.isOnBoard(x, y):
                        break
                if not self.isOnBoard(x, y):
                    continue
                if self.board[x][y] == disk:
                    while True:
                        x -= xdir
                        y -= ydir
                        if x == xstart and y == ystart:
                            break
                        flippable_disks.append([x, y])       
        
        self.board[xstart][ystart] = 0
        return flippable_disks
   
    def makeMove(self, disk, xstart, ystart):
        flippable_disks = self.isValidMove(disk, xstart, ystart)
        for x, y in flippable_disks:
            self.board[x][y] = disk*(-1)
        return self.board
            
    def allLegalMoves(self, disk):
        result=[ (i,j) for i in range(n) for j in range(n) if ~self.isValidMove(disk, i, j) and (self.isValidMove(disk, i, j)) != [] ]
#         for i in range(n):
#             for j in range(n):
#                 if self.isValidMove(disk, i, j):
#                     if len(self.isValidMove(disk, i, j)) >0:
#                         result.append((i,j))
                
    
def play(board, black_strategy, white_strategy):
    player = BLACK
    strategy = lambda who: black_strategy if who == BLACK else white_strategy
    print('start')
    while player is not None:
        print(print_board(board))
        print('white:',score(WHITE, board),'black:',score(BLACK, board))
        move = get_move(strategy(player), player, board)
        make_move(move, player, board)
        player = next_player(board, player)

    print(print_board(board))
    print('white:',score(WHITE, board),'black:',score(BLACK, board))
    print('end')
    return board, score(BLACK, board)

def next_player(board, prev_player):
    """Which player should move next?  Returns None if no legal moves exist."""
    opp = opponent(prev_player)
    if any_legal_move(opp, board):
        return opp
    elif any_legal_move(prev_player, board):
        return prev_player
    return None

def get_move(strategy, player, board):
    """Call strategy(player, board) to get a move."""
    copy = list(board) # copy the board to prevent cheating
    move = strategy(player, copy)
    if not is_valid(move) or not is_legal(move, player, board):
        raise IllegalMoveError(player, move, copy)
    return move

def score(player, board):
    """Compute player's score (number of player's pieces minus opponent's)."""
    mine, theirs = 0, 0
    opp = opponent(player)
    for sq in squares():
        piece = board[sq]
        if piece == player: mine += 1
        elif piece == opp: theirs += 1
    return mine - theirs


weigted_matrix1 = np.array([[120, -20,  20,   5,   5,  20, -20, 120],
                  [-20, -40,  -5,  -5,  -5,  -5, -40, -20],
                  [20,  -5,  15,   3,   3,  15,  -5,  20],
                  [5,  -5,   3,   3,   3,   3,  -5,   5],
                  [5,  -5,   3,   3,   3,   3,  -5,   5],
                  [20,  -5,  15,   3,   3,  15,  -5,  20],
                  [-20, -40,  -5,  -5,  -5,  -5, -40, -20],
                  [120, -20,  20,   5,   5,  20, -20, 120]])

weigted_matrix2 = np.array([[100, -25, 20, 5, 5, 10, -25, 100],
                  [-25, -25, 1, 1, 1, 1, -25, -25],
                  [ 10, -1, 5, 2, 2, 5, 1, 10],
                  [ 5, 1, 2, 1, 1, 2, 1, 5],
                  [ 5, 1, 2, 1, 1, 2, 1, 5],
                  [ 10, -1, 5, 2, 2, 5, 1, 10],
                  [-25, -25, 1, 1, 1, 1, -25, -25],
                  [100, -25, 20, 5, 5, 10, -25, 100]])

weigted_matrix3 = np.array([[4, -3, 2, 2, 2, 2, -3, 4],
                  [-3, -4, -1, -1, -1, -1, -4, -3],
                  [ 2, -1, 1, 0, 0, 1, -1, 2],
                  [ 2, -1, 0, 1, 1, 0, -1, 2],
                  [4, -3, 2, 2, 2, 2, -3, 4],
                  [-3, -4, -1, -1, -1, -1, -4, -3],
                  [ 2, -1, 1, 0, 0, 1, -1, 2],
                  [ 2, -1, 0, 1, 1, 0, -1, 2]])

weigted_matrix_all=[weigted_matrix1, weigted_matrix2, weigted_matrix3]

def random_strategy(player, board):
    return np.random.choice(allLegalMoves(self, disk))

def WeightMatrixScore(player, board):
    opponent = player*(-1)
    score=np.sum((board==player)*weigted_matrix2)-np.sum(((board==opponent)*weigted_matrix2))
    return score

def maximizer(player, board):
    return max(allLegalMoves(player, board), key=score_move)

def minimax(player, board, depth, evaluate):
    def value(board):
        return -minimax(opponent(player), board, depth-1, evaluate)[0]
    if depth == 0:
        return evaluate(player, board), None
    
    moves = legal_moves(player, board)
    if not moves:
        if not any_legal_move(opponent(player), board):
            return final_value(player, board), None
        return value(board), None
    
    return max((value(make_move(m, player, list(board))), m) for m in moves)

MAX_VALUE = sum(map(abs, SQUARE_WEIGHTS))
MIN_VALUE = -MAX_VALUE

def final_value(player, board):
    diff = score(player, board)
    if diff < 0:
        return MIN_VALUE
    elif diff > 0:
        return MAX_VALUE
    return diff

def minimax_searcher(depth, evaluate):
    def strategy(player, board):
        return minimax(player, board, depth, evaluate)[1]
    return strategy

def alphabeta(player, board, alpha, beta, depth, evaluate):
    if depth == 0:
        return evaluate(player, board), None

    def value(board, alpha, beta):
        return -alphabeta(opponent(player), board, -beta, -alpha, depth-1, evaluate)[0]

    moves = legal_moves(player, board)
    if not moves:
        if not any_legal_move(opponent(player), board):
            return final_value(player, board), None
        return value(board, alpha, beta), None

    best_move = moves[0]
    for move in moves:
        if alpha >= beta:
            break
        val = value(make_move(move, player, list(board)), alpha, beta)
        if val > alpha:
            alpha = val
            best_move = move
    return alpha, best_move

def alphabeta_searcher(depth, evaluate):
    def strategy(player, board):
        return alphabeta(player, board, MIN_VALUE, MAX_VALUE, depth, evaluate)[1]
    return strategy

