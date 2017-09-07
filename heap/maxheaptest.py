from heap import MaxHeap

capacity = 64
myheap = MaxHeap(capacity)

items = [3, 4, 2, 1, 6, 8, 5, 7]
for item in items:
    myheap.add(item)

assert len(myheap) == 8, "Wrong __len__!"
assert myheap.capacity() == capacity, "Wrong capacity!"

for i in range(8):
    assert myheap.extract() == 8 - i, "Wrong extract!"