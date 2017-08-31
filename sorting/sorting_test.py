from sorting import Sorting

items = [2, 3, 9, 7, 5, 6]
sorting_items = Sorting(items)
for item in sorting_items.insertion_sort():
    print item