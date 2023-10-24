import copy
import os

goal=[['1', '2', '3'],
      ['4', '5', '6'],
      ['7', '8', '_']]

exploredList=[]

def getInitialBoard():
    board=[]
    print("Enter the starting position (_ for blank)")
    for i in range(0,3):
        row = input().split(" ")
        board.append(row)
    return board

#function to swap blank space with U, D, L, R tile and return new board
def result(board, blank_x, blank_y, move):
    if move=='U':
        tile_x=blank_x
        tile_y=blank_y-1
    elif move=='D':
        tile_x=blank_x
        tile_y=blank_y+1
    elif move=='L':
        tile_x=blank_x-1
        tile_y=blank_y
    elif move=='R':
        tile_x=blank_x+1
        tile_y=blank_y
    #swap tiles
    board[blank_y][blank_x], board[tile_y][tile_x]=board[tile_y][tile_x], board[blank_y][blank_x]
    return board
    
def getMoves(board):
    validMoves=[]
    for row in range(0,3):
        if '_' in board[row]:
            blank_y, blank_x=row, board[row].index('_')
    if blank_x+1<3:
        validMoves.append('R')
    if blank_x-1>=0:
        validMoves.append('L')
    if blank_y+1<3:
        validMoves.append('D')
    if blank_y-1>=0:
        validMoves.append('U')
    return blank_x, blank_y,validMoves

#heuristic function=count of misplaced tiles
#it can be changed to manhattan distamce later for efficiency
def h(board):
    sum=0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]!=goal[i][j] and board[i][j]!='_':
                sum+=getManhattanDistance(board, goal, i,j)
    return sum

def getManhattanDistance(board, goal, x, y):
    value=board[x][y]
    for i in range(0,3):
        for j in range (0,3):
            if goal[i][j]==value:
                return abs(i-x)+abs(j-y)

def getBestMove(board):
    blank_x, blank_y,moveList=getMoves(board)
    leastHVal=9999
    for move in moveList:
        board_copy=copy.deepcopy(board)
        child=result(board_copy,blank_x, blank_y, move)
        if child in exploredList:
            continue
        hval=h(child)
        if leastHVal>hval:
            leastHVal=hval
            bestChild=child
    return bestChild


def goalTest(board):
    if h(board)==0:
        return True
    return False

def printBoard(board):
    for i in range (0,3):
        for j in range(0,3):
            print(board[i][j], end=" ")
        print()
    print()

c=0
board=getInitialBoard()
os.system('cls')
printBoard(board)
while(not goalTest(board)):
    c+=1
    print("  |")
    print("  |")
    print("  V")
    exploredList.append(board)
    board=getBestMove(board)
    print("\nStep", c)
    printBoard(board)
    