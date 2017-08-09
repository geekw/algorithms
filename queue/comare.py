import time
from pylistqueue import Queue as lQueue
from arrayqueue import Queue as aQueue

CAPACITY = 100000
mydata = range(CAPACITY)

start_time = time.time()
myqueue = lQueue()
for item in mydata:
    myqueue.enqueue(item)

for i in range(CAPACITY):
    myqueue.dequeue()
elapsed_time = time.time() - start_time
print elapsed_time

start_time = time.time()
myqueue = aQueue(CAPACITY)
for item in mydata:
    myqueue.enqueue(item)

for i in range(CAPACITY):
    myqueue.dequeue()
elapsed_time = time.time() - start_time
print elapsed_time
