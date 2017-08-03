# Implementation of the unbounded Priority Queue ADT using a Python list
# with new items appended to the end.
class PriorityQueue :
    # Create an empty unbounded priority queue.
    def __init__( self ):
        self._qList = list()

    # Returns True if the queue is empty.
    def isEmpty( self ):
        return len(self) == 0

    # Returns the number of items in the queue.
    def __len__( self ):
        return len(self._qList)

    # Adds the given item to the queue.
    def enqueue( self, item, priority ):
        # Create a new instance of the storage class and place it at the right place.
        entry = _PriorityQEntry(item, priority)
        rightindex = 0
        for inentry in self._qList:
            if entry.priority >= inentry.priority:
                rightindex += 1
            else:
                break
        self._qList.insert(rightindex,entry)

    # Removes and returns the first item in the queue.
    def dequeue( self ) :
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        entry = self._qList.pop(0)
        return entry.item

# Private storage class for associating queue items with their priority.
class _PriorityQEntry( object ):
    def __init__( self, item, priority ):
        self.item = item
        self.priority = priority