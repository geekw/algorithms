# Implmentation of a 2-D array
from listbag import Bag

class QueensBoard:
    def __init__(self, size):
        self._size = size
        self._board = [[0 for i in range(self._size)] for j in range(self._size)]
        self._queenPositions = Bag()

    def size(self):
        return self._size

    def numQueens(self):
        return len(self._queenPositions)

    def unguarded(self, row, col):
        if self._board[row][col] != 0:
            return False
        else:
            for placedPosition in self._queenPositions:
                if placedPosition["row"] == row or placedPosition["col"] == col or \
                    (abs(placedPosition["row"] - row) == abs( placedPosition["col"] - col)):
                    return False
        return True

    def placeQueen(self, row, col):
        self._board[row][col] = 1
        self._queenPositions.add({"row":row, "col":col})
        print "Placed ", row, col

    def removeQueen(self, row, col):
        self._board[row][col] = 0
        self._queenPositions.remove({"row":row, "col":col})
        print "Removed ", row, col

    def reset(self):
        for row in range(self.size()):
            for col in range(self.size()):
                self._board[row][col] = 0
        self._queenPositions = Bag()

    def draw(self):
        for row in range(self.size()):
            line = ''
            for col in range(self.size()):
                if self._board[row][col] == 0:
                    line += 'o'
                else:
                    line += 'x'
            print line

