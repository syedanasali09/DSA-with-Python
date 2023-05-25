class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception('Stack is empty')

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise Exception('Stack is empty')

    def is_empty(self):
        return len(self.items) == 0


S = Stack()
for i in range(25):
    S.push(i)
for i in range(12):
    try:
        S.top()
    except Exception as e:
        pass  
for i in range(10):
    try:
        S.pop()
    except Exception as e:
        pass 
size = len(S.items)

print("Current size of S:", size)
