from itertools import product

# def gensquares(N):
#     for i in range(N):
#         yield i**2

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

# def permutations(iterable, r=None):
#     pool = tuple(iterable)
#     n = len(pool)
#     r = n if r is None else r
#     for indices in product(range(n), repeat=r):
#         if len(set(indices)) == r:
#             yield tuple(pool[i] for i in indices)

mystr = "ABCD"
perms = permutations(mystr, r=2)
for perm in perms:
    print perm