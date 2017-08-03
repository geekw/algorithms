from priorityq import PriorityQueue

Q = PriorityQueue()
Q.enqueue( "purple", 5 )
Q.enqueue( "black", 1 )
Q.enqueue( "orange", 3 )
Q.enqueue( "white", 0 )
Q.enqueue( "green", 1 )
Q.enqueue( "yellow", 5 )

assert Q.dequeue() is "white"
assert Q.dequeue() is "black"
assert Q.dequeue() is "green"
assert Q.dequeue() is "orange"
assert Q.dequeue() is "purple"
assert Q.dequeue() is "yellow"

print "Congratulations! Passed all tests!"