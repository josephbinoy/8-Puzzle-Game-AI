import copy

class Board:
    def __init__(self,value,gn,fn, parent):
        self.value = value
        self.gn = gn
        self.fn = fn
        self.parent=parent
        
    def result(self, blank_x, blank_y, move):
        board_copy=copy.deepcopy(self.value)
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
        board_copy[blank_y][blank_x], board_copy[tile_y][tile_x]=board_copy[tile_y][tile_x], board_copy[blank_y][blank_x]
        return board_copy
    
    def getMoves(self):
        validMoves=[]
        for row in range(0,3):
            if '_' in self.value[row]:
                blank_y, blank_x=row, self.value[row].index('_')
        if blank_x+1<3:
            validMoves.append('R')
        if blank_x-1>=0:
            validMoves.append('L')
        if blank_y+1<3:
            validMoves.append('D')
        if blank_y-1>=0:
            validMoves.append('U')
        return blank_x, blank_y, validMoves
    
    def printBoard(self):
        print("┍---┰---┰---┑")
        for i in range (0,3):
            print("| ", end="")
            for j in range(0,3):
                print(self.value[i][j],"| ", end="")
            print()
            if i !=2:
                print("|---|---|---|")
        print("┕---┷---┷---┙")
    