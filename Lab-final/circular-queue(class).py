class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return (self.tail + 1) % self.k == self.head

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full.")
        elif self.is_empty():
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = item
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
        elif self.head == self.tail:
            item = self.queue[self.head]
            self.queue[self.head] = None
            self.head = -1
            self.tail = -1
            return item
        else:
            item = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.k
            return item

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        elif self.tail >= self.head:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()



# Usage example:
queue = CircularQueue(4)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()

queue.dequeue()
queue.display()

queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.display()

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.display()
