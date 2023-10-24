import os
from Board import *

goal=[['1', '2', '3'],
      ['4', '5', '6'],
      ['7', '8', '_']]

closedList=[]
openList=[]

def getInitialBoard():
    board=[]
    print("Enter the starting position (_ for blank)")
    for i in range(0,3):
        row = input().split(" ")
        board.append(row)
    hn=h(board)
    startBoard=Board(board, 0, hn, None)
    return startBoard

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
            

def checkIfAlreadyExplored(board):
    for alreadyExploredBoard in closedList:
        if board.value==alreadyExploredBoard.value:
            return True
    return False

def getSolvedBoard(board):
    if goalTest(board.value):
        return board
    closedList.append(board)
    blank_x, blank_y,moveList=board.getMoves()
    gn=board.gn+1
    for move in moveList:
        child=board.result(blank_x, blank_y, move)
        fn=h(child)+gn
        childBoard=Board(child, gn, fn, board)
        if(not checkIfAlreadyExplored(childBoard)):
            openList.append(childBoard)
    openList.sort(key = lambda x:x.fn)
    bestChild=openList.pop(0)
    return getSolvedBoard(bestChild)


def goalTest(board):
    if h(board)==0:
        return True
    return False

def printSolutionSteps(board):
    while board is not None:
        board.printBoard()
        if(board.parent is not None):
            print("\n      ↑")
            print("      ↑")
            print("      ↑\n")
        board=board.parent

board=getInitialBoard()
os.system('cls')
solvedBoard=getSolvedBoard(board)
printSolutionSteps(solvedBoard)





    