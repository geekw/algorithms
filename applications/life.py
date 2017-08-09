# Implements the LifeGrid ADT for use with the game of Life.
from matrix import Matrix


class LifeGrid:
    # Define constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    # Creates the game grid and initializes the cells to dead.
    def __init__(self, numRows, numCols):
        self._grid = Matrix(numRows, numCols)

    # Returns the number of rows in the grid.
    def numRows(self):
        return self._grid.numRows()

    # Returns the number of columns in the grid.
    def numCols(self):
        return self._grid.numCols()

    # Configures the grid to contain the given live cells.
    def configure(self, coordList):
        # Clear the game grid.
        for i in range(self.numCols()):
            for j in range(self.numCols()):
                self.clearCell(i, j)

        # Set the indicated cells to be alive.
        for coord in coordList:
            self.setCell(coord[0], coord[1])

    # Does the indicated cell contain a live organism?
    def isLiveCell(self, row, col):
        return self._grid[row, col] == LifeGrid.LIVE_CELL

    # Clears the indicated cell by setting it to dead.
    def clearCell(self, row, col):
        self._grid[row, col] = LifeGrid.DEAD_CELL

    # Sets the indicated cell to be alive.
    def setCell(self, row, col):
        self._grid[row, col] = LifeGrid.LIVE_CELL

    # Returns the number of live neighbors of the given cell.
    def numLiveNeighbors(self, row, col):
        rowStart = max(0, row - 1)
        rowEnd = min(row + 1, self.numRows() - 1)
        colStart = max(0, col - 1)
        colEnd = min(col + 1, self.numCols() - 1)
        numLiveNeighbors = 0
        for i in range(rowStart, rowEnd + 1):
            for j in range(colStart, colEnd + 1):
                if self.isLiveCell(i, j):
                    numLiveNeighbors += 1

        # Exclude the given cell itself
        if (self.isLiveCell(row, col)):
            numLiveNeighbors -= 1

        return numLiveNeighbors

    # Draws the life grid with specified characters
    def draw(self, live='@', dead='.'):
        for i in range(self.numRows()):
            line = ''
            for j in range(self.numCols()):
                if self.isLiveCell(i, j):
                    line += live + ' '
                else:
                    line += dead + ' '
            print line
        print '\n'
