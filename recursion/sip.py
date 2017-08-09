def printRev(n):
    if n > 0:
        print n
        printRev(n - 1)


def printInc(n):
    if n > 0:
        printInc(n - 1)
        print n


printRev(4)
printInc(4)
