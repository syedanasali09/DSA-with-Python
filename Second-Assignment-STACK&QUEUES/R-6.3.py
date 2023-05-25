def transfer(S, T):
    while not S.is_empty():  
        element = S.pop()  
        T.push(element) 

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

S = Stack()
T = Stack()

S.push(1)
S.push(2)
S.push(3)
S.push(4)
S.push(5)

transfer(S, T)

while not T.is_empty():
    print(T.pop(), end=' ')