class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.size = 0

    def enqueue(self, item):
        if self.size == self.capacity:
            raise IndexError("Queue is full")
        rear = (self.front + self.size) % self.capacity
        self.data[rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def is_empty(self):
        return self.size == 0

Q = ArrayQueue(30)

for i in range(32):
    Q.enqueue(i)

for i in range(10):
    Q.dequeue()

final_front = Q.front

print("Final value of front:", final_front)
