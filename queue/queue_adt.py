"""implementation of the queue ADT using a Python deque"""
from collections import deque


class Queue:
    def __init__(self, capacity):
        #  ensure the capacity is of integer type
        if not isinstance(capacity, int):
            raise TypeError('The queue capacity must be of type int')
        else:
            self.queue = deque()
            self.capacity = capacity

    def enqueue(self, item):
        """
        Add data to the end of the queue.
        Params -> Data: any Python data type, e.g., int, str, etc.
        """
        if len(self.queue) == self.capacity:
            raise Exception('Queue is Full')
        else:
            self.queue.append(item)
            return self.queue

    def dequeue(self):
        """Remove data from the queue"""
        if len(self.queue) == 0:
            raise Exception('Queue is empty')
        else:
            return self.queue.popleft()

    def size(self):
        return len(self.queue)
