from nqueens1d import QueensBoard

def solveQueens(board, col):
    # A solution was found if n-queens have been placed on the board.
    if board.numQueens() == board.size():
        board.draw()
        return True
    else:
        # Find the next unguarded square within this column.
        for row in range(board.size()):
            if board.unguarded(row, col):
                # Place a queen in that square.
                board.placeQueen(row, col)
                # Continue placing queens in the following columns.
                if solveQueens(board, col+1):
                    # We are finished if a solution was found.
                    return True
                else :
                    # No solution was found with the queen in this square, so it
                    # has to be removed from the board.
                    board.removeQueen(row, col)

    # If the loop terminates, no queen can be placed within this column.
    return False

size = 8
board = QueensBoard(size)
solveQueens(board, 0)