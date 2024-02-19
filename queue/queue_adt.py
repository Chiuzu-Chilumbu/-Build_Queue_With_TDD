"""implementation of the queue ADT using a Python deque"""
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)
        return self.queue

    def size(self):
        return len(self.queue)

