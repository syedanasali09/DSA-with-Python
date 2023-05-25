class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.items) == 0

Q = Queue()

for i in range(32):
    Q.enqueue(i)

for i in range(10):
    Q.dequeue()

ignored_errors = 0
for i in range(5):
    try:
        Q.dequeue()
    except IndexError:
        ignored_errors += 1

current_size = len(Q.items) - (10 + ignored_errors)

print("Current size of Q:", current_size)
