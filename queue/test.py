from arrayqueue import Queue

mydata = [7, 13, 45, 19, 28, -1]
myqueue = Queue(20)
assert myqueue.isEmpty(), "A newly created queue should be empty!"
assert myqueue.length() == 0, "The length of an empty queue shoul be 0!"

myqueue.enqueue(mydata[0])
assert myqueue.length() == 1, "Enqueueing an item should change the length of an empty queue to 1!"
assert not myqueue.isEmpty(), "A queue having items should not be empty!"

myqueue.enqueue(mydata[1])
assert myqueue.length() == 2, "Enqueing an item should change the length of an empty queue to 1!"
assert not myqueue.isEmpty(), "A queue having items should not be empty!"

myqueue.enqueue(mydata[2])
myqueue.enqueue(mydata[3])
assert myqueue.dequeue() == mydata[0], "dequeue() should return the item that is first inserted!"
assert myqueue.length() == 3, "dequeue() operation on an non-empty queue should decrease the length by 1!"

myqueue.enqueue(mydata[0])
myqueue.enqueue(mydata[4])
myqueue.enqueue(mydata[5])
assert myqueue.length() == len(mydata), "The length of the queue should be equal to that of the original list!"
assert myqueue.dequeue() == mydata[1], "The order of the dequeued items should be the one of the original list!"
assert myqueue.dequeue() == mydata[2], "The order of the dequeued items should be the one of the original list!"
assert myqueue.dequeue() == mydata[3], "The order of the dequeued items should be the one of the original list!"
assert myqueue.dequeue() == mydata[0], "The order of the dequeued items should be the one of the original list!"
assert myqueue.dequeue() == mydata[4], "The order of the dequeued items should be the one of the original list!"
assert myqueue.dequeue() == mydata[5], "The order of the dequeued items should be the one of the original list!"
assert myqueue.isEmpty(), "With all items dequeued, the queue should be empty again!"

print "Congratulations! Passed all tests!"