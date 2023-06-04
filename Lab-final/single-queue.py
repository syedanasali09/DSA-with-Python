class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)



queue = Queue()


queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Queue size:", queue.size())

# Dequeue elements
print(queue.dequeue())
print(queue.dequeue())


print("Is the queue empty?", queue.is_empty())
