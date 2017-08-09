# Program for building and solving a maze.
from maze import Maze


# The main routine.
def main():
    maze = buildMaze("mazefile.txt")
    if maze.findPath():
        print("Path found....")
        maze.draw()
        path = maze.path()
        for item in path:
            print item.row, item.col
    else:
        print("Path not found....")


# Builds a maze based on a text format in the given file.
def buildMaze(filename):
    infile = open(filename, "r")

    # Read the size of the maze.
    nrows, ncols = readValuePair(infile)
    maze = Maze(nrows, ncols)

    # Read the starting and exit positions.
    row, col = readValuePair(infile)
    maze.setStart(row, col)
    row, col = readValuePair(infile)
    maze.setExit(row, col)

    # Read the maze itself.
    for row in range(nrows):
        line = infile.readline()
        for col in range(ncols):
            if line[col] == "*":
                maze.setWall(row, col)

    # Close the maze file and return the newly constructed maze.
    infile.close()
    return maze


# Extract an integer value pair from the given input file.
def readValuePair(infile):
    """

    :rtype : 2 integers
    """
    line = infile.readline()
    valA, valB = line.split()
    return int(valA), int(valB)


# Call the main routine to execute the program
if __name__ == '__main__':
    main()
