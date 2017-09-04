from sorting import Sorting, quick_sort
import random


seq = [item for item in range(100)]
random.shuffle(seq)
quick_sort(seq)
for item in seq:
    print item
