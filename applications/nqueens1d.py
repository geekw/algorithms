# Implmentation of a 1-D array
from listbag import Bag

class QueensBoard:
    def __init__(self, size):
        self._size = size
        self._board = [-1 for i in range(self._size)]
        self._queenPositions = Bag()

    def size(self):
        return self._size

    def numQueens(self):
        return len(self._queenPositions)

    def unguarded(self, row, col):
        if self._board[row] == col:
            return False
        else:
            for placedPosition in self._queenPositions:
                if placedPosition["row"] == row or placedPosition["col"] == col or \
                    (abs(placedPosition["row"] - row) == abs( placedPosition["col"] - col)):
                    return False
        return True

    def placeQueen(self, row, col):
        self._board[row] = col
        self._queenPositions.add({"row":row, "col":col})

    def removeQueen(self, row, col):
        self._board[row] = -1
        self._queenPositions.remove({"row":row, "col":col})

    def reset(self):
        for i in range(self.size()):
            self._board[i] = -1
        self._queenPositions = Bag()

    def draw(self):
        for row in range(self.size()):
            line = ''
            for col in range(self.size()):
                if self._board[row] == col:
                    line += 'x'
                else:
                    line += 'o'
            print line

