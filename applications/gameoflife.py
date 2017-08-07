# Program for playing the game of life
from life import LifeGrid

# Define the initial configuration of live cells.
# INIT_CONFIG = [ (1,1), (1,2), (2,2), (3,2) ]
# INIT_CONFIG = [ (1,2), (2,1), (2,2), (2,3) ]
INIT_CONFIG = [ (2,1), (2,2), (2,3) ]

# Set the size of the grid.
GRID_WIDTH = 5
GRID_HIGHT = 5

# Indicate the number of generations.
NUM_GENS = 10

def main():
    # Construct the game grid and configure it.
    grid = LifeGrid(GRID_HIGHT, GRID_WIDTH)
    # grid.configure(INIT_CONFIG)
    init(grid)

    # Play the game
    grid.draw()
    for i in range(NUM_GENS):
        evolve(grid)
        grid.draw()


# Init the grid
def init(grid):
    """
    :type grid: LifeGrid
    """
    coorList = list()
    for i in range(GRID_HIGHT):
        for j in range(GRID_WIDTH):
            coorList.append((i, j))
    grid.configure(coorList)

# Generates the next generation of organisms.
def evolve(grid):
    # List for storing the live cells of the next generation.
    """

    :type grid: LifeGrid
    """
    liveCells = list()

    # Iterate over the elements of the grid.
    for i in range( grid.numRows() ) :
        for j in range( grid.numCols() ) :
            # Determine the number of live neighbors for this cell.
            neighbors = grid.numLiveNeighbors( i, j )

            # Add the (i,j) tuple to liveCells if this cell contains
            # a live organism in the next generation.
            if (neighbors == 2 and grid.isLiveCell( i, j )) or \
                (neighbors == 3 ) :
                liveCells.append( (i, j) )

    # Reconfigure the grid using the liveCells coord list.
    grid.configure( liveCells )

# Executes the main routine.
main()