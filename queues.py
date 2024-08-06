from collections import deque
# Python's collections.deque is a double-ended queue, which means you can push and pop an element from either end in constant time.
# For a deque q = deque()

# enqueue: q.append, O(1)
# dequeue: q.popleft(), O(1). Note that it's pop*left*. pop is also supported but it's for getting element at the end of the double-ended queue.
# peek: q[0], O(1). Accesses the first element of the queue just like an array.
# size: len(q), O(1)

q = deque()

q.append(2)
q.append(3)
q.append(1)

print("Length of the queue is: " + str(len(q)))
print("Peeking the first element is: " + str(q[0]))
print("Queue values are: " + str(q))

q.popleft()
print("After dequeing once we have " + str(q))

q.popleft()
print("After dequeing twice we have " + str(q))

print("End result: " + str(q))
# In coding interviews, we see queues most often in breadth-first search. We'll also cover the monotonic deque, where elements are sorted inside the deque, which is useful in solving some advanced coding problems.