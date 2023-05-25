from collections import deque

class QueueAdapter:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def front(self):
        if not self.is_empty():
            return self.queue[0]

    def __str__(self):
        return str(list(self.queue))

q = QueueAdapter()

q.enqueue(5)
q.enqueue(3)
q.dequeue()
q.enqueue(2)
q.enqueue(8)
q.dequeue()
q.dequeue()
q.enqueue(9)
q.enqueue(1)
q.dequeue()
q.enqueue(7)
q.enqueue(6)
q.dequeue()
q.dequeue()
q.enqueue(4)
q.dequeue()
q.dequeue()

print("Final size of queue:", q.size())
print("Current queue:", q)
print("Front of queue:", q.front())
