class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full. Unable to enqueue value.")
            return
        if self.is_empty():
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.k
        self.queue[self.tail] = value

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Unable to dequeue value.")
            return None
        value = self.queue[self.head]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.k
        return value

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return (self.tail + 1) % self.k == self.head

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        index = self.head
        elements = []
        while index != self.tail:
            elements.append(self.queue[index])
            index = (index + 1) % self.k
        elements.append(self.queue[self.tail])
        print("Queue:", elements)


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