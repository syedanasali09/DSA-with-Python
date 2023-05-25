class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

queue = Queue()

queue.enqueue(5)
print("Enqueue(5) -> Queue:", queue.items)

queue.enqueue(3)
print("Enqueue(3) -> Queue:", queue.items)

dequeued_value = queue.dequeue()
print("Dequeue() -> Dequeued:", dequeued_value)
print("After Dequeue() -> Queue:", queue.items)

queue.enqueue(2)
print("Enqueue(2) -> Queue:", queue.items)

queue.enqueue(8)
print("Enqueue(8) -> Queue:", queue.items)

dequeued_value = queue.dequeue()
print("Dequeue() -> Dequeued:", dequeued_value)
print("After Dequeue() -> Queue:", queue.items)

dequeued_value = queue.dequeue()
print("Dequeue() -> Dequeued:", dequeued_value)
print("After Dequeue() -> Queue:", queue.items)

queue.enqueue(9)
print("Enqueue(9) -> Queue:", queue.items)

queue.enqueue(1)
print("Enqueue(1) -> Queue:", queue.items)

dequeued_value = queue.dequeue()
print("Dequeue() -> Dequeued:", dequeued_value)
print("After Dequeue() -> Queue:", queue.items)

queue.enqueue(7)
print("Enqueue(7) -> Queue:", queue.items)

queue.enqueue(6)
print("Enqueue(6) -> Queue:", queue.items)

dequeued_value = queue.dequeue()
print("Dequeue() -> Dequeued:", dequeued_value)
print("After Dequeue() -> Queue:", queue.items)

dequeued_value = queue.dequeue()
print("Dequeue() -> Dequeued:", dequeued_value)
print("After Dequeue() -> Queue:", queue.items)

queue.enqueue(4)
print("Enqueue(4) -> Queue:", queue.items)

dequeued_value = queue.dequeue()
print("Dequeue() -> Dequeued:", dequeued_value)
print("After Dequeue() -> Queue:", queue.items)

dequeued_value = queue.dequeue()
print("Dequeue() -> Dequeued:", dequeued_value)
print("After Dequeue() -> Queue:", queue.items)