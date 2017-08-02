# Implementation of the Queue ADT using a circular array.
# This implementation is better than the list implementation, because in the
# latter one, dequeue() involves shifting the whole list, which is time
# consuming. The weak point of this implementation is that the length is fixed.
from array import array

class Queue:
    # Creates an empty queue.
    def __init__(self, maxSize):
        self._count = 0
        self._front = 0
        self._back = maxSize - 1
        self._qArray = [None]*maxSize

    # Returns True if the queue is empty.
    def isEmpty( self ) :
        return self._count == 0

    # Returns True if the queue is full.
    def isFull( self ) :
        return self._count == len(self._qArray)

    # Returns the number of items in the queue.
    def length( self ) :
        return self._count

    # Adds the given item to the queue.
    def enqueue( self, item ):
        assert not self.isFull(), "Cannot enqueue on a full queue!"
        self._back = (self._back + 1) % len(self._qArray)
        self._qArray[self._back] = item
        self._count += 1

    # Removes and returns the first item in the queue.
    def dequeue( self ):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue!"
        item = self._qArray[self._front]
        self._front = (self._front + 1) % len(self._qArray)
        self._count -= 1
        return item
