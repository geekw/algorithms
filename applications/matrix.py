# Implementation of the Matrix ADT
class Matrix:
    # Creates a matrix of size numRows x numCols initialized to 0.
    def __init__( self, numRows, numCols ):
        self._theGrid = [[0 for j in range(numCols)] for i in range(numRows) ]

    # Return the number of rows in the matrix.
    def numRows(self):
        return len(self._theGrid)

    # Return the number of columns in the matrix.
    def numCols(self):
        return len(self._theGrid[0])

    # Returns the value of element (i, j): x[i,j]
    def __getitem__( self, ndxTuple ):
        return self._theGrid[ndxTuple[0]][ndxTuple[1]]

    # Sets the value of element (i,j) to the value s: x[i,j] = s
    def __setitem__(self, ndxTuple, scalar):
        self._theGrid[ndxTuple[0]][ndxTuple[1]] = scalar

    # Scales the matrix by the given scalar.
    def scaleBy( self, scalar ):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r, c] = scalar

    # Creates and returns a new matrix that is the transpose of this matrix.
    def tranpose( self ):
        transpose = Matrix(self.numCols(), self.numRows())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                transpose[j, i] = self[i, j]

    # Creates and returns a new matrix that results from matrix addition.
    def __add__( self, rhsMatrix ):
        assert rhsMatrix.numRows() == self.numRows() and rhsMatrix.numCols() == self.numCols(), \
            "Matrix sizes not compatible for add operation!"
        # Create the new matrix
        newMatrix = Matrix(self.numRows(), self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                newMatrix[i, j] = self[i, j] + rhsMatrix[i, j]

        return newMatrix

    # Creates and returns a new matrix that results from matrix subtraction.
    def __sub__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and rhsMatrix.numCols() == self.numCols(), \
            "Matrix sizes not compatible for sub operation!"
        # Create the new matrix
        newMatrix = Matrix(self.numRows(), self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                newMatrix[i, j] = self[i, j] - rhsMatrix[i, j]

        return newMatrix

    # Creates and returns a new matrix resulting from matrix multiplication.
    def __mul__( self, rhsMatrix ):
        assert rhsMatrix.numCols() == self.numRows() , \
            "Matrix sizes not compatible for mul operation!"
        # Create the new matrix
        newMatrix = Matrix(self.numRows(), self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                for k in range(rhsMatrix.numCols()):
                    newMatrix[i, k] += self[i, j] * rhsMatrix[j, k]

        return newMatrix
