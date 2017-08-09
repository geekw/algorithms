from lliststack import Stack

mydata = [7, 13, 45, 19, 28, -1]
mystack = Stack()
assert mystack.isEmpty(), "A newly created stack should be empty!"
assert mystack.length() == 0, "The length of an empty stack shoul be 0!"

mystack.push(mydata[0])
assert mystack.length() == 1, "Pushing an item should change the length of an empty stack to 1!"
assert not mystack.isEmpty(), "A stack having items should not be empty!"
assert mystack.peek() == mydata[0], "The most recently inserted item should be on top of the stack!"

mystack.push(mydata[1])
assert mystack.length() == 2, "Pushing an item should change the length of an empty stack to 1!"
assert not mystack.isEmpty(), "A stack having items should not be empty!"
assert mystack.peek() == mydata[1], "The most recently inserted item should be on top of the stack!"

mystack.push(mydata[2])
mystack.push(mydata[3])
assert mystack.pop() == mydata[3], "pop() should return the item that is most recently inserted!"
assert mystack.length() == 3, "pop() operation on an non-empty stack should decrease the length by 1!"

mystack.push(mydata[3])
mystack.push(mydata[4])
mystack.push(mydata[5])
assert mystack.peek() == mydata[-1], "The most recently inserted item should be on top of the stack!"
assert mystack.length() == len(mydata), "The length of the stack should be equal to that of the original list!"
assert mystack.pop() == mydata[-1], "The order of the popped items should be the reverse one of the original list!"
assert mystack.pop() == mydata[-2], "The order of the popped items should be the reverse one of the original list!"
assert mystack.pop() == mydata[-3], "The order of the popped items should be the reverse one of the original list!"
assert mystack.pop() == mydata[-4], "The order of the popped items should be the reverse one of the original list!"
assert mystack.pop() == mydata[-5], "The order of the popped items should be the reverse one of the original list!"
assert mystack.pop() == mydata[-6], "The order of the popped items should be the reverse one of the original list!"
assert mystack.isEmpty(), "With all items popped out, the stack should be empty again!"

print "Congratulations! Passed all tests!"
