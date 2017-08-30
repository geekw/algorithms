from itertools import permutations
from applications.myutils.combinatorial import Permutation

def permustd(theList):
    return permutations(theList)

def permumine(theList):
    perms = Permutation(theList)
    return perms.solutions()

mylist = [i for i in range(3)]
perms1 = permustd(mylist)
perms2 = permumine(mylist)