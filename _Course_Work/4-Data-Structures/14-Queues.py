# Stacks work with the LIFO order/beahaviour

# We have another useful data structure called QUEUE
# The QUEUE data structure works with FIFO order/behaviour

# LIFO = Last In First Out
# FIFO = First In First Out

# This resembles real world behaviour of a queue

# Technically we can use a LIST to mimic a queue in Python

[1, 2, 3]

# If we want to remove an item from the QUEUE
# We should remove the one at the beginning
# So we remove "1" and then "2" and then "3"

# ***Disadvantage
# If you are dealing with a large queue or a large list
# You might see some adverse effects on the performance

# ***Reason
# This is because when you remove an item from the beginning of the list
# All the other/remaining items need to be shifted to the left
# So if you have a list with 1001 items, when you remove one item
# 1000 items needs to be moved in memory

# ***Remedy
# In situations like this it is better to use a DEQUEUE object
# How do we do this?

# We have a module called "collections"
# In the "collections" module, we have a CLASS called "deque"
# We call this the "deque" object

# Fist we need to import the "deque" class from the "collections" module


# Instead of declaring a variable and setting it to an empty list like below:
# queue = []

# We wrap the list with the "deque" object
# So we call deque() and pass our empty list as an argument

from collections import deque
queue = deque([])

# The "deque" object has similar methods that we have in the list object

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

# Now to remove an item from the beginning of the queue, we call "queue.popleft()"

queue.popleft()
queue.popleft()
queue.popleft()
queue.popleft()
queue.popleft()

# Note that we don't have the "popleft()" method in list object, but we do have "popleft()" in "deque" object

# So after we remove one item, let's look at our queue
print(queue)

# The result will be - deque([2, 3, 4, 5])

# Also similar to list, we can easily check if a queue is empty
# By using the "not" operator
if not queue: # This means we have an empty queue
    print("empty")