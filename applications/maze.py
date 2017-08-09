# Impplements the Maze ADT using a matrix
from matrix import Matrix
from lliststack import Stack


# Private storage class for holding a cell position
class _CellPosition:
    def __init__(self, row, col):
        self.row = row
        self.col = col



class Maze:
    # Define constants to represent contents of the maze cells.
    MAZE_WALL = "*"
    MAZE_OPEN = "."
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"

    # Creates a maze object with all cells marked as open.
    def __init__(self, numRows, numCols):
        self._mazeCells = Matrix(numRows, numCols, Maze.MAZE_OPEN)
        self._startCell = None
        self._exitCell = None
        self._path = Stack()

    # Returns the number of rows in the maze.
    def numRows(self):
        return self._mazeCells.numRows()

    # Returns the number of columns in the maze.
    def numCols(self):
        return self._mazeCells.numCols()

    # Return the found path.
    def path(self):
        return self._path

    # Fills the indicated cell with a "wall" marker
    def setWall(self, row, col):
        assert 0 <= row < self.numRows() and \
               0 <= col < self.numCols(), "Cell index out of range."
        self._mazeCells[row, col] = Maze.MAZE_WALL

    # Sets the starting cell position.
    def setStart(self, row, col):
        assert 0 <= row < self.numRows() and \
               0 <= col < self.numCols(), "Cell index out of range."
        self._startCell = _CellPosition(row, col)

    # Sets the exit cell positon.
    def setExit(self, row, col):
        assert 0 <= row < self.numRows() and \
               0 <= col < self.numCols(), "Cell index out of range."
        self._exitCell = _CellPosition(row, col)

    # Attempts to solve the maze by finding a path from the starting cell
    # to the exit. Returns True if a path is found and False otherwise.
    def findPath(self):
        currentCell = self._startCell
        while True:
            # Try Up
            if self._validMove(currentCell.row-1, currentCell.col):
                if self._exitFound(currentCell.row-1, currentCell.col):
                    self._markPath(currentCell.row, currentCell.col)
                    self._path.push(currentCell)
                    self._markPath(self._exitCell.row, self._exitCell.col)
                    self._path.push(self._exitCell)
                    return True
                self._markPath(currentCell.row, currentCell.col)
                self._path.push(currentCell)
                currentCell = _CellPosition(currentCell.row-1, currentCell.col)
                continue

            # Try Down
            elif self._validMove(currentCell.row+1, currentCell.col):
                if self._exitFound(currentCell.row+1, currentCell.col):
                    self._markPath(currentCell.row, currentCell.col)
                    self._path.push(currentCell)
                    self._markPath(self._exitCell.row, self._exitCell.col)
                    self._path.push(self._exitCell)
                    return True
                self._markPath(currentCell.row, currentCell.col)
                self._path.push(currentCell)
                currentCell = _CellPosition(currentCell.row+1, currentCell.col)
                continue

            # Try Left
            elif self._validMove(currentCell.row, currentCell.col-1):
                if self._exitFound(currentCell.row, currentCell.col-1):
                    self._markPath(currentCell.row, currentCell.col)
                    self._path.push(currentCell)
                    self._markPath(self._exitCell.row, self._exitCell.col)
                    self._path.push(self._exitCell)
                    return True
                self._markPath(currentCell.row, currentCell.col)
                self._path.push(currentCell)
                currentCell = _CellPosition(currentCell.row, currentCell.col-1)
                continue

            # Try Right
            elif self._validMove(currentCell.row, currentCell.col+1):
                if self._exitFound(currentCell.row, currentCell.col+1):
                    self._markPath(currentCell.row, currentCell.col)
                    self._path.push(currentCell)
                    self._markPath(self._exitCell.row, self._exitCell.col)
                    self._path.push(self._exitCell)
                    return True
                self._markPath(currentCell.row, currentCell.col)
                self._path.push(currentCell)
                currentCell = _CellPosition(currentCell.row, currentCell.col+1)
                continue

            # Dead End
            else:
                if currentCell == self._startCell:
                    return False
                self._markTried(currentCell.row, currentCell.col)
                currentCell = self._path.pop()
                continue


    # Resets the maze by removing all "path" and "tried" tokens.
    def reset(self):
        for row in range(self.numRows()):
            for col in range(self.numCols()):
                if self._mazeCells[row, col] == Maze.PATH_TOKEN or \
                        self._mazeCells[row, col] == Maze.TRIED_TOKEN:
                    self._mazeCells[row, col] = Maze.MAZE_OPEN

    # Prints a text-based representation of the maze.
    def draw(self):
        for row in range(self.numRows()):
            line = ""
            for col in range(self.numCols()):
                line += self._mazeCells[row, col]
            print line

    # Returns True if the given cell position is a valid move.
    def _validMove(self, row, col):
        return 0 <= row < self.numRows() \
               and 0 <= col < self.numCols() \
               and self._mazeCells[row, col] == '.'

    # Helper method to determine if the exit was found.
    def _exitFound(self, row, col):
        return row == self._exitCell.row and \
               col == self._exitCell.col

    # Drops a "tried" token at the given cell.
    def _markTried(self, row, col):
        self._mazeCells[row, col] = Maze.TRIED_TOKEN

    # Drops a "path" token at the given cell.
    def _markPath(self, row, col):
        self._mazeCells[row, col] = Maze.PATH_TOKEN


