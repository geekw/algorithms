# Solves the N-Queens problem with brute force

from itertools import permutations

# For the N-Queens problem, if a set of queens' position
# is represented using a 1-D array of permutation, there is
# no need to check if any pair of queens are on the same
# row or column. Therefore, we only need to exclude the diagonal situations.
def isValidPositions(permutation):
    length = len(permutation)
    for ind0 in range(length):
        for ind1 in range(ind0+1, length):
            if abs(permutation[ind1] - permutation[ind0]) == abs(ind1-ind0):
                return False

    return True

board_size = 10
elements = range(board_size)
perms = permutations(elements)

validSolutions = list()
for perm in perms:
    if isValidPositions(perm):
        validSolutions.append(perm)

print len(validSolutions), " in Total!"


